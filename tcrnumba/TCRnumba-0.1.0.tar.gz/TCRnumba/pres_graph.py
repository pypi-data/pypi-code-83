# info: make graphs for the presentation

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def make_clusters():
    """
    info: 
    input: 
    output: 
    """
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    g1 = nx.gnp_random_graph(20, 0.1)
    
    num_nodes = len(list(g1.nodes()))
    cluster_idxs = list([None]*num_nodes)
    print("\n clusters_idxs: ", cluster_idxs)
    a = list(nx.connected_components(g1))
    for i in range(len(a)):
        for j in range(len(a[i])):
            cluster_idxs[list(a[i])[j]] = i/len(a)
    
    print("\n c: ", list(a))
    print("\n cluster_idxs: ", cluster_idxs)
    cmap = [(0.0, el, 0.0, 1.0) for el in cluster_idxs]
    
    nx.draw(g1, ax=ax1, node_color=cmap)
    plt.show()

def make_cliques():
    """
    info:
    input: 
    output: 
    """
    fig1, ax1 = plt.subplots()
    
    g = nx.gnp_random_graph(20, 0.2)
    
    num_nodes = len(list(g.nodes()))
    cliques_idxs = list([None]*num_nodes)
    """
    a = list(nx.find_cliques(g))
    print("\n a: ", a)
    for i in [0]:#range(len(a)):
        for j in range(len(a[i])):
            cliques_idxs[list(a[i])[j]] = 1#i/len(a)
    """
    
    cliques_idxs = list(nx.max_clique(g))
    print("\n cliques_idxs: ", cliques_idxs)
    for i in range(len(cliques_idxs)):
        if cliques_idxs[i] == None:
            cliques_idxs[i] = 0
        else: 
            cliques_idxs[i] = 1
    print("\n cliques_idxs: ", cliques_idxs)
    cmap = [(0.0, el, 0.0, 1.0) for el in cliques_idxs]
    nx.draw(g, ax=ax1, node_color=cmap)
    plt.show()

if __name__ == "__main__":
    #make_clusters()
    make_cliques()
