"""jyk jyk exceptions"""


class jykCriticalError(Exception):
    """jyk critical error"""


class jykLoggingError(jykCriticalError):
    """jyk scan error"""
