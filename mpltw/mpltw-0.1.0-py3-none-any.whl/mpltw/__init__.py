import os
import matplotlib as mpl
import matplotlib.font_manager as fm

#for convenience
from matplotlib import pyplot as plt

fe = fm.FontEntry(
    fname=os.path.join(os.path.dirname(__file__), 'TaipeiSansTCBeta-Regular.ttf'),
    name='Taipei Sans TC Beta')
fm.fontManager.ttflist.insert(0, fe)
mpl.rcParams['font.family'] = fe.name