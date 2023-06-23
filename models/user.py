#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
from models.city import City
from os import getenv


class User(BaseModel, Base):
    """ Represent a user for a MySQL database.

    Attributes:
        __tablename__: represents the table name, users
        email: (sqlalchemy String): The user's email address.
        password (sqlalchemy String): The user's password.
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
        places (sqlalchemy relationship): The user-Place relationship.
        reviews (sqlalchemy relationship): The user-Review relationship.

    """
    __tablename__ = 'users'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(string(128), nullable=False)
        password = Column(string(128), nullable=False)
        first_name = Column(string(128))
        last_name = Column(string(128))
        places = relationship('Place', cascade='delete', backref='user')
        reviews = relationship('Review', cascade='delete', backref='user')

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
