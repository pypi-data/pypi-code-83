import os

from system.platform import get_platform


def start_up():
    if get_platform() == 'Windows':
        os.system('color')
