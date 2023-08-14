#!/usr/bin/python3
'''
Module to instantiate a storage object
'''

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
