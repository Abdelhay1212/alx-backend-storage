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

    def store(self, data: Union[int, float, str, bytes]) -> str:
        ''' store data '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
