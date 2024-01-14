#!/usr/bin/python3
"""This module defines the User class, a subclass of BaseModel."""

from models.base_model import BaseModel

class User(BaseModel):
    """Represents a user for the AirBnB project."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
