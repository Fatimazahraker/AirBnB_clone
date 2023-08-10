#!/usr/bin/python3
"""base class, parent class that child class enherit from it"""

import models
import datetime
import uuid


class BaseModel:
    """ it is  basemodel calss that define 
    all attributes and
    methodes for other class
    """
    def  __init__(self, *args, **kwargs):
        """ intialization of the magic init method.

        args:
            *args: tuples of argumets.
            **kwargs: dictionary of arguments.
        Attr:
            id: unique id by uuid4
            created_id: created datetime
            updated_at: updated datetime
        """
        if len(kwargs) > 0:
             for k, v in kwargs.items():
                 if k == "__class__":
                     pass
                 elif k in ("created_at", "updated_at"):
                     self.__dict__[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                 else:
                     self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute 
        updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """it a public methode returns a dictionary containing 
        all keys/values of __dict__ of the instance
        """
        newdict = {}
        newdict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                newdict[key] = value.isoformat()
            else:
                newdict[key] = value
        return newdict

    def __str__(self):
        """it is a str format of all instance and its attribute"""
        classname = self.__class__.__name__
        return f"{[classname]} {(self.id)} {self.__dict__}"


