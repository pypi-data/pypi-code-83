import os
import random
from sys import argv

from termcolor import cprint

from run.startup import start_up
from settings.config import if_config_type
from system.platform import get_platform

start_up()


def print_start_name(name, weight, name_col, border_col):
    space_no = weight - len(name) - 2
    space_no = int(space_no / 2)
    cprint('-' * weight, border_col)
    cprint('|' + ' ' * space_no, border_col, end='')
    cprint(name, name_col, end='')
    cprint(' ' * space_no + '|', border_col)
    cprint('-' * weight, border_col)


def cp_start():
    try:

        color = ['magenta', 'yellow', 'cyan', 'blue']
        pt = 50
        name_col = random.choice(color)
        border_col = random.choice(color)
        print_start_name('ai-virtual-assistant', 50, name_col, border_col)

        pt = '-' * pt
        cprint(pt, border_col)
        from tools.OJ.cp import cp_manager

        lt = list(argv)
        lt = lt[1:]
        msg = ''
        for w in lt:
            msg += w + ' '

        if if_config_type(msg):
            return

        status = cp_manager(msg.strip())

        cprint(pt, border_col)
        cprint(f' (^-^) -> Good luck sir.', 'green')
        cprint(pt, border_col)
        if status == '$SHELL':
            if get_platform() != 'Windows':
                os.system('$SHELL')

    except Exception as e:
        print(e)
        cprint("Can't open sir.", 'red')
