#!/usr/bin/python3

"""Define FileStorage class """
import json, sys
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return all objects stored in the dictionnary"""
        return (FileStorage.__objects)

    def new(self, obj):
        """Set in __objects the obj with the key <obj classname>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to JSON fie"""
        objects_copy = FileStorage.__objects.copy()
        objects_dict = {
            obj: objects_copy[obj].to_dict() for obj in objects_copy.keys()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects_dict, f)


    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects_dict = json.load(f)
                for obj in objects_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
