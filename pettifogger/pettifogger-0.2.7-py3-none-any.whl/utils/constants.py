# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

ENV_VAR_REGEX = r"\$\{{0,1}([a-zA-Z_][a-zA-Z0-9_]*)\}{0,1}"
# SUSPECTED_ENV_VARS_REGEX = r"(?<!\$)\{{0,1}\b([A-Z_][A-Z0-9_]*)\}{0,1}\b"
SUSPECTED_ENV_VARS_REGEX = r"(?<!\$)\b((?:[A-Z_][A-Z0-9_]*)|(?:\{[A-Z_][A-Z0-9_]*\}))\b"
ENV_VAR_DEFINITION_REGEX = r"\{{0,1}(?P<key>[a-zA-Z_][a-zA-Z0-9_]*)\}{0,1}=(?P<value>.*)"