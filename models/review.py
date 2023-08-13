#!/usr/bin/python3
""" module that represent review model """
from .base_model import BaseModel


class Review(BaseModel):
    """ class of review model inherit from BaseModel class
        Attr:
            place_id: public class attr for place id
            user_id: public class attr for user id
            text: public class attr for text of review
    """
    place_id = ""
    user_id = ""
    text = ""
