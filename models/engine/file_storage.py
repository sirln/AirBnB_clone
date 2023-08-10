#!/usr/bin/python3

'''
FileStorage Module
'''
from models.base_model import BaseModel
import json


class FileStorage(BaseModel):
    '''
    FileStorage Class to serialize an instance
    into a JSON file and deserialize JSON file
    into FileStorage class object/instance

    Attributes
    ----------
    __file_path : str
        file path to the location of a JSON file
    __objects : dict
        dictionary with FileStorage instances/objects

    Methods
    -------
    all()
        returns __objects attribute
    new(obj)
        set __objects attribute with key
    save()
        serialize FileStorage object (__object) into a JSON file
    reload()
        deserialize a JSON file into FileStorage object (__object)
    '''
    __file_path= './siso.json'
    __objects = {}

    def __init__(self):
        '''
        Instantiating an instance/object of FileStorage
        '''
        super().__init__(*args, **kwargs)
        dictionary = super().to_dict()
        __objects = dictionary['__class__'] + '.' + dictionary['id']

    def all(self):
        '''
        Returns dictionary containing object
        class name and object id.

        Returns
        -------
        dict
            returns the __object attribute
        '''
        return self.__objects

    @new.setter
    def new(self, obj):
        '''
        Initializes an object with a key

        Arguments
        -------
        obj : dict
            set __object with obj variable
        '''
        self.__objects[f'{type(obj).__name__}.{obj.id}'] = obj
        # self.__objects[f'{type(obj).__name__}.{obj["id"]}'] = obj

    def save(self):
        '''
        Serialize objects in __objects dictionary into
        the JSON file initialied in __file_path attribute
        '''
        filename = self.__file_path
        if self.__objects:
            with open(filename, 'w') as file:
                json.dump(self.__objects, file))

    def reload(self):
        '''
        Deserialize JSON file in (__file_path) class attribute.
        Otherwise, do nothing. Does not raise an exception if 
        file is not found
        '''
        filename = self.__file_path
        if filename:
            with open(filename, 'r') as file:
                json_object = json.load(file)
                for  key, value in json_object.items():
                    del json_object['__class__']
                    self.new()
