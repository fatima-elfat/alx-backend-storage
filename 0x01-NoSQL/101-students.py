#!/usr/bin/env python3
"""
Task 14: Top students.
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score.
    The average score must be part of each item
    returns with key = averageScore.
    """
    top_stdts = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])
    return top_stdts
