from os import system

from termcolor import cprint

from system.platform import get_platform

color = ['blue', 'yellow', 'green']


def line_sep(t=1):
    for i in range(t):
        cprint('-' * 50, 'magenta')


def thoughts_processing(msg):
    x = ('.' * 10 + msg + '.' * 10)
    cprint(x, 'magenta')


def command_sep():
    x = ('-' * 23 + 'X-X-X' + '-' * 22)
    cprint(x, 'magenta')


def clear_screen():
    if get_platform() == 'windows':
        _ = system('cls')
    else:
        _ = system('clear')
