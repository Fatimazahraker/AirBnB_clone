#!/usr/bin/python3
"""Defines  FileStorage class."""
from models.amenity import Amenity
from models.review import Review
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place



class FileStorage:
    """Represent abstracted storage engine.

    Attributes:
        __file_path (str):  name of  file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for p in objdict.values():
                    cls_name = p["__class__"]
                    del p["__class__"]
                    self.new(eval(cls_name)(**p))
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return


