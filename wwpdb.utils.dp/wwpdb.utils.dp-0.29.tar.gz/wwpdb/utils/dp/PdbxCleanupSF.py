#
# File:    PdbxSFCleanupSF.py
##
"""  Classes to aid in cleanup of mmCif formatted SF files
"""

__docformat__ = "restructuredtext en"
__author__ = "Ezra Peisach"
__email__ = "ezra.peisach@rcsb.org"
__license__ = "Apache 2.0"

import logging
import os
import sys

from mmcif.io.IoAdapterCore import IoAdapterCore

logger = logging.getLogger(__name__)


class PdbxCleanupSF(object):
    def __init__(self):
        pass

    def cleanupSF(self, pathIn, pathOut, pdbid=None):
        """Cleans up incoming SF file by reading and writing it out, 
        updating a few key items

        Returns True on success, False on failure
        """

        # Some basics - determine pdb id if possible
        if pdbid is None:
            pdbid = "xxxx"
            
        try:
            io = IoAdapterCore()
            containerList = io.readFile(pathIn)
            if containerList is None:
                logger.error("Container list could not be read %s", pathin)
                return False
            if len(containerList) < 1:
                logger.error("Empty structure factor file %s", pathin)
                return False

            ok = self.updateEntryIds(pdbid, containerList)
            if not ok:
                return ok

            ok = self.updateContainerNames(idCode=pdbid, containerList=containerList)
            if not ok:
                return ok
            
            return io.writeFile(pathOut, containerList)
                
        except Exception as e:
            logger.exception("Failing with %s" % str(e))
            return False

    def updateEntryIds(self, idCode, containerList):
        catNameList=[('cell','entry_id'),('entry','id'),('symmetry','entry_id')]
        try:
            for ii,container in enumerate(containerList):
                for catName,attribName in catNameList:
                    catObj = container.getObj(catName)
                    if catObj is not None:
                        nRows=catObj.getRowCount()
                        if nRows == 1:
                            ok=catObj.setValue(value=idCode,attributeName=attribName,rowIndex=0)
            return True
        except Exception as e:
            logger.exception("While updating entry id")
            return False

    def updateContainerNames(self, idCode, containerList):
        try:
            for ii,container in enumerate(containerList):
                if ii < 1:
                    cName='r'+str(idCode).lower()+'sf'
                else:
                    rem = int((ii -1)/26)
                    mod = (ii -1) % 26
                    opt = ""
                    if sys.version_info[0] > 2:
                        if rem > 0:
                            opt = str(chr(rem+64))
                        cName='r'+str(idCode).lower()+str(chr(mod+65))+opt+'sf'
                    else:
                        if rem > 0:
                            opt = str(unichr(rem+64))
                        cName='r'+str(idCode).lower()+str(unichr(mod+65))+opt+'sf'
                container.setName(cName)
            return True
        except Exception as e:
            logger.exception("While updating datablock names")
            
        return False
            
