# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

class Strategy:
    def __init__(self, definition):
        self.matrix = definition.get("matrix")
        self.fail_fast = definition.get("fail-fast")
        self.max_parallel = definition.get("max-parallel")