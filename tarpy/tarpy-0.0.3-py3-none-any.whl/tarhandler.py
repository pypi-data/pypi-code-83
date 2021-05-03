#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' Make TAR Archive

'''

import os
import tarfile

# Internal Imports
from tarpy import config
from tarpy.utils import real_path
from tarpy.filters import filtered_walk


class TarArchive:
    ''' TAR Archive

    Attributes
    ----------
    EXCLUSIONS : list
        A list of strings for extra exclusions.

    Parameters
    ----------
    start_point : str
        The most top path to start archiving from.
        For extracting TAR archives it is the file-
        name of the Archive to esxtract.
    target_dir : str
        The target Path of the TAR Operation.
    exclude_file : str
        The Path of the file with defined exclusions.
    compression : str
        Compression Mode.
    mode : str
        Which Operation on Tar Archive;
        private.
    '''
    EXCLUSIONS = []

    def __init__(self,
            start_point: str,
            target_dir: str,
            exclude_file: str,
            compression: str,
            mode: str,
            ) -> None:
        self.start_point = str(real_path(start_point))
        self.target_dir = str(real_path(target_dir)) if target_dir else None
        self.exclude_file = str(real_path(exclude_file)) if exclude_file else None
        self.compression = compression if compression else None
        self._mode = mode

        # Make sure Exclusions are set.
        self.add_exclusions()

    def add_exclusions(self, *excludes) -> None:
        ''' Set own Exclusions

        There have to be some program related
        exclusions (e.g. the directory of this
        script) independently from the user
        defined exclusions from the file.

        Parameters
        ----------
        *excludes : tuple
            A Tuple containing exclusions re-
            presented by strings.
        '''
        if excludes:
            for elem in excludes:
                self.EXCLUSIONS.append(elem)

        # self.EXCLUSIONS.append(str(self.target_dir))

        # If there is a Blacklist file:
        if self.exclude_file:
            with open(self.exclude_file, 'r') as ex_f:
                for exclude in ex_f.readlines():
                    if exclude != '\n':
                        self.EXCLUSIONS.append(exclude.strip('\n'))

    def tar_writer(self) -> None:
        ''' Write TAR Archive

        Method for writing the archive.
        '''
        name = str(real_path(
                f'{self.target_dir}/{config.SYSTEMNAME}_{config.TODAY}.tar'
                ))
        if self.compression:
            name += f'.{self.compression}'

        with tarfile.open(
                name,
                f'w:{self.compression if self.compression else ""}'
        ) as tar_f:

            for path in filtered_walk(self.start_point, self.EXCLUSIONS):
                # The recursive option
                # should be set to False.
                # Catch Errors
                try:
                    tar_f.add(path, recursive=False)
                except FileNotFoundError:
                    pass
                except PermissionError:
                    pass

    def tar_extractor(self) -> None:
        ''' Extract TAR Archive

        Method for extracting the archive.
        '''
        if self.target_dir:
            os.chdir(self.target_dir)
        with tarfile.open(
                self.start_point,
                f'r:{self.compression if self.compression else ""}'
        ) as tar_f:
            try:
                tar_f.extractall()
            except PermissionError:
                pass

    def tar_appender(self) -> None:
        ''' Append on existing TAR Archive
        '''
        ...

    def tar_inspector(self) -> None:
        ''' Inspect Content uf TAR Archive
        '''
        ...

    def __repr__(self) -> str:
        return (f'Class: {self.__class__.__name__!r}\n'
                f'Start from: {str(self.start_point)!r}\n'
                f'Target Directory: {str(self.target_dir)!r}\n'
                f'Compression: {self.compression!r}\n'
                f'Exclude File: {str(self.exclude_file)!r}\n'
                )

    def __str__(self) -> str:
        return (f'Source: {str(self.start_point)}\n'
                f'Target: {str(self.target_dir)}\n'
                f'Compression: {self.compression}\n'
                f'Exclusions: {self.EXCLUSIONS}\n'
                f'Mode: {self._mode}\n'
                )

    def __call__(self, verbose: bool) -> str:
        ''' Make this class callable
        '''

        if verbose:
            print(self.__str__())
        if self._mode == 'w':
            self.tar_writer()
        elif self._mode == 'e':
            self.tar_extractor()
