#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        """Test the attributes of the Amenity class."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

if __name__ == "__main__":
    unittest.main()
