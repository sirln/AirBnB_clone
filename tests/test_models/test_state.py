#!/usr/bin/python3
'''
State Class Unit Test Module
'''
import models
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    # ----------------------- Docstring Testing -------------------------
    def test_module_docstring(self):
        '''
        Test if base_model module has a docstring.
        '''
        doc = models.state.__doc__
        msg1 = f'Module base_model should have a docstring'
        msg2 = f'Module base_model docstring should not be empty'
        self.assertIsNotNone(doc, msg1)
        self.assertTrue(len(doc) > 1, msg2)

    def test_class_docstring(self):
        '''
        Test if the class BaseModel has a docstring.
        '''
        doc = State.__doc__
        msg1 = f'Class BaseModel should have a docstring'
        msg2 = f'Class docstring should not be empty'
        self.assertIsNotNone(doc, msg1)
        self.assertTrue(len(doc) > 1, msg2)


    def setUp(self):
        '''
        Setup test instance of State
        '''
        self.state = State()

    def test_instance(self):
        '''
        Test if instance of State class
        '''
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        '''
        Test if the State instance has the attribute and if they're initialized correctly
        '''
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_inherits_BaseModel(self):
        '''
        Test if State is a subclass of BaseModel
        '''
        self.assertTrue(issubclass(State, BaseModel))

    def tearDown(self):
        '''
        Teardown test instance
        '''
        del self.state

if __name__ == '__main__':
    unittest.main()
