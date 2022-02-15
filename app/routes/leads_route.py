from flask import Blueprint

from app.controllers.leads_controller import create_lead, get_all_leads, update_lead_by_email, delete_lead

bp = Blueprint("",__name__, url_prefix="/leads")

bp.post("")(create_lead)
bp.get("")(get_all_leads)
bp.patch("")(update_lead_by_email)
bp.delete("")(delete_lead)