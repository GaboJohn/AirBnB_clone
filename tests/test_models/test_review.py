#!/usr/bin/python3
"""Defines unittests for models/review.py."""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_attributes(self):
        """Test the attributes of the Review class."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == "__main__":
    unittest.main()
