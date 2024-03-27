#!/usr/bin/env python3
"""
task 5: Implementing an expiring web cache and tracker.
answer using the same thing as task 2.
Bonus: implement this use case with decorators.
"""
from functools import wraps
import redis
import requests
from typing import Callable

_redis = redis.Redis()


def count_reqsts(
        method: Callable
        ) -> Callable:
    """
    how many times a particular
    URL was accessed in the key "count:{url}"
    """

    @wraps(method)
    def wrapper(url):
        """
        cache the result with
        an expiration time of 10 seconds.
        """
        _redis.incr("count:{}".format(url))
        txt = "results:{}".format(url)
        r = _redis.get(txt)
        if r:
            return r.decode("utf-8")
        r = method(url)
        _redis.setex(txt, 10, r)
        return r
    return wrapper


@count_reqsts
def get_page(url: str) -> str:
    """
    uses the requests module to obtain the
    HTML content of a particular URL and returns it.
    """
    return requests.get(url).text
