"""
This module defines the environments within the brahma virtual world.
There are two main envirnents present:

1. The static environment: The static envirnment represents the population of 
bots/indis in the virtual world. {e.g. trading bots}

2. The dynamic envirnment: The dynamic environment provides the 'pressure' within
which the bots/indis live. {e.g. market price}

Coupled, these two environemnts interact to provide the source and pressure required
to evolve bots to live in the virtual environment.
"""

import os, sys
#insert root dir into system path for python
#config core
sys.path.append('../')
from configCore import *

class StaticEnvironment(object):
    """
    The Environment class provides the population for the brahmaCore game. 
    For example, in trading applicaiton, this would represent the popualtion
    of trading bots in the brahma virtual world.
    
    Arguments:
        object -- Root object
    """
    
    def __init__(self, op_parms=None):
        """
        initialise the Environment object. Optimisation paramters are required
        and simply represent the parameters for the game/optimsation.

        The logger for the module is also set.

        :param op_parms: These are the parameters for the 'game', defaults to None, but are required
        :type op_parms:key-value dictionary of game options, optional
        """
        self.optimisationParameters = op_parms

        #logger
        self.logger = GetBrahmaLogger("Environment")

        if DEBUG:
            self.print_parms()

    def PrintParms(self):
        """
        Simply display the parameters read by the game/optimisation.
        Output to log.
        """
        for key, value in self.OptimisationParameters.items():
            #print (key + " : " + str(value))
            self.logger.debug((key + " : " + str(value)))

    def BuildEnvironment(self):
        """
        This is the workhorse of the Environment class. Here we build the population
        that will be used in the game. User defined indivis/bots will have to be 
        used here via the Population class.
        """

        #---build population
        self.population = Population(self.optimisationParameters, name=self.optimisationParameters['population_name'])
        self.population.populate(species=self.optimisationParameters['species'])
        
        if DEBUG:
            self.population.show()

        #---deprecated
        #---build dynami nature (this will be what is used to apply pressure & select the best decision makers in the population)
        #self.NaturalWorld = nature



class DynamicEnvironment(object):
    """
    The dynamic aspect of the environment.Here we provide the force that will 
    apply pressure to the population and allow for a fitness distribution 
    required for evolution of bots/indis in the game.

    Arguments:
        object {class]} -- root class
    """

    def __init__(self):
        """
        Initialise the DynamicEnvironment class. Sets pressure conduit and pressure to none. 
        These key environmental variables will be initialised when the dynamic
        environment is built.
        """

        self.pressureConduit = None
        self.pressure = None

    def BuildEnvironment(self, parms=None, live=False):
        """
        Build the dynamic environment. Optimisation parameters will be required.

        :param parms: Optimisation parameters. This is initially defined by
        brahmaCore, but user defined variables can also be added for full 
        customisation.
        :type parms: Key value structure
        :param live: is the dynamic environment for use in an optimisation 
        capacity or forward running mode, defaults to False
        :type live: bool, optional
        :return: Status of  the pressureConduit and pressure components. [1,-1]
        :rtype: int
        """

        self.pressureSource = DataSeries()
        self.pressureSource.AddEnv(parms['env'])
        self.pressureSource.BuildDataStructures()

        if ENV_DEBUG and self.PressureConduit:
            print ("Pressure conduit setup")

        self.pressure = SimulatedFeed(market = parms['env'], numberOfDays = parms['numberEpochs'])
        self.pressure.BuildSimulatedFeed(parms['startData'], parms['endData'])
        self.pressure.SetDataSeries(self.pressureConduit)

        if ENV_DEBUG and self.Pressure:
            print ("Pressure source setup")

        if self.pressureConduit and self.pressure:
            print ("success")
            return 1

        else:
            return -1

if __name__ == "__main__":
    pass

    '''
    static_env = Environment(op_parms = OptimsationParameters)
    static_env.build_environment()
    dyn_env = DynamicEnvironment()
    dyn_env.build(OptimsationParameters)
    ''' 
