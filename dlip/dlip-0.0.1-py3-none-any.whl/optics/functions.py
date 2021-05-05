# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:45:42 2021

@author: schell
"""

import math

def deg2rad(angle_deg: float) -> float:
    '''
    Converts angles in degree to angles in radians

    Parameters
    ----------
    angle_deg : float
        angle in degrees.

    Returns
    -------
    float
        angle in radians.

    '''
    return 2 * math.pi * angle_deg / 360

def rad2deg(angle_rad: float) -> float:
    '''
    Converts angles in radians to angles in degrees

    Parameters
    ----------
    angle_rad : float
        angle in radians.

    Returns
    -------
    float
        angle in degrees.

    '''
    return angle_rad / 2 / math.pi * 360

def period_from_angle(angle: float, wavelength: float, num_beams: int, 
           degree: bool=True) -> float:
    '''
    Calculate spatial period for a given angle, wavelength and number of
    laser beams. Beams must have equal angle towards the optical axis.

    Parameters
    ----------
    angle : float
        angle of interference in degree.
    wavelength : float
        wavelength of the laser radiation in meters.
    num_beams : int
        number of interfering laser beams.
    degree : bool
        Use angle in degree if True, else in radians

    Raises
    ------
    ValueError
        in case of unknown number of beams.

    Returns
    -------
    float
        spatial period.

    '''
    if num_beams == 2:
        factor = 0.5
    elif num_beams == 4:
        factor = 1 / math.sqrt(2)
    else:
        raise ValueError(f'{num_beams} not supported')
    if degree:
        angle = deg2rad(angle)
    return factor * wavelength / math.sin(angle)

def angle_from_period(period: float, wavelength: float, 
                      num_beams: int, degree: bool=True) -> float:
    '''
    Calculate angle for a given period, wavelength and number of
    laser beams. Beams must have equal angle towards the optical axis.


    Parameters
    ----------
    period : float
        DESCRIPTION.
    wavelength : float
        wavelength of the laser radiation in meters.
    num_beams : int
        number of interfering laser beams.
    degree : bool
        Compute angle in degree if True, else in radians

    Raises
    ------
    ValueError
        in case of unknown number of beams.

    Returns
    -------
    float
        angle in degree, in radians if degree is set to False.

    '''
    if num_beams == 2:
        factor = 0.5
    elif num_beams == 4:
        factor = 1 / math.sqrt(2)
    else:
        raise ValueError(f'{num_beams} not supported')
    angle = math.asin(factor * wavelength / period)
    if degree:
        angle = rad2deg(angle)
    return angle

