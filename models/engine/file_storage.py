##!/usr/bin/python3
'''
FileStorage Module
'''
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
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
    __file_path = 'siso.json'
    __objects = {}

    def all(self):
        '''
        Returns dictionary containing object
        class name and object id.

        Returns
        -------
        dict
            returns the __object attribute
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Initializes an object with a key

        Arguments
        -------
        obj : dict
            set __object with obj variable
        '''
        key = f'{type(obj).__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serialize objects in __objects dictionary into
        the JSON file initialied in __file_path attribute
        '''
        filename = FileStorage.__file_path
        with open(filename, 'w') as file:
            json_objects = {key: value.to_dict()
                            for key, value in FileStorage.__objects.items()}
            json.dump(json_objects, file)

    def reload(self):
        '''
        Deserialize JSON file in (__file_path) class attribute.
        Otherwise, do nothing. Does not raise an exception if
        file is not found
        '''
        filename = FileStorage.__file_path
        if path.exists(filename):
            with open(filename, 'r') as file:
                json_object = json.load(file)
                for key, value in json_object.items():
                    class_name = value['__class__']
                    s_class = eval(class_name)
                    new_object = s_class(**value)
                    # i.e new_object = eval(Basemodel(**value))
                    # new_object = eval((value['__class__'](**value))
                    FileStorage.__objects[key] = new_object
