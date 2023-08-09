#!/usr/bin/python3

'''
BaseModel Class Module
'''
from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''
    BaseModel class
    '''

    def __init__(self, *args, **kwargs):
        '''
        BaseModel class object instances initialization

        Parameters
        ----------
        args : list
            list of parameters for created BaseModel instance
        kwargs : dict
            dictionary of parameters for created BaseModel instance

        Methods
        -------
        save()
            updates the public instance attribute updated_at
            with the current datetime
        to_dict()
            returns a dictionary containing all keys/values
            of __dict__ of the instance
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    #value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''
        overriding the __str__ method

        Returns
        -------
        str
            String output in the format:
                [<class name>] (<self.id>) <self.__dict__>
        '''
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        '''
        updating update_at attribute with the current datetime
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        Get all keys/values of the object instance

        Returns
        -------
        dict
            a dictionary containing all keys/values of the instance
        '''
        new_dictionary = self.__dict__.copy()
        new_dictionary['__class__'] = self.__class__.__name__
        new_dictionary['created_at'] = self.created_at.isoformat()
        new_dictionary['updated_at'] = self.updated_at.isoformat()
        return (new_dictionary)
