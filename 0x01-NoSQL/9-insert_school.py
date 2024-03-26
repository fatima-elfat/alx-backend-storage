#!/usr/bin/env python3
"""
Task 9: Insert a document in Python.
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs.
    """
    _id = mongo_collection.insert(kwargs)
    return _id
