# info: plot3.py

import funcDictionary as dic
#import funcDictionaryLevenshtein as dicLeven

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
#import funcDictionaryLevenshtein as dicLeven
import plotData as pD

import pandas as pd

import matplotlib.patches as mpatches
# from matplotlib.pypot import gca, show

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import ListedColormap
from collections import OrderedDict

#import graph_tool as gt
#from graph_tool.all import *
def degree_mean(g):
    deg = dict(g.degree())
    deg_values = list(deg.values())
    deg_mean = np.mean(deg_values)
    return deg_mean
def public_data(thresholds, dic_num_values): 
    """
    info: sort the values of the dictionary into the thresholds
    input: thresholds: an array of the thresholds (usually e.g. [1, 2, 3, 4, 5, 6, 7])
        dic_num_values: ...
    output: public_nums_normed: ...
    """
    print("\n --- thresholds: ", thresholds)
    print("\n --- len(dic_num_values): ", len(dic_num_values))

    public_nums = np.zeros(len(thresholds))
    for j in range(len(thresholds)):
        threshold = thresholds[j]
        public_num = 0
        for i in range(len(dic_num_values)):
            if dic_num_values[i] > threshold:
                public_num += 1
        public_nums[j] = public_num

    for i in range(len(thresholds)):
        pass

    len_dic_num_values = len(dic_num_values)
    public_nums_normed = [el/len_dic_num_values for el in public_nums]


    return public_nums_normed

def frequency_distribution(seq, samples, sample_size, thresholds):
    """
    info: make frequency distribution of the sequences
    input: seq: list of sequences
        samples: number of samples
        sample_size: size of a sample
        thresholds: list of thresholds, usually 
            is [1, 2, 3, 4, 5, 6, 7]
    output: public_nums_normed: the finished data of the frequencies over the threshold values
    """
     
    print("\n AAA len(seq): ", len(seq))
    dic = {}
    dic_num = {}

    # info: make normal list, which
    #     includes the indices, 
    #     where each sequence occurs
    #     (so each element is a list)
    for i in range(len(seq)):
        try: 
            dic[seq[i]].append(i)
        except: 
            dic[seq[i]] = list()
            dic[seq[i]].append(i)
   
    dic_values = list(dic.values())

    for i in range(len(dic_values)):
        for j in range(len(dic_values[i])):
            for sample in range(samples):
                lower_bound = sample*sample_size
                upper_bound = (sample+1)*sample_size

                if dic_values[i][j] >= lower_bound:
                    if dic_values[i][j] < upper_bound:
                        try: 
                            dic_num[seq[i]] += 1
                        except: 
                            dic_num[seq[i]] = 1
    
    
    dic_num_values = list(dic_num.values())
    
    public_nums_normed = public_data(thresholds, dic_num_values)

    return public_nums_normed, dic_num

def load_seq_choices(i, N):
    """
    Info: 
    Args: 
    Returns: 
    """
    print("\n --- load_seq_choices i: ", i, "N: ", N)
    src_name = "sequences/sequence_" + str(i+1) + ".txt"#name
    
    plotData = pD.PlotDataLevenshtein()
    plotData.clusterMinLen = 1
    plotData.N = N#10**6#4*10**3
    plotData.min_ldVal = -1
    plotData.maxVal = 3
    plotData.max_ldVal = plotData.maxVal
    gpu_l = 8000 #5000
    step = 0
    _, _, seq, filename, _ = dic.loadSequence(step, plotData, isExtractNum=False, src=src_name)
    
    return seq

def find_public(seq, sample_size, ax_10, ax_public_simple, name, samples_big):
    """
    info: find the public sequences among a list 
        of sequences
    input: seq: set of the sequences
        sample_size: size of a sample
    output: 
    """
    
    print("\n A -- A -- A : len(seq): ", len(seq))

    # info: set label parameters
    xlabel = 0.02
    ylabel = 0.92

    DxLabel = 0.115
    DyLabel = 0.1

    samples = int(len(seq)/sample_size)
    print("\n --- samples: ", samples, "; len(seq): ", len(seq))

    #dic_num_mean = frequency_distribution(seq, samples, sample_size)
    
    # info: find out, how many public exist:
    thresholds = [0, 1, 2, 3, 4, 5, 6]
    public_nums_array = []

    #samples_big = 2#20
    for i in range(samples_big):
        # info: randomly choose a subsample, in order to make many samples
        #seq_choices = random.sample(seq, int(len(seq)/2))
        seq_choices = load_seq_choices(i, len(seq))

        if i == 0:
            public_nums_normed, dic_num = frequency_distribution(seq_choices, samples, sample_size, thresholds)
            # info: plot data points
            #-ax_10.plot(thresholds, public_nums_normed, '.', color='blue')
            public_nums_array.append(public_nums_normed)
            public_nums_normed = [el/samples_big for el in public_nums_normed]
        else:
            public_nums_normed_i, _ = frequency_distribution(seq_choices, samples, sample_size, thresholds)
            # info: plot data points
            #-ax_10.plot(thresholds, public_nums_normed_i, '.', color='blue')
            public_nums_array.append(public_nums_normed_i)
            public_nums_normed = [public_nums_normed[j] + public_nums_normed_i[j]/samples_big for j in range(len(public_nums_normed))]
    

    # info: We give these empty start data, just
    #     to shift the seaborn plot, thus it is the 
    #     pair (-1, 0) is just for graphics design
    data_x = [-1]
    data_y = [0]
    data_x_reduced = []
    data_y_reduced = []
    
    for i in range(len(public_nums_array)):
        for j in range(len(public_nums_array[i])):
            data_x.append(j)
            data_y.append(public_nums_array[i][j])
            # TODO: We now plot only j=2; Is that already accumulated or should
            #     we still do that?
            if j == 1:
                data_x_reduced.append(j)
                data_y_reduced.append(public_nums_array[i][j])
    
    y_mean = np.mean(data_y_reduced)
    y_std = np.std(data_y_reduced)
    #TODO: std okay or should we make /sqrt(N)
    
    """
    print("\n --- data_x: ", data_x)
    print("\n --- data_y: ", data_y)
    print("\n data_x_reduced: ", data_x_reduced)
    print("\n data_y_reduced: ", data_y_reduced)
    print("\n y_mean: ", y_mean)
    print("\n y_std: ", y_std)
    """
    data = pd.DataFrame({"x": data_x, "y": data_y})
    data_reduced = pd.DataFrame({"x": data_x_reduced, "y": data_y_reduced})

    #sns.stripplot(x="x", y="y", data=data_reduced, ax=ax_public_simple)
    ax_public_simple.bar([0], [public_nums_normed[1]], zorder=-1.0)
    #ax_public_simple.errorbar([0], [y_mean], yerr=[y_std], capsize=100.0, zorder=1.0)
    sns.violinplot(x="x", y="y", data=data_reduced, ax=ax_public_simple, color=(0.6, 0.6, 1.0, 0.5), linewidth=0, zorder = 3, width=0.5)

    ax_public_simple.set_xlim(-0.5, 0.5)
    ax_public_simple.set_ylim(bottom=0.0)
    ax_public_simple.set_xticks([])
    ax_public_simple.set_xticklabels([])
    ax_public_simple.set_ylabel("$f_{k=2}$")
    ax_public_simple.set_xlabel("public")
    
    thresholds = [el+1 for el in thresholds]
    if name=="human":
        col="green"#"orange"
    if name=="mouse":
        col=(0.3, 0.3, 0.8, 1.0)
    ax_10.plot(thresholds, public_nums_normed, zorder=-1, label=name, color=col)
    sns.violinplot(x="x", y="y", data=data, ax=ax_10, linewidth=0.0, color=(0.6, 0.6, 1.0, 0.5))
    ax_10.set_xticks([1, 2, 3, 4, 5, 6, 7])
    ax_10.set_xticklabels(["1", "2", "3", "4", "5", "6", "7"])
    ax_10.set_xlim(1, max(thresholds))
    ax_10.set_ylim(10**(-4), 10**0)
    #ax_10.set_ylim(0, max(public_nums))
    ax_10.set_yscale('log')
    ax_10.set_xlabel("$k$")
    ax_10.set_ylabel("$f_k(k)$")
    ax_10.legend(frameon=False)

    ax_10.add_patch(Polygon([[0.0, 1.0], [DxLabel, 1.0], [DxLabel, 1.0 - DyLabel], [0.0, 1.0 - DyLabel]],
      closed=False, fill=True, color="white", alpha=0.9, transform = ax_10.transAxes, zorder=2))
    ax_10.text(xlabel, ylabel, '(a)', transform = ax_10.transAxes, zorder=3)

    return dic_num, ax_10, ax_public_simple

def network_properties(g_vdj, seqs_original, ax_10, ax_public_simple, name, samples_big, with_graph=True):
    # Why is he using g_vdj AND seqs_original?
    """
    info: %...
    input: %...
    output: %...
    """
    
    dic_num, ax_10, ax_public_simple = find_public(seqs_original, int(len(seqs_original)/10), ax_10, ax_public_simple, name, samples_big)
    with_graph = False
    if with_graph: 
        g_public = nx.Graph()
        g_vdj_nodes = list(g_vdj.nodes())

        threshold = 2

        print("\n /home/paul/Documents/imnet-master2/public_analysis/plot3.py: len(dic_num): ", len(dic_num))

        for i in range(len(g_vdj_nodes)):
            try:
                if i%1000==0:
                    print("\n /home/paul/Documents/imnet-master2/public_analysis/plot3.py: i: ", i)
                if dic_num[seqs_original[i]] > threshold:
                    g_public.add_node(i)
            except:
                print("\n /home/paul/Documents/imnet-master2/public_analysis/plot3.py: i: ", i, "; WARNING: there seems to be an element, that is not present in collection. (paul)")
        
        edges_list = list(g_vdj.edges())

        for i in range(len(edges_list)):
            if (edges_list[i][0] in g_public) and (edges_list[i][1] in g_public):
                g_public.add_edge(edges_list[i][0], edges_list[i][1])
                #gt_public.add_edge(edges_list[i][0], edges_list[i][1])

        # info: calculate_properties: 
        degree_mean_vdj = degree_mean(g_vdj)
        degree_mean_public = degree_mean(g_public)
        """-
        assortativity_coefficient_vdj = nx.degree_assortativity_coefficient(g_vdj)
        if len(list(g_public.nodes())) > 0:
            assortativity_coefficient__public = nx.degree_assortativity_coefficient(g_public)
        else: 
            assortativity_coefficient__public = -1
            print("\n /home/paul/Documents/imnet-master2/public_analysis/plot3.py: The g_public is 0, you should have a look.")
        """
        assortativity_coefficient_vdj = -1
        assortativity_coefficient__public = -1
    else: 
        degree_mean_vdj = -1
        degree_mean_public = -1
        assortativity_coefficient_vdj = -1
        assortativity_coefficient__public = -1

    return degree_mean_vdj, degree_mean_public, assortativity_coefficient_vdj, assortativity_coefficient__public, ax_10, ax_public_simple

def plot3(ax_10, g_vdj, seqs_originals, ax_a, ax_public_simple, samples_big=2):
    """
    info: 
    input: 
    output: 
    """
    
    names = ["mouse", "human"]
    print("\n CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")

    for name in names: 
        ax_10, ax_a, ax_public_simple, ax_b = plot3_species(ax_10, g_vdj, seqs_originals[name], ax_a, ax_public_simple, name, samples_big)

    return ax_10, ax_a, ax_public_simple, ax_b

def plot3_species(ax_10, g_vdj, seqs_original, ax_a, ax_public_simple, name, samples_big):
    """
    info: %...
    input: %...
    output: %...
    """ 
    
    #g_vdj = dicLeven.make_graph(seq_sample, min_ld=plotData.min_ldVal,
    #            max_ld=plotData.max_ldVal, gpu_l=gpu_l)

    # info: make samples, where for each sample a network is created 
    #     and the network properties are calculated
    samples = 1
    
    degree_mean_vdj_array = []
    degree_mean_public_array = []
    assortativity_coefficient_array = []
    assortativity_coefficient_public_array = []

    for i in range(samples):
        print("\n /home/paul/Documents/imnet-master2/public_analysis/plot3.py: ", \
                " samples: ", i, " / ", samples)
        #-g_vdj = dicLeven.make_graph(seqs_original, min_ld=-1, \
        #-       max_ld=2, gpu_l=8000)
        g_vdj = None

        # info: loading the seqs_ax_10 sequences
        plotData = pD.PlotDataLevenshtein()
        plotData.clusterMinLen = 1
        plotData.N = len(seqs_original)#-10**6
        plotData.min_ldVal = -1
        plotData.maxVal = 3
        plotData.max_ldVal = plotData.maxVal
        a, a4, seqs_ax_10, filename, ls = dic.loadSequence(0, plotData, isExtractNum=False, animal=name)

        print("\n len(seqs_ax_10): ", len(seqs_ax_10))

        # info: proceed with the network properties
        degree_mean_vdj, degree_mean_public, assortativity_coefficient_vdj, \
            assortativity_coefficient_public, ax_10, ax_public_simple = network_properties(g_vdj, seqs_ax_10, ax_10, ax_public_simple, name, samples_big)

        degree_mean_vdj_array.append(degree_mean_vdj)
        degree_mean_public_array.append(degree_mean_public)
        assortativity_coefficient_array.append(assortativity_coefficient_vdj)
        assortativity_coefficient_public_array.append(assortativity_coefficient_public)
        
    ones = list(np.ones(len(degree_mean_vdj_array)))
    twos = [el*2 for el in ones]
    
    xs = ones + ones + twos + twos
    ys = degree_mean_vdj_array + degree_mean_public_array + assortativity_coefficient_array + assortativity_coefficient_public_array
    h = ones + twos + ones + twos
    total_array = pd.DataFrame({"x": ys, "y": xs, "hue": h})

    degree_mean_vdj_array = pd.DataFrame({'x':
        ones, 'y':
        degree_mean_vdj_array})
    degree_mean_public_array = pd.DataFrame({'x':
        twos,
        'y': degree_mean_public_array})
    assortativity_coefficient_array = pd.DataFrame({'x':
        ones,
        'y': assortativity_coefficient_array})
    assortativity_coefficient_public_array = pd.DataFrame({'x': 
        twos, 
        'y': assortativity_coefficient_public_array})
    
    """
    print("\n /home/paul/Documents/imnet-master2/public_analysis/plot3.py: ", \
            "degree_mean_vdj_array: ", degree_mean_vdj_array)
    print("\n degree_mean_public_array: ", degree_mean_public_array)
    print("\n assortativity_coefficient_array: ", assortativity_coefficient_array)
    print("\n assortativity_coefficient_public_array: ", assortativity_coefficient_public_array)
    
    print("\n degree_mean_vdj: ", degree_mean_vdj)
    print("\n degree_mean_public: ", degree_mean_public)
    print("\n assortativity_coefficient_vdj: ", assortativity_coefficient_vdj)
    print("\n assortativity_coefficient_public: ", assortativity_coefficient_public)
    ""
    sns.stripplot(x="y", y="x", data=degree_mean_vdj_array, ax=ax_a, orient='h', color='red')
    sns.stripplot(x="y", y="x", data=degree_mean_public_array, ax=ax_a, orient='h', color='red')
    sns.stripplot(x="y", y="x", data=assortativity_coefficient_array, ax=ax_a, orient='h', color='red')
    sns.stripplot(x="y", y="x", data=assortativity_coefficient_public_array, ax=ax_a, orient='h', color='red')
   
    print("\n total_array: ", total_array)
    sns.violinplot(x="x", y="y", hue="hue", data=total_array, ax=ax_a, orient='h', width=0.7, color=(0.5, 0.8, 1.0, 0.8))
    #sns.violinplot(x="x", y="y", hue="hue", data=data, ax=ax1, width=0.7, color=(0.5, 0.8, 1.0, 0.8))
    """
    width = 0.6
    #-col_blue = (0.5, 0.5, 1.0, 1.0)
    #-col_red = (1.0, 0.5, 0.5, 1.0)
    if name == "mouse": 
        col_blue = (0.5, 0.5, 1.0, 0.5)
        col_red = (1.0, 0.5, 0.5, 0.5)
    if name == "human":
        col_blue = (0.5, 0.5, 1.0, 0.5)
        col_red = (1.0, 0.5, 0.5, 0.5)

    ax_a.barh([0.0], [degree_mean_vdj], color=col_blue, zorder=-3, height=width)
    ax_a.barh([0.5], [degree_mean_public], color=col_red, zorder=-2, height=width)
    #sns.stripplot(x="x", y="y", data=test_data, ax=ax_a)
    """
    ax_a.bar(g = sns.catplot(
        data=penguins, kind="bar",
        x="species", y="body_mass_g", hue="sex",
        ci="sd", palette="dark", alpha=.6, height=6
        ))
    ax_b.bar()
    """
    """
    ax_a.set_ylabel("degree")
    ax_b.set_ylabel("DAC")
    ax_a.set_xticks([1, 2])
    ax_b.set_xticks([1, 2])
    ax_a.set_xticklabels(["public", "private"])
    ax_b.set_xticklabels(["public", "private"])
    """
    ax_a.set_yticks([0.25, 1.75])
    ax_a.set_yticklabels(["$d$", "$a$"])
    #-ax_a.legend(["total", "public"], frameon = False)
    ax_a.legend(["total", "public"], frameon = False, loc="lower right")
    ax_a.set_xlabel("degree $d$")
    ax_a.set_xlim([0.0, 30.0])

    ax_b = ax_a.twiny()

    ax_b.barh([1.5], [assortativity_coefficient_vdj], color=col_blue, zorder=-3, height=width)
    ax_b.barh([2.0], [assortativity_coefficient_public], color=col_red, zorder=-2, height=width)
    ax_b.set_xlim([0.0, 1.0])
    ax_b.set_xlabel("assortativity $a$")
    
    #plt.setp(ax_b.get_yticklabels(), rotation=45)
    
    #ax_b = ax_a.twinx()
    #ax_b = ax_a.twinx(ii)

    #ax_b.set_yticklabels(["", ""])
    #ax_b.legend([], frameon = False)
    #ax_b.

    """
    g_private = nx.Graph()
    g_public = nx.Graph()
    #gt_public = gt.Graph()

    collection_keys = collection.keys()
    collection_values = collection.values()
     
    seqs = list(g_vdj.nodes())

    # info: suppose, that the order of sequences
    #     in collection is the same as in seqs

    for i in range(len(seqs)):
        try: 
            if collection[seqs_original[i]] > 2:
                g_public.add_node(i)
                #gt_public.add_vertex(i)
        except:
            print("\n WARNING: there seems to be an element, that is not present in collection. (paul)")

    edges_list = list(g_vdj.edges())
 
    for i in range(len(edges_list)):
        if (edges_list[i][0] in g_public) and (edges_list[i][1] in g_public):
            g_public.add_edge(edges_list[i][0], edges_list[i][1])
            #gt_public.add_edge(edges_list[i][0], edges_list[i][1])
    
    nodes_public = len(list(g_public.nodes()))
    nodes_total = len(list(g_vdj.nodes()))
    
    print("\n nodes_public: ", nodes_public)
    print("\n nodes_total: ", nodes_total)
    print("\n nodes_public/nodes_total: ", nodes_public/nodes_total)
    """
    return ax_10, ax_a, ax_public_simple, ax_b
