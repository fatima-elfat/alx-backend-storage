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
        docs = nginx_collection.find({"method": method})
        count = len(list(docs))
        print('\tmethod {}: {}'.format(method, count))
    stats = nginx_collection.find(
        {
            "method": "GET",
            "path": "/status"
        })
    count = len(list(stats))
    print('{} status check'.format(count))


if __name__ == "__main__":
    server = 'mongodb://127.0.0.1:27017'
    client = MongoClient(server)
    get_stats(client.logs.nginx)
