#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(string(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """ that returns the list of City instances
        with state_id equals to the current
        State.id => It will be the FileStorage
        relationship between State and City

        """
        Clist = []
        for city in list(models.storage.all(City).values()):
            if city.state_id == self.id:
                city_list.append(city)
        return Clist
