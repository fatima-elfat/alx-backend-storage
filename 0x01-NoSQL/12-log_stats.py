#!/usr/bin/env python3
"""
Task 12: Log stats.
"""

from pymongo import MongoClient


def get_stats(nginx_collection):
    """
    provides some stats about Nginx logs stored in MongoDB
    """
    _logs = nginx_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('{} logs'.format(_logs))
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print('\tmethod {}: {}'.format(method, count))
    stats = nginx_collection.count_documents(
        {
            "method": "GET",
            "path": "/status"
        })
    print('{} status check'.format(stats))


if __name__ == "__main__":
    server = 'mongodb://127.0.0.1:27017'
    get_stats(MongoClient(server).logs.nginx)