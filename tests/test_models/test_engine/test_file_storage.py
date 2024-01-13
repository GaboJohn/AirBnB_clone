#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""

import unittest
import os
import json
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.file_path = "test_file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down the test environment."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method."""
        obj_dict = {'id': '123', 'name': 'test'}
        obj = BaseModel(**obj_dict)
        self.storage.new(obj)
        self.storage.save()
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn("BaseModel.123", all_objs)

    def test_new(self):
        """Test the new method."""
        obj_dict = {'id': '123', 'name': 'test'}
        obj = BaseModel(**obj_dict)
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn("BaseModel.123", all_objs)

    def test_save_reload(self):
        """Test the save and reload methods."""
        obj_dict = {'id': '123', 'name': 'test'}
        obj = BaseModel(**obj_dict)
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        all_objs = new_storage.all()
        self.assertIn("BaseModel.123", all_objs)

if __name__ == "__main__":
    unittest.main()
