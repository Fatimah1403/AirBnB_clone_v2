#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

time_frmt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A base class that define that defines all common attributes"""
    id = Column(String(60), primary_key=True, unique=True, nullable=False)
    Created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if 'updated_at' != kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            setattr(self, key, value)
            if isinstance(self.created_at, str):
                self.created_at = datetime.strptime(self.created_at, time_frmt)
            if isinstance(self.updated_at, str):
                self.updated_at = datetime.strptime(self.updated_at, time_frmt)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """ Function delete the current instance from the storage """
        models.storage.delete(self)
