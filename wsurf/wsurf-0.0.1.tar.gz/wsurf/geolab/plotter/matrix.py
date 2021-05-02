import numpy as np

from scipy.sparse import find

from geolab.plotter.glyphs import MeshGlyph

from geolab.geometry import mesh_plane

from geolab.plotter import Faces

from geolab.plotter import Edges

from geolab.plotter import view

# -----------------------------------------------------------------------------


def plot_matrix(matrix):
    F1 = matrix.shape[0]
    F2 = matrix.shape[1]
    x = np.linspace(0, 1000, F1+1)
    y = np.linspace(0, 1000*F2/F1, F2+1)
    i, j, d = find(matrix)
    N = len(i)
    F = np.reshape(np.arange(4*N), (N, 4), 'C')
    Vx = np.column_stack((x[i], x[i+1], x[i+1], x[i]))
    Vy = np.column_stack((y[j], y[j], y[j+1], y[j+1]))
    V = np.column_stack((Vy.flatten('C'), -Vx.flatten('C'), np.zeros(4*N)))
    M = MeshGlyph(V, quads=F)
    source = [Faces(M, face_data=np.abs(d), color='plasma', lut_range='0:+')]
    B = mesh_plane(1, 1, (0, 1000*F2/F1), (-1000, 0))
    source.append(Edges(B, color=(200, 200, 200)))
    view(source, background=(1, 1, 1))
    return source

