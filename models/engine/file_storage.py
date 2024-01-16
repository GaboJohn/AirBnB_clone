#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
import datetime

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def get_class_instances(self, class_name):
        """Returns a list of instances of the specified class."""
        instances = []
        for key, value in self.__objects.items():
             if class_name in key:
                 instances.append(value)
        return instances

    def classes(self):
        """Returns dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        classes_dict = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "Place": {
                "city_id": str,
                "name": str,
                "user_id": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "City": {
                "state_id": str,
                "name": str
            },
            "State": {
                "name": str
            },
            "Amenity": {
                "name": str
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return classes_dict

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded_objs = json.load(file)
                for key, obj_dict in loaded_objs.items():
                    class_name, obj_id = key.split('.')
                    try:
                        obj_class = self.classes().get(class_name)
                        if obj_class:
                            obj_instance = obj_class(**obj_dict)
                            self.__objects[key] = obj_instance
                        else:
                            print(f"Class '{class_name}' not found")
                    except Exception as e:
                        print(f"Error creating instance: {e}")
        except FileNotFoundError:
            pass                            
