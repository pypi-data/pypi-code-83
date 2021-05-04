#insert root dir into system path for python

import os, sys, random, time


#config core
sys.path.append('../')
from brahma.configCore import *

from brahma.genome.vixen_genome import *

class VixenDNA(object):
    """
    Vixen DNA is the root DNA structure of all genetic material within an individual (indi) within the Vixen
    virtual world.

    Interaction between VixenDNA and the environment leads to expression levels which dictate the decision making
    process of an indi. Evolution of these DNA structures eventually leads to the development of AI indis.

    Args:
        object (Object): Root Object
    """

    def __init__(self, deltaD = "1", dataLength=1, envName="test", dataDelay=0, dnaType=''):
        """
        Initialise a strand of DNA. A strand of DNA can have 1 or more genomes
        attached to it. This is a representation of the genetic heirarchy found in
        nature. The DNA strand,ultimately will provide an activation metric between 0 
        and 1.This class is considered the root DNA class.

        DNA activation metric will be used in the transcription process to see if any
        "protein" should be expressed.

        Args:
            deltaD (str, optional): 
                This is the difference between data points in the 
                dataset or 'time' value used to  gorup  discretised data.
                It is important to determine this properly when implementing
                the AI problem as initialisation of DNA strands is dependent upon
                it as the DNA strand requires suffiecient data for for expression.
                
                Defaults to "1".

            dataLength (int, optional): .
                The number of data buckets required for the DNA strand to express
                itself. A single data epoch corresponds to a data input discretised 
                according to the user algorithm using 'deltaD' as the input parameter.
  
                Defaults to 1.

            envName (str, optional):
                The name of the environment or system being investigated.
                {e.g. in financial price prediction this may be the market.}

                Defaults to "test".

            dataDelay (int, optional): 
                The number of data epochs the DNA looks back before accessing data
                required to express its genome(s)

                Defaults to 0.  {0 - no delay}

            dnaType (str, optional): 
                The type of DNA. {"", "risk"}
                    Note: This is implemented in the initial distribution of BrahmaCore, 
                    but will more than likely be replaced with a more generic approach  and
                    deprectated in future releases.. 
                Defaults to ''.

        Returns:
            DNA Structure:  Each bot requires at least 1 DNA strand in order to live.
                            All genetic structure is built within this DNA structure. The expression 
                            of the DNA structure is required for transcription.

        """
        import random

        self.deltaD = deltaD
        self.dataLength = dataLength
        self.envName = envName
        self.dataDelay = dataDelay
        self.dnaType = dnaType
        self.env = envName

        self.genome = {}                        #collection of genomes in the DNA Strand
        self.name = random.randint(100,100000)  #name of DNA strand
        self.initialised = False                #initialised state (updated at every iteration)
        self.expressionTable = {}               #expression of each genome in the DNA 


        #logger
        self.logger = GetBrahmaLogger("DNA-")

    def __exit__(self):
        print ("deleting DNA")
        logger = logging.getLogger()
        while logger.hasHandlers():
            logger.removeHandler(logger.handlers[0])    
        del self.logger

    def __str__(self):
        """
        Override for printing the DNA object.

        Returns:
            String: Overview of DNA structure.
        """

        return ("Tag: {3} Market: {0} ; Data Required: {1} ; Delay: {4} Delta D: {2} Genome Size: {5}; Init: {6}".format(self.envName, self.dataLength, self.deltaD, self.name, self.dataDelay, len(self.genome), self.initialised))

    def IsInitialised(self, data_vector_length = 0):
        """

        DNA structures comprise of genomes which require data input in order
        to apply genetic expression. The volume and delay of data required
        by each DNA differs. An indi can only 'live' when all its DNA have enough
        data or environmental influence. This is represenbted by the 'initialised' state
        of the DNA. The initialised state of the DNA is determined at each iteration 
        and is required in order to determine the initialised state of an individual and 
        therefore indi and whether or not expression is possible. 

        Args:
            data_vector_length (int, optional): 
            the length of the vector holding the discretised representation of the
            environmental data of interest {e.g. length of vector holding candles in 
            financial implementations}
            .
            Defaults to 0.

        Returns:
            Bool: Initialised stae of the DNA.
        """

        if data_vector_length > (self.dataLength + self.dataDelay):
            self.initialised = True
            
            if GENOME_DEBUG:
                self.logger.debug("Chrom ID:{0} Init".format(self.name))
            return True
        else:
            
            self.initialised = False
            return False

    def GetDnaData(self, data = []):
        """
        Read the current data in the environmental input and chop out
        the data required by the DNA.

        Args:
            data (list, optional): 
            A list of the discretised representation of the data for this
            DNA structure.

            Defaults to [] { empty vector }.

        Returns:
            [data epoch representtion]: A list of the discretised representation of the data for this
            DNA structure.
        """
        #get the last index
        lastIndx = len(data)-2
        startingIndx = lastIndx - (self.dataLength + self.dataDelay)
        endIndx = startingIndx + self.dataLength

        return data[startingIndx : endIndx]

    def ExpressDNA(self, data = {}):
        """
        Calculate and return the expression value of the DNA (all genomes)
        from the expression table.

        Returns:
            double: The value of expression. {0<n<1} 
        """

        #express all genomes first. This defines the genome espression table.
        #if 0 is returned, we know that it is not yet initialised and can return with
        #a dna level of 0.
        #reset
        self.expressionTable =  {}
        init_state = self.ExpressGenome(data)

        #debug -> volatile e  levels
        #print (init_state)
        
        #check to see if return from building genome expression table is initialised
        if init_state == 0:
            #not yet initialised & not required to proceed for transcription
            self.initialised = False
            return -10.0

        #This DNA structure is initialised so...
        self.initialised = True

        #We can now determine the expression value (single) for the DNA Structure
        expression = 0
        sum_express = 0
        num_genome = len(self.genome)

        #---debug for why gene states not flipping
        local_debug = []       
        #print ("size: {0}".format(self.dataLength))

        for genomeID, genome in self.genome.items():

            
            if genomeID in self.expressionTable:
        
                #e vol debug -.
                #print (self.expressionTable[genomeID])

                sum_express = sum_express + self.expressionTable[genomeID]
                #e vol debug -.
                #print (sum_express)
                local_debug.append(self.expressionTable[genomeID])

                if GENOME_DEBUG == True:
                    self.logger.debug("Genome Expression Vector")
                    self.logger.debug(self.expressionTable[genomeID])

            else:
                sum_express = sum_express
                if TRANSCRIPTION_DEBUG:
                    self.logger.debug("Can't find genome expression for transcription data! Expression Tabe for chromosome: \n")
                    self.logger.debug(self.expressionTable)
            


        #debug - volatile expression levels
        #print ("sum {}".format(sum_express))

        #Determine the expression value...
        
        expression = sum_express/num_genome
        #e vol debug -.
        #print ("{} {} {}".format(expression, sum_express, num_genome))
        #if expression == 0.0:
        #    exit()
        #---debug breakdown of structure vals
        local_debug.append(len(self.genome))
        #print (*local_debug)
        #print ("*")
        return expression

    def ExpressGenome(self, data = {}):
        """
        Express (get excitement levels) of all the genomes in the DNA strand and 
        build the expression table of the genomes in the DNA strand. 
        Excitement levels or expression levels of each genome is within the range
        (0<e<1)

        Returns:
            int:    fallback initialisation state of the DNA. 
                    {1:  initialised, 0: not initialised}
        """
        #Edit nov 2020 - removed and moved to gene ( custom code section)
        current_pressure = data['current']
        current_pressure_vector = data['buckets']

        
        #removed/added nov 2020
        if self.IsInitialised(data_vector_length = len(current_pressure_vector)-2):


            #get active dna to send to genome
            if EXPRESS_DEBUG:
                self.logger.debug("Market DNA Initialised. Calling genome")

            
            activeDNA = self.GetDnaData(current_pressure_vector)
            data['buckets'] = activeDNA


            #now run against genome & get expression level
            for genomeTag, genome in self.genome.items():
                if EXPRESS_DEBUG: 
                    self.logger.debug("Expressing genome in DNA")

                self.expressionTable[genomeTag] = genome.express(data)
                #debug volatile e
                #print (self.expressionTable[genomeTag])
                


            return 1 # init as enough data for all genomes...

        else:

            return 0 # not init yet. more data required

    def PrintExpressionTable(self):
        """
        Ouput expression table. The expression values are provided by the genome.
        These can be displayed after every iteration to show expression levels.
        Used as debug.
        """
        self.logger.debug(len(self.expressionTable))
        for dnaTag, expression in self.expressionTable.items():
            self.logger.debug("DNA Tag: {2} ; Genome Tag {0} ; Expresson {1}; Init {3} \n".format(dnaTag, expression, self.name, self.initialised))
  
    def AddRiskGenome(self, parms=None):
        """
        Builds the risk genome for the individual. The risk genome applies constraints
        on the individuals.  { e.g. loss value in financial trading implementation}

        Args:
            parms (Dict, optional): Optimisation parametes. Defaults to None, but required 
            for build.
        """
        self.logger.critical("Building risk genome.")
        vx_genome = VixenGenome(1,1, envName = self.envName, genomeType='risk')
        vx_genome.BuildGenome()
        self.genome[vx_genome.genomeTag] = vx_genome
        vx_genome = None

        self.logger.critical(vx_genome.__str__())
        self.logger.critical("Risk genome added.")

    def AddGenome(self, parms=None):
        """
        Adds a genome to the indi. A random number of genes are applied to the genome
        with limits set out in the 'parms' argument.

        Args:
            parms (Dict, optional): Optimisation 
            parameters required.
                {   
                    minGenomeSize : int  # min number of genes in genome ( > 0)
                    maxGenomeSize : int  # max number of genes in genome 
                }
                Defaults to None, but must be provided

        """
        self.logger.critical("Building normal genome.")
        # exit()
        vx_genome = VixenGenome(parms['minGenomeSize'],parms['maxGenomeSize'], self.envName)
        vx_genome.BuildGenome()
        self.genome[vx_genome.genomeTag] = vx_genome
        self.logger.critical(vx_genome.__str__())
        
        self.logger.critical("Normal Genome built")
    def GetStructureData(self):
        """
        Builds and returns the structure of a DNA strand

        Returns:
            [type]: [description]
        """
        dnaExpressionVector = {}
        for genomeTag, expression in self.expressionTable.items():
            dnaExpressionVector[genomeTag] = expression

        genomeStructure = {}
        for genomeTag, genome in self.Genome.items():
            genomeStructure[genomeTag] = genome.get_structure()

        dna_structure = {}
        dna_structure['dnaSize'] = self.Length
        dna_structure['delay'] = self.Delay
        dna_structure['deltaT'] = self.DeltaT
        dna_structure['dna_expression'] = dnaExpressionVector
        dna_structure['dna_structure'] = genomeStructure

        return dna_structure




