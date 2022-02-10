from flask import Blueprint
from app.controllers.lead_controllers import lead_delete, lead_get, lead_post, lead_update


bp_lead = Blueprint("bp_lead", __name__, url_prefix="/leads")

bp_lead.post("")(lead_post)
bp_lead.get("")(lead_get)
bp_lead.patch("")(lead_update)
bp_lead.delete("")(lead_delete)