import os, sys

#config core
#sys.path.append('../') #core code root ( /brahama/code/ )
from brahma.configCore import *
from brahma.genes import *
#!!!!!!!!!!!!!!!!!!!!
#must edit this
#from g_DownFractalPresent import *
#from g_UpFractalPresent import *
#from risk_RiskGeneAlpha import *
#from g_DeltaValue import *

if 'GENETIC_DATA_FOLDER_USR' in os.environ:
    
    userGenesFolder = os.environ['GENETIC_DATA_FOLDER_USR']
    print (userGenesFolder)
    sys.path.insert(0,userGenesFolder)
    from fgenes import *

else:
    print ('no user genetic material')




class VixenGenome(object):

    """
    Genome for Vixen's DNA. The genome, located within the DNA structure, 
    defines the genes within the individual. Each gene interacts with the data vector
    of discretised environmental conditions and will ultimately adopt an on/off state.
    These differing states will provide an excitement level/expression for the genome
    in which they sit. The expression level (e) of the genome will satisfy {0 < e < 1}
    
    IMPORTANT: Genomes within the same DNA structure will all recieve the same 
    size vector of data and resident genes must be able to adopt a state with any 
    given data vector sizes. 

    This 'VixenGenome' is considered the root of all genome structures. Genomes must be
    able to,  at the very minimum, build & express the genome.
    
    Arguments:
        object {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
   

    def __init__(self, minSize=1, maxSize=1, envName="test", genomeType=""):
        """
        Creates a genome structure

        Args:
            minSize (int, optional): min number of genes. Defaults to 1.
            maxSize (int, optional): max number of genes. Defaults to 1.
            envName (str, optional): name of environment. Defaults to "test".
            genomeType (str, optional): [description]. Defaults to "".
        """
        import random

        self.expressionLevel = 0    #expression level of the genome
        self.genomeSize=random.randint(int(minSize), int(maxSize)) #number of genes in the genome
        self.envName = envName #environment within which the genome interacts {e.g. EURUSD}
        self.genomeTag = "genome" + str(random.randint(100, 10000)) #unique id of the genome
        self.genome = {} #hashtag of all genes in the genome
        self.genomeExpression = {} #expression of gene tagged by geneID
        self.geneticSelectionDict = {} #dict of gene types from which to select TODO: apply number contraints
        #nov 2020
        #self.riskGeneticSelectionDict = {} #dict of risk genes from which to select 
        self.genomeType = genomeType  #type of genome { normal, risk }  NOTE: will depracate soon  
        

        #self.logger = GetBrahmaLogger("GENOME")


    def __str__(self):
        """
        Override print method for description of Genome and all genes ( or conditions )

        Returns:
            string: Description of genome (can be used in logging / debugging)
        """
        returnStr = ""
        returnStr += ("Tag: {2} Size: {0} ; Environment {1}".format(self.genomeSize, self.envName, self.genomeTag)) + "\n"
        returnStr += "*************** DETAILS ************ \n"

        for geneTag, gene in self.genome.items():
            returnStr += ("Tag: {0} Type: {1}".format(gene.i_D, gene.condition)) + "\n"

        return returnStr

    def __exit__(self):
        pass
        #del self.logger
    
    def BuildGenome(self):
        
        """
        Build a genome >
        >. determine type of genome
        >. build a selection vector of available genes
        >. build and attach the genes to the genome.
        """
        

        # if self.genomeType=="risk":
        #     #self.logger.info("Building Risk Genome - Gene count: {0}".format(self.genomeSize))
        #     #build list of avilable risk genes
        #     self.BuildRiskGeneSelectionDict()

        #     for geneCnt in range(0, self.genomeSize):


                
        #         geneType = self.SelectRiskGeneFromSelectionDict()
        #         #logger.info("Risk gene selected: {0}".format(geneType))
        #         geneStructureTmp = self.BuildGeneStructure(geneType, self.riskGeneticSelectionDict)
        #         #self.genome[geneStructureTmp.i_D] = geneStructureTmp
        #         #self.logger.info("Gene built: {0}".format(geneType))
        #     #attach to genome
        #         #kill tmp structure
        #         geneStructureTmp = None




        #     return

        #self.logger.info("Building Normal Genome - Gene count: {0}".format(self.genomeSize))
        self.BuildGeneSelectionDict()

        for geneCnt in range(0, self.genomeSize):
            #select
            geneType = self.SelectGeneFromSelectionDict()
            #self.logger.debug("Normal gene selected: {0}".format(geneType))

            #build & get tagID
            geneStructureTmp = self.BuildGeneStructure(geneType,  self.geneticSelectionDict)
            #self.logger.info("Gene built: {0}".format(geneType))
            #attach to genome

            self.genome[geneStructureTmp.i_D] = geneStructureTmp
            #kill tmp structure
            geneStructureTmp = None




    def BuildRiskGeneSelectionDict(self):

        import os
        
        geneFileList = os.listdir(BRAHMA_GENETIC_DATA_FOLDER_LCL)
        for fileName in geneFileList:
            if fileName.endswith('.py'):
                fnArray = fileName.split('.')
                geneType = fnArray[0]
                if geneType != "dnaroot":
                    prefix = geneType.split('_')
                    prefixStr = prefix[0]
                    if prefixStr == "risk":
                        geneName = prefix[1]
                        #logger.info("Adding Gene to Selection: {0}".format(geneName))
                        self.riskGeneticSelectionDict[geneName] = eval(geneName)

    def SelectRiskGeneFromSelectionDict(self):
        import random
        
        try:
            #self.logger.debug("Trying to grab a random risk gene tag.")
            randomGeneTag = random.choice(list(self.riskGeneticSelectionDict))
            #self.logger.debug("Random gene tag: {0}".format(randomGeneTag))
            
            return randomGeneTag

        except Exception as e:
            #self.logger.critical("type error: " + str(e))
            #self.logger.critical(traceback.format_exc())
            #self.logger.critical("Error selecting risk gene")
            exit(0)
        return -1


    def BuildGeneSelectionDict(self):
        """Build gene type selection lists
        """


        import os
        

        #local genes loaded {todo: custom genes}
        #geneFileList = os.listdir(BRAHMA_GENETIC_DATA_FOLDER_LCL)
        #edit
        genetic_material_folder = USER = os.getenv('GENETIC_DATA_FOLDER_USR')
        geneFileList = os.listdir(genetic_material_folder)
        for fileName in geneFileList:
            
            if fileName.endswith('.py'):
                fnArray = fileName.split('.')
                geneType = fnArray[0]
                if geneType != "dnaroot":
                    prefix = geneType.split('_')
                    prefixStr = prefix[0]
                    if prefixStr == "g":
                        geneName = prefix[1]
                        #print (dir())
                        #logger.info("Adding Gene to Selection: {0}".format(geneName))
                        self.geneticSelectionDict[geneName] = eval(geneName)

    def SelectGeneFromSelectionDict(self):
        """Select a genetype from the list
        and return to caller
        """
        import random
        try:
            #self.logger.debug("Trying to grab a random gene tag.")
            
            randomGeneTag = random.choice(list(self.geneticSelectionDict))
            #self.logger.debug("Random gene tag: {0}".format(randomGeneTag))
            
            return randomGeneTag

        except Exception as e:
            
            #self.logger.critical("Error selecting gene")
            exit(-1)
        return -1


    def BuildGeneStructure(self, gene_type = "", classCollection=None):
        if gene_type != "":
            pass
        else:
            #self.logger.critical("No genetic material found for gene_type: {0}".format(gene_type))
            exit("No genetic material")

        
        tmpGene = None
        #self.logger.debug("attempting to create gene from new selection approach: {0}".format(gene_type))
        try:
            #print (gene_type)
            #print (self.geneticSelectionDict)
            #tmpGene = self.geneticSelectionDict[gene_type]("test")
            tmpGene = classCollection[gene_type]("test")
        except Exception as e:
            #self.logger.critical("Attempting to create gene from new selection approach: FAIL")
            
            exit(0)

        return tmpGene

        ''' lets get rid of this...
        if gene_type == "direction_negative_alpha":
            tmpGene = DirectionNegativeAlpha(mkt=self.envName)

        if gene_type == "direction_positive_alpha":
            tmpGene = DirectionPositiveAlpha(mkt=self.envName)

        if gene_type == "down_fractal_present":
            tmpGene = DownFractalPresent(mkt=self.envName)

        if gene_type == "up_fractal_present":
            tmpGene = UpFractalPresent(mkt=self.Market)

        if gene_type == "risk_alpha":
            tmpGene =  RiskGeneAlpha(mkt=self.Market)

        if gene_type == "risk_beta":
            tmpGene =  RiskGeneBeta(mkt=self.Market)
        '''



       

    def express(self ,data):
        """[summary]

        :param data: [description]
        :type data: [type]
        :return: [description]
        :rtype: [type]
        """
        expressSum = 0
        
        #debug  -> variable expression
        #print ("genome size:{0}".format(len(self.genome)))

        for geneTag, gene in self.genome.items():
            if EXPRESS_DEBUG:
                pass
                #self.logger.debug("Genome expressing")

            #get express value
            expression = 0
            expression = gene.run(data)
            #---debug - structure value analysis. 
            #print ("gene e: {0}".format(expression))
            #if expression == 0:
            #    print ("--------------")


            #-----
            self.genomeExpression[geneTag] = expression
            if GENOME_DEBUG:
                if gene.SafeRun == False:
                    pass
                    #self.logger.debug("Gene error. Not a safe run. {0}".format(gene.condition))
            expressSum = expressSum + expression
            #debug  -> variable expression
            #print("expressSum {0}".format(expressSum))
            #print("gene: {0}".format(expression))
            #print("gene_c: {0}".format(gene.condition))


            if EXPRESS_DEBUG:
                pass
                #self.logger.debug("Gene Expression : {0}".format(expression))



        if EXPRESS_DEBUG:
            pass
            #self.logger.debug("Genome Expression Vector:")
            #self.logger.debug(self.print_genome_expression())


        #edit expression -> expressSunm Nov 2020
        if expressSum != 0:
            self.ExpressionLevel = float(expressSum/self.genomeSize)

            #print("final expressSum {0}".format(expressSum))
        else:
            self.ExpressionLevel = 0

        #debug - volatile
    

        #debug - volatile
        #print ("genome expression  value: {0}".format(self.ExpressionLevel))


         #debug ---> gene flip analysis
            
        return self.ExpressionLevel




    def print_genome_expression(self):
        for geneTag, expressionVal in self.GenomeExpression.items():
            print ("Gene Tag: {0} ; GeneExpression {1}".format(geneTag, expressionVal))
    def get_structure(self):
        structure = {}
        genome_structure = {}
        genome_structure['numberGenes'] = self.GenomeSize
        gene_structures = {}
        for geneTag, gene in self.Genome.items():
            pt_structures = {}
            pt_structures['condition'] = gene.Condition
            pt_structures['id'] = gene.I_D
            pt_structures['dob'] = gene.DOB
            gene_structures[geneTag] = pt_structures

        structure['genome_meta'] = genome_structure
        structure['genes'] = gene_structures

        return structure

