#!/usr/bin/python3
"""Defines the FileStorage class."""

import json


class FileStorage:
    """Represent an abstracted storage engine."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objects_dict = FileStorage.__objects
        objects_dict_serialized = {obj: objects_dict[obj].to_dict() for obj in objects_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects_dict_serialized, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objects_dict_serialized = json.load(f)
                for serialized_obj in objects_dict_serialized.values():
                    class_name = serialized_obj["__class__"]
                    del serialized_obj["__class__"]
                    #self.new(eval(class_name)(**serialized_obj))
        except FileNotFoundError:
            return
