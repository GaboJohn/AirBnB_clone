#!/usr/bin/python3
"""Defines the FileStorage class."""

import json

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
            key = "{}.{}".format(type(obj).__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded_objs = json.load(file)
                for key, obj_dict in loaded_objs.items():
                    class_name, obj_id = key.split('.')
                    obj_class = eval(class_name)
                    obj_instance = obj_class(**obj_dict)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass                                             
