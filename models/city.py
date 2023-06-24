#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import models
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(string(128), nullable=False)
    state_id = Column(string(60), nullable=False, ForeignKey(('state.id'))
    places = relationship(
    "Place",
    backref="cities",
     cascade="all, delete-orphan")
