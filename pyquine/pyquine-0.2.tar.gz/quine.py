"""Upon import, print the source of the main module."""

import inspect
import __main__

try:
    source = inspect.getsource(__main__)
except TypeError:  # In interactive mode, __main__ has no source.
    pass
else:
    print(source, end='')
