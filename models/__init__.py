#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


type_dbstorage = os.getenv('HBNB_TYPE_STORAGE')

if type_dbstorage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.db_storage import FileStorage
    storage = FileStorage()

storage.reload()
