#!/usr/bin/python3
"""Defines the Place class."""

from models.base_model import BaseModel


class Place(BaseModel):
    """class represent place .

    Attr:
        city_id : The id of City.
        user_id : The id of User.
        name : the place's name.
        description: place description.
        number_rooms: The number of rooms of the place.
        number_bathrooms: The number of bathrooms.
        max_guest: The maximum number of guests of the place.
        price_by_night: The price by night of the place.
        latitude: The latitude of the place.
        longitude: longitude.
        amenity_ids: une list cntain the amendety ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
