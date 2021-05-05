# load net stuff:

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

def convert_pure(sparse, single_sidelength):
    """
    Info: 
    Args: 
    Returns: 
    """
    
    sidelength = single_sidelength*len_x
    data = None

    for i in range(len(sparse)):
        var = sparse[i]
        val1 = var%sidelength
        val2 = int(var/sidelength)
        val = (val1, val2)
        if val1 != val2 and val1 < val2:
            #data[i][0] = val1
            #data[i][1] = val2
            data.append([val1, val2])
        else:
            pass
            #print("\n data i: ", i, "; equal val1: ", val1, "; val2: ", val2)
    
    return data

def convert_edges(name="data/sparse.txt", len_x=10, single_sidelength=4*10**3):
    """
    Info: open file with name "name" and convert the contained single number indices
        to two-number indices
    Args: name: name of the file
        len_x: number of blocks in a single row
        single_sidelength: sidelength of a single block
    Returns: G: assembled graph
    """
    
    xs = list()
    ys = list()

    sidelength = single_sidelength*len_x
    data = None
    
    dic = {}

    with open(name, "r") as f:
        lines = f.readlines()
        #data = np.zeros([len(lines), 2])
        data = list()
        for i in range(len(lines)):
            #data = np.array([line.strip().split() for line in f],float)
            var = int(lines[i])

            #print("\n var: ", var, "; var.strip(): ", var.strip(), "; var.strip().split(): ", var.strip().split())
            #var = int(var.strip())
            val1 = var%sidelength
            val2 = int(var/sidelength)
            """
            val = (val1,val2)
            try:
                dic[val].append(1)
                print("\n --- i: ", i, "; vals twice")
            except:
                dic[val] = list()
            """
            #print("\n --- val1: ", val1, "; val2: ", val2, "; var: ", var, "; sidelength: ", sidelength)
            #data.append([val1, val2])
            if val1 != val2 and val1 < val2:
                #data[i][0] = val1
                #data[i][1] = val2
                data.append([val1, val2])
            else:
                pass
                #print("\n data i: ", i, "; equal val1: ", val1, "; val2: ", val2)
    #print("\n L: ", len(lines))
    #lines = np.loadtxt('sparse.txt')
    return data

def assemble_graph(data, cut_value = -1):
    """
    Info: assemble graph from two-number edge list "data"
    Args: data: two-number edgelist
        cut_value: int number: In case you only want to use the first 
            N edges of the file, you can set input some cut_value=N, otherwise 
            it should usually be set to -1.
    Returns: G: assembled graph
    """

    # info: make a graph and 
    G = Graph()
    ug = Graph(directed = False)
    # info: adding nodes, in order to first create all the nodes for the network
    t0 = time.time()
    #G.add_nodes_from(list(range(len(data))))
    #for i )):
    t1 = time.time()
    
    # info: adding the edges
    #G.add_edges_from(data)
    vals = list()
    dic = {}
    len_data = len(data)
    vals_edge_list = list()
   
    # TODO: D the analysis for higher index
    if cut_value == -1:
        len_val = len(data)
    else:
        len_val = min(len(data), cut_value)
    
    data_1 = [el[0] for el in data]
    data_2 = [el[1] for el in data]
    max_val = max([max(data_1), max(data_2)])
    print("\n max_val: ", max_val, "; len_val: ", len_val)
    G.add_vertex(max_val)#(len_val)
    #print("\n A G.vertices: ", len(list(G.vertices())))
    for i in range(len_val): 
        vals_edge_list.append([data[i][0], data[i][1]])
        if i%10000==0:
            print("\n i: ", i, " / ", len_val)
    G.add_edge_list(vals_edge_list)
    
    """
    for i in range(len_val):#(len(data)):#range(len(data)):
        data_i0 = data[i][0]
        data_i1 = data[i][1]
        
        try: 
            idx_1 = dic[data_i0]
        except: 
            idx_1 = len(list(dic.keys()))
            dic[data_i0] = idx_1

        try:
            idx_2 = dic[data_i1]
            vals_edge_list.append([idx_2])
        except:
            idx_2 = len(list(dic.keys()))
            dic[data_i1] = idx_2

        vals_edge_list.append([idx_1, idx_2])
        ""
        if data_i0 in vals: 
            pass
        else: 
            vals.append(data_i0)
        
        if data_i1 in vals:
            pass
        else:
            vals.append(data_i1)
        vals_edge_list.append([vals.index(data_i0), vals.index(data_i1)])
        ""
        #G.add_edge(vals.index(data_i0), vals.index(data_i1))
        
        #G.add_edge(data[i][0], data[i][1])
        if i%1000 == 0:
            print("\n i: ", i, " / ", len_data, "; data[i][0]: ", data[i][0], "; data[i][1]: ", data[i][1], "; len(list(G.vertices())): ",  len(list(G.vertices())), "; dt: ", (time.time() - t1))
        if i%10**4 == 0:
            print("\n dt: ", (time.time() - t1))
    """
    #print("\n len(vals_edge_list): ", len(vals_edge_list))
    t2 = time.time()    
    for v in G.vertices():
        neighbors = v.all_neighbors()
        #print("\n v: ", [G.vertex_index[neighbor] for neighbor in neighbors])
    #print("\n len(data): ", len(data)) 
    #print("\n len(list(G.vertices())): ",  len(list(G.vertices())))
    """   
    # info: if the graph is empty, then add at least one node,
    #     which is called the "ZeroNode"
    if len(G.nodes()) == 0:
        G = nx.Graph()
        G.add_node("ZeroNode")
    """
    return G
