#!/usr/bin/python3

"""Method that is used to create a unique
FileStorage instance of our Hbnb Application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
