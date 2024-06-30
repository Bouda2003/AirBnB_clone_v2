#!/usr/bin/python3
"""db storage engine"""

from os import getenv
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class DBStorage:
    """class for the db storage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """fetches the objects"""
        new_dict = {}
        if cls is None:
            for c in classes:
                arr = self.__session.query(classes[c]).all()
                for obj in arr:
                    new_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        else:
            arr = self.__session.query(classes[cls]).all()
            for obj in arr:
                new_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return new_dict

    def new(self, obj):
        """adds a new object"""
        self.__session.add(obj)

    def save(self):
        """saves the current changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads all the objects from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
