from ksl_util import time
from functools import wraps


def current_time():
    now = time.localtime()
    r_time = "%04d%02d%02d__%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

    return r_time

def current_date():
    now = time.localtime()
    r_time = "%04d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday)

    return r_time

class time_checker:
    def __init__(self):
        self.__start__      = 0
        self.__end__        = 0

    def start(self):
        self.__start__ = time.time()

    def end(self, printable=True):
        self.__end__ = time.time()
        timer = self.__end__ - self.__start__
        if printable: print('time : ', timer, '(s)')
        return timer


def TimeCheck(func):
    def wrapeer(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            tc = time_checker()
            tc.start()
            result = func(*args, **kwargs)
            print('{:<30} : '.format(func.__name__), tc.end(printable=False), '(s)')
            return result
        return decorated
    return wrapeer(func)

def Sleep(__time):
    def wrapeer(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            time.sleep(__time)
            result = func(*args, **kwargs)
            return result
        return decorated
    return wrapeer


