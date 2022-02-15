from dataclasses import dataclass

from sqlalchemy import Column, Date, String
from app.configs.database import db

@dataclass
class Vaccine(db.Model):
    cpf : str
    name : str
    first_shot_date : str
    second_shot_date : str
    vaccine_name : str
    health_unit_name : str

    __tablename__ = "vaccine_cards"
    cpf = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(Date)
    second_shot_date = Column(Date)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)
    

