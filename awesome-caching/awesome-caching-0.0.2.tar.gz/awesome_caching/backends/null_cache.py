# -*- coding: utf-8 -*-

from .base_cache import BaseCache


class NullCache(BaseCache):
    """A cache that doesn't cache. This can be useful for unit testing."""

    def has(self, key):
        return False
