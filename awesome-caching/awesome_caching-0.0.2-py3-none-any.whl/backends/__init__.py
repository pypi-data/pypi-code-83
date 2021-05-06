# -*- coding: utf-8 -*-
"""
    awesome_caching.backends
    ~~~~~~~~~~~~~~~~~~~~~~

    Various caching backends.
"""
from .null_cache import NullCache

from .redis_cache import (
    RedisCache,
    RedisSentinelCache,
    RedisClusterCache,
)
from .simple_cache import SimpleCache

__all__ = (
    "null",
    "simple",
    "redis",
    "redis_sentinel",
    "redis_cluster",
    "NullCache",
    "SimpleCache",
    "RedisCache",
    "RedisSentinelCache",
    "RedisClusterCache",
)


def null(config, args, kwargs):
    return NullCache.factory(config, args, kwargs)


def simple(config, args, kwargs):
    return SimpleCache.factory(config, args, kwargs)


def redis(config, args, kwargs):
    return RedisCache.factory(config, args, kwargs)


def redis_sentinel(config, args, kwargs):
    return RedisSentinelCache.factory(config, args, kwargs)


def redis_cluster(config, args, kwargs):
    return RedisClusterCache.factory(config, args, kwargs)
