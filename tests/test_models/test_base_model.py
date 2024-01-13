#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Test the initialization of the BaseModel."""
        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.updated_at)
        self.assertIsNotNone(model.created_at)

    def test_save(self):
        """Test the save method of the BaseModel."""
        model = BaseModel()

        first_updated_at = model.updated_at

        model.save()

        self.assertNotEqual(first_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel."""
        model = BaseModel()

        model_dict = model.to_dict()

        self.assertEqual(model_dict["__class__"], 'BaseModel')
        self.assertIsInstance(model_dict['id'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertIsInstance(model_dict['created_at'], str)

    def test_str(self):
        """Test the string representation (__str__) of the BaseModel."""
        model = BaseModel()

        self.assertTrue(str(model).startswith('[BaseModel]'))

        self.assertIn(model.id, str(model))

        self.assertIn(str(model.__dict__), str(model))

if __name__ == "__main__":
    unittest.main()
