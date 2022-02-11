from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.configs.database import db
import re


@dataclass
class LeadModel(db.Model):
    keys_valid=["name", "email", "phone"]
    __tablename__= "leads"

    id = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    email: str = Column(String, nullable=False, unique=True)
    phone: str = Column(String, nullable=False, unique=True)
    creation_date: str = Column(DateTime, nullable=False)
    last_visit: str = Column(DateTime, nullable=False)
    visits: int = Column(Integer)

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.creation_date = datetime.now()
        self.last_visit = datetime.now()
        self.visits = 1

    @staticmethod
    def visit(lead):
        lead.last_visit = datetime.now()
        lead.visits = lead.visits + 1
        return lead

    @staticmethod
    def verify_keys_and_values(data, keys= keys_valid):
        list_keys= [key for key in data]
        values= [value for value in data.values()]

        for value in values:
            if not isinstance(value, str):
                return "string only accepted values"
        
        if (set(list_keys) == set(keys)):
            phone = re.fullmatch(r"\(\d{2}\)\d{5}\-\w{4}",data["phone"])
            if not phone:
                return "phone this only format (xx)xxxxx-xxxx"
            return data 
        else:
            return {
                "waiting" : keys,
                "received": list_keys
            }

