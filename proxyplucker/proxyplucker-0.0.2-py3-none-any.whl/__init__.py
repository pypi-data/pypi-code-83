from .freeproxylistnet import proxylist
from random import choice

class proxy:
    def __init__(self):
        self.origin = 'all'
    
    def get(self):
        return choice(proxylist(self))

    def getlist(self):
        return proxylist(self)