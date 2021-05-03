# -*- coding: utf-8 -*-
import pyvista as pv
import numpy as np
from typing import Union, List
from pyvista import examples

x = np.linspace(-10, 10, 500)
y = np.linspace(-5, 8.5, 500)

def gauss(x: np.ndarray, y: np.ndarray, x0: float, y0: float,a:float, sigmax: float, sigmay: float) -> np.ndarray:
    r"""
    gaussian
    """
    return a*np.exp(-((x-x0)**2/ sigmax +(y-y0)**2)/ sigmay**2)

def f(x: Union[float,np.ndarray], y: Union[float,np.ndarray]) -> np.ndarray:
    r"""
    Inner function
    """
    return 1.5*np.sin(0.5 * np.sqrt(0.4*(x ** 2 + y ** 2)))\
           + gauss(x,y,x0=-15,y0=-5,a=7.5,sigmax=5,sigmay=5)\
           + gauss(x,y,x0=-15,y0=5,a=5,sigmax=5,sigmay=5)\
           + gauss(x,y,x0=15,y0=-5,a=7.5,sigmax=5,sigmay=5)\
           + gauss(x,y,x0=7,y0=5,a=3.5,sigmax=3,sigmay=2.5)\
           + gauss(x,y,x0=0,y0=5,a=3,sigmax=10,sigmay=5)\
           + gauss(x,y,x0=0,y0=-5,a=3,sigmax=10,sigmay=5) \
           + gauss(x, y, x0=15, y0=-7.5, a=4, sigmax=4, sigmay=4)\
           + gauss(x, y, x0=-15, y0=0, a=4, sigmax=4, sigmay=4)\
           + gauss(x, y, x0=-15, y0=8, a=4, sigmax=7, sigmay=4)\
           + gauss(x, y, x0=15, y0=10, a=4, sigmax=4, sigmay=4)\
           + gauss(x, y, x0=0, y0=11, a=4, sigmax=15, sigmay=2)

def build_path_section(start: np.ndarray, end: np.ndarray, num:int=10)-> List[np.ndarray]:
    r"""
    gets the xy position of a start and endpoint and distributes num equally space points between them.
    """
    vec = end - start
    l = np.linalg.norm(vec) / float(num)
    points = []
    for i in range(num+1):
        p2d = start.copy() + l * i * (vec / np.linalg.norm(vec))
        z = f(p2d[0], p2d[1])
        points.append([p2d[0], p2d[1], z + 0.05])

    return points

def build_path(points: np.ndarray) -> np.ndarray:
    r"""
    calculates a linear segments between points given here
    """
    path = []
    for (idx,point) in enumerate(points[:-1]):
        path.extend(build_path_section(start=point, end=points[idx+1]))
    return np.array(path)


def circle_around_point(point: np.ndarray, radius: float, num: int) -> np.ndarray:
    r"""
    Calculates num points on a circle around an initial state
    """
    phi = np.linspace(0,2*np.pi,num)
    X = point[0] + radius * np.sin(phi)
    Y = point[1] + radius * np.cos(phi)
    points=[]
    for (idx,x) in enumerate(X):
        points.append([x,Y[idx],f(x,Y[idx])])
    return np.array(points)

def project_to_surface(point:np.ndarray, zoffset: float = 0) -> np.ndarray:
    r"""
    Projects point onto energy surface
    """
    return np.array([point[0],point[1],f(point[0],point[1])+zoffset])

# setup landscape ===========================================================
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
r = np.dstack([X, Y, Z])
rr = np.reshape(r, (r.shape[0] * r.shape[1], r.shape[2]))
cloud = pv.PolyData(rr)
surf = cloud.delaunay_2d()
surf.point_arrays['scalars'] = surf.points[:, 2]
cont = surf.contour()
# create dictionary of parameters to control scalar bar
#sargs = dict(interactive=True)  # Simply make the bar interactive
p = pv.Plotter()
pv.set_plot_theme("ParaView")
p.set_background('white')
p.add_mesh(surf,scalars='scalars',show_scalar_bar=False)
p.add_mesh(cont,color='white',show_scalar_bar=False)
# ==========================================================================

# build circle =============================================================
l_rad = 1.5
l_min = np.array([0,0])
circle = circle_around_point(point=l_min, radius=l_rad, num=100)
circlespline = pv.Spline(circle, 1000)
circlespline["scalars"] = np.arange(circlespline.n_points)
circletube=circlespline.tube(radius=0.025)
#===========================================================================

# build paths ==============================================================
# first path ***************************************************************
l_end1 = np.array([10,2])
# first calculate intersection with circle.
l_vec1 = l_end1 - l_min
l_start1 = l_min + l_rad * l_vec1 / np.linalg.norm(l_vec1)
path1 = build_path(np.vstack((l_start1,l_end1)))
spline1 = pv.Spline(path1, 1000)
spline1["scalars"] = np.arange(spline1.n_points)
tube1 = spline1.tube(radius=0.05)
# second path **************************************************************
l_end2 = np.array([-2,-2])
# first calculate intersection with circle.
l_vec2 = l_end2 - l_min
l_start2 = l_min + l_rad * l_vec2 / np.linalg.norm(l_vec2)
points_p2 = np.array([[-3,0],
                      [-4,0.8],
                      [-5,1.3],
                      [-6,1.7],
                      [-10,1.9]])
path2 = build_path(points=np.vstack((l_start2,points_p2)))
spline2 = pv.Spline(path2, 1000)
spline2["scalars"] = np.arange(spline2.n_points)
tube2 = spline2.tube(radius=0.05)
# third path **************************************************************
l_end3 = np.array([-2,2])
# first calculate intersection with circle.
l_vec3 = l_end3 - l_min
l_start3 = l_min + l_rad * l_vec3 / np.linalg.norm(l_vec3)
points_p3 = np.array([[-6,1.7],
                      [-10,1.9]])

path3 = build_path(points=np.vstack((l_start3,points_p3)))
spline3 = pv.Spline(path3, 1000)
spline3["scalars"] = np.arange(spline3.n_points)
tube3 = spline3.tube(radius=0.05)
# foruth path **************************************************************
l_end4 = np.array([0,-5])
# first calculate intersection with circle.
l_vec4 = l_end4 - l_min
l_start4 = l_min + l_rad * l_vec4 / np.linalg.norm(l_vec4)
points_p4 = np.array([0,-5])

path4 = build_path(points=np.vstack((l_start4,points_p4)))
spline4 = pv.Spline(path4, 1000)
spline4["scalars"] = np.arange(spline4.n_points)
tube4 = spline4.tube(radius=0.05)
# fifth path **************************************************************
l_end5 = np.array([0,8.5])
# first calculate intersection with circle.
l_vec5 = l_end5 - l_min
l_start5 = l_min + l_rad * l_vec5 / np.linalg.norm(l_vec5)
points_p5 = np.array([0,8.5])

path5 = build_path(points=np.vstack((l_start5,points_p5)))
spline5 = pv.Spline(path5, 1000)
spline5["scalars"] = np.arange(spline5.n_points)
tube5 = spline5.tube(radius=0.05)

# identify saddlepoints
sp5 = spline5.points[spline5.points[:, 2] == np.max(spline5.points[:, 2])]
sp4 = spline4.points[spline4.points[:, 2] == np.max(spline4.points[:, 2])]
sp3 = spline3.points[spline3.points[:, 2] == np.max(spline3.points[:, 2])]
sp2 = spline2.points[spline2.points[:, 2] == np.max(spline2.points[:, 2])]
sp1 = spline1.points[spline1.points[:, 2] == np.max(spline1.points[:, 2])]




# build minima points
l_minima = pv.PolyData(np.vstack((project_to_surface(l_min,zoffset=0.15), project_to_surface(l_end1,zoffset=0.15))))
l_circlestartpoints = pv.PolyData(np.vstack((project_to_surface(l_start1),project_to_surface(l_start2),project_to_surface(l_start3),project_to_surface(l_start4),project_to_surface(l_start5))))
l_saddlepoints = pv.PolyData(np.vstack((sp1,sp2,sp3,sp4,sp5)))


p.add_mesh(tube1,smooth_shading=True, color='gray')
p.add_mesh(tube2,smooth_shading=True, color='gray')
p.add_mesh(tube3,smooth_shading=True, color='gray')
p.add_mesh(tube4,smooth_shading=True, color='gray')
p.add_mesh(tube5,smooth_shading=True, color='gray')
p.add_mesh(circletube,smooth_shading=True, color='gray')


#p.show_grid()
p.add_mesh(l_minima, color='maroon', point_size=15., render_points_as_spheres=True, label='local minima')
p.add_mesh(l_circlestartpoints, color='gray', point_size=10, render_points_as_spheres='displace minimum')
p.add_mesh(l_saddlepoints, color='g', point_size=15, render_points_as_spheres=True, label='saddle points')



def screenshot():
    #print("Window size ", p.window_size)
    p.screenshot("try.png", transparent_background=True, window_size=[2000,1500])#, window_size=[2560,int(2560*p.window_size[1]/p.window_size[0])])
    print("Camera position ", p.camera_position)
p.add_key_event("s", screenshot)
p.show()
