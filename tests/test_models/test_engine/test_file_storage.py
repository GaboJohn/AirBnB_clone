#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
from models.user import User

class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Make a backup of the existing file.json if it exists
        if os.path.exists("file.json"):
            os.rename("file.json", "file.json.bak")

    @classmethod
    def tearDownClass(cls):
        # Restore the original file.json if a backup exists
        if os.path.exists("file.json.bak"):
            os.rename("file.json.bak", "file.json")

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up the objects in the storage
        self.storage._FileStorage__objects = {}

    def test_all(self):
        # Ensure the all method returns a dictionary
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        # Ensure new method adds an object to the storage
        user = User()
        self.storage.new(user)
        self.assertIn("User." + user.id, self.storage._FileStorage__objects)

    def test_save_reload(self):
        # Ensure save and reload methods work together
        user = User()
        self.storage.new(user)
        self.storage.save()
        new_storage = FileStorage()
        self.assertIn("User." + user.id, new_storage._FileStorage__objects)

if __name__ == '__main__':
    unittest.main()
