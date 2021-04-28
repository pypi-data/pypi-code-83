# encoding: utf-8
"""
exception
"""


class InvalidUrl(Exception):
    pass


class InvalidCallbackResult(Exception):
    pass


class InvalidLogLevelError(Exception):
    pass


class SpiderHookError(Exception):
    pass


class UsageError(Exception):
    """To indicate a command-line usage error"""
    def __init__(self, *a, **kw):
        self.print_help = kw.pop('print_help', True)
        super(UsageError, self).__init__(*a, **kw)
