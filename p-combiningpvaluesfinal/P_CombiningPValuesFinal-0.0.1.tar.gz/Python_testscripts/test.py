#from combinationpvalues import InfinitePs
#from combinationpvalues import CountPs
#from combinationpvalues import StoufferMethod

import combinationpvalues as cp

import inspect

all_functions = inspect.getmembers(cp, inspect.isfunction)


A = cp.CountPs("Stouffer") #name of statistic: Fisher, Pearson, Ed, Stouffer, George, Tippett
Input = A.InfinitePs(0.1,.3,.7)
Output = A.StoufferMethod(Input)
print(Output)






