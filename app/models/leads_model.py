from multiprocessing.dummy import Array
from sqlalchemy import Column, Integer, String, DateTime
from app.configs.database import db
from dataclasses import dataclass

@dataclass
class Leads(db.Model):
    id: int 
    name: str
    email: str
    phone: str 
    creation_date: str 
    last_visit: str 
    visits: int

    __tablename__  = "leads"
    
    id = Column(Integer, primary_key = True, unique = True)
    name = Column(String, nullable = False)
    email = Column(String, unique = True, nullable = False)
    phone = Column(String, nullable =  False, unique = True)
    creation_date = Column(DateTime, nullable = False)
    last_visit = Column(DateTime, nullable = False)
    visits = Column(Integer, default = 1)

    @classmethod
    def serializer(cls, data):
        if type(data)  ==  Leads: 
            print("Entreiii")
            return{
                "name":data.name,
                "email":data.email,
                "phone":data.phone,
                "creation_date":data.creation_date,
                "last_visit":data.last_visit,
                "visits":data.visits
            }
        if type(data) is list:
            return[
                {
                "name":lead.name,
                "email":lead.email,
                "phone":lead.phone,
                "creation_date":lead.creation_date,
                "last_visit":lead.last_visit,
                "visits":lead.visits
                }
                for lead in data
            ]
       