# -*- coding: utf-8 -*-
import pyvista as pv
import numpy as np
from typing import Union, List
from pyvista import examples

x = np.linspace(-10, 15, 500)
y = np.linspace(-5, 20, 500)


def gauss(x: np.ndarray, y: np.ndarray, x0: float, y0: float, a: float, sigmax: float, sigmay: float) -> np.ndarray:
    r"""
    gaussian
    """
    return a * np.exp(-((x - x0) ** 2 / sigmax + (y - y0) ** 2) / sigmay ** 2)


def gauss2(x: np.ndarray, y: np.ndarray, x0: float, y0: float, a: float, sigmax: float, sigmay: float) -> np.ndarray:
    r"""
    gaussian
    """
    return a * np.exp(-((x - x0) ** 2 / sigmax + (y - y0) ** 2 / sigmay ** 2))


def f(x: Union[float, np.ndarray], y: Union[float, np.ndarray]) -> np.ndarray:
    r"""
    Inner function
    """
    return 1.5 * np.sin(0.5 * np.sqrt(0.4 * (x ** 2 + y ** 2))) \
           + gauss(x, y, x0=-15, y0=-5, a=7.5, sigmax=5, sigmay=5) \
           + gauss(x, y, x0=-15, y0=5, a=5, sigmax=5, sigmay=5) \
           + gauss(x, y, x0=15, y0=-5, a=7.5, sigmax=5, sigmay=5) \
           + gauss(x, y, x0=7, y0=5, a=3.5, sigmax=3, sigmay=2.5) \
           + gauss(x, y, x0=0, y0=5, a=3, sigmax=10, sigmay=5) \
           + gauss(x, y, x0=0, y0=-5, a=3, sigmax=10, sigmay=5) \
           + gauss(x, y, x0=15, y0=-7.5, a=4, sigmax=4, sigmay=4) \
           + gauss(x, y, x0=-15, y0=0, a=4, sigmax=4, sigmay=4) \
           + gauss(x, y, x0=-15, y0=8, a=4, sigmax=7, sigmay=4) \
           + gauss(x, y, x0=15, y0=10, a=4, sigmax=4, sigmay=4) \
           + gauss(x, y, x0=-5, y0=20, a=6, sigmax=10, sigmay=5) \
           + gauss(x, y, x0=-10, y0=15, a=6, sigmax=5, sigmay=5) \
           + gauss2(x, y, x0=15, y0=10, a=4, sigmax=3, sigmay=10) \
           + gauss2(x, y, x0=-5, y0=12, a=3, sigmax=4, sigmay=4)


def build_path_section(start: np.ndarray, end: np.ndarray, num: int = 10) -> List[np.ndarray]:
    r"""
    gets the xy position of a start and endpoint and distributes num equally space points between them.
    """
    vec = end - start
    l = np.linalg.norm(vec) / float(num)
    points = []
    for i in range(num + 1):
        p2d = start.copy() + l * i * (vec / np.linalg.norm(vec))
        z = f(p2d[0], p2d[1])
        points.append([p2d[0], p2d[1], z + 0.05])

    return points


def build_path(points: np.ndarray) -> np.ndarray:
    r"""
    calculates a linear segments between points given here
    """
    path = []
    for (idx, point) in enumerate(points[:-1]):
        path.extend(build_path_section(start=point, end=points[idx + 1]))
    return np.array(path)


def circle_around_point(point: np.ndarray, radius: float, num: int) -> np.ndarray:
    r"""
    Calculates num points on a circle around an initial state
    """
    phi = np.linspace(0, 2 * np.pi, num)
    X = point[0] + radius * np.sin(phi)
    Y = point[1] + radius * np.cos(phi)
    points = []
    for (idx, x) in enumerate(X):
        points.append([x, Y[idx], f(x, Y[idx])])
    return np.array(points)


def project_to_surface(point: np.ndarray, zoffset: float = 0) -> np.ndarray:
    r"""
    Projects point onto energy surface
    """
    return np.array([point[0], point[1], f(point[0], point[1]) + zoffset])


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
# sargs = dict(interactive=True)  # Simply make the bar interactive
p = pv.Plotter()
pv.set_plot_theme("ParaView")
p.set_background('white')
p.add_mesh(surf, scalars='scalars', show_scalar_bar=False)
p.add_mesh(cont, color='white', show_scalar_bar=False)
# ==========================================================================
l_mins = np.array([[0, 0],
                   [12.5, 2],
                   [7.5, 12.5],
                   [-8, 11]])
# build circles =============================================================
l_rad = 1.5
for minimum in l_mins:
    circle = circle_around_point(point=minimum, radius=l_rad, num=100)
    circlespline = pv.Spline(circle, 1000)
    circlespline["scalars"] = np.arange(circlespline.n_points)
    circletube = circlespline.tube(radius=0.025)
    p.add_mesh(circletube, smooth_shading=True, color='gray')
# ===========================================================================


# build paths ==============================================================
# first path ***************************************************************
l_end1 = l_mins[1]
# first calculate intersection with circle.
l_vec1 = l_end1 - l_mins[0]
l_start1 = l_mins[0] + l_rad * l_vec1 / np.linalg.norm(l_vec1)
path1 = build_path(np.vstack((l_start1, l_end1)))
spline1 = pv.Spline(path1, 1000)
spline1["scalars"] = np.arange(spline1.n_points)
tube1 = spline1.tube(radius=0.05)
# second path **************************************************************
l_end2 = np.array([-2, -2])
# first calculate intersection with circle.
l_vec2 = l_end2 - l_mins[0]
l_start2 = l_mins[0] + l_rad * l_vec2 / np.linalg.norm(l_vec2)
points_p2 = np.array([[-3, 0],
                      [-4, 0.8],
                      [-5, 1.3],
                      [-6, 1.7],
                      [-10, 1.9]])
path2 = build_path(points=np.vstack((l_start2, points_p2)))
spline2 = pv.Spline(path2, 1000)
spline2["scalars"] = np.arange(spline2.n_points)
tube2 = spline2.tube(radius=0.05)
# third path **************************************************************
l_end3 = np.array([-2, 2])
# first calculate intersection with circle.
l_vec3 = l_end3 - l_mins[0]
l_start3 = l_mins[0] + l_rad * l_vec3 / np.linalg.norm(l_vec3)
points_p3 = np.array([[-4, 1.7],
                      [-10, 1.9]])

path3 = build_path(points=np.vstack((l_start3, points_p3)))
spline3 = pv.Spline(path3, 1000)
spline3["scalars"] = np.arange(spline3.n_points)
tube3 = spline3.tube(radius=0.05)
# foruth path **************************************************************
l_end4 = np.array([0, -5])
# first calculate intersection with circle.
l_vec4 = l_end4 - l_mins[0]
l_start4 = l_mins[0] + l_rad * l_vec4 / np.linalg.norm(l_vec4)
points_p4 = np.array([0, -5])

path4 = build_path(points=np.vstack((l_start4, points_p4)))
spline4 = pv.Spline(path4, 1000)
spline4["scalars"] = np.arange(spline4.n_points)
tube4 = spline4.tube(radius=0.05)
# fifth path **************************************************************
l_end5 = np.array([0, 8.5])
# first calculate intersection with circle.
l_vec5 = l_end5 - l_mins[0]
l_start5 = l_mins[0] + l_rad * l_vec5 / np.linalg.norm(l_vec5)
points_p5 = np.array([[0, 7.5],
                      [1, 8.5],
                      [l_mins[2][0], l_mins[2][1]]])
path5 = build_path(points=np.vstack((l_start5, points_p5)))
spline5 = pv.Spline(path5, 1000)
spline5["scalars"] = np.arange(spline5.n_points)
tube5 = spline5.tube(radius=0.05)
# sixth path **************************************************************
l_end6 = l_mins[2]
# first calculate intersection with circle.
l_vec6 = l_end6 - l_mins[1]
l_start6 = l_mins[1] + l_rad * l_vec6 / np.linalg.norm(l_vec6)
points_p6 = np.array([[12.25, 4],
                      [12.5, 5],
                      [12, 7],
                      [l_mins[2][0], l_mins[2][1]]])

path6 = build_path(points=np.vstack((l_start6, points_p6)))
spline6 = pv.Spline(path6, 1000)
spline6["scalars"] = np.arange(spline6.n_points)
tube6 = spline6.tube(radius=0.05)
# seventh path **************************************************************
l_end7 = l_mins[3]
# first calculate intersection with circle.
l_vec7 = l_end7 - l_mins[2]
l_start7 = l_mins[2] + l_rad * l_vec7 / np.linalg.norm(l_vec7)
points_p7 = np.array([[l_mins[3][0], l_mins[3][1]]])

path7 = build_path(points=np.vstack((l_start7, points_p7)))
spline7 = pv.Spline(path7, 1000)
spline7["scalars"] = np.arange(spline7.n_points)
tube7 = spline7.tube(radius=0.05)

# identify saddlepoints
sp7 = spline7.points[spline7.points[:, 2] == np.max(spline7.points[:, 2])]
sp6 = spline6.points[spline6.points[:, 2] == np.max(spline6.points[:, 2])]
sp5 = spline5.points[spline5.points[:, 2] == np.max(spline5.points[:, 2])]
sp4 = spline4.points[spline4.points[:, 2] == np.max(spline4.points[:, 2])]
sp3 = spline3.points[spline3.points[:, 2] == np.max(spline3.points[:, 2])]
sp2 = spline2.points[spline2.points[:, 2] == np.max(spline2.points[:, 2])]
sp1 = spline1.points[spline1.points[:, 2] == np.max(spline1.points[:, 2])]

# build minima points

l_minima = pv.PolyData(np.vstack((project_to_surface(l_mins[0], zoffset=0.15),
                                  project_to_surface(l_mins[1], zoffset=0.15),
                                  project_to_surface(l_mins[2], zoffset=0.15),
                                  project_to_surface(l_mins[3], zoffset=0.15))))
l_circlestartpoints = pv.PolyData(np.vstack((project_to_surface(l_start1), project_to_surface(l_start2),
                                             project_to_surface(l_start3), project_to_surface(l_start4),
                                             project_to_surface(l_start5), project_to_surface(l_start6),
                                             project_to_surface(l_start7))))
l_saddlepoints = pv.PolyData(np.vstack((sp1, sp2, sp3, sp4, sp5, sp6, sp7)))

p.add_mesh(tube1, smooth_shading=True, color='gray')
p.add_mesh(tube2, smooth_shading=True, color='gray')
p.add_mesh(tube3, smooth_shading=True, color='gray')
p.add_mesh(tube4, smooth_shading=True, color='gray')
p.add_mesh(tube5, smooth_shading=True, color='gray')
p.add_mesh(tube6, smooth_shading=True, color='gray')
p.add_mesh(tube7, smooth_shading=True, color='gray')

p.add_mesh(l_minima, color='maroon', point_size=15., render_points_as_spheres=True, label='local minima')
p.add_mesh(l_circlestartpoints, color='gray', point_size=10, render_points_as_spheres='displace minimum')
p.add_mesh(l_saddlepoints, color='g', point_size=15, render_points_as_spheres=True, label='saddle points')


# ========================VISUALIZE SPIN TEXTURES=======================================================================
def theta(r: np.ndarray, c: float, w: float) -> np.ndarray:
    comp1 = np.arcsin(np.tanh((-r - c) * 2 / w))
    comp2 = np.arcsin(np.tanh((-r + c) * 2 / w))
    return np.pi + comp1 + comp2


def phi(p: np.ndarray, vorticity: float, helicity: float) -> np.ndarray:
    return vorticity * p + helicity


def rotationmatrix_z(theta: float) -> np.ndarray:
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta), np.cos(theta), 0],
                     [0, 0, 1]])

def buildfm():
    a1 = np.array([0.5, np.sqrt(3) / 2, 0]) * 0.5
    a2 = np.array([0.5, -np.sqrt(3) / 2, 0]) * 0.5
    latt = np.array([j * a1 + i * a2 for i in range(15) for j in range(15)])
    return latt, np.array([[0.0, 0.0, 1.0] for i in range(len(latt))]), np.array([m for m in range(len(latt))])

def build_bimeron(R):
    def theta_bim(R, c_i, c_j, a1, a2):
        rho = np.sqrt(a1 * c_i ** 2 + a2 * c_j ** 2)
        return np.arccos(R * c_i / (rho ** 2 + (R ** 2) / 4))

    def phi_bim(R, c_i, c_j):
        return np.arctan((c_i - R / 2) / (c_j)) - np.arctan((c_i + R / 2) / (c_j))
    r = 1
    a1 = np.array([0.5, np.sqrt(3) / 2, 0]) * 0.5
    a2 = np.array([0.5, -np.sqrt(3) / 2, 0]) * 0.5
    lattpoints = np.array([j * a1 + i * a2 for i in range(15) for j in range(15)])
    mid_point = np.round(np.mean(lattpoints, axis=0), 8)
    X = lattpoints[:, 0] - mid_point[0]
    Y = lattpoints[:, 1] - mid_point[1]
    th, ph = [], []
    for n in range(len(X)):
        th.append(theta_bim(R,X[n],Y[n],1,4))
        ph.append(phi_bim(R, X[n], Y[n]))
    th = np.array(th)
    ph = np.array(ph)
    MX = np.round(r* np.sin(th) * np.cos(ph),8)
    MY = np.round(r* np.sin(th) * np.sin(ph),8)
    MZ = np.round(r* np.cos(th),8)
    mag = np.vstack((MX, MY, MZ)).T * 0.5
    return lattpoints, mag, MZ


def buildskyrmion(vorticity: int= 1.0, helicity: float = np.pi / 2, c: float=2.5, w: float=3.0, AFM: bool = False):
    r"""
    """
    a1 = np.array([0.5, np.sqrt(3) / 2, 0]) * 0.5
    a2 = np.array([0.5, -np.sqrt(3) / 2, 0]) * 0.5
    lattpoints = np.array([j * a1 + i * a2 for i in range(15) for j in range(15)])
    mid_point = np.round(np.mean(lattpoints, axis=0), 8)
    X = lattpoints[:, 0] - mid_point[0]
    Y = lattpoints[:, 1] - mid_point[1]
    r = np.sqrt(X ** 2 + Y ** 2)
    pp = np.arctan2(Y, X)
    th = theta(r, c, w)
    ph = phi(pp, vorticity, helicity)
    n = np.arange(0,len(X),1)
    if AFM:
        sign = (-1) ** (n % 2 + n // int(np.sqrt(len(X))))
    else:
        sign = 1
    uplo = 1
    MX = np.sin(th) * np.cos(ph) * sign
    MY = np.sin(th) * np.sin(ph) * sign
    MZ = np.cos(th) * float(uplo) * sign
    mag = np.vstack((MX, MY, MZ)).T * 0.5
    return lattpoints, mag, MZ


lattpoints, mag, th = buildskyrmion()

lattpoints_2, mag_2, th_2 = buildskyrmion(AFM=True)

lattpoints_fm, mag_fm, th_fm = buildfm()

lattpoints_bim, mag_bim, th_bim = build_bimeron(R=2.5)

# rotation of lattice points
for (idx, l) in enumerate(lattpoints):
    lattpoints[idx] = rotationmatrix_z(-45).dot(l)
# displace lattice points
skyrpos = np.array([-7, 0, 10])
lattpoints += skyrpos
p.add_text('Skyrmion',position=(-7.0,0.0,10.0))

# rotation of lattice points
for (idx, l) in enumerate(lattpoints_2):
    lattpoints_2[idx] = rotationmatrix_z(-45).dot(l)
# displace lattice points
lattpoints_2 += np.array([-12,11, 10])

# rotation of lattice points
for (idx, l) in enumerate(lattpoints_fm):
    lattpoints_fm[idx] = rotationmatrix_z(-45).dot(l)
# displace lattice points
lattpoints_fm += np.array([12.5,20, 10])

# rotation of lattice points
for (idx, l) in enumerate(lattpoints_bim):
    lattpoints_bim[idx] = rotationmatrix_z(-45).dot(l)
# displace lattice points
lattpoints_bim += np.array([12.5,5, 10])




skyr = pv.PolyData(lattpoints)
skyr['oop'] = th
skyr.vectors = mag
geom = pv.Arrow(start=np.array([-.45, 0, 0]), tip_length=1, scale=0.9, tip_radius=0.2)
glyphs = skyr.glyph(orient=True, scale=False, geom=geom)
p.add_mesh(glyphs, scalars='oop', show_scalar_bar=False)
spline_skyr = pv.Spline(np.vstack((project_to_surface(l_mins[0]), np.mean(lattpoints, axis=0))), 1000)
spline_skyr["scalars"] = np.arange(spline_skyr.n_points)
p.add_mesh(spline_skyr.tube(radius=0.025), smooth_shading=True, color='maroon')


skyr_2 = pv.PolyData(lattpoints_2)
skyr_2['oop_2'] = th_2
skyr_2.vectors = mag_2
glyphs_2 = skyr_2.glyph(orient=True, scale=False, geom=geom)
p.add_mesh(glyphs_2, scalars='oop_2', show_scalar_bar=False)
spline_antiskyr = pv.Spline(np.vstack((project_to_surface(l_mins[3]), np.mean(lattpoints_2, axis=0))), 1000)
spline_antiskyr["scalars"] = np.arange(spline_antiskyr.n_points)
p.add_mesh(spline_antiskyr.tube(radius=0.025), smooth_shading=True, color='maroon')


fm = pv.PolyData(lattpoints_fm)
fm['oop_fm'] = th_fm
fm.vectors = mag_fm
glyphs_fm = fm.glyph(orient=True, scale=False, geom=geom)
p.add_mesh(glyphs_fm, color='r', show_scalar_bar=False)
spline_fm = pv.Spline(np.vstack((project_to_surface(l_mins[2]), np.mean(lattpoints_fm, axis=0))), 1000)
spline_fm["scalars"] = np.arange(spline_fm.n_points)
p.add_mesh(spline_fm.tube(radius=0.025), smooth_shading=True, color='maroon')


bim = pv.PolyData(lattpoints_bim)
bim['oop_bim'] = th_bim
bim.vectors = mag_bim
glyphs_bim = bim.glyph(orient=True, scale=False, geom=geom)
p.add_mesh(glyphs_bim, scalars='oop_bim', show_scalar_bar=False)
spline_bim = pv.Spline(np.vstack((project_to_surface(l_mins[1]), np.mean(lattpoints_bim, axis=0))), 1000)
spline_bim["scalars"] = np.arange(spline_bim.n_points)
p.add_mesh(spline_bim.tube(radius=0.025), smooth_shading=True, color='maroon')


def screenshot():
    # print("Window size ", p.window_size)
    p.screenshot("try.png", transparent_background=True,
                 window_size=[4000, 4000])  # , window_size=[2560,int(2560*p.window_size[1]/p.window_size[0])])
    print("Camera position ", p.camera_position)


p.camera_position = [(3.0008694344962867, 41.022889929466665, 50.36022309079117),
 (4.13612578884189, 6.649370212888337, 2.866769974807978),
 (0.08834195946796153, -0.8059188652304697, 0.5853977116994847)]
#p.view_xy()
#p.show_grid()
p.add_key_event("s", screenshot)
p.show()
