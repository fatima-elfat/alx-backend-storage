#!/usr/bin/env python3
"""
Task 8: List all documents in Python.
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection.
    """
    return [document for document in mongo_collection.find()]
