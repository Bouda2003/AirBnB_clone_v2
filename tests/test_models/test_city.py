#!/usr/bin/python3
"""Defines Unittest for models/city.py"""
import os
import pep8
import models
import MySQLdb
import unittest
from datetime import datetime
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker


class test_City(test_basemodel):
    """Defines unnittests for models/city.py """

    def setUpClass(self):
        """City testing setup"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage_objects = {}
        self.filestorage = FileStorage()
        self.state = state(name="California")
        self.city = City(name="San Francisco", state_id=self.state.id)

        if type(models.storage) == DBStorage:
            self.dbstorage = DBStorage()
            base.metadata.create_all(clx.dbstorage._DBStorage__engine)
            session = sessionmaker(bind=self.dbstorage._DBStorage_engine)
            self.dbstorage._DBStorage_session = Session()

    def tearDownClass(self):
        """city testing teardown"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        del self.state
        del self.city
        del self.filestorage
        if type(models.storage) == DBStorage:
            self.dbstorage._DBStorage_session.close()
            del self.dbstorage

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/city.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Check for attributes."""
        ct = City()
        self.assertEqual(str, type(ct.id))
        self.assertEqual(datetime, type(ct.created_at))
        self.assertEqual(datetime, type(ct.updated_at))
        self.assertTrue(hasattr(ct, "__tablename__"))
        self.assertTrue(hasattr(ct, "name"))
        self.assertTrue(hasattr(ct, "state_id"))

    def test_is_subclass(self):
        """Check that City is a subclass of BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_init(self):
        """Test initialization."""
        self.assertIsInstance(self.city, City)

    def test_two_models_are_unique(self):
        """Test that different City instances are unique."""
        ct = City()
        self.assertNotEqual(self.city.id, ct.id)
        self.assertLess(self.city.created_at, ct.created_at)
        self.assertLess(self.city.updated_at, ct.updated_at)

    def test_init_args_kwargs(self):
        """Test initialization with args and kwargs."""
        dt = datetime.utcnow()
        ct = City("1", id="5", created_at=dt.isoformat())
        self.assertEqual(ct.id, "5")
        self.assertEqual(ct.created_at, dt)

    def test_to_dict(self):
        """Test to_dict method."""
        city_dict = self.city.to_dict()
        self.assertEqual(dict, type(city_dict))
        self.assertEqual(self.city.id, city_dict["id"])
        self.assertEqual("City", city_dict["__class__"])
        self.assertEqual(self.city.created_at.isoformat(),
                         city_dict["created_at"])
        self.assertEqual(self.city.updated_at.isoformat(),
                         city_dict["updated_at"])
        self.assertEqual(self.city.name, city_dict["name"])
        self.assertEqual(self.city.state_id, city_dict["state_id"])

    if __name__ == "__main__":
        unittest.main()
