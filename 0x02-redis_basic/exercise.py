#!/usr/bin/env python3

import uuid
import redis
from functools import wraps
from typing import Union, Callable
''' Writing strings to Redis '''


def count_calls(method: Callable) -> Callable:
    ''' count method calls '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f'{method.__qualname__}'
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    ''' call method history '''
    @wraps(method)
    def wrapper(self, *args):
        input_key = f'{method.__qualname__}:inputs'
        self._redis.rpush(input_key, str(args))

        output_key = f'{method.__qualname__}:outputs'
        output = method(self, *args)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


class Cache:
    ''' cache class '''

    def __init__(self) -> None:
        ''' init the class '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
