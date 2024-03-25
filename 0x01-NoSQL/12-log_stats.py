#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs"""
import pymongo


def get_logs_stats(mongo_collection):
    """ provides some stats about Nginx logs stored in MongoDB"""
    methods = {'GET': 0, 'POST': 0, 'PUT': 0, 'PATCH': 0, 'DELETE': 0}
    results = mongo_collection.find()
    count = 0
    status = 0
    for obj in results:
        count += 1
        if obj['method'] in methods.keys():
            methods[obj['method']] += 1
        if obj['path'] == '/status':
            status += 1
    print("{} logs \n\tmethod GET: {}\n\tmethod POST: {}\n\tmethod PUT: {}\n\t\
        method PATCH: {}\n\tmethod DELETE: {}\n{} status check"
          .format(count, methods["GET"], methods["POST"],
                  methods["PUT"], methods["PATCH"], methods["DELETE"], status))


if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['logs']
    collection = db['nginx']
    get_logs_stats(collection)
