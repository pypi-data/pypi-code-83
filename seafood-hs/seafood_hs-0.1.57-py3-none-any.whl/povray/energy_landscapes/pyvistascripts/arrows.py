import pyvista as pv
import numpy as np

p = pv.Plotter()
ar1 = pv.Arrow(np.array([0,0,0]),direction=np.array([1,0,0]))
ar2 = pv.Arrow(np.array([0,0,0]),direction=np.array([0,1,0]))
ar3 = pv.Arrow(np.array([0,0,0]),direction=np.array([0,0,1]))
p.add_mesh(ar1)
p.add_mesh(ar2)
p.add_mesh(ar3)
p.show_grid()
p.show()