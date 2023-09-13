#!/usr/bin/python3
'''
BaseModel Class Unit Test Module
'''
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    # ----------------------- Docstring Testing -------------------------
    def test_module_docstring(self):
        '''
        Test if file_storage module has a docstring.
        '''
        doc = models.engine.file_storage.__doc__
        msg1 = f'Module file_storage should have a docstring'
        msg2 = f'Module file_storage docstring should not be empty'
        self.assertIsNotNone(doc, msg1)
        self.assertTrue(len(doc) > 1, msg2)

    def test_class_docstring(self):
        '''
        Test if the class FileStorage has a docstring.
        '''
        doc = FileStorage.__doc__
        msg1 = f'Class FileStorage should have a docstring'
        msg2 = f'Class docstring should not be empty'
        self.assertIsNotNone(doc, msg1)
        self.assertTrue(len(doc) > 1, msg2)

    def test_class_methods_docstring(self):
        '''
        Test if class methods have docstrings
        '''
        class_methods = [
                            method for method in dir(FileStorage)
                            if (not method.startswith('__')
                                or method == '__str__')
                            and callable(getattr(FileStorage, method))
                        ]
        for method in class_methods:
            doc = getattr(FileStorage, method).__doc__
            msg1 = f'Method {method} should have docstring'
            msg2 = f'Method {method} docstring should not be empty'
            self.assertIsNotNone(doc, msg1)
            self.assertTrue(len(doc) > 1, msg2)

    # ----------------------- Initialization Testing ----------------------
    def test_models_storage_initialized(self):
        '''
        check if storage is initialized
        '''
        self.assertEqual(type(models.storage), FileStorage)

    # ----------------------- Setting Up Testing Instance -----------------
    def setUp(self):
        '''
        Setup test instance and remove previous JSON file
        '''
        self.file_storage = FileStorage()
        if os.path.exists('siso.json'):
            os.remove('siso.json')

    # ----------------------- Attribute Testing ----------------------
    def test_file_path(self):
        '''
        Test for __file_path attribute
        '''
        file = self.file_storage._FileStorage__file_path
        self.assertEqual(file, 'siso.json')

    def test_objects(self):
        '''
        Test for __objects attribute
        '''
        self.assertIsInstance(self.file_storage._FileStorage__objects, dict)

    # ----------------------- Methods Testing ----------------------
    def test_all(self):
        '''
        Test for all() method
        '''
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 0)

    def test_new(self):
        '''
        Test for new() method
        '''
        new_base_model = BaseModel()
        self.file_storage.new(new_base_model)
        key = f'{type(new_base_model).__name__}.{new_base_model.id}'
        self.assertIn(key, self.file_storage.all())

    def test_save(self):
        '''
        Test for save() method
        '''
        new_base_model = BaseModel()
        self.file_storage.new(new_base_model)
        self.file_storage.save()
        self.assertTrue(os.path.exists('siso.json'))
        with open('siso.json', 'r') as f:
            data = json.load(f)
            key = f'{type(new_base_model).__name__}.{new_base_model.id}'
            self.assertIn(key, data)

    def test_reload(self):
        '''
        Test for reload() method
        '''
        new_base_model = BaseModel()
        self.file_storage.new(new_base_model)
        self.file_storage.save()
        self.file_storage._FileStorage__objects = {}
        self.file_storage.reload()
        key = f'{type(new_base_model).__name__}.{new_base_model.id}'
        self.assertIn(key, self.file_storage.all())

    def tearDown(self):
        '''
        Tear down test instance and remove JSON file
        '''
        if os.path.exists('siso.json'):
            os.remove('siso.json')


if __name__ == '__main__':
    unittest.main()
