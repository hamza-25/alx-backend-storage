#!/usr/bin/env python3
"""Module defines class and methods redis
"""
import redis
from typing import Union, Callable, Optional
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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """get key from redis and covert it to required format"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """parametrize Cache.get with the correct conversion function."""
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> str:
        """parametrize Cache.get with the correct conversion function."""
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
