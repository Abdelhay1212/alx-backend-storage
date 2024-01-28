#!/usr/bin/env python3
''' Implementing an expiring web cache and tracker '''
import redis
import requests
from functools import wraps
from typing import Callable


r = redis.Redis()


def cache_response(fn: Callable) -> Callable:
    ''' cache response '''
    @wraps(fn)
    def wrapper(url: str) -> str:
        r.incr(f'count:{url}')
        cached_response = r.get(url)
        if cached_response:
            return cached_response.decode('utf-8')

        response = fn(url)
        r.setex(url, 10, response)
        r.set(f'count:{url}', 1)

        return response

    return wrapper


@cache_response
def get_page(url: str) -> str:
    ''' get page '''
    response = requests.get(url)
    return response.text
