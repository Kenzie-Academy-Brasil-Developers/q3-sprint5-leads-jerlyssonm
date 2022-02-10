from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.configs.database import db

@dataclass
class LeadModel(db.Model):

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