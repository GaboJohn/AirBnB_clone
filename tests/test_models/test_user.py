#!/usr/bin/python3
"""Unittests for User class."""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test the User class."""

    def setUp(self):
        """Set up for test."""
        self.user = User()

    def tearDown(self):
        """Clean test files."""
        del self.user

    def test_instance(self):
        """Test for correct instantiation of User instance."""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test the attributes of User class."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_default_values(self):
        """Test default values of User attributes."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_method(self):
        """Test the __str__ method of User class."""
        expected_str = "[User] ({}) {}".format(
            self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method of User class."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['__class__'], "User")
        self.assertEqual(user_dict['created_at'],
                         self.user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'],
                         self.user.updated_at.isoformat())

    def test_created_at_type(self):
        """Test the type of created_at attribute."""
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at_type(self):
        """Test the type of updated_at attribute."""
        self.assertIsInstance(self.user.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
