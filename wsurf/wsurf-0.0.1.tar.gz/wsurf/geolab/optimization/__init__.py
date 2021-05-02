
try:
    from wsurf.geolab.optimization.sparse_mkl.scipy_aliases import spsolve
except:
    from scipy.sparse.linalg import spsolve
    print('Efficiency Warning: mkl spsolve not available')

try:
    from wsurf.geolab.optimization.sparse_mkl.sparse_dot import dot_product_mkl as spdot
    from wsurf.geolab.optimization.routines import hdot_mkl as hdot

except:
    from wsurf.geolab.optimization.routines import spdot
    from wsurf.geolab.optimization.routines import hdot
    print('Efficiency Warning: mkl dot not available')

from wsurf.geolab.optimization.guidedprojectionbase import GuidedProjectionBase


