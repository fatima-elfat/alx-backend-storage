#!/usr/bin/env python3
"""
Task 0-4 : Redis basic.
"""
from functools import wraps
import redis
from typing import Union, Optional, Callable
from uuid import uuid4, UUID


def count_calls(
        method: Callable
        ) -> Callable:
    """
    task 2.
    count how many times methods of
    the Cache class are called
    """
    # As a key, use the qualified name
    # of method using the __qualname__ dunder method.
    _key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        increments the count for that key every
        time the method is called and returns
        the value returned by the original method.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(_key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(
        method: Callable
        ) -> Callable:
    """
    task 3.
    store the history of inputs and outputs
    for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        retrieve the output.
        Pro tip: Store the output using rpush
        in the "...:outputs" list, then return the output.
        """
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        key_output = str(method(self, *args, **kwargs))
        self._redis.rpush(
            method.__qualname__ + ":outputs",
            key_output)
        return key_output
    return wrapper


def replay(fn: Callable) -> None:
    """
    task 4.
    display the history of calls of a particular function.
    """
    fn_name = fn.__qualname__
    _redis = redis.Redis()
    h = _redis.get(fn_name)
    try:
        h = h.decode("utf-8")
    except Exception:
        h = 0
    print("{} was called {} times:".format(fn_name, h))
    ins = fn_name + ":inputs"
    inputs = _redis.lrange(ins, 0, -1)
    outs = fn_name + ":outputs"
    outputs = _redis.lrange(outs, 0, -1)
    for input, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
            fn_name,
            input.decode("utf-8"),
            output.decode("utf-8")
        ))


class Cache:
    """
    Writing strings to Redis.
    """

    def __init__(self):
        """
        task 0.
        store an instance of the Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        task 0.
        generate a random key (e.g. using uuid),
        store the input data in Redis using the random
        key and return the key.
        """
        _key = str(uuid4())
        self._redis.set(_key, data)
        return _key

    def get(self,
            key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """
        task 1.
        convert the data back to the desired format.
        """
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        """
        task 1.
        automatically parametrize Cache.
        get with the correct conversion function.
        """
        val = self._redis.get(key)
        try:
            val = val.decode("utf-8")
        except Exception:
            val = ""
        return val

    def get_int(self, key: str) -> int:
        """
        task 1.
        automatically parametrize Cache.
        get with the correct conversion function.
        """
        val = self._redis.get(key)
        try:
            val = int(val.decode("utf-8"))
        except Exception:
            val = 0
        return val
