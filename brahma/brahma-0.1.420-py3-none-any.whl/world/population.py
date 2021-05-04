"""Population class for evolutionary algorithms
"""



import os, sys, random
#insert root dir into system path for python
#config core
#sys.path.append('../')
from brahma.configCore import *

#import root bot
from brahma.bots.bot_root import *


class Population(object):
    """
    Population is the container object for all bots/indis in the game/optimisation run.
    
    Arguments:
        object {root object} -- object class
    """

    def __init__(self, parms=None, name="vx_dm"):
        """
        Create the Population class. This class holds all bots in the game.

        :param parms: optimisation parameters - from config file but passed through for now, defaults to None
        :type parms: key/value pairs, optional
        :param name: name root, defaults to "vx_dm"
        :type name: str, optional
        """
        #print ("fsdfw")
        self.name = name + str(random.randint(10,10000))
        self.parms = parms
        #bot names in list
        self.bots = []
        #species structure tagged by name
        self.species = {}
        #logger

        #self.logger = GetBrahmaLogger("Population")

    def __exit__(self):
        pass
        #del self.logger

    def Populate(self, species = "BotRoot", args = None):

        if species != "tribal":
            
            
            if DEBUG:
                print ("Size: " + str(self.parms['PopulationSize']))
            for i in range(0, int(self.parms['PopulationSize'])):
                if DEBUG:
                    print ("creating bot")
                self.CreateBot(species = species, args = args)
                
        else:

            self.CreateBot(species = species, args = args)

        # self.logger(self.show())
        self.show()

    def test(self):
        pass
    
    def CreateBot(self, species = None, args = None):
        self.botStr = {}
        self.botStr[species] = eval(species)
        

        #build the bot here - general
        bot_tmp = self.botStr[species](self.parms["env"], myspecies = species, myargs = args)
        bot_tmp.BuildBot(parms=self.parms)
        
        
        self.bots.append(bot_tmp.name)
        self.species[bot_tmp.name] = bot_tmp

        '''
        print ("Building.. " + species)
        bot_tmp = trader_template(self.Parms['market'])
        bot_tmp.build_trader(parms=self.Parms)
        self.Bots.append(bot_tmp.Name)
        self.Species[bot_tmp.Name] = bot_tmp
        bot_tmp = None
        '''

    def show(self):
        for key, value in self.species.items():
            #print (value)
            pass



if __name__ == "__main__":
    pass
    '''
    pop = Population(parms={'PopulationSize' : '100'}, name = "demo")
    pop.populate('trader')
    '''

