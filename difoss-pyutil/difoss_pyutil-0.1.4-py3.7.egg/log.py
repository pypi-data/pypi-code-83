#!python3
# -*- coding:utf-8 -*-
# author: difosschan
#

__all__ = (
    'set_printable',
    'colorful_level',
    'colorful_key_value',
    'P',
)

import json
import sys

import click

__printable = False


def set_printable(d: bool):
    global __printable
    __printable = d


def colorful_level(level: str) -> str:
    level = level.upper()
    if level == 'DEBUG':
        return click.style('[D]', fg='green')
    elif level == 'INFO':
        return click.style('[I]', fg='cyan')
    elif level == 'WARNING' or level == 'WARN':
        return click.style('[W]', fg='magenta')
    elif level == 'ERROR':
        return click.style('[E]', fg='red')

    return level


def colorful_key_value(k, v, key_color='green', value_color=None) -> str:
    return '%s=%s' % (click.style(str(k), fg=key_color), click.style(str(v), fg=value_color))


def P(*args, **kwargs):
    must = kwargs.pop('_must', False)
    global __printable
    if must or __printable:
        key_color = kwargs.pop('_key_color', 'green')
        value_color = kwargs.pop('_value_color', None)
        level = kwargs.pop('_level', 'DEBUG')
        file = kwargs.pop('_file', sys.stderr)
        indent = kwargs.pop('_indent', None)

        print(colorful_level(level), *args,
              ', '.join([colorful_key_value(k, v if not indent else json.dumps(v, indent=indent, ensure_ascii=False), key_color, value_color)
                         for k, v in kwargs.items()]),
              file=file)
