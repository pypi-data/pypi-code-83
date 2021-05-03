''' Filter Paths Out

Related functions to filter out
paths.
'''

import fnmatch
import os
from collections.abc import Callable, Iterable
from pathlib import Path
from tarpy.utils import check_symlink, check_existence


def should_exclude(path: str, exclusions: list[str]) -> bool:
    ''' Should Exclude

    This module checks against fnmatch and
    returns a bool.

    Parameters
    ----------
    path : str
        A Path to check against fnmatch.
    exclusions : list[str]
        The list with exclusions.

    Returns
    -------
     : bool
        True if it matches at least on of
        the exclusions.
        False if not.
    '''
    return any(fnmatch.fnmatch(path, exclude) for exclude in exclusions)

def filter_paths(source: str, rule: Callable[str], exclusions: list[str]) -> Iterable[str]:
    ''' Filter Paths

    It is filtering out paths like defined in
    self.should_exclude.
    Is returning then the path as a string.

    Parameters
    ----------
    source : str
        The corresponding Path.
    rule : Callable[str]
        A function which is checking if to
        filter or not.
    exclusions : list[str]
        The list of exclusions.

    Returns
    -------
        : Iterable[str]
        A Generator with only "good" Paths.
    '''
    if (
            not rule(source, exclusions) and
            source is not None and
            not check_symlink(source) and
            check_existence(source)
        ):
        yield source

def filtered_walk(source: Path, exclusions: list[str]) -> Iterable[str]:
    ''' Filtered Walk over Paths

    This method acts like a generator.
    It yields all paths except those filtered out liked defined
    in the EXCLUSIONS.

    Returns
    -------
        : Iterable[str]
        A Generator giving the filtered Paths.
    '''
    for root, dirs, files in os.walk(source):
        try:
            for directory in dirs:
                tmp_dir = os.path.realpath(os.path.join(root, directory))
                yield from filter_paths(tmp_dir, should_exclude, exclusions)
            for elem in files:
                tmp_file = os.path.realpath(os.path.join(root, elem))
                yield from filter_paths(tmp_file, should_exclude, exclusions)

        except PermissionError:
            continue
        except FileNotFoundError:
            continue
