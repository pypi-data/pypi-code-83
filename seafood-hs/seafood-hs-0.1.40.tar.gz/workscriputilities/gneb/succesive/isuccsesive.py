# -*- coding: utf-8 -*-
r"""
Abstract base class for succesive gneb calculations
"""
from abc import ABC, abstractmethod
from pathlib import Path
from python3.shell_commands import *
from typing import Dict, List


class ISuccsesive(ABC):
    r"""
    Class to inherit from if implementing succesive gneb calculation scripts
    """

    @staticmethod
    def checkgnebfiles(dir: Path = Path.cwd(), check_interlayerinput: bool = False) -> True:
        r"""
        Checks if all necessary files are present for starting a succesive gneb calculation

        Args:
            dir(Path): directory to check. Default is the cwd.

            check_interlayerinput(bool): A Flag wether a not existing interlayer.in file should raise an error. To treat
            monolayer systems correct the Default is False. For treating multilayer systems this switch has to be
            activated.

        Returns:
            boolean representing if all files are present
        """
        filespresent = []
        filespresent.append((dir / 'GNEB.in').is_file())
        filespresent.append((dir / 'inp').is_file())
        filespresent.append((dir / 'lattice.in').is_file())
        filespresent.append((dir / 'momfile_i').is_file())
        filespresent.append((dir / 'mofifle_f').is_file())
        filespresent.append((dir / 'simu.in').is_file())
        if check_interlayerinput:
            filespresent.append((dir / 'interlayer.in').is_file())
        filespresent.append((dir / 'image-GNEB_1.dat').is_file())
        filespresent.append((dir / 'image-GNEB-saddlepoint.dat').is_file())
        if all(filespresent):
            return True
        else:
            return False

    def copygnebfiles(self, target: Path, destination: Path, check_interlayerinput: bool = False) -> None:
        r"""
        Copies all the files necessary to start a gneb calculation from the old calculation

        Args:
            target(Path): target folder

            destination(Path): destination folder

            check_interlayerinput(bool): A Flag wether a not existing interlayer.in file should raise an error. To treat
            monolayer systems correct the Default is False. For treating multilayer systems this switch has to be
            activated.
        """
        copy_element(target / 'GNEB.in', destination / 'GNEB.in')
        copy_element(target / 'inp', destination / 'inp')
        if check_interlayerinput:
            copy_element(target / 'interlayer.in', destination / 'interlayer.in')
        copy_element(target / 'lattice.in', destination / 'lattice.in')
        copy_element(target / 'momfile_f', destination / 'momfile_f')
        copy_element(target / 'momfile_i', destination / 'momfile_i')
        copy_element(target / 'simu.in', destination / 'simu.in')
        for f in target.glob('image-GNEB*.dat'):
            copy_element(target / str(f), destination / str(f))


    @staticmethod
    def checkconvergence(dir: Path = Path.cwd(), convergencecrit: float = 1.5e-8) -> bool:
        r"""
        Checks ifs a gneb calculation is converged

        Args:
            dir(Path): directory in which the output is checked. Default is the cwd.

            convergencecrit(float): If the forces are lower than that value a calculation is considered converged.

        Returns:
            boolean representing if the calculation is converged
        """
        if not (dir / 'force_mep.txt').is_file():
            raise ValueError('File force_mep.txt is not present cannot test for convergence!')

        L = [0, 10]
        for line in reversed(open(str(dir / 'force_mep.txt')).readlines()):
            L = line.split()
            break

        if float(L[1]) <= convergencecrit:
            return True
        else:
            return False


    def goon(self, actual: float) -> bool:
        r"""
        Decides whether the succesive calculation goes on depending on decreasing or increasing direction.

        Args:
            actual(float): actual value of the variation parameter

        Returns:
            whether to go on or not
        """
        if self.incordec == 'inc':
            if actual > self.stop:
                return False
            else:
                return True
        elif self.incordec == 'dec':
            if actual < self.stop:
                return False
            else:
                return True
        else:
            raise ValueError('Choose either increasing (inc) or decreasing (dec) direction!')

    def propagate(self, actual: float) -> float:
        r"""
        Propagates the actual parameter along the correct direction for a step

        Args:
            actual(float): actual value

        Returns:
            the increased or decreased value
        """
        if self.incordec == 'inc':
            l_step = self.step
        elif self.incordec == 'dec':
            l_step = -1 * self.step
        else:
            raise ValueError('the attribute incordec has to either inc or dec')
        return actual + l_step

    @abstractmethod
    def __call__(self, adjuster: Dict[str, List[str]]):
        r"""
        calls the succesive gneb calculation

        Args:
            adjuster(Dict): controls the variation of the parameters along the succsessive calculation. The keys in the
            dictionary are the names of the input files that shall be adjusted. The value is a list of every key in this
            input files that shall be updated.
        """

    @property
    @abstractmethod
    def incordec(self) -> str:
        r"""
        Returns:
            A string representing the direction of the succesive calculation -> inc or dec
        """

    @property
    @abstractmethod
    def start(self) -> float:
        r"""
        Returns:
            the start value for the gneb calculation
        """

    @property
    @abstractmethod
    def step(self) -> float:
        r"""
        Returns:
            the step value for the gneb calculation
        """

    @property
    @abstractmethod
    def stop(self) -> float:
        r"""
        Returns:
            the stop value for the gneb calculation
        """

    @property
    @abstractmethod
    def calcdir(self) -> Path:
        r"""
        Returns:
            Directory for calculation
        """

    @property
    @abstractmethod
    def startdir(self) -> Path:
        r"""
        Returns:
            Starting point for calculation
        """

    @property
    @abstractmethod
    def prefix(self) -> str:
        r"""
        Returns:
            the prefix of the foldernames, somehow characterizes the system
        """
