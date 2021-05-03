# -*- coding: utf-8 -*-
r"""
This module contains some useful functions for embedding within other workscripts.
"""
from pathlib import Path


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
        return False

    L = [0, 10]
    for line in reversed(open(str(dir / 'force_mep.txt')).readlines()):
        L = line.split()
        break

    if float(L[1]) <= convergencecrit:
        return True
    else:
        return False