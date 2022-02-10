from http import HTTPStatus
from sqlalchemy.exc import ProgrammingError
from app.models.lead_model import LeadModel
from app.configs.database import db
from flask import jsonify, request
from werkzeug.exceptions import NotFound


def lead_post():
    data = request.get_json()

    lead = LeadModel(**data)
    db.session.add(lead)
    db.session.commit()
    return jsonify(lead),HTTPStatus.CREATED

def lead_get():
    leads_list = (
        LeadModel.query.all()
    )
    return jsonify(leads_list), HTTPStatus.OK

def lead_update():
    try:
        data_email = request.get_json()["email"]
        lead_updated = (
            LeadModel
            .query
            .filter_by(email = data_email)
            .first_or_404()
        )
        updated = LeadModel.visit(lead_updated)
        db.session.add(updated)
        db.session.commit()
        return  jsonify(updated), HTTPStatus.NO_CONTENT
    except NotFound:
        return {"error": f"email {data_email} not found"},HTTPStatus.NOT_FOUND
    except (KeyError,ProgrammingError ):
        return {"Alert Error": "example email: email@example.com"},HTTPStatus.NOT_ACCEPTABLE


def lead_delete():
    try:
        data_email =request.get_json()["email"]
        lead_updated = (
            LeadModel
            .query
            .filter_by(email = data_email)
            .first_or_404()
        )
        db.session.delete(lead_updated)
        db.session.commit()

        return  '',HTTPStatus.NO_CONTENT
    except NotFound:
        return {"error": f"email {data_email} not found"}
    except:
        return {"Alert Error": f"use 'email': 'email@example.com'"}