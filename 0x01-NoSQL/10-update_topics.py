#!/usr/bin/env python3
# 10-update_topics.py
"""
change school topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update many rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
