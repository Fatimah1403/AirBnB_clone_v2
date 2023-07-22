#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import models
import os
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """ that returns the list of City instances
        with state_id equals to the current
        State.id => It will be the FileStorage
        relationship between State and City

        """
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
