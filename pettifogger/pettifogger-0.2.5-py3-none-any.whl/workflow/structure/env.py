# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

import re


class Env(dict):
    key_re = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")
    ENV_VAR_REGEX = re.compile(r"\${{0,1}([a-zA-Z_][a-zA-Z0-9_]*)}{0,1}")
    SUSPECTED_ENV_VARS_REGEX = re.compile(r"(?<!\$)\b([A-Z_][A-Z0-9_]*|{[A-Z_][A-Z0-9_]*})\b")
    ENV_VAR_DEFINITION_REGEX = re.compile(r"{{0,1}(?P<key>[a-zA-Z_][a-zA-Z0-9_]*)}{0,1}=(?P<value>.*)")
    # SUSPECTED_ENV_VARS_REGEX = r"(?<!\$)\{{0,1}\b([A-Z_][A-Z0-9_]*)\}{0,1}\b"

    def __init__(self, env, *args, **kwargs):
        for key, value in env.items():
            if not Env.key_re.match(key):
                print(f"Key {key} does not follow the standard *nix environment variable format")
        super().__init__(**env, **kwargs)