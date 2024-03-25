#!/usr/bin/env python3
""" inserts a new document in a collection based on kwargs"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """function that Insert a documents in a collection"""
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
