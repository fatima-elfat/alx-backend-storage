#!/usr/bin/env python3
"""
Task 15: Log stats - new version.
"""

from pymongo import MongoClient


def get_stats(nginx_collection):
    """
    provides some stats about Nginx logs stored in MongoDB
    """
    _logs = nginx_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    """print("{} logs".format(_logs))"""
    print(f"{_logs} logs")
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    count = nginx_collection.count_documents(
        {
            "method": "GET",
            "path": "/status"
        })
    """print("{} status check".format(count))"""
    print(f"{count} status check")
    print("IPs:")
    logs = nginx_collection.aggregate(
        [
            {
                "$group": {"_id": "$ip", "count": {"$sum": 1}}
            },
            {"$sort": {"count": -1}},
            {"$limit": 10}
        ]
    )
    for log in logs:
        ip = log.get("_id")
        count = log.get("count")
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    server = "mongodb://127.0.0.1:27017"
    client = MongoClient(server)
    get_stats(client.logs.nginx)
