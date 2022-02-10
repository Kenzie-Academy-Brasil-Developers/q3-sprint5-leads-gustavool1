from http import HTTPStatus
from flask import current_app, jsonify, request
from datetime import datetime
from sqlalchemy.exc import IntegrityError
import re 
from app.exc.NumberInvalidError import NumberInvalidError
from app.models.leads_model import Leads
from sqlalchemy import desc



def create_lead():
    try:
        data = request.get_json()

        is_number_valid = re.fullmatch("\([1-9]{2}\)[0-9]{5}\-[0-9]{4}", data["phone"])    

        for value in data.values():
            if type(value) is not str:
                return {"msg":"All the fields must be an string"}, HTTPStatus.BAD_REQUEST

        if not is_number_valid:
            raise NumberInvalidError


        lead = Leads(**data)

        current_app.db.session.add(lead)
        current_app.db.session.commit()

       
        return jsonify(Leads.serializer(lead)), HTTPStatus.CREATED  

    except IntegrityError:
        return {"msg":"This phone or email already exist on the database"}, HTTPStatus.CONFLICT
    
    except NumberInvalidError:
        return {"msg":"Your phone number must follow the following rule ->  (xx)xxxxx-xxxx"}, HTTPStatus.BAD_REQUEST
    
    except TypeError:
        return {"msg":"The only fields allowed in the requisiton are -> name, email, phone. And all of then must be string "}, HTTPStatus.BAD_REQUEST
        




def get_all_leads():
    leads = Leads.query.order_by(desc(Leads.visits)).all()
    leads = Leads.serializer(leads)
    return jsonify(leads), HTTPStatus.OK
    



def update_lead_by_email():
    data = request.get_json()
    for key in data.keys():
        if key != "email":
            return {"msg":"Only email is allowed in the body"}, HTTPStatus.BAD_REQUEST
    
    if type(data["email"]) is not str:
        return {"msg":"The email must be an string"}, HTTPStatus.BAD_REQUEST
        
    lead_updated = Leads.query.filter(Leads.email == data["email"]).first()
    
    if not lead_updated:
        return {"msg": "Email not found"}, HTTPStatus.NOT_FOUND

    lead_updated.visits = lead_updated.visits + 1
    lead_updated.last_visit =  str(datetime.now().strftime("%d/%m/%Y %H:%M"))
    
    current_app.db.session.add(lead_updated)
    current_app.db.session.commit()
    return "", HTTPStatus.NO_CONTENT




def delete_lead():
    data = request.get_json()

    for key in data.keys():
        if key != "email":
            return {"msg":"Only email is allowed in the body"}, HTTPStatus.BAD_REQUEST
    
    if type(data["email"]) is not str:
        return {"msg":"Email must be an string"}, HTTPStatus.BAD_REQUEST
            
    lead = Leads.query.filter(Leads.email == data["email"]).first()
    
    if not lead:
        return {"msg":"No lead this email was found"}, HTTPStatus.NOT_FOUND 

    current_app.db.session.delete(lead)
    current_app.db.session.commit()
    return "", HTTPStatus.NO_CONTENT