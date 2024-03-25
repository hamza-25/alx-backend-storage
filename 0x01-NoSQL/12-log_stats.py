#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs"""
import pymongo


def get_logs_stats(mongo_collection):
    """ provides some stats about Nginx logs stored in MongoDB"""
    methods = {'GET': 0, 'POST': 0, 'PUT': 0, 'PATCH': 0, 'DELETE': 0}
    results = mongo_collection.find()
    count = 0
    status_check = 0
    for obj in results:
        count += 1
        if obj['method'] in methods.keys():
            methods[obj['method']] += 1
        if obj['path'] == '/status' and obj['method'] == 'GET':
            status_check += 1
    print("{} logs\nMethods:\n\tmethod GET: {}\n\tmethod POST: {}\n\t\
method PUT: {}\n\tmethod PATCH: {}\n\tmethod DELETE: {}\n{} status check"
          .format(count, methods["GET"], methods["POST"],
                  methods["PUT"], methods["PATCH"],
                  methods["DELETE"], status_check))


if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['logs']
    collection = db['nginx']
    get_logs_stats(collection)

# from pymongo import MongoClient


# METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


# def log_stats(mongo_collection, option=None):
#     """
#     Prototype: def log_stats(mongo_collection, option=None):
#     Provide some stats about Nginx logs stored in MongoDB
#     """
#     items = {}
#     if option:
#         value = mongo_collection.count_documents(
#             {"method": {"$regex": option}})
#         print(f"\tmethod {option}: {value}")
#         return

#     result = mongo_collection.count_documents(items)
#     print(f"{result} logs")
#     print("Methods:")
#     for method in METHODS:
#         log_stats(nginx_collection, method)
#     status_check = mongo_collection.count_documents({"path": "/status"})
#     print(f"{status_check} status check")


# if __name__ == "__main__":
#     nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
#     log_stats(nginx_collection)
