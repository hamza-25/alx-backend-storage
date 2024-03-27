#!/usr/bin/env python3
"""Module defines func web cache and tracker
"""
import requests
from functools import wraps
import redis

ins_redis = redis.Redis()


def count_url_access(method):
    """ track how many times a particular URL was accessed """
    @wraps(method)
    def wrapper(url):
        cached_key = f"cached:{url}"
        cached_data = ins_redis.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = f"count:{url}"
        html_content = method(url)

        ins_redis.incr(count_key)
        ins_redis.set(cached_key, html_content)
        ins_redis.expire(cached_key, 10)
        return html_content
    return wrapper

@count_url_access
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text
