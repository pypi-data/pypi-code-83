#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:20:15 2021

@author: nick
"""

from matplotlib import pyplot as plt
import os
import pandas as pd
import numpy as np

def debug_layers(alt, sig, wct, std, geom, snr_factor):
    
    
    ulim_y = np.round(np.max(sig)*1.1, decimals = -int(np.log10(1.1*np.max(sig)))+1)
    print(ulim_y)
    bases = geom.sel(features = 'base').values
    tops = geom.sel(features = 'top').values
    coms = geom.sel(features = 'center_of_mass').values
    # peaks = geom.sel(features = 'peak').values
    
    # Plots
    plt.figure
    plt.title('Product ID')
    plt.subplot(122)
    xlims = [0, ulim_y]
    ylims = [0, 10.]
    plt.title('Product ID')
    for i in range(geom.shape[0]):
        if geom.sel(features='residual_layer_flag').values[i] == 1:
            clrs = ['gray', 'black', 'grey']
        if geom.sel(features='residual_layer_flag').values[i] == 0:
            clrs = ['purple', 'cyan', 'purple']
        plt.plot(xlims, [bases[i], bases[i]], color = clrs[0])
        plt.plot(xlims, [tops[i], tops[i]], color =  clrs[1])
        plt.plot(xlims, [coms[i], coms[i]], '--', color = 'goldenrod')
        plt.axhspan(bases[i], tops[i], facecolor = clrs[2], alpha = 0.2)
    plt.plot(sig, alt)
    plt.axis(xlims + ylims)
    plt.xlabel('Aerosol Back. Coef. [$Mm^{-1} \cdot sr^{-1}$]')
    plt.ylabel('Altitude [m]')

    plt.subplot(121)
    xlims = [-0.05*ulim_y, 0.05*ulim_y]
    ylims = [0, 10.]
    for i in range(geom.shape[0]):
        if geom.sel(features='residual_layer_flag').values[i] == 1:
            clrs = ['gray', 'black', 'grey']
        if geom.sel(features='residual_layer_flag').values[i] == 0:
            clrs = ['purple', 'cyan', 'purple']
        plt.plot(xlims, [bases[i], bases[i]], color = clrs[0])
        plt.plot(xlims, [tops[i], tops[i]], color =  clrs[1])
        plt.plot(xlims, [coms[i], coms[i]], '--', color = 'goldenrod')
        plt.axhspan(bases[i], tops[i], facecolor = clrs[2], alpha = 0.2)
    plt.plot( wct, alt)
    plt.plot( snr_factor*std, alt, '--', color = 'darkgreen')
    plt.plot(-snr_factor*std, alt, '--', color = 'lightgreen')
    plt.axis(xlims + ylims)
    plt.xlabel('Wavelet Cov. Transform [$Mm^{-1} sr^{-1}$]')
    plt.ylabel('Altitude [m]')
    
    # ts = pd.to_datetime(str(date)) 
    # date_s = ts.strftime("%Y%m%d_%H%M%S")
    
    plt.tight_layout()
    # plt.savefig(os.path.join(dir_out,f'{date_s}_{i_d}.png'),
    #             dpi = dpi_val)
    # plt.close()
    plt.show()
    
    return()