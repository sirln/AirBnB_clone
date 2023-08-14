#!/usr/bin/python3
'''
BaseModel Class Unit Test Module
'''
import models
import unittest
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    # ----------------------- Docstring Testing -------------------------
    def test_module_docstring(self):
        '''
        Test if base_model module has a docstring.
        '''
        doc = models.base_model.__doc__
        msg1 = f'Module base_model should have a docstring'
        msg2 = f'Module base_model docstring should not be empty'
        self.assertIsNotNone(doc, msg1)
        self.assertTrue(len(doc) > 1, msg2)

    def test_class_docstring(self):
        '''
        Test if the class BaseModel has a docstring.
        '''
        doc = BaseModel.__doc__
        msg1 = f'Class BaseModel should have a docstring'
        msg2 = f'Class docstring should not be empty'
        self.assertIsNotNone(doc, msg1)
        self.assertTrue(len(doc) > 1, msg2)

    def test_class_methods_docstring(self):
        '''
        Test if class methods have docstrings
        '''
        class_methods = [
                            method for method in dir(BaseModel)
                            if (not method.startswith('__')
                                or method == '__str__')
                            and callable(getattr(BaseModel, method))
                        ]
        for method in class_methods:
            doc = getattr(BaseModel, method).__doc__
            msg1 = f'Method {method} should have docstring'
            msg2 = f'Method {method} docstring should not be empty'
            self.assertIsNotNone(doc, msg1)
            self.assertTrue(len(doc) > 1, msg2)

    # ----------------------- Instantiation Testing ----------------------
    def test_base_model_init_with_kwargs(self):
        """Tests initialization of BaseModel with kwargs."""
        _id = str(uuid4())
        time = datetime.now()
        iso_time = time.isoformat()
        b = BaseModel(id=_id, created_at=iso_time, updated_at=iso_time)
        self.assertEqual(b.id, _id)
        self.assertEqual(b.created_at, time)
        self.assertEqual(b.updated_at, time)


if __name__ == '__main__':
    unittest.main()
