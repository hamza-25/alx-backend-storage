#!/usr/bin/env python3
"""List all documents in Python Mongodb"""
import pymongo


def list_all(mongo_collection):
    """function that lists all documents in a collection"""
    results = mongo_collection.find()
    if mongo_collection is None:
        return []
    return list(results)
