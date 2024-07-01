#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes
        email(str): user's email
        password(str): user's password
        first_name(str): user's first name
        last_name(str): user's last name
        places(relationship): user-place relationship
        reviews(relationship): user-review relationship
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user")
    reviews = relationship("Review", backref="user")
