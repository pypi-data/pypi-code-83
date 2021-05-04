"""
Module to give interpretation of errors given by AVBP code in log files.
Takes in input a 'avbp.o' file or a 'job.out' file,
parses the file as it looks for the Error message, 
and returns an explanation for the error.

"""

import yaml
import os
import pkg_resources 

__all__ = ["parse_avbp_o"]

def init_format_rules(logclassify_rc=None):
    """Load format rules from resources.
    """
    if logclassify_rc is None:
            logclassify_rc = pkg_resources.resource_filename('runcrawler',
             './scan_log.yml')


    with open(logclassify_rc) as fin:
        scan_dict = yaml.load(fin, Loader=yaml.SafeLoader)

    return scan_dict


def parse_avbp_o(fname, logclassify_rc=None):
    """
    Parses the avbp.o file and searches for a key in the
    dictionnary
    """

    out = -1

    # read the avbp.o file
    with open(fname, "r") as fin:
        lines = fin.readlines()

    # get the standard dictionary     
    scan_dict = init_format_rules(logclassify_rc=None)

    for error in scan_dict:        
        pattern = error["pattern"]
        code = error["code"]

        for line in lines:
            if pattern in line:
                if code > out:
                    out = code

    return out

