#!/usr/bin/python3
"""represent  User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """class  User.

    Attrs:
        email: user 's email.
        password: user 's password .
        first_name:user 's  first name.
        last_name: last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
