#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship



class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(string(), nullable=False)
    cities = relationship("City", backref="state")
