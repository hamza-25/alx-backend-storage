#!/usr/bin/env python3
"""Module defines class and methods redis
"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """declares Cache redis class"""
    def __init__(self):
        """store an instance of the Redis client"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """return id as string and set on redis data"""
        id = str(uuid4())
        self._redis.set(id, data)
        return id
