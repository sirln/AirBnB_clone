#!/usr/bin/python3

"""City module"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from
    class BaseModel

    Attributes
    ----------

    state_id: str
        This refers to the state.id
    name: str
        This refers to the name of the city

    """

    state_id = ""
    name = ""
