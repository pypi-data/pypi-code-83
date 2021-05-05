# info: perform analysis of the private and the public parts
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from matplotlib import rcParams
from . import graphics

import sys
sys.path.append("./public_analysis/")
import plot1 as p1
import plot2 as p2
import plot3 as p3
import plot4 as p4

from . import funcDictionary as dic
#import funcDictionaryLevenshtein as dicLeven
from . import plotData as pD

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import os

import time

import networkx as nx
import sys

#import imnet
import random

import matplotlib.patches as mpatches

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import ListedColormap
from collections import OrderedDict

import seaborn as sns

# info: "graphics" is a script, written by myself
from . import graphics
import matplotlib.gridspec as gridspec

plotData = pD.PlotDataLevenshtein()
plotData.clusterMinLen = 1

# info: plotData.N: the total number of sequences, which is loaded
plotData.N = 10**5

# info: size of one sample (and then they compare many samples
#     in order to perform the private vs. public analysis)
sample_size = 8*10**3 # 40*10**3 seems to be possible
samples = 5

plotData.min_ldVal = -1
plotData.maxVal = 3
plotData.max_ldVal = plotData.maxVal
step = 0

maxVals = [1, 2, 3, 4, 5]

#------------------------------------------------------------------

fig_size, params = graphics.design()
rcParams.update({'figure.figsize': fig_size})

# tell matplotlib about your params
rcParams.update(params)

#fig, ax = plt.subplots(nrows = 2, ncols = 2)
fig = plt.figure()
fig_dummy = plt.figure()

gs00 = gridspec.GridSpec(1, 1)
gs01 = gridspec.GridSpec(1, 1)
gs11 = gridspec.GridSpec(1, 1)
gs10A = gridspec.GridSpec(1, 1)
gs10B = gridspec.GridSpec(1, 1)

ax00 = fig.add_subplot(gs00[0])
ax01 = fig.add_subplot(gs01[0])
ax10 = fig.add_subplot(gs10A[0])
#-ax_public_simple = fig.add_subplot(gs10B[0])
ax_public_simple = fig_dummy.add_subplot(gs10B[0])
ax11 = fig.add_subplot(gs11[0])
ax = [[ax00, ax01], [ax10, ax11]]

gs00.tight_layout(fig, rect=[0.5, 0.5, 1.0, 1.0])
gs01.tight_layout(fig, rect=[0.0, 0.0, 0.5, 0.5])

gs11.tight_layout(fig, rect=[0.5, 0.0, 1.0, 0.5])
gs10A.tight_layout(fig, rect=[0.0, 0.5, 0.5, 1.0])

plt.tight_layout()

# set nice figure sizes
fig_width_pt = 245/1.00    # Get this from LaTeX using \showthe\columnwidth
golden_mean = (np.sqrt(5.) - 1.) / 2.  # Aesthetic ratio
ratio = golden_mean
inches_per_pt = 1. / 72.27  # Convert pt to inches
fig_width = fig_width_pt * inches_per_pt  # width in inches
fig_height = fig_width*ratio  # height in inches
fig_size = [fig_width, fig_height]
rcParams.update({'figure.figsize': fig_size})

# tell matplotlib about your params
rcParams.update(params)

fig_bars, ax_a = plt.subplots()
fig_bars = plt.figure()
ax_a = plt.subplot2grid((2, 2), (0, 0), rowspan=2, colspan=2)

for name in ["not_important"]: 
    #-ax_a, ax_b, ax_c, _, ax[0][0], collection = p1.plot1(ax_a, ax_b, ax_c, ax_d, ax[0][0])
    ax_a, ax[0][0], collections = p1.plot1(ax_a, ax[0][0])
    #_, ax[0][0], collection = p1b.plot1(ax_a, ax[0][0])
    #ax[0][1] = p2.plot2(ax[0][1], collections)
    sample_size = 10**5#8*10**3
    ax[1][1], g_vdj, seqss = p4.plot4(ax[1][1], sample_size=sample_size)
    print("\n --- len(seqss): ", len(seqss['mouse']), "; len(seqss): ", len(seqss['mouse']))
    print(str(os.path.realpath(__file__)), ": done plot4, starting plot3 ...")
    #print("\n /home/paul/Documents/imnet-master2/public_analysis.py: done plot4, starting plot3 ...") 
    ax[1][0], ax_a, ax_public_simple, ax_b = p3.plot3(ax[1][0], g_vdj, seqss, ax_a, ax_public_simple, samples_big=2)
    print("\n /home/paul/Documents/imnet-master2/public_analysis.py: done this part")
    # info: ax[1][0] - somehow cliquesize of the network created from certain frequency networks 

fig.tight_layout()
fig_bars.tight_layout()
fig.savefig("public_analysis.png", dpi=300, bbox_inches="tight")
fig_bars.savefig("parameters.png", dpi=300, bbox_inches="tight")
#fig_public_simple.savefig("public_simple.png", dpi=300, bbox_inches="tight")
plt.show()
