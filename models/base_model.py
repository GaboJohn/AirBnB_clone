#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            id (str): Unique identifier for the instance.
            created_at (datetime): Timestamp of the instance creation.
            updated_at (datetime): Timestamp of the instance's last update.
        """
        if kwargs:
            for key, value in kwargs.items():
                 if key != '__class__':
                     if key in ['created_at', 'updated_at']:
                         setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                     else:
                         setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        Update the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """
        Return the string representation of the BaseModel instance.

        Returns:
            str: String representation of the instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary containing all keys/values of the instance attributes.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
