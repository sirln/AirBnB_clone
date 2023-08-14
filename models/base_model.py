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
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                # if key == 'created_at' or key == 'updated_at':
                # alternative way of doing it
                if key in ['created_at', 'updated_at']:
                    # value = datetime.fromisoformat(value)
                    # alternative way of doing it
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    # self.__dict__[key] = value
                    # alternative way of doing it
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        Get all keys/values of the object instance

        Returns
        -------
        dict
            a dictionary containing all keys/values of the instance
        '''
        # new_dictionary = dict(self.__dict__)
        new_dictionary = self.__dict__.copy()
        new_dictionary['__class__'] = self.__class__.__name__
        new_dictionary['created_at'] = self.created_at.isoformat()
        new_dictionary['updated_at'] = self.updated_at.isoformat()
        return (new_dictionary)
