#!/usr/bin/env python3

import uuid
import redis
from typing import Union
''' Writing strings to Redis '''


class Cache:
    ''' cache class '''

    def __init__(self) -> None:
        ''' init the class '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' store data '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None):
        ''' get value by its data type '''
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key):
        ''' get value of key with the type of string '''
        value = self._redis.get(key)
        return str(value)

    def get_int(self, key):
        ''' get value of key with the type of integer '''
        value = self._redis.get(key)
        return int(value)
