''' Utils

Module of tarpy.
'''

import os
import pathlib


def real_path(path: str) -> pathlib.PosixPath[str]:
    ''' Real Paths

    Makes sure to get a real Path.
    '''
    try:
        return pathlib.Path(path).resolve()
    except TypeError:
        pass

def check_existence(to_check: str) -> bool:
    ''' Check if File / Directory
        exists or not
    '''
    if not os.path.exists(to_check):
        return False
    return True

def check_symlink(to_check: str) -> bool:
    ''' Check if File is a Symlink
    '''
    return pathlib.Path(to_check).is_symlink()
