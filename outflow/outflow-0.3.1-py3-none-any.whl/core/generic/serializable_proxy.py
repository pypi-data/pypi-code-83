# -*- coding: utf-8 -*-
from .lazy_object_proxy import LazyObjectProxy


class SerializableProxy(LazyObjectProxy):
    def __getstate__(self):
        return {}

    def __setstate__(self, state):
        pass

    def getstate(self):
        return self.__wrapped__.__getstate__()

    def setstate(self, state):
        self.__wrapped__.__setstate__(state)
