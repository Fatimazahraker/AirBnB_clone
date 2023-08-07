#!/usr/bin/python3
"""base class, parent class that child class enherit from it"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel of the project.
    define all common attribute of othes classes 
    """

    def __init__(self, *args, **kwargs):
        """define a class with a magic init method.

        Args:
            *args: tuples of argumets.
            **kwargs: dictionary of arguments.
        Attr:
            id: unique id by uuid4
            created_id: created datetime
            updated_at: updated datetime
        """
        timfrm = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timfrm)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """pulic instance methode to save the updated time"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """public instance method return a dictionary
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        newdict = self.__dict__.copy()
        newdict["created_at"] = self.created_at.isoformat()
        newdict["updated_at"] = self.updated_at.isoformat()
        newdict["__class__"] = self.__class__.__name__
        return newdict

    def __str__(self):
        """it is method return print/st representation of the class."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
