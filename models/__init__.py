#!/usr/bin/python3
"""Runs initialization of the models module"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
