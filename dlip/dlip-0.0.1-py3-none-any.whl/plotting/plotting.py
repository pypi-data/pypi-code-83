import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import griddata

def colormap(data=None, x=None, y=None, z=None, resolution=300, aspect_ratio=1,
             cmap='jet', ax=None, show_points=True, colorbar=True, xlabel=None,
             ylabel=None, zlabel=None, title=None, vmin=None, vmax=None):
    
    if data is None:
        raise ValueError('No data specified')
    if x is None:
        raise ValueError('No x value specified')
    if y is None:
        raise ValueError('No y value specified')
    if z is None:
        raise ValueError('No z value specified')
    
    points = data[[x, y]].values
    values = data[z].values
    xmin = points[:,0].min()
    xmax = points[:,0].max()
    ymin = points[:,1].min()
    ymax = points[:,1].max()
    dx = (xmax - xmin) / (resolution - 1)
    dy = (ymax - ymin) / (resolution - 1)
    grid_x, grid_y = np.mgrid[xmin:xmax:resolution * 1j, 
                              ymin:ymax:resolution * 1j]
    z_interp = griddata(points, values, (grid_x, grid_y), method='cubic').T
    extent = (xmin - dx/2, xmax + dx/2, ymin - dy/2, ymax + dy/2)
    aspect_correction = (xmax - xmin) / (ymax - ymin)
    aspect = aspect_correction * aspect_ratio
    
    if ax:
        fig = ax.get_figure()
    else:
        fig, ax = plt.subplots()
    im = ax.imshow(z_interp, origin='lower', extent=extent, aspect=aspect, 
                   cmap=cmap, vmin=vmin, vmax=vmax)
    ax.set_xticks(data[x].unique())
    ax.set_yticks(data[y].unique())
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    
    if show_points:
        ax.scatter(points[:,0], points[:,1], marker='o', s=50, edgecolor='k', 
                   facecolor='w')
    if colorbar:
        cax = fig.add_axes([ax.get_position().x1 + 0.01,ax.get_position().y0, 
                            0.02,ax.get_position().height])
        plt.colorbar(im, cax=cax, label=zlabel) 
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
        
    return ax