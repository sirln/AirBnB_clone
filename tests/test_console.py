#!/usr/bin/python3
'''
Console module unittests
'''

import sys
import unittest
from io import StringIO
from models import storage
from unittest.mock import patch
from models.base_model import BaseModel
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def test_do_quit(self):
        '''Tests the do_quit method'''
        console = HBNBCommand()
        self.assertTrue(console.onecmd("quit"))

    def test_do_EOF(self):
        '''Tests the do_EOF method'''
        console = HBNBCommand()
        self.assertTrue(console.onecmd("EOF"))

    def test_emptyline(self):
        '''Tests the emptyline method'''
        console = HBNBCommand()
        self.assertFalse(console.onecmd(""))

    def test_do_create(self):
        '''Tests the do_create method'''
        console = HBNBCommand()

        # Testing missing class name
        console.onecmd("create")
        self.assertEqual("** class name missing **\n", self.held_output.getvalue())
        self.held_output.truncate(0)
        self.held_output.seek(0)

        # Testing non-existent class
        console.onecmd("create MyClass")
        self.assertEqual("** class doesn't exist **\n", self.held_output.getvalue())
        self.held_output.truncate(0)
        self.held_output.seek(0)

        # Testing valid class
        console.onecmd("create BaseModel")
        id = self.held_output.getvalue().strip()
        self.held_output.truncate(0)
        self.held_output.seek(0)
        self.assertIn("BaseModel." + id, storage.all())

    def test_do_show(self):
        '''Tests the do_show method'''
        console = HBNBCommand()

        # Testing missing class name
        console.onecmd("show")
        self.assertEqual("** class name missing **\n", self.held_output.getvalue())
        self.held_output.truncate(0)
        self.held_output.seek(0)

        # Testing non-existent class
        console.onecmd("show MyClass 1234-5678-9012")
        self.assertEqual("** class doesn't exist **\n", self.held_output.getvalue())
        self.held_output.truncate(0)
        self.held_output.seek(0)

if __name__ == "__main__":
    unittest.main()
