#!/usr/bin/env python3
"""
Changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """Update all topics of a school document based on its name"""
    if mongo_collection is None:
        return
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
