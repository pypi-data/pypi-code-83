# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from itertools import product

from ..diacritics import ACUTE
from ..utils import applier, replacer

IN, OUT = 'I', 'І'
AFTER = 'AEIOU'


def get_step2():
    data = {c + i: c + o for c, i, o in
            product(AFTER + AFTER.lower(), IN + IN.lower(), OUT + OUT.lower())}

    return replacer(data)


def get_step3():
    data = {i: o for i, o in product(IN + IN.lower(), OUT + OUT.lower())}
    keys = tuple(data)

    def _(text):
        if text.startswith(keys):
            return data[text[0]] + text[1:]
        return text

    return _


step1 = replacer({ACUTE + i: o for i, o in
                  product(IN + IN.lower(), OUT + OUT.lower())})

convert = applier(step1, get_step2(), get_step3())
