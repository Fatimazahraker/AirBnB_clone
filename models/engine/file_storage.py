#!/usr/bin/python3
""" molule to store all obejcts """
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ class that serialize instance to json
    and deserialize json file to instance
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """pulic instance method return __object dic"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Public instance methods
        sets in __objects the obj with key <obj class name>.id
        """
        frmat = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[frmat] = obj

    def save(self):
        """
        Public instance methods
        serializes __objects to the JSON file (path: __file_path)
        """
        dictobj = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf_8") as file:
            json.dump(dictobj, file)

    def reload(self):
        """
        Public instance methods
        deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing. If the
        file doesn’t exist, no exception should be raised)
        """
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }

        try:
            dic = {}
            with open(FileStorage.__file_path, "r", encoding="utf_8") as fi:
                dic = json.load(fi)
                for key, value in dic.items():
                    cls_name = value['__class__']
                    if cls_name in classes:
                        cls = classes[cls_name]
                        obj = cls(**value)
                        self.all()[key] = obj
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
