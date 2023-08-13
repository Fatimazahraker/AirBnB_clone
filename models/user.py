#!/usr/bin/python3
"""represent  User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """class  User.

    Attrs:
        email:  email of the user.
        password: password of the user.
        first_name: first name of the user.
        last_name: last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
