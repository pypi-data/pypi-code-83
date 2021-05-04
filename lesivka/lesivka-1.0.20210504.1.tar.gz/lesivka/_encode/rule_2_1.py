# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from itertools import product

from ..diacritics import ACUTE
from ..utils import applier, replacer, translator

IN, OUT = 'І', 'I'
AFTER = 'AEIOUJ' + ACUTE


def get_step2():
    data = product(AFTER + AFTER.lower(), OUT + OUT.lower())
    repl = replacer({c + ACUTE + i: c + i for c, i in data})

    def _(text):
        text = repl(text)
        return text.lstrip(ACUTE)

    return _


step1 = translator({IN: ACUTE + OUT, IN.lower(): ACUTE + OUT.lower()})

convert = applier(step1, get_step2())
