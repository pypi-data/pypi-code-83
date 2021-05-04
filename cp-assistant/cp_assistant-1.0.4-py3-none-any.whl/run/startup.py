import os
from settings.first_load import check_if_first_time
from system.platform import get_platform


def start_up():
    if get_platform() == 'Windows':
        os.system('color')
    check_if_first_time()
