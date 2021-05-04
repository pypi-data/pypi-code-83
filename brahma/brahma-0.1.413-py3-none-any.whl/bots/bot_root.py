"""This is v1.0 of the trader template. Procedures for birth, death evolution must be contained here.
This is a template for a general intraday futures/fx trader. (obs)
"""
import os, sys, time, copy, datetime, random

#config core
#sys.path.append('../')


from brahma.configCore import *
from brahma.dna.vixen_dna import *
from brahma.genome.transcription import *

class BotRoot(object):
    
    """
    BotRoot is the root class of all indis/bots in the brahma world.
    Genetic material is deterined by lcl folder for material and derived bots  can add
    functionality. e.g.  trader  - direction of bot.

    todo: visualise bot genetic strucure

    :param object: [description]
    :type object: [type]
    :param object: [description]
    :type object: [type]
    :param object: [description]
    :type object: [type]

    """
    def __init__(self, myenv="", myspecies = "BotRoot", myargs=None):
        self.name = "VxBot" + str(random.randint(100,1000000)) 
        self.env = myenv
        self.dob = datetime.datetime.now()
        self.species = myspecies
        #genetic material
        self.parent = "Eden"
        
        self.dNA = {}           #contains strands of DNA
        #self.riskDNA = {}
        self.numberDNA = 0
        self.dNAExpression = {}         #expression value of each DNA strand 
                                        #this is required for transcription

        #self.dNARiskExpression = {}     #expression value of each risk DNA strand 
                                        #this is required for transcription

        #protein transcription
        self.transcriptionDNA = None    #this is what is used for transcription
                                        #DNA expression levels is required

        #initialised
        self.initialised = False

        #logger
        #self.logger = GetBrahmaLogger("Bot Creation")

    def __str__(self):
        """
        Overide of print method.Export high level description of bot. 

        :return: High  level description of bot.
        :rtype: String
        """
        return ("Name: {0} Number DNA: {1} Env: {2} Species: {3}".format(self.name, self.numberDNA, self.env, self.species))

    def BuildBot(self, parms = None):
        """
        Build the bot and all its genetic material. This is the root class 
        so all root genetic material is built. 

        :param parms: [description], defaults to None
        :type parms: [type], optional
        """
        print ("here")
        #logger.info("***Building Bot : {0}".format(self.name))
        
        #determine numer of dna strands
        if parms != None:
            self.numberDNA = random.randint(parms['minNumberMarketDNA'], parms['maxNumberMarketDNA'])
            
        else:
            exit(0)



        #build risk DNA - alpha - one for now.  keep simple.
        #riskDNA =  VixenDNA(deltaD = 1, dataLength=1, envName=self.env, dataDelay=1)
        #riskDNA_tag = riskDNA.name
        #riskDNA.AddRiskGenome()
        #self.riskDNA[riskDNA_tag] = riskDNA
        #self.dNARiskExpression[riskDNA_tag] = 0.0
        #del(riskDNA)
        
        
        #number of marketDNA
        for i in range(0,self.numberDNA):
            #print (self.numberDNA)
            
            #build market dna

            #get deltaT
            #dna_deltaT = random.randint(1, parms['maxDeltaT'])
            dna_deltaT = random.choice(EpochBuckets)
            
            #get length
            dna_length = random.randint(parms['minMarketDNASize'], parms['maxMarketDNASize'])
            #get delay
            dna_delay = random.randint(0, parms['maxDNADelay'])
            

            marketDNA = VixenDNA(deltaD = dna_deltaT, dataLength=dna_length, envName=self.env, dataDelay=dna_delay)
            marketDNA_tag = marketDNA.name
            #add genome... only one per DNA strand - yes for now
            marketDNA.AddGenome(parms=parms)
            # print ("dna: {}".format(i))
            # ()exit
            self.dNA[marketDNA_tag] = marketDNA
            # del(marketDNA)
            marketDNA = None
            self.dNAExpression[marketDNA_tag] = 0.0
            #print (self.MarketDNA[marketDNA_tag].ExpressionTable)
            # exit()

            

        #build transcription DNA
        self.transcriptionDNA = Transcription()
            

    def StartUp(self):
        """
        All expression levels must be set to zero before starting a new run.
        """

        for dnaTag, e in self.dNAExpression.items():
            self.dNAExpression[dnaTag] = 0.0

        #for dnaTag, e in self.dNARiskExpression.items():
        #    self.dNARiskExpression[dnaTag] = 0.0
    
    def ExpressDNA(self, data={}):
        """
        Express each strand of DNA in the bot and build the DNA epression table for
        the bot. Return values are 1 for bot is now initialised and 0 for not initialised.

        :param data: Pressure data, defaults to {} for root as no data required 
                    for test data. User defined for derived bot data requirements
        :type data: dict, optional
        :return: Initialised state of bot. True: is initialised False: not initialised 
        :rtype: Bool
        """

        #run risk first
        '''
        for dnaTag, dna in self.riskDNA.items():
            expression_value = dna.ExpressDNA(data=data)
            #check to see if all the genetic material has been initialised
            #a value of False means that one of the genomes has not been initialised
            #so ExpressDNA also returns false after settng the initialised value to  False
            if expression_value == False:
                self.initialised = False
                return  False

            self.dNARiskExpression[dnaTag] = expression_value
        '''

        #print (self.initialised)
        for dnaTag, dna in self.dNA.items():
            
            #get current data print and bucket vector--
            #bucket vector comes from derived structure (data series custom made)
            data_print = data['data_print']
            bucket_vector = data['derived_data'].GetBuckets(self.env, deltaT = dna.deltaD)

            pressure_data = {
                'current' : data_print,
                'buckets' : bucket_vector,
                'options' : data['opt']
            }

            expression_value = dna.ExpressDNA(data=pressure_data)

            #debug ---> gene flip analysis
            #print  (expression_value)
            #check to see if all the genetic material has been initialised
            #a value of False means that one of the genomes has not been initialised
            #so ExpressDNA also returns false after settng the initialised value to  False


            #update nov 2020 :  returning boolean and floating point
            if expression_value == -10:
                self.initialised = False
                return  False


            #debug ---> gene flip analysis
            #if expression_value  == 1.0:
                
            #    print  ("++++++++++++++++++++++++")
            #    exit()
            #print (expression_value)

            self.dNAExpression[dnaTag] = expression_value


        #we have expressed all DNA strands which means all genomes inside have been run
        #which means that the individual is now intialised.
        self.initialised = True

        #---debug output
        tickExpress = []
        for key, val in self.dNAExpression.items():
            #print (val)
            fp = open ("express.txt", "a")
            fp.write("{0}\n".format(val))
            fp.close()
            tickExpress.append(val)
        #print (self.initialised)
        #print (*tickExpress)
        
        #print ("***")
        #---

        return True

    def GetExpressionData(self, type=""):
        return self.dNAExpression



# class myTradeBot(BotRoot):
#   def __init__(self, myenv="", myspecies = "myTradeBot", myargs=None):
#     super().__init__(myenv=myenv, myspecies = myspecies, myargs=myargs)
    
#     #looking for a buyer here
#     self.direction = 1

#   #def ExpressDNA(self):
#   #  pass

