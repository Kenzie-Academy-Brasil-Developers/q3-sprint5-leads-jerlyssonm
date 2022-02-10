from sqlalchemy import Column, Integer, String, DateTime
from app.configs.database import db


class LeadModel(db.Model):
    id: int
    name: str
    email: str
    phone: str
    creation_date: int
    last_visit: int
    visits: int

    __tablename__= "leads"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    creation_date = Column(DateTime, nullable=False)
    last_visit = Column(DateTime, nullable=False)
    visits = Column(Integer)