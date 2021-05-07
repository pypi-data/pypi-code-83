'''
Formula being used
    f(x) = (b-a)(x-min)/(max-min)
'''
from math import log,log10


def change_range(x,min,max,a,b):
    try:
        return round((log(((b-a)*(x-min))/(max-min)*1e5)/log(5))*10)
    except:
        #print("No Change")
        return ((b-a)*(x-min))/(max-min)