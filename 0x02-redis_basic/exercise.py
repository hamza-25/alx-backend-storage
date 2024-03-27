#!/usr/bin/env python3
"""Define Cache class
"""
import redis
from typing import Union
from uuid import uuid1


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """store an instance of the Redis client"""
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, float, bytes, int]) -> str:
        """return id as string and set on redis data"""
        id = str(uuid1())
        self.__redis.set(id, data)
        return id
