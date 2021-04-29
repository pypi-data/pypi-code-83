#!python3
# -*- coding:utf-8 -*-
# author: difosschan
#

__all__ = ('walk',)

import os
from typing import Tuple, List
from . import get_file_info
from .log import P


def walk_tail_recursive(input_dir: str, dirs=[], files=[],
             exclude_dirs=None,
             exclude_files=None,
             exclude_extensions=None,
             include_extensions=None):
    '''walk'''
    fileList = os.listdir(input_dir)

    for file in fileList:
        # P(file=file,  _level='WARN', _must=True, _file=None)
        filePath = os.path.join(input_dir, file)
        if os.path.isdir(filePath):
            if exclude_dirs and file in exclude_dirs:
                P("IGNORE dir cause exclude-dirs", dir=file)
                continue
            dirs.append(filePath)
            walk_tail_recursive(filePath, dirs, files, exclude_dirs, exclude_files, exclude_extensions, include_extensions)

        elif os.path.isfile(filePath):
            ext = get_file_info(file)['extension']
            if exclude_files and file in exclude_files:
                P("IGNORE file cause exclude-files", file=file)
                continue
            elif exclude_extensions and ext in exclude_extensions:
                P("IGNORE file cause match exclude-extensions", file=file, ext=ext)
                continue

            if include_extensions and ext not in include_extensions:
                P("IGNORE file cause not match include-extensions",
                  file=file, ext=ext)
                continue
            files.append(filePath)


def walk(input_dir: str,
         exclude_dirs: list=None,
         exclude_files: list=None,
         exclude_extensions: list=None,
         include_extensions: list=None,
         without_root_path: bool = False,
         **kwargs) -> Tuple[List[str], List[str]]:

    dirs = []
    files = []

    walk_tail_recursive(input_dir, dirs, files, exclude_dirs, exclude_files, exclude_extensions, include_extensions)

    if without_root_path:
        if not input_dir.endswith(os.path.sep):
            input_dir = input_dir + os.path.sep
        input_dir_byte_len = len(input_dir)
        dirs = [x[input_dir_byte_len:] for x in dirs]
        files = [x[input_dir_byte_len:] for x in files]

    return dirs, files
