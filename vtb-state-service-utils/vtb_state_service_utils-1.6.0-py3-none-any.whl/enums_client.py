import hashlib
import os
from enum import Enum
from typing import Optional

import requests
import ujson
from envparse import env


class EnumsClient:
    __slots__ = ('_data', '_url', '_hash_sum', '_cache_file', '_timeout')

    def __init__(self, url, timeout, cache_file=None):
        self._url = url
        self._timeout = timeout
        self._cache_file = cache_file
        self._data = dict()  # `name`:`enum`
        self._hash_sum = None  # store hash sum for comparing

        try:
            self.update_from_remote()  # try to update from external
        except requests.RequestException as error:
            if cache_file is None:
                raise error
            self.update_from_cache()  # try to update from cache

    def __getattr__(self, item):
        if item in self._data:
            return self._data[item]
        updated = self.update_from_remote()
        if not updated:
            raise AttributeError(f'No changes from the remote. Hash sums are equal.')
        if item not in self._data:
            raise AttributeError(f'Remote changes were received, but they do not contain `{item}`.')
        return self._data[item]

    def update_from_remote(self) -> bool:
        text = self.fetch_remote()
        hash_sum = _get_hash(text)
        if self._hash_sum == hash_sum:
            return False
        self._data = _deserialize(text)
        self._hash_sum = hash_sum
        self._dumps_to_cache(text)
        return True

    def update_from_cache(self) -> bool:
        if not (text := self._loads_from_cache()):
            return False
        self._data = _deserialize(text)
        self._hash_sum = _get_hash(text)
        return True

    def fetch_remote(self) -> str:
        return requests.get(url=self._url, timeout=self._timeout).text

    def _dumps_to_cache(self, text):
        if self._cache_file:
            with open(self._cache_file, 'w') as f:
                f.write(text)

    def _loads_from_cache(self):
        if not self._cache_file:
            return None
        with open(self._cache_file) as f:
            return f.read()


def _deserialize(text: str) -> dict:
    return {ref['name']: Enum(ref['name'], _create_enums_values(ref['data']))
            for ref in ujson.loads(text)}


def _create_enums_values(data: dict) -> dict:
    return {k: data[k] if data[k] is not None else k.lower() for k in data}


def _get_hash(text) -> str:
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def _initialize() -> EnumsClient:
    cache_file = None
    if env.bool('REFERENCES_USE_CACHE', default=False):
        cache_file = _create_cache_file(env.str('REFERENCES_CACHE_FILE', default='/cache_references/references.json'))
    path = env.str('REFERENCES_ENUMS_PATH', default='/api/v1/pages/?directory__name=enums')
    timeout = env.int('REFERENCES_TIMEOUT', default=1)
    url = env.str('REFERENCES_HOST_URL').rstrip('/') + path
    return EnumsClient(url, timeout, cache_file=cache_file)


def _create_cache_file(filename: str) -> Optional[str]:
    path = os.path.join(os.getcwd(), *filename.split('/'))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'a').close()
    return path


enums = _initialize()
