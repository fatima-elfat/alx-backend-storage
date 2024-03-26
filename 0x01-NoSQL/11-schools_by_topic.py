#!/usr/bin/env python3
"""
Task 11: Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic.
    """
    search = {"topics": topic}
    return [document for document in mongo_collection.find(search)]
