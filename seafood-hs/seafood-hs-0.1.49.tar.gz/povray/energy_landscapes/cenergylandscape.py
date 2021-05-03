# -*- coding: utf-8 -*-
r"""
Module contains energy landscape scene
"""
from typing import Union, List, Tuple, Dict
from pathlib import Path
from povray.predefined_povrayobjects.ccamera import CCameraForSpinLattice
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.spatial import Delaunay
import pyvista as pv



class CEnergyLandscape:
    r"""

    """

    def __init__(self, location: Union[None, List[float]] = None,
                 lookat: Union[None, List[float]] = None, viewangle: float = 90,
                 viewdistance: Union[float, None] = None) -> None:
        r"""
        Initializes the visualization

        Args:
            location(List[float]): location of the observer. Default value is None. In that case the location will be
            automatically set from extent of landscape.

            lookat(List[float]): location of the observed point. Default value is None. In that case the location will
            be automatically set from extent of landscape

            viewangle(float): Angle for vector from location to lookat. Default angle is 90 degree, which corresponds
            to a view from the top. Will be used only if location and lookat are None

            viewdistance(float): Distance from the camera to the observed point. Default distance is None. Will be used
            only if location and lookat are None and if it is different from None. In case that location and lookat are
            not defined, a viewangle is selected and this parameter is None the distance will be calculated automatic
            from the landscape
        """
        # r are the 3d points (x,y,z) for which the function z(x,y) is evaluated.
        self._r = self._loadfunction(xlim=(-10,10), ylim=(-10, 10))
        #self._camera = CCameraForSpinLattice(self._r, location, lookat, viewangle, viewdistance).cam

    def _loadfunction(self, xlim: Tuple[float,float], ylim: Tuple[float, float], resolution: int= 50) -> np.ndarray:
        r"""

        """
        def f(x: np.ndarray, y: np.ndarray) -> np.ndarray:
            r"""
            Inner function
            """
            return np.sin(np.sqrt(x ** 2 + y ** 2))

        x = np.linspace(xlim[0], xlim[1], resolution)
        y = np.linspace(ylim[0], ylim[1], resolution)

        X, Y = np.meshgrid(x, y)
        Z = f(X, Y)

        r = np.dstack([X,Y,Z])
        rr = np.reshape(r, (r.shape[0] * r.shape[1], r.shape[2]))

        cloud = pv.PolyData(rr)
        surf = cloud.delaunay_2d()
        #surf.plot(show_edges=True)
        #cloud.plot(point_size=15)


        contours = cloud.contour()

        p = pv.Plotter()
        p.add_mesh(cloud, opacity=0.85)
        p.add_mesh(contours, color="white", line_width=5)
        p.show()


        """tri = Delaunay(rr)
        print(tri.simplices)
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        rT = rr.T
        ax.scatter(rT[0], rT[1], rT[2])
        for simplex in tri.simplices:
            vertex1 = rr[simplex[0]]
            vertex2 = rr[simplex[1]]
            vertex3 = rr[simplex[2]]
            ax.plot([vertex1[0],vertex2[0]],[vertex1[1],vertex2[1]],[vertex1[2],vertex2[2]],'k-')
            #ax.plot([vertex1[0],vertex3[0]],[vertex1[1],vertex3[1]],[vertex1[2],vertex3[2]],'k-')
            #ax.plot([vertex2[0],vertex3[0]],[vertex2[1],vertex3[1]],[vertex2[2],vertex3[2]],'k-')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_zlim((0,1))
        plt.show()"""

        return Z

CEnergyLandscape()