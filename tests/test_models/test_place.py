#!/usr/bin/python3
'''
Place Class Unit Test Module
'''
import models
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    # ----------------------- Docstring Testing -------------------------
    def test_module_docstring(self):
        '''
        Test if base_model module has a docstring.
        '''
        doc = models.place.__doc__
        msg1 = f'Module base_model should have a docstring'
        msg2 = f'Module base_model docstring should not be empty'
        self.assertIsNotNone(doc, msg1)
        self.assertTrue(len(doc) > 1, msg2)

    def test_class_docstring(self):
        '''
        Test if the class BaseModel has a docstring.
        '''
        doc = Place.__doc__
        msg1 = f'Class BaseModel should have a docstring'
        msg2 = f'Class docstring should not be empty'
        self.assertIsNotNone(doc, msg1)
        self.assertTrue(len(doc) > 1, msg2)


    def setUp(self):
        '''
        Setup test instance of State
        '''
        self.place = Place()

    def test_instance(self):
        '''
        Test if instance of State class
        '''
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        '''
        Test if the State instance has the attribute and if they're initialized correctly
        '''
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0)
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(self.place.longitude, 0.0)
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])

    def test_inherits_BaseModel(self):
        '''
        Test if State is a subclass of BaseModel
        '''
        self.assertTrue(issubclass(Place, BaseModel))

    def tearDown(self):
        '''
        Teardown test instance
        '''
        del self.place

if __name__ == '__main__':
    unittest.main()
