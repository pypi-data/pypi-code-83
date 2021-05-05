import numpy as np 
import scipy.special as spec
import matplotlib.pyplot as plt

def barabasi_p_degree(k, l, m):
    """
    info: k and l must always be equal or bigger to m
    input: 
    output: 
    """
    if m > min(k, l):
        print("\n /home/paul/Documents/imnet-master2: WARNING: m > max(k, l)")
    c1 = m*(k+2)/(k*l*(l+1))
    c2 = 1 - (spec.binom(2*m+1, m+1)*spec.binom(k+l-2*m, l-m))/spec.binom(k+l+2, l+1)

    return c1*c2

def barabasi_mean_degree(n, m, deg_0):
    """
    info: 
    input: 
    output: 
    """
    mean_deg = 0

    for deg in range(m, n): 
        p_deg = barabasi_p_degree(deg_0, deg, m)
        mean_deg += deg*p_deg

    return mean_deg

def barabasi_dist(n, m):
    """
    info: 
    input: 
    output: 
    """
    deg = np.zeros(n)

    for deg_0 in range(m, n):
        deg[deg_0] = barabasi_mean_degree(n, m, deg_0)

    return deg

def barabasi_plot():
    n = 20
    m = 1
    plt.plot(barabasi_dist(n, m))
    plt.show()

if __name__ == "__main__":
    barabasi_p__degree(1, 2, 1)
