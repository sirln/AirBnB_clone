#!/usr/bin/python3

""""Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from
    BaseModel class

    Attributes
    ----------

    place_id: str
        This refers to the place.id
    user_id: str
        This refers to the user.id
    text: str
        This refers to the review made by
        the person.
    """

    place_id = ""
    user_id = ""
    text = ""
