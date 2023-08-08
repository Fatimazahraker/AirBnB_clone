#!/usr/bin/python3
"""base class, parent class that child class enherit from it"""
import models
import datetime
from uuid import uuid4


class BaseModel:
    """ it is a basemodel calss that define 
    all attributes and
    methodes for other class
    """
    def  __init__(self):
        """ intialization of the magic init method.

        args:
            *args: tuples of argumets.
            **kwargs: dictionary of arguments.
        Attr:
            id: unique id by uuid4
            created_id: created datetime
            updated_at: updated datetime
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """updates the public instance attribute 
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

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


