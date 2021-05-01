# -*- coding: utf-8 -*-
import pyvista as pv
import numpy as np
from pyvista import examples

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)


def f(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    r"""
    Inner function
    """
    return np.sin(np.sqrt(x ** 2 + y ** 2))
m = examples.load_random_hills()
print(m)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
zeropoint=np.array([[0.0,0.0,0.0]])
r = np.dstack([X, Y, Z])
rr = np.reshape(r, (r.shape[0] * r.shape[1], r.shape[2]))

cloud = pv.PolyData(rr)
zero = pv.PolyData(zeropoint)
surf = cloud.delaunay_2d()
surf.point_arrays['scalars']=surf.points[:,2]
cont = surf.contour()
print(surf.n_arrays)
#print(type(surf_scalar))
#surf.contour(scalars=surf_scalar)
# x = np.arange(-10, 10, 0.25)
# y = np.arange(-10, 10, 0.25)
# x, y = np.meshgrid(x, y)
# r = np.sqrt(x ** 2 + y ** 2)
# z = np.sin(r)
#grid = pv.StructuredGrid(x, y, z)
#c = grid.contour()
p = pv.Plotter()
p.add_mesh(surf)
p.add_mesh(cont)
p.add_mesh(zero, color='maroon', point_size=20.,
                 render_points_as_spheres=True)
p.show()

"""
mesh = examples.load_random_hills()
p = pv.Plotter()
p.add_mesh(mesh)
p.add_mesh(mesh.contour(), color='white',line_width=5)
p.show()"""
