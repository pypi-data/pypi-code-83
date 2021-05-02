'''
This module contains all error classes used across the CLI.
'''


class AFError(Exception):
    '''
    Base error class, all error classes should inherit from this one.
    '''

    def __init__(self, message: str, code: int = 1) -> None:
        '''
        Creates a new error instance.

        Message will be written to stderr and code will be
        used as exit code.
        '''
        super(AFError, self).__init__(message)
        self.message = message
        self.code = code

    def __str__(self) -> str:
        '''
        Srting representation of the error,
        invoked by `str()`.
        '''
        return f'[{self.code}] {self.message}'
