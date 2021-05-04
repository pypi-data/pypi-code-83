

"""
BrahmaCore configuration file. Included:

1 - Standard python imports
2 - BrahmaLogging Formatter
3 - Standard output paths {e.g. log folder}

written by Rahul Tandon for Vixen Capital 2020. 
rahul@vixencapital.com
  
"""

#standard imports
import os, sys, random

'''
APP_FOLDER = os.path.join(os.path.expanduser('~'),'dev','app','tutorial-bot','')
sys.path.insert(0,APP_FOLDER)
from brahmaAppConf import *
'''
#
#path definitions {e.g. log folder(s)} All paths set to just add filename
#

#---brahma core root. IMPORTANT as other paths are ALL relative to this
#edit for dist. Don't want paths as package installed
#DO NOT TOUCH!!!
#BRAHMA_CORE_ROOT_PATH  = os.environ['BRAHMA_CORE_ROOT_PATH']
#BRAHMA_CORE_LOG_PATH = BRAHMA_CORE_ROOT_PATH + os.path.join('logs','')
#os.environ['BRAHMA_CORE_LOG_PATH'] = str(BRAHMA_CORE_LOG_PATH)

#BRAHMA_GENOME_CODE_ROOT_PATH =  BRAHMA_CORE_ROOT_PATH + os.path.join('code','genome','')
#BRAHMA_DNA_CODE_ROOT_PATH =  BRAHMA_CORE_ROOT_PATH + os.path.join('code','dna','')
#BRAHMA_GENETIC_DATA_FOLDER_LCL = BRAHMA_CORE_ROOT_PATH+ os.path.join('code','genes','') 
#BRAHMA_WORLD_PATH = BRAHMA_CORE_ROOT_PATH + os.path.join('code','world','')
#BRAHMA_BOT_ROOT_PATH = BRAHMA_CORE_ROOT_PATH + os.path.join('code','bots','')
#os.environ['BOT_SOURCE_LCL'] = BRAHMA_BOT_ROOT_PATH

#
#add brahma imports
#


#add dna code to system
#sys.path.insert(0,BRAHMA_DNA_CODE_ROOT_PATH)

#add genome code to system
#sys.path.insert(0,BRAHMA_GENOME_CODE_ROOT_PATH)

#add local genes repo
#sys.path.insert(0,BRAHMA_GENETIC_DATA_FOLDER_LCL)

#add environment 
#sys.path.insert(0,BRAHMA_WORLD_PATH)

#add bot root
#sys.path.insert(0,BRAHMA_BOT_ROOT_PATH)


#import brahma logging format
#from brahmaLogging import *
#logger = GetBrahmaLogger("CORE_CONFIG")

#import dna
#logger.debug("importing DNA from : {0}".format(BRAHMA_DNA_CODE_ROOT_PATH))
#from vixen_dna import *

#import genes -  only lcl brahma ones
'''
logger.debug("importing local genes from : {0}".format(BRAHMA_GENETIC_DATA_FOLDER_LCL))
'''
'''
from g_DownFractalPresent import *
from g_UpFractalPresent import *
from risk_RiskGeneAlpha import *
'''


#import genome
#logger.debug("importing Genome from : {0}".format(BRAHMA_GENOME_CODE_ROOT_PATH))
#from vixen_genome import *

#import environment -> static and dynamic
#logger.debug("importing World from : {0}".format(BRAHMA_WORLD_PATH))
#from population import *
#from dataSeries import *
#from simulatedfeed import *

#import bot root
#logger.debug("importing Bot Root from : {0}".format(BRAHMA_BOT_ROOT_PATH))
#from bot_root.py import *

#run flags



DEBUG = False
GENOME_DEBUG = False
ENV_DEBUG = False
SP_DEBUG = False
RUN_DEBUG = False
EXPRESS_DEBUG = False
TRADER_DEBUG = False
DNA_EXPRESS_DEBUG = False
TRANSCRIPTION_DEBUG = False
DECISION_DEBUG = False
DECISION_SUMMARY_DEBUG = True
DECISION_STATE_DEBUG = False
DECISION_ADDING_MEC = False
FITNESS_DEBUG = False
EVOLUTION_ALLOWED = True
OPEN_TRADE = False
LIVE_TRANSCRIPTION_DATA = False
#data output
POOL_TRADER_DATA = False
TOURNAMENT_DEBUG = False
CHILD_DEBUG = False
STRUCTURE_OUTPUT = False
MOOD_OUTPUT = False
PL_OUTPUT = False
PL_OUTPUT_LOCAL = True
#CandleBuckets = [1, 2, 4, 5, 10, 15, 20, 30]
CandleBuckets = [1, 2]
generationWinners = True

MAX_DECISIONS = 100
OUTPUT_ITERATION_DATA = True

#logger.info("configCore file read.")
#EpochBuckets = [1, 2, 4, 5, 10, 15, 20, 30]
EpochBuckets = [1, 2]

'''
from dnaroot import *
from g_DownFractalPresent import *
from g_UpFractalPresent import *
from risk_RiskGeneAlpha import *
'''
