import sys
import os


def abort(msg: str, code: int = 1):
    print(msg, file=sys.stderr)
    sys.exit(code)
