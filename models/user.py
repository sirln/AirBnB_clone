#!/usr/bin/python3

"""
A User module that inherits the characteristics
from the class BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel

    Attributes
    ----------

    email: str
        This refers to the email address of the person
    password: str
        This refers to the password of the person
    first_name: str
        This refers to the person's first name
    last_name: str
        This refers to the person's last name

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
