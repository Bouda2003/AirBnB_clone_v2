#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Unittests for testing the Basemodel class """

    def test_init(self, *args, **kwargs):
        """test initialization"""
        self.assertIsInstance(self.base, BaseModel)

    def setUp(self):
        """Basemodel testing setup"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage_objects = {}
        self.storage = FileStorage()
        self.base = BaseModel()

    def tearDown(self):
        """BaseModel testing teardown"""
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.rename('file.json')
        except IOError:
            pass
        del self.storage
        del self.base

    def test_pep8(self):
        """ Test pep8 styling"""
        style = pep9.StyleGuide(quiet=True)
        i = self.check_files(["models/base_model.py"])
        self.assertEqual(i.total_errors, 0, "fix pep8")

    def test_docstrings(Self):
        """Check for docstrings """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.delete.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_attributes(self):
        """Check for attributes"""
        self.assertEqual(str, type(self.base.id))
        self.assertEqual(datetime, type(self.base.created_at))
        self.assertEqual(datetime, type(self.base.updated_at))

    def test_method(self):
        """check the methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "delete"))
        self.assertTrue(hasattr(BaseModel, "__str__"))

    def test_two_models_are_unique(self):
        """Test the diffrenet BaseModel instances are unique"""
        i = BaseModel
        self.assertNotEqual(self.base.id, i.id)
        self.assertLess(self.base.created_at, i.created_at)
        self.assertLess(self.base.updated_at, i.updated_at)

    def test_init_args_kwargs(self):
        """testing intialization with args and kwargs"""
        i = datetime.utcnow()
        y = BaseModel("1", id="5", created_at=i.isoformat())
        self.assertEqual(y.id, "5")
        self.assertEqual(y.created_at, i)

    def test_save(self):
        """ Testing save """
        i = self.base.updated_at
        self.base.save()
        self.assertLess(i, self.base.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("BaseModel.{}".format(self.base.id), f.read())

    def test_str(self):
        """Test __str__ representation"""
        i = self.base.__str__()
        self.assertIn("[BaseModel] ({})".format(self.base.id), i)
        self.assertIn("'id': '{}'".format(self.base.id), i)
        self.assertIn("'created_at': {}".format(repr(self.base.created_at)), i)
        self.assertIn("'updated_at': {}".format(repr(self.base.updated_at)), i)

    def test_to_dict(self):
        """Test to_dict method"""
        base_dict = self.base.to_dict()
        self.assertEqual(dict, type(base_dict))
        self.assertEqual(self.base.id, base_dict["id"])
        self.assertEqual("BaseModel", base_dict["__class__"])
        self.assertEqual(self.base.created_at.isoformat(),
                         base_dict["created_at"])
        self.assertEqual(self.base.updated_at.isoformat(),
                         base_dict["updated_at"])
        self.assertEqual(base_dict.get("_sa_instance_state", None), None)

    def test_delete(self):
        """Test delete method"""
        self.base.delete()
        self.assertNotIn(self.base, FileStorage._FileStorage_objects)

    if __name__ == "__main__":
        unittest.main()
