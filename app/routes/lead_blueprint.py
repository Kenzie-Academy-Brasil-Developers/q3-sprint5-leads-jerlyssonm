from flask import Blueprint
from app.controllers.lead_controllers import lead_post


bp_lead = Blueprint("bp_lead", __name__, url_prefix="/leads")

bp_lead.post("")(lead_post)