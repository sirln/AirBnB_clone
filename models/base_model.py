#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

"""Definition of a BaseModel"""


class BaseModel:
    """The main BaseModel for the HBnB Project"""

    def __init__(self):
        """Initialisation"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """Returns the string representation of the BaseModel
        instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates the updated_at attribute with the current
        datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """converts an instance of a class into a dictionary"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
