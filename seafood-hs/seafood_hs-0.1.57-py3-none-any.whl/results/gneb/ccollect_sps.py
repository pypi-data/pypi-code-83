r"""
This module is responsible for collecting saddle point images for further evaluation
"""
from pathlib import Path
from python3.shell_commands import copy_element
import os


class CCollectSps:
    r"""
    Class for collecting saddlepoint of calculations within directory
    """

    def __init__(self, calcdir: Path = Path.cwd(), resultdir: Path = Path.cwd().parent / 'sps',
                 subfoldername: str = 'gneb_onep') -> None:
        r"""
        Initializes the collection
        """
        resultdir.mkdir(exist_ok=False)
        self._calcdir = calcdir
        self._resultdir = resultdir
        self._subfoldername = subfoldername

    def __call__(self) -> None:
        r"""
        Calls the collection of saddlepoints
        """
        for folder in os.listdir(str(self._calcdir)):
            if (self._calcdir / str(folder) / self._subfoldername).is_dir():
                copy_element(self._calcdir / str(folder) / self._subfoldername / 'image-GNEB-saddlepoint.dat',
                             self._resultdir / f'sp_{folder}.dat')
            else:
                print(f'Folder {self._subfoldername} not present in {folder} -> skip')
