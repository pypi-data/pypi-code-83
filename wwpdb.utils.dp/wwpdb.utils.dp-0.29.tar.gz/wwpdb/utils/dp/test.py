import logging
import os

from wwpdb.utils.dp.PdbxCleanupSF import PdbxCleanupSF
from mmcif.io.IoAdapterCore import IoAdapterCore

logger = logging.getLogger(__name__)


class ModelIo(object):
    def getPdbCode(self, modelPath):
        """ Return the database code for the input database id/name
        
        Returns None if unknown
        """

        if modelPath is None or not os.path.exists(modelPath):
            return None

        io = IoAdapterCore()
        containerList = io.readFile(modelPath, selectList=['database_2'])
        if containerList is None or len(containerList) < 1:
            return None

        c0 = containerList[0]
        print(c0.getObjNameList())
        try:
            catObj = c0.getObj('database_2')

            vals  = catObj.selectValuesWhere("database_code", "PDB", "database_id")
            return self.__firstOrDefault(vals,default=None)
        except Exception as e:
            return None

    def __isEmptyValue(self,val):
        if ((val is None) or (len(val) == 0) or (val in ['.','?'])):
            return True
        else:
            return False

    def __firstOrDefault(self,valList,default=''):
        if len(valList) > 0 and not self.__isEmptyValue(valList[0]):
            return valList[0]
        else:
            return default


sfin = "sf-test.cif"
sfout = "testout.cif"
modelIn= "6s0v.cif"

mio = ModelIo()
pdbId = mio.getPdbCode(modelIn)
pcsf = PdbxCleanupSF()
#ret = pcsf.cleanupSF("6s0v-small.cif", "testout.cif")
ret = pcsf.cleanupSF("sf-test.cif", "testout.cif", pdbId)
print("FInished status is %s" % ret)
      
