# info: try to use the numba_test_2.py created sparse file to make a network

import numpy as np
#import networkx as nx
import matplotlib.pyplot as plt
import time

from graph_tool.all import *
from . import graphics

from matplotlib import rcParams

import pandas as pd 

import seaborn as sns
import numpy as np

import sys 
import argparse

from . import pathogen_analysis as pa
from . import load_net
from . import net_lib as nl
#import graph_support as gs
from . import spec as s
"""
def plot(xs, ys, log=True, name=None):
    ""
    Info: plot the array ys over the array xs with 
        some standard settings and save it
    Args: xs: array of x-values
        ys: array of y-values
        log: bool: True: log-log-plot; False: no log-plot
        name: name of the file to save to
    Returns: -
    ""
    
    fig_size, params = graphics.design(factor=1)
    rcParams.update({'figure.figsize': fig_size})

    fig_1, ax_1 = plt.subplots()

    ax_1.plot(xs, ys, '.')
    if log == True:
        ax_1.set_xscale('log')
        ax_1.set_yscale('log')
    if name!=None:
        fig_1.tight_layout()
        fig_1.savefig(name, dpi=300, bbox_inches="tight")
    plt.show()
"""
def load_idx(name):
    """
    Info: 
    Args: 
    Returns: 
    """
    
    with open(name, "r") as f:
        vals = np.loadtxt(f)
        idx_max = int(vals-1)
    return idx_max

def spec_analysis():
    """
    Info: correlate the specificity values with the values
    Args: -
    Returns: -
    """
    # TODO: check if the values in the dataset really denote the specificity

    data = load_net.convert_edges(name="data/spec_1.txt", len_x=1, single_sidelength=4*10**3)
    g = load_net.assemble_graph(data)
    CDR3s, idx_max, specs = s.specificity()
    
    xs = list()
    ys = list()
    for v, i in zip(g.vertices(), range(len(list(g.vertices())))):
        y = g.get_total_degrees([v])
        x = specs[i]
        ys.append(y)
        xs.append(x)
    plt.plot(xs, ys, '.')
    plt.show()

def main(): 
    """
    Info: Do all the graph analysis
    Args: -
    Returns: -
    """

    print("\n pathogens ...")
    # info: pathogens
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--len_x", help="")
    parser.add_argument("--single_sidelength", help="")
    
    args = parser.parse_args()
    parser_len_x = int(args.len_x) if not args.len_x == None else 1#50
    parser_single_sidelength = int(args.single_sidelength) if not args.single_sidelength == None else 4*10**3
    
    pathogens = ["Influenza", "HIV", "Alzheimer", "Parkinson", "Tuberculosis", "COVID-19"]
    cols = {"Influenza": (1.0, 0.0, 0.0, 1.0), 
            "HIV": (0.0, 1.0, 0.0, 1.0), 
            "Alzheimer": (0.0, 0.0, 1.0, 1.0),
            "Parkinson": (0.0, 0.0, 0.0, 1.0), 
            "Tuberculosis": (0.5, 0.5, 0.5, 1.0), 
            "COVID-19": (0.5, 0.5, 0.0, 1.0)}
    ress = {}
    
    ress_pathogen = list()
    ress_val = list()
       
    fig, ax = plt.subplots(nrows=2, ncols=2)
    ax_00 = ax[0][0]
    ax_01 = ax[0][1]
    ax_10 = ax[1][0]
    ax_11 = ax[1][1]
    """
    # info:  normal analysis
    i = 1
    name = "data/sparse_" + str(i)+ ".txt"
    name_params = "data/sparse_" + str(i) + ".txt"
    print("\n normal: name: ", name, "; name_params: ", name_params)
    data = load_net.convert_edges(name=name, len_x=parser_len_x, single_sidelength=parser_single_sidelength)
    g = load_net.assemble_graph(data)
    nl.net_analysis(g)

    # info: pathogen analysis
    for pathogen in pathogens:
        dic_total = {}
        dic_total["betweenness_dist"] = {}
        dic_total["degree_dist"] = {}
        
        samples = 1
        for i in range(samples):
            #name = "data/" + pathogen + "_small.txt"
            name = "data/" + pathogen + "_small_" + str(i)+ ".txt"
            name_params = "data/" + pathogen + "_params_" + str(i) + ".txt"
            print("\n name: ", name)
            print("\n name_params: ", name_params)
            data = load_net.convert_edges(name=name, len_x=parser_len_x, single_sidelength=parser_single_sidelength)
            g = load_net.assemble_graph(data)
            idx_max = load_idx(name_params)
            print("\n loaded idx_max: ", idx_max)
            res_raw = pa.pathogen_analysis(g, idx_max)
            #TODO: load idx_max value
            ""betw
            res = res_raw["betweenness"][:idx_max]
            print("\n pathogen: ", pathogen, "; res: ", res)
            for i in range(len(res)):
                ress_pathogen.append(pathogen)
                ress_val.append(res[i])
            
            dic = res_raw["betweenness_dist"]
            keys = list(dic.keys())
            vals = list(dic.values())
            
            for j in range(len(vals)):
                try: 
                    dic_tota["betweenness_dist"][keys[j]].append(vals[j])
                except: 
                    dic_total["betweenness_dist"][keys[j]] = list()
                    dic_total["betweenness_dist"][keys[j]].append(vals[j])
            ""
            dic = res_raw["degree_dist"]
            keys = list(dic.keys())
            vals = list(dic.values())

            for j in range(len(vals)):
                try:
                    dic_total["degree_dist"][keys[j]].append(vals[j])
                except:
                    dic_total["degree_dist"][keys[j]] = list()
                    dic_total["degree_dist"][keys[j]].append(vals[j])
        ""betw
        for key in list(dic_total["betweenness_dist"].keys()):
            dic_total["betweenness_dist"][key] = np.mean(dic_total["betweenness_dist"][key])
        ""
        for key in list(dic_total["degree_dist"].keys()):
            dic_total["degree_dist"][key] = np.mean(dic_total["degree_dist"][key])
        keys = list(dic_total["betweenness_dist"].keys())
        vals = list(dic_total["betweenness_dist"].values())
          
        ax_10.plot(keys, vals, '.', color=cols[pathogen])
            
        dic = res_raw["degree_dist"]
        keys = list(dic_total["degree_dist"].keys())
        vals = list(dic_total["degree_dist"].values())
        ax_11.plot(keys, vals, '.', color=cols[pathogen])
        
        ax_01.plot(res_raw["raw_degs"], color=cols[pathogen])

    ax_10.set_title("pathogens")
    #ax_10.set_xscale("log")
    #ax_10.set_yscale("log")
    ax_11.set_xscale("log")
    ax_11.set_yscale("log")
    #res[pathogen] = res["betweenness"] 
    plt.show()   
    #xs, ys = viruses(g)
    ress["pathogen"] = ress_pathogen
    ress["val"] = ress_val
    data = pd.DataFrame(ress)
    sns.stripplot(data=data, x="pathogen", y="val", ax=ax_00)
    """ 
    
    spec_analysis()
    #data = pd.DataFrame(ress)
    #ax_01.plot(ress)
    """
    g = assemble_graph("sparse_virus.txt")
    """
    # TODO: some virus graph analysis

if __name__ == "__main__":
    main()
