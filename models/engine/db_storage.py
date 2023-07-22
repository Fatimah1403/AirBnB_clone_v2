#!/usr/bin/python3
"""DataStorage file """
import json
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base
from sqlalchemy import (create_engine)


class DBStorage:
    """Datastorage class """
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, database),
                                      pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session (self.__session)
         all objects depending of the class name (argument cls)

        """

        dic = {}
        classes_con = [State, City, User, Place, Review, Amenity]

        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls)
            for elem in objs:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem

        else:
            for state in classes_con:
                objs = self.__session.query(state)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """ add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.session.commit()

    def delete(self, obj=None):
        """ delete from the current database session"""
        if not self.session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ creates the current database session """
        try:
            Base.metadata.create_all(self.__engine)
            session_rel = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
            self.__session = scoped_session(session_factory)
        except Exception as E:
            print(E)

    def close(self):
        """ remove our session"""
        self.__session.close()
