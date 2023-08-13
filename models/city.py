#!/usr/bin/python3
"""it a class name city"""

from models.base_model import BaseModel


class City(BaseModel):
    """class name city.

    Attr:
        state_id (str):  representt id.
        name (str):  string name of city.
    """

    state_id = ""
    name = ""
