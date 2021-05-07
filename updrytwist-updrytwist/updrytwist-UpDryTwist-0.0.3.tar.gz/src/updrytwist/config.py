#!/usr/bin/env python

import logging
import os
import yaml
import sys
import argparse

DEFAULT_CONFIG    = os.getenv( 'CONFIGFILE', 'myapp.yaml' )
DEFAULT_LOGFILE   = os.getenv( 'LOGFILE', 'myapp.log' )

DEFAULT_LOGFORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DEFAULT_LOGLEVEL  = 'INFO'


def dictread( dictionary, key, default=None ):
    if dictionary is None:
        return default
    elif key in dictionary:
        return dictionary[key]
    else:
        return default


def forceread ( dictionary, key ):
    value = dictread(dictionary, key, None )
    if value is None:
        raise ValueError( f'Failed to read value {key} from configuration!')
    return value


class Config:

    c = None

    def __init__ ( self, filename=None ):

        if filename is None:
            filename = DEFAULT_CONFIG

        self.filename = filename
        self.readCommandLine()

        with open(self.filename) as source:
            self.config = yaml.load( source, Loader=yaml.FullLoader )

    def value ( self, key, default=None ):
        return dictread(self.config, key, default)

    @staticmethod
    def get ( key, default=None ):
        return dictread(Config.c.config, key, default)

    def readCommandLine ( self ):

        parser = argparse.ArgumentParser(description='Generic UpDryTwist Command Parser')
        parser.add_argument('--config', help='Path to configuration file', default=None)
        args = parser.parse_args()
        if 'config' in vars(args):
            fileName = vars(args)['config']
            if fileName is not None:
                self.filename = fileName


def getConfig () -> Config :
    return Config.c


def loadConfig ():
    try:
        Config.c = Config()
    except Exception as e:
        print( "Cannot load configuration from file {}: {}".format( DEFAULT_CONFIG, str(e)))
        sys.exit(2)


def initLogging ():

    logFile   = Config.get( 'logfile',   DEFAULT_LOGFILE )
    logFormat = Config.get( 'logformat', DEFAULT_LOGFORMAT )
    logLevel  = Config.get( 'loglevel',  DEFAULT_LOGLEVEL )

    root = logging.getLogger()
    root.setLevel( logLevel )

    handler = logging.FileHandler( logFile )
    handler.setLevel( logLevel )
    handler.setFormatter( logging.Formatter(logFormat ))
    root.addHandler( handler )

    """
    handler = logging.StreamHandler( sys.stdout )
    handler.setLevel( logLevel )
    handler.setFormatter( logging.Formatter( logFormat ))
    root.addHandler( handler )
    """


def initialize ():
    loadConfig()
    initLogging()
