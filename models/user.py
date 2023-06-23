#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
from models.city import City


class User(BaseModel, Base):
    """This class defines a user by various attributes of user class"""

    __tablename__ = "users"
    email = Column(string(128), nullable=False)
    password = Column(string(128), nullable=False)
    first_name = Column(string(128))
    last_name = Column(string(128))
    places = relationship('Place', cascade='delete', backref='user')
    reviews = relationship('Review', cascade='delete', backref='user')
