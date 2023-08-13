#!/usr/bin/python3
"""Defines  Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent  amenity.

    Attributes:
        name (str):  name of the amenity.
    """

    name = ""

