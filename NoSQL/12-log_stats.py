#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def main():
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(m, collection.count_documents({"method": m})))
    print("{} status check".format(
        collection.count_documents({"method": "GET", "path": "/status"})
    ))


if __name__ == "__main__":
    main()
