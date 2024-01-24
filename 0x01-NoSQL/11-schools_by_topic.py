#!/usr/bin/env python3
''' Where can I learn Python? '''


def schools_by_topic(mongo_collection, topic):
    ''' school by topic '''
    res = list(mongo_collection.find({topic: {'$in': 'topics'}}))
    return res
