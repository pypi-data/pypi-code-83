from EzCheck import *
from DataModel import *
from EzCustomerMovement import *
from EzRFM import *
from EzCohort import *

check = EzCheck()
dm = DataModel()
rfm = EzRFM()
cm = EzCustomerMovement()
ch = EzCohort()
libs = [check,dm,rfm,cm,ch]
if __name__ == "__main__":
    for lib in libs:
        print(f"{lib.prep_data}")