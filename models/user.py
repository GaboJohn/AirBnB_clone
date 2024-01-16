#!/usr/bin/python3
"""This module defines the User class, a subclass of BaseModel."""

from models.base_model import BaseModel

class User(BaseModel):
    """Represents a user for the AirBnB project."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
         """Initialize User instance."""
         super().__init__(*args, **kwargs)

    @classmethod
    def all(cls):
        """Return a list of all User instances."""
        from models import storage
        return [obj for obj in storage.all().values() if isinstance(obj, cls)]

    @classmethod
    def count(cls):
        """Return the number of User instances."""
        return len(cls.all())

