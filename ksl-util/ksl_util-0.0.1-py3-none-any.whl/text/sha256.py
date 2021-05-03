import hashlib


def makehash(string):

    return hashlib.sha256(string.encode()).hexdigest()