# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:30:36 2021

@author: schell
"""
from abc import ABC


class AbstractConfiguration(ABC):
    '''
    Abstract configuration class that forces the definition of class 
    attributes as config parameters for any subclasses. User defined 
    configurations should be subclassed from this class and given the 
    necessary class attributes.
    '''
    @classmethod
    def __init_subclass__(cls):
        required_class_variables = [
            'H_AXIS',
            'H_LEFT',
            'H_RIGHT',
            'V_AXIS',
            'V_UP',
            'V_DOWN',
            'R_AXIS',
            'R_UP',
            'R_DOWN',
            'SPEED_MIN',
            'SPEED_MAX',
            'DSPEED_LOW',
            'DSPEED_HIGH'
        ]
        for var in required_class_variables:
            if not hasattr(cls, var):
                raise NotImplementedError(
                    f'Class {cls} lacks required `{var}` class attribute'
                )


def create_config(h_axis, h_left, h_right, v_axis, v_up, v_down, r_axis, r_up, 
                  r_down, speed_min, speed_max, dspeed_low, dspeed_high):
    '''
    Convenience function to create a user defined configuration file from
    the AbstractConfiguration class.

    Parameters
    ----------
    h_axis : str
        axis for the horizontal buttons (e.g. 'X').
    h_left : int
        direction indicated by -1 or 1.
    h_right : int
        direction indicated by -1 or 1.
    v_axis : str
        axis for the vertical buttons (e.g. 'Y').
    v_up : int
        direction indicated by -1 or 1.
    v_down : int
        direction indicated by -1 or 1.
    r_axis : str
        axis for the r buttons (e.g. 'Z').
    r_up : int
        direction indicated by -1 or 1.
    r_down : int
        direction indicated by -1 or 1.
    speed_min : float
        minimum speed of the axis that can be set.
    speed_max : float
        maximum speed of the axis that can be set.
    dspeed_low : float
        low speed increment
    dspeed_high : float
        high speed increment
    

    Returns
    -------
    Confuguration.
    '''
    
    class Configuration(AbstractConfiguration):
        H_AXIS = h_axis
        H_LEFT = h_left
        H_RIGHT = h_right
        V_AXIS = v_axis
        V_UP = v_up
        V_DOWN = v_down
        R_AXIS = r_axis
        R_UP = r_up
        R_DOWN = r_down
        SPEED_MIN = speed_min
        SPEED_MAX = speed_max
        DSPEED_LOW = dspeed_low
        DSPEED_HIGH = dspeed_high
        
    return Configuration


class uFab(AbstractConfiguration):
    H_AXIS = 'Y'
    H_LEFT = 1
    H_RIGHT = -1
    V_AXIS = 'X'
    V_UP = -1
    V_DOWN = 1
    R_AXIS = 'U'
    R_UP = 1
    R_DOWN = -1
    SPEED_MIN = 1
    SPEED_MAX = 100
    DSPEED_LOW = 1
    DSPEED_HIGH = 10
    
    
class Scanner205(AbstractConfiguration):
    H_AXIS = 'X'
    H_LEFT = -1
    H_RIGHT = 1
    V_AXIS = 'Y'
    V_UP = 1
    V_DOWN = -1
    R_AXIS = 'A'
    R_UP = 1
    R_DOWN = -1
    SPEED_MIN = 1
    SPEED_MAX = 100
    DSPEED_LOW = 1
    DSPEED_HIGH = 10
    
    
class Picosecond205(AbstractConfiguration):
    H_AXIS = 'X'
    H_LEFT = -1
    H_RIGHT = 1
    V_AXIS = 'Y'
    V_UP = -1
    V_DOWN = 1
    R_AXIS = 'A'
    R_UP = 1
    R_DOWN = -1
    SPEED_MIN = 1
    SPEED_MAX = 100
    DSPEED_LOW = 1
    DSPEED_HIGH = 10
    

class HighSpeed(AbstractConfiguration):
    H_AXIS = 'Y'
    H_LEFT = 1
    H_RIGHT = -1
    V_AXIS = 'X'
    V_UP = 1
    V_DOWN = -1
    R_AXIS = 'A'
    R_UP = 1
    R_DOWN = -1
    SPEED_MIN = 1
    SPEED_MAX = 300
    DSPEED_LOW = 1
    DSPEED_HIGH = 10





