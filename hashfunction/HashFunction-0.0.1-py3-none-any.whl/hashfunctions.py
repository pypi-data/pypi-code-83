import functools as fctls


def alphanumeric_hash_function(str, n):
    return sum([ord(x) for x in str]) % n


def numeric_hash_function(num, n):
    return int(num % n)
