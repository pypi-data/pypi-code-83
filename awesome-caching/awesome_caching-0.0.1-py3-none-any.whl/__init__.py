import hashlib

from .cache import Cache, function_namespace

SUPPORTED_HASH_FUNCTIONS = [
    hashlib.sha1,
    hashlib.sha224,
    hashlib.sha256,
    hashlib.sha384,
    hashlib.sha512,
    hashlib.md5,
]
__all__ = [
    "Cache",
    "function_namespace"
]
