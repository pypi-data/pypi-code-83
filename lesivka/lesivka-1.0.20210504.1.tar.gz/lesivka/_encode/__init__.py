# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE, APOSTROPHES
from ..utils import Converter, applier
from . import (
    postprocess,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_1_7,
    rule_2_1,
    rule_2_2,
    rule_3_1,
    rule_3_2,
)

ORDER = (
    rule_2_2,
    rule_3_2,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_1_7,
    rule_2_1,
    rule_3_1,
    postprocess,
)

CYR = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' + ACUTE + APOSTROPHES

convert = applier(*(rule.convert for rule in ORDER))
encode = Converter(r'([^\w%s]+)' % (ACUTE + APOSTROPHES), CYR, convert)
