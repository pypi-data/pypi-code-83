# -*- coding: utf-8 -*-
r"""
Module for classes realizing succesive gneb calculations with just one path segment
"""
from workscriputilities.gneb.succesive.isuccsesive import ISuccsesive
from pathlib import Path
from python3.shell_commands import *
from typing import Dict, List


class CSuccsesiveOnep(ISuccsesive):
    r"""
    Class for realizing succesive gneb calculations for gneb calculations without intermediate minima.
    For example bilayer systems.
    """

    def __init__(self, startdir: Path, prefix: str, start: float, step: float, stop: float, incordec: str = 'inc',
                 calcdir: Path = Path.cwd() / 'gneb_onep_succ', multilayer: bool = True, further: bool = False) -> None:
        r"""
        Initializes calculation

        Args:
            startdir(Path): Directory of the converged GNEB calculation from which to start.
            prefix(str): prefix of the foldernames for the created succesive folders
            start(float): Start value for calc.
            step(float): Step value for calc.
            stop(float): Stop value for calc.
            incordec(str): Direction for calc. Default is inc
            calcdir(Path): Directory where the calc. shall be performed. Default is a new folder within the cwd.
            multilayer(bool): Flag whether the systems is a multilayer system. Default is here True. If no interlayer.in
            file is present assign False here
        """
        self._incordec = incordec
        self._start = start
        self._step = step
        self._stop = stop
        self._startdir = startdir
        self._prefix = prefix
        self._calcdir = calcdir
        if not further:
            self._calcdir.mkdir()
        self._multilayer = multilayer
        if not self._startdir.is_dir():
            raise FileNotFoundError('Did not find the directory with the converged GNEB calculation!')
        if not self.checkgnebfiles(self._startdir):
            raise FileNotFoundError('Not all the necessary input files in the start directory where found!')

    def preparegnebinputs(self, directory: Path) -> None:
        r"""
        In a succsesive calculation you want to set the randomizing parameters to zero, because you want to start
        exactly from the prescribed path. This is important if the local energy minimum of the path is shallow. For the
        same reason you dont want to rerun the gneb method but only rerun the ci-gneb

        Args:
            directory(Path): directory in which to adjust the gneb inputs.
        """
        adjust_parameter('amp_rnd_path', '0.0', directory / 'GNEB.in')
        adjust_parameter('amp_rnd', '0.0', directory / 'GNEB.in')
        adjust_parameter('do_gneb', 'N', directory / 'GNEB.in')

    def __call__(self, adjuster: Dict[str, List[str]]) -> bool:
        r"""
        Calls the succesive calculation

        Args:
            adjuster(Dict): controls the variation of the parameters along the succsessive calculation. The keys in the
            dictionary are the names of the input files that shall be adjusted. The value is a list of every key in this
            input files that shall be updated.

        Returns: a boolean whether the last step of the calculation converged or not.
        """
        actual = self.propagate(self._start)
        prev_dir = self._startdir
        self.preparegnebinputs(directory=prev_dir)

        while self.goon(actual=actual) and self.checkconvergence(prev_dir):
            actual_dir = self._calcdir / (self._prefix + str(actual))
            actual_dir.mkdir()
            self.copygnebfiles(prev_dir, actual_dir, check_interlayerinput=self._multilayer)
            with change_directory(actual_dir):
                for (inpfile, keys) in adjuster.items():
                    for k in keys:
                        adjust_parameter(keyword=k, value=str(actual) + 'd-3', directory_file=Path.cwd() / inpfile)
                        # start procedure
                        if not cluster():
                            call_spin()
                        else:
                            jobname = 'oPsc' + str(actual)
                            adjust_line_under_key('#!/bin/bash', f'#SBATCH --job-name={jobname}',
                                                  '/work_beegfs/supas384/jobs/job_cau_agheinze.sh')
                            call_sbatch('/work_beegfs/supas384/jobs/job_cau_agheinze.sh')
            # wait for procedure to finish:
            if not cluster():
                raise NotImplementedError('waiting for job on local machine not implemented yet. Run on cluster please')
            else:
                ready = False
                while not ready:
                    # wait 5 minutes until next request
                    time.sleep(300)
                    bashCommand = f'squeue --name={jobname}'
                    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                    output, error = process.communicate()
                    ready = bytes(jobname, 'utf-8') not in output.split()

            # updating values for next run
            prev_dir = actual_dir
            actual = self.propagate(actual)

        return self.checkconvergence(prev_dir)

    @property
    def incordec(self) -> str:
        r"""
        Returns:
            A string representing the direction of the succesive calculation -> inc or dec
        """
        return self._incordec

    @property
    def start(self) -> float:
        r"""
        Returns:
            the start value for the gneb calculation
        """
        return self._start

    @property
    def step(self) -> float:
        r"""
        Returns:
            the step value for the gneb calculation
        """
        return self._step

    @property
    def stop(self) -> float:
        r"""
        Returns:
            the stop value for the gneb calculation
        """
        return self._stop

    @property
    def calcdir(self) -> Path:
        r"""
        Returns:
            the calc dir for the calculation
        """
        return self._calcdir

    @property
    def startdir(self) -> Path:
        r"""
        Returns:
            the starting point for the calculation
        """
        return self._startdir

    @property
    def prefix(self) -> str:
        r"""
        Returns:
            the prefix of the foldernames, somehow characterizes the system
        """
        return self._prefix
