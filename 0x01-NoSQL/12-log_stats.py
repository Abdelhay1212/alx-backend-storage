#!/usr/bin/env python3
''' Log stats '''
from pymongo import MongoClient


def stats_about_nginx_logs(collection):
    ''' stats about Nginx logs '''

    # count documents in nginx collection
    num_collections = collection.count_documents({})

    # count documents in nginx collection for every method
    get_method = collection.count_documents({'method': 'GET'})
    post_method = collection.count_documents({'method': 'POST'})
    put_method = collection.count_documents({'method': 'PUT'})
    patch_method = collection.count_documents({'method': 'PATCH'})
    delete_method = collection.count_documents({'method': 'DELETE'})

    # status check
    num_checks = collection.count_documents({'path': '/status'})

    # print the stats
    print(f'''
{num_collections} logs
Methods:
    method GET: {get_method}
    method POST: {post_method}
    method PUT: {put_method}
    method PATCH: {patch_method}
    method DELETE: {delete_method}
{num_checks} status check''')


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.logs
collection = db.nginx

# call the function and print the stats
stats_about_nginx_logs(collection)
