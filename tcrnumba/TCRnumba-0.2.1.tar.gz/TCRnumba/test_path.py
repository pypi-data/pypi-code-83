#import inspect, os

#print (inspect.getfile(inspect.currentframe())) # script filename (usually with path)
#print (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) # script directory

import os

print(os.path.realpath(__file__))
