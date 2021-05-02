# -*- coding: utf-8 -*-


# !/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import absolute_import

from __future__ import print_function

from __future__ import division

import numpy as np

from scipy import sparse

# -----------------------------------------------------------------------------

from .geolab.geometry.polyline import Polyline

from .geolab import optimization

from .geolab import plotter

from .geolab import fitting

from .geolab import utilities

# -----------------------------------------------------------------------------

__author__ = 'Davide Pellis'

'''
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
                        WEINGARTEN B-SPLINE OPTIMIZATION
-------------------------------------------------------------------------------
                                     2020
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
                                    Notes
-------------------------------------------------------------------------------
 indexing:
 C = control points
 S = sample points
-------------------------------------------------------------------------------
 unknows vector X:
 3C | 3S | 4S | 3S | 2S + 2S

                | N1              | N2                  | N3
 [x_C, y_C, z_C, Nx_S, Ny_S, Nz_S, E_S, F_S, G_S, det_S, L_S, M_S, N_S,

 | N4      | N5                                                   | N6
  K_S, H_S, Ku^2_S, KuKv_S, Kv^2_S, Hu^2_S, HuHv_S, Hv^2_S, DK, DH, a, b, c]
-------------------------------------------------------------------------------
 K = (LN - M^2) / (EG - F^2)
 H = (LG - 2MF + NE) / 2(EG - F^2)
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
                                  Constraints
-------------------------------------------------------------------------------
                      fi = Hi_jk X_j X_k + bi_j X_j - ci
-------------------------------------------------------------------------------
            H_ij = 2 Hi_jk X_k + bi_j;    r_i = Hi_jk X_j X_k - ci
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
'''

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

Base = optimization.GuidedProjectionBase


class WsurfOptimizer(Base):
    _N1 = 0

    _N2 = 0

    _N3 = 0

    _N4 = 0

    _N5 = 0

    _N6 = 0

    _bspline = None

    _curves = []

    _reference = None

    _boundary_curves = None

    _fixed_points = np.array([], 'i')

    _handle = None

    _scale = 1

    __scale = 1

    clusters = None

    include_boundary = False

    adaptive_curve = True

    normalize_geometry = True

    linear_coefficients = (0, 0, 0)

    n_curve_control_points = 4

    straightening = 0.1

    n_clusters = 1

    cluster_coefficients = [1, 1, 1, 1, 1]

    def __init__(self, bspline=None):
        Base.__init__(self)

        weights = {

            'normals': 1,

            'first': 1,

            'determinant': 1,

            'second': 1,

            'gaussian': 1,

            'mean': 1,

            'delta': 1,

            'squared_gradients': 1,

            'gradients_norms': 1,

            # -----------------------------------------------------------------
            #                           User weights
            # -----------------------------------------------------------------

            'hk': 0,

            'reference': 0,

            'control_lengths': 0,

            'fixed': 100,

            'gliding': 0,

            'control_fairness': 0,

            'curvature_fairness': 0,

            'curvature_minimization': 0,

            'isolines_parallel': 0,

            'linear_fitting': 0,

            'curve_fitting': 0,

        }

        self.add_weights(weights)

        self.bspline = bspline

    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------

    @property
    def curves(self):
        return self._curves

    @property
    def bspline(self):
        return self._bspline

    @bspline.setter
    def bspline(self, bspline):
        self._bspline = bspline
        if bspline is not None:
            self.normalize_bspline()
            self._fixed_points = np.array([], 'i')
            self._handle = None
            self.initialize = True
            self.add_value('curve_closest', None)

    @property
    def sampling(self):
        return self.bspline.sampling

    @sampling.setter
    def sampling(self, sampling):
        self.bspline.sampling = sampling
        self.reinitialize()

    @property
    def handle(self):
        if self._handle is None:
            return np.array([], 'i')
        else:
            return self._handle

    @handle.setter
    def handle(self, handle):
        if handle is None:
            handle = np.array([], 'i')
        self._handle = np.array(handle, 'i')

    @property
    def fixed_points(self):
        return self._fixed_points

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, scale):
        if scale > 0:
            self._scale = scale
            self.normalize_bspline()
            self.reinitialize()

    # -------------------------------------------------------------------------
    #                               Initialization
    # -------------------------------------------------------------------------

    def fix_points(self, points):
        points = np.array(points, 'i')
        self._fixed_points = np.unique(np.hstack((self.fixed_points, points)))

    def fix_boundary_points(self):
        self._fixed_points = self.bspline.boundary_control_points()

    def unfix_points(self, points):
        mask = np.invert(np.in1d(self._fixed_points, points))
        self._fixed_points = self._fixed_points[mask]

    def set_reference(self):
        self.add_value('reference', np.copy(self._bspline.control_points))
        self.add_value('control_lengths', self.control_lengths())
        self.add_value('control_diagonals', self.control_diagonals())
        self.make_boundary_curves()
        self.initialize = True

    def make_boundary_curves(self):
        bdr = self.bspline.boundary_control_curves()
        self._boundary_curves = []
        for b in bdr:
            P = self.bspline.control_points[b]
            crv = Polyline(P, closed=True)
            crv.refine(5)
            self._boundary_curves.append(crv)

    # -------------------------------------------------------------------------
    #                               HK diagram
    # -------------------------------------------------------------------------

    def fit_linear_relation(self):
        C = self.linear_coefficients
        if C[0] == 0 and C[1] == 0 and C[2] == 0:
            K, H, k1, k2 = self.bspline.curvatures()
            c = fitting.linear_regression(np.column_stack((K, H)))
            n = c[0][0]
            b = np.sum(c[1] * n)
            return n[0], n[1], b
        else:
            return C

    # -------------------------------------------------------------------------
    #                               Initialization
    # -------------------------------------------------------------------------

    def set_dimensions(self):
        self._N1 = 3 * self.bspline.C
        self._N2 = self._N1 + 3 * self.bspline.S
        self._N3 = self._N2 + 4 * self.bspline.S
        self._N4 = self._N3 + 3 * self.bspline.S
        self._N5 = self._N4 + 2 * self.bspline.S
        N6 = self._N4 + 2 * self.bspline.S
        N = self._N4 + 2 * self.bspline.S
        if self.get_weight('isolines_parallel') > 0:
            N += 8 * self.bspline.S
            N6 += 8 * self.bspline.S
        if self._N != N:
            self.reinitialize()
        self._N6 = N6
        self._N = N

    def initialize_unknowns_vector(self):
        Base.initialize_unknowns_vector(self)
        X = self.bspline.control_points.flatten('F')
        Du, Dv = self.bspline.first_derivatives()
        N = np.cross(Du, Dv)
        X = np.hstack((X, N.flatten('F')))
        E, F, G, L, M, N, K, H = self.bspline.fundamental_forms()
        X = np.hstack((X, E, F, G, E * G - F ** 2, L, M, N, K, H))
        if self.get_weight('isolines_parallel') > 0:
            Ku, Kv = self.bspline.uv_central_differences(K)
            Hu, Hv = self.bspline.uv_central_differences(H)
            DK = (E * G - F ** 2) ** (-1) * (E * Kv ** 2 - 2 * F * Ku * Kv + G * Ku ** 2)
            DH = (E * G - F ** 2) ** (-1) * (E * Hv ** 2 - 2 * F * Hu * Hv + G * Hu ** 2)
            X = np.hstack((X, Ku ** 2, Ku * Kv, Kv ** 2, Hu ** 2, Hu * Hv, Hv ** 2, DK, DH))
        self._X = X
        self._X0 = np.copy(X)

    def make_errors(self):
        self.normals_error()
        self.first_error()
        self.determinant_error()
        self.second_error()
        self.gaussian_error()
        self.mean_error()
        self.squared_gradients_error()
        self.gradients_norms_error()
        self.hk_error()
        self.k1k2_error()

    def post_iteration_update(self):
        C = self.bspline.C
        self.bspline.control_points[:, 0] = self.X[0:C]
        self.bspline.control_points[:, 1] = self.X[C:2 * C]
        self.bspline.control_points[:, 2] = self.X[2 * C:3 * C]

    # -------------------------------------------------------------------------
    #                                Interaction
    # -------------------------------------------------------------------------

    def normalize_bspline(self):
        K, H, k1, k2 = self.bspline.curvatures()
        norm = np.mean(np.abs(np.hstack((k1, k2))))
        self.scale_bspline(norm * 5 * self._scale)

    def scale_bspline(self, factor):
        if self.normalize_geometry:
            self._bspline.scale(factor)
            for i in range(len(self.curves)):
                self.curves[i].control_points *= factor
        self.set_reference()
        self.reinitialize()
        c = self.bspline.curvatures()
        ref = (np.mean(np.abs(c[0])), np.mean(np.abs(c[1])))
        self.add_value('ref_curvatures', ref)
        self.__scale *= factor

    def rebuild_bspline(self, u_points=None, v_points=None,
                        u_degree=None, v_degree=None):
        self.bspline.rebuild(u_points, v_points, u_degree, v_degree)
        self.set_reference()
        self.reinitialize()

    def resize_bspline(self):
        self._bspline.scale(1/self.__scale)

    def unresize_bspline(self):
        self._bspline.scale(self.__scale)

    def reset_scaling(self):
        self.__scale = 1

    # -------------------------------------------------------------------------
    #                                  Results
    # -------------------------------------------------------------------------

    def control_points(self):
        C = self.bspline.C
        points = self.X[0:3 * C]
        points = np.reshape(points, (C, 3), order='F')
        return points

    def normals(self, initialized=False):
        if initialized:
            X = self._X0
        else:
            X = self._X
        N1 = self._N1
        S = self.bspline.S
        normals = X[N1:N1 + 3 * S]
        normals = np.reshape(normals, (S, 3), order='F')
        return normals

    def first(self, initialized=False):
        if initialized:
            X = self._X0
        else:
            X = self._X
        N2 = self._N2
        S = self.bspline.S
        EFG = X[N2:N2 + 3 * S]
        EFG = np.reshape(EFG, (S, 3), order='F')
        return EFG

    def determinant(self, initialized=False):
        if initialized:
            X = self._X0
        else:
            X = self._X
        N2 = self._N2
        S = self.bspline.S
        Det = X[N2 + 3 * S:N2 + 4 * S]
        return Det

    def second(self, initialized=False):
        if initialized:
            X = self._X0
        else:
            X = self._X
        N3 = self._N3
        S = self.bspline.S
        LMN = X[N3:N3 + 3 * S]
        LMN = np.reshape(LMN, (S, 3), order='F')
        return LMN

    def gaussian(self, initialized=False):
        if initialized:
            X = self._X0
        else:
            X = self._X
        N4 = self._N4
        S = self.bspline.S
        K = X[N4:N4 + S]
        return K

    def mean(self, initialized=False):
        if initialized:
            X = self._X0
        else:
            X = self._X
        N4 = self._N4
        S = self.bspline.S
        H = X[N4 + S:N4 + 2 * S]
        return H

    def squared_gradients(self, initialized=False):
        if self.get_weight('isolines_parallel') <= 0:
            return None
        if initialized:
            X = self._X0
        else:
            X = self._X
        N5 = self._N5
        S = self.bspline.S
        sg = X[N5:N5 + 6 * S]
        return sg.reshape((6, S), order='F')

    def gradients_norms(self, initialized=False):
        if self.get_weight('isolines_parallel') <= 0:
            return None
        if initialized:
            X = self._X0
        else:
            X = self._X
        N5 = self._N5
        S = self.bspline.S
        sg = X[N5 + 6 * S:N5 + 8 * S]
        return sg.reshape((S, 2), order='F')

    # -------------------------------------------------------------------------
    #                                  Errors
    # -------------------------------------------------------------------------

    def normals_error(self):
        N0 = self.normals(initialized=True)
        N = self.normals()
        e = np.linalg.norm(N - N0, axis=1) / np.median(np.linalg.norm(N0, axis=1))
        Emean = np.mean(e)
        Emax = np.max(e)
        self.add_error('normals', Emean, Emax, self.get_weight('normals'))

    def first_error(self):
        F0 = self.first(initialized=True)
        F = self.first()
        e = np.abs(np.sum(F - F0, axis=1) / (np.mean(np.abs(F0) + 1e-8)))
        Emean = np.mean(e)
        Emax = np.max(e)
        self.add_error('first', Emean, Emax, self.get_weight('first'))

    def determinant_error(self):
        D0 = self.determinant(initialized=True)
        D = self.determinant()
        e = np.abs((D - D0) / (np.mean(np.abs(D0) + 1e-8)))
        Emean = np.mean(e)
        Emax = np.max(e)
        self.add_error('determinant', Emean, Emax,
                       self.get_weight('determinant'))

    def second_error(self):
        S0 = self.second(initialized=True)
        S = self.second()
        e = np.abs(np.sum(S - S0, axis=1) / (np.mean(np.abs(S0) + 1e-8)))
        Emean = np.mean(e)
        Emax = np.max(e)
        self.add_error('second', Emean, Emax, self.get_weight('second'))

    def gaussian_error(self):
        K0 = self.gaussian(initialized=True)
        K = self.gaussian()
        e = np.abs((K - K0) / (np.mean(np.abs(K0) + 1e-8)))
        Emean = np.mean(e)
        Emax = np.max(e)
        self.add_error('gaussian', Emean, Emax, self.get_weight('gaussian'))

    def mean_error(self):
        H0 = self.mean(initialized=True)
        H = self.mean()
        e = np.abs((H - H0) / (np.mean(np.abs(H0) + 1e-8)))
        Emean = np.mean(e)
        Emax = np.max(e)
        self.add_error('mean', Emean, Emax, self.get_weight('mean'))

    def hk_error(self):
        K = self.gaussian(True)
        H = self.mean(True)
        p, up, um, vp, vm = self.bspline.uv_central_differences_iterators()
        e = ((K[up] - K[um]) * (H[vp] - H[vm]) - (K[vp] - K[vm]) * (H[up] - H[um]))
        Emean = np.mean(np.abs(e))
        Emax = np.max(np.abs(e))
        self.add_error('hk', Emean, Emax, self.get_weight('hk'))

    def k1k2_error(self):
        K = self.gaussian(True)
        H = self.mean(True)
        D = np.abs((H ** 2 - K)) ** .5
        p, up, um, vp, vm = self.bspline.uv_central_differences_iterators()
        M11 = H[up] + D[up] - H[um] - D[um]
        M21 = H[vp] + D[vp] - H[vm] - D[vm]
        M12 = H[up] - D[up] - H[um] + D[um]
        M22 = H[vp] - D[vp] - H[vm] + D[vm]
        e = np.abs(M11 * M22 - M12 * M21)
        Emean = np.mean(e)
        Emax = np.max(e)
        self.add_error('k1k2', Emean, Emax, self.get_weight('hk'))

    def squared_gradients_error(self):
        if self.get_weight('isolines_parallel') <= 0:
            return None
        SG = self.squared_gradients()
        SG0 = self.squared_gradients(True)
        e = np.abs(SG - SG0)
        n = 1 / (np.mean(np.abs(SG0), axis=1) + 1e-5)
        for i in range(6):
            e[:, i] *= n[i]
        Emean = np.mean(e[:, :3])
        Emax = np.max(e[:, :3])
        self.add_error('K_sq_gradients', Emean, Emax, self.get_weight(
            'squared_gradients'))
        Emean = np.mean(e[:, 3:])
        Emax = np.max(e[:, 3:])
        self.add_error('H_sq_gradients', Emean, Emax, self.get_weight(
            'squared_gradients'))

    def gradients_norms_error(self):
        if self.get_weight('isolines_parallel') <= 0:
            return None
        SG = self.gradients_norms()
        SG0 = self.gradients_norms(True)
        e = np.abs(SG - SG0)
        n = 1 / (np.mean(np.abs(SG0), axis=0) + 1e-5)
        for i in range(2):
            e[:, i] *= n[i]
        Emean = np.mean(e[:, 0])
        Emax = np.max(e[:, 0])
        self.add_error('K_grad_norms', Emean, Emax, self.get_weight(
            'gradients_norms'))
        Emean = np.mean(e[:, 1])
        Emax = np.max(e[:, 1])
        self.add_error('H_grad_norms', Emean, Emax, self.get_weight(
            'gradients_norms'))

    def geometric_error(self):
        e_mean = 0
        e_max = 0
        n = 0
        errors = ['normals', 'first', 'second', 'determinant',
                  'gaussian', 'mean']
        for key in errors:
            err = self.get_error(key)
            e_mean += err[0]
            e_max = max(err[1], e_max)
            n += 1
        return e_mean / n, e_max

    # -------------------------------------------------------------------------
    #                                   Utilities
    # -------------------------------------------------------------------------

    def control_lengths(self):
        v1, v2 = self._bspline.edge_vertices()
        E = self._bspline.control_points[v1] - self._bspline.control_points[v2]
        l = np.linalg.norm(E, axis=1)
        return l

    def control_diagonals(self):
        v1, v2 = self._bspline.face_diagonals()
        E = self._bspline.control_points[v1] - self._bspline.control_points[v2]
        l = np.linalg.norm(E, axis=1)
        return l

    def info_string(self):
        out = str(self.bspline) + '\n'
        out += 'sampling: ({},{})'.format(self.bspline.u_sampling,
                                          self.bspline.v_sampling)
        out += 'reference: {:.4f}\n'.format(self.get_weight('reference'))
        out += 'control fairness: {:.4f}\n'.format(self.get_weight(
            'control_fairness'))
        out += 'isolines fairness: {:.4f}\n'.format(self.get_weight(
            'curvature_fairness'))

    def principal_curvatures(self, initialized=True):
        H = self.mean(initialized)
        K = self.gaussian(initialized)
        d = np.abs(H ** 2 - K) ** .5
        k1 = H + d
        k2 = H - d
        return k1, k2

    def plot_surface(self):
        plot = []
        self.bspline.plot_mode = 'control'
        plot.append(plotter.Edges(self.bspline))
        plot.append(plotter.Points(self.bspline.control_points,
                                       radius=0.15, color='gold'))
        self.bspline.plot_mode = 'surface'
        plot.append(plotter.Faces(self.bspline))
        plotter.view(plot)

    # --------------------------------------------------------------------------
    #                                Errors strings
    # --------------------------------------------------------------------------

    def geometric_error_string(self):
        return '{:.4E} | {:.4E}'.format(*self.geometric_error())

    # -------------------------------------------------------------------------
    #                                  Constraints
    # -------------------------------------------------------------------------

    def forms_constraints(self):
        C = self.bspline.C
        S = self.bspline.S
        N = self.N
        X = self._X
        s, u, v, c, cu, cv = self.bspline.uv_sampling_iterators()
        Nu, Nv = self.bspline.basis_functions()
        Nuu, Nvv = self.bspline.derivative_basis_functions(d=1)
        Nuuu, Nvvv = self.bspline.derivative_basis_functions(d=2)
        Du, Dv, Duu, Duv, Dvv = self.bspline.second_derivatives()
        s0 = np.arange(S)
        one = np.ones(S)
        # ----------------------------------------------------------------------
        #                             normals
        # ----------------------------------------------------------------------
        w = self.get_weight('normals')
        i = np.hstack((s, s, s, s, s0))
        # ----------------------------------------------------------------------
        nx0 = self._N1 + s0
        j = np.hstack((C + c, 2 * C + c, C + c, 2 * C + c, nx0))
        data = np.hstack((Nuu[u, cu] * Nv[v, cv] * Dv[s, 2],
                          Nu[u, cu] * Nvv[v, cv] * Du[s, 1],
                          -Nu[u, cu] * Nvv[v, cv] * Du[s, 2],
                          -Nuu[u, cu] * Nv[v, cv] * Dv[s, 1],
                          -one)) * w
        r = (Du[s0, 1] * Dv[s0, 2] - Du[s0, 2] * Dv[s0, 1]) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'Nx')
        # ----------------------------------------------------------------------
        ny0 = nx0 + S
        j = np.hstack((2 * C + c, c, 2 * C + c, c, ny0))
        data = np.hstack((Nuu[u, cu] * Nv[v, cv] * Dv[s, 0],
                          Nu[u, cu] * Nvv[v, cv] * Du[s, 2],
                          -Nu[u, cu] * Nvv[v, cv] * Du[s, 0],
                          -Nuu[u, cu] * Nv[v, cv] * Dv[s, 2],
                          -one)) * w
        r = (Du[s0, 2] * Dv[s0, 0] - Du[s0, 0] * Dv[s0, 2]) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'Ny')
        # ----------------------------------------------------------------------
        nz0 = ny0 + S
        j = np.hstack((c, C + c, c, C + c, nz0))
        data = np.hstack((Nuu[u, cu] * Nv[v, cv] * Dv[s, 1],
                          Nu[u, cu] * Nvv[v, cv] * Du[s, 0],
                          -Nu[u, cu] * Nvv[v, cv] * Du[s, 1],
                          -Nuu[u, cu] * Nv[v, cv] * Dv[s, 0],
                          -one)) * w
        r = (Du[s0, 0] * Dv[s0, 1] - Du[s0, 1] * Dv[s0, 0]) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'Nz')
        # ----------------------------------------------------------------------
        #                       first fundamental form
        # ----------------------------------------------------------------------
        w = self.get_weight('first')
        # ----------------------------------------------------------------------
        e0 = self._N2 + s0
        i = np.hstack((s, s, s, s0))
        j = np.hstack((c, C + c, 2 * C + c, e0))
        data = np.hstack((2 * Nuu[u, cu] * Nv[v, cv] * Du[s, 0],
                          2 * Nuu[u, cu] * Nv[v, cv] * Du[s, 1],
                          2 * Nuu[u, cu] * Nv[v, cv] * Du[s, 2], -one)) * w
        r = np.einsum('ij,ij->i', Du[s0], Du[s0]) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'E')
        # ----------------------------------------------------------------------
        f0 = e0 + S
        i = np.hstack((s, s, s, s, s, s, s0))
        j = np.hstack((c, C + c, 2 * C + c, c, C + c, 2 * C + c, f0))
        data = np.hstack((Nuu[u, cu] * Nv[v, cv] * Dv[s, 0],
                          Nuu[u, cu] * Nv[v, cv] * Dv[s, 1],
                          Nuu[u, cu] * Nv[v, cv] * Dv[s, 2],
                          Nu[u, cu] * Nvv[v, cv] * Du[s, 0],
                          Nu[u, cu] * Nvv[v, cv] * Du[s, 1],
                          Nu[u, cu] * Nvv[v, cv] * Du[s, 2],
                          -one)) * w
        r = np.einsum('ij,ij->i', Du[s0], Dv[s0]) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'F')
        # ----------------------------------------------------------------------
        g0 = f0 + S
        i = np.hstack((s, s, s, s0))
        j = np.hstack((c, C + c, 2 * C + c, g0))
        data = np.hstack((2 * Nu[u, cu] * Nvv[v, cv] * Dv[s, 0],
                          2 * Nu[u, cu] * Nvv[v, cv] * Dv[s, 1],
                          2 * Nu[u, cu] * Nvv[v, cv] * Dv[s, 2], -one)) * w
        r = np.einsum('ij,ij->i', Dv[s0], Dv[s0]) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'G')
        # ---------------------------------------------------------------------
        #                       second fundamental form
        # ---------------------------------------------------------------------
        w = self.get_weight('second')
        nx = self._N1 + s
        ny = nx + S
        nz = ny + S
        Nn = self.normals()
        det = np.abs(self.determinant()) ** .5
        i = np.hstack((s, s, s, s0, s0, s0, s0))
        # ---------------------------------------------------------------------
        l = self._N3 + s0
        j = np.hstack((c, C + c, 2 * C + c, nx0, ny0, nz0, l))
        data = np.hstack((Nuuu[u, cu] * Nv[v, cv] * X[nx] / det[s],
                          Nuuu[u, cu] * Nv[v, cv] * X[ny] / det[s],
                          Nuuu[u, cu] * Nv[v, cv] * X[nz] / det[s],
                          Duu[s0, 0] / det[s0], Duu[s0, 1] / det[s0],
                          Duu[s0, 2] / det[s0], -one)) * w
        r = np.einsum('ij,ij,i->i', Duu[s0], Nn[s0], 1 / det[s0]) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'L')
        # ---------------------------------------------------------------------
        m = l + S
        j = np.hstack((c, C + c, 2 * C + c, nx0, ny0, nz0, m))
        data = np.hstack((Nuu[u, cu] * Nvv[v, cv] * X[nx] / det[s],
                          Nuu[u, cu] * Nvv[v, cv] * X[ny] / det[s],
                          Nuu[u, cu] * Nvv[v, cv] * X[nz] / det[s],
                          Duv[s0, 0] / det[s0], Duv[s0, 1] / det[s0],
                          Duv[s0, 2] / det[s0], -one)) * w
        r = np.einsum('ij,ij,i->i', Duv[s0], Nn[s0], 1 / det[s0]) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'M')
        # ---------------------------------------------------------------------
        n = m + S
        j = np.hstack((c, C + c, 2 * C + c, nx0, ny0, nz0, n))
        data = np.hstack((Nu[u, cu] * Nvvv[v, cv] * X[nx] / det[s],
                          Nu[u, cu] * Nvvv[v, cv] * X[ny] / det[s],
                          Nu[u, cu] * Nvvv[v, cv] * X[nz] / det[s],
                          Dvv[s0, 0] / det[s0], Dvv[s0, 1] / det[s0],
                          Dvv[s0, 2] / det[s0], -one)) * w
        r = np.einsum('ij,ij,i->i', Dvv[s0], Nn[s0], 1 / det[s0]) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'N')
        # ---------------------------------------------------------------------

    def determinant_constraints(self):
        w = self.get_weight('determinant')
        S = self.bspline.S
        N = self.N
        X = self._X
        s = np.arange(S)
        e = self._N2 + s
        f = e + S
        g = f + S
        det = g + S
        i = np.hstack((s, s, s, s))
        j = np.hstack((e, g, f, det))
        data = np.hstack((X[g], X[e], -2 * X[f], -np.ones(S))) * w
        r = (X[e] * X[g] - X[f] ** 2) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'Det')

    def curvature_constraints(self):
        S = self.bspline.S
        N = self.N
        X = self._X
        s = np.arange(S)
        e = self._N2 + s
        f = e + S
        g = f + S
        det = g + S
        l = self._N3 + s
        m = l + S
        n = m + S
        # ---------------------------------------------------------------------
        w = self.get_weight('gaussian')
        k = self._N4 + s
        i = np.hstack((s, s, s, s, s))
        j = np.hstack((l, m, n, k, det))
        data = np.hstack((X[n], -2 * X[m], X[l], -X[det], -X[k])) * w
        r = (X[n] * X[l] - X[m] ** 2 - X[k] * X[det]) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'K')
        # ---------------------------------------------------------------------
        # H = (LG - 2MF + NE) / 2(EG - F^2)
        w = self.get_weight('mean')
        h = self._N4 + S + s
        i = np.hstack((s, s, s, s, s, s, s, s))
        j = np.hstack((e, f, g, l, m, n, h, det))
        data = np.hstack((X[n], -2 * X[m], X[l], X[g], -2 * X[f], X[e],
                          -2 * X[det], -2 * X[h])) * w
        r = (X[l] * X[g] - 2 * X[m] * X[f] + X[n] * X[e] - 2 * X[h] * X[det]) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'H')

    def hk_constraints(self):
        w = self.get_weight('hk')
        N = self.N
        p, up, um, vp, vm = self.bspline.uv_central_differences_iterators(
            include_boundary=self.include_boundary)
        Hu, Hv = self.bspline.uv_central_differences(self.mean())
        Ku, Kv = self.bspline.uv_central_differences(self.gaussian())
        Hu = Hu[p]
        Hv = Hv[p]
        Ku = Ku[p]
        Kv = Kv[p]
        k = self._N4
        h = self._N4 + self.bspline.S
        S = len(p)
        Kn = (Ku ** 2 + Kv ** 2) ** .5 + 1e-8
        Hn = (Hu ** 2 + Hv ** 2) ** .5 + 1e-8
        nr = np.mean(Kn * Hn) / (Kn * Hn) * 100
        nr = np.minimum(nr, 10 * np.mean(nr))
        # nr = 100
        # nr = np.mean(Kn) / Kn * 100
        i = np.arange(S)
        i = np.hstack((i, i, i, i, i, i, i, i))
        j = np.hstack((k + up, k + um, h + vp, h + vm, k + vp, k + vm,
                       h + up, h + um))
        data = np.hstack((Hv * nr, -Hv * nr, Ku * nr, -Ku * nr,
                          -Hu * nr, Hu * nr, -Kv * nr, Kv * nr)) * w
        r = (Ku * Hv - Kv * Hu) * nr * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'Wein')

    def hk_constraints2(self):
        w = self.get_weight('hk')
        S = self.bspline.S
        N = self.N
        X = self._X
        p, up, um, vp, vm = self.bspline.uv_central_differences_iterators()
        K = self._N4
        H = self._N4 + S
        i = np.arange(S)
        i = np.hstack((i, i, i, i, i, i, i, i))
        j = np.hstack((K + up, K + um, H + vp, H + vm, K + vp, K + vm, H + up, H + um))
        data = np.hstack(((X[H + vp] - X[H + vm]), -(X[H + vp] - X[H + vm]),
                          (X[K + up] - X[K + um]), -(X[K + up] - X[K + um]),
                          -(X[H + up] - X[H + um]), (X[H + up] - X[H + um]),
                          -(X[K + vp] - X[K + vm]), (X[K + vp] - X[K + vm]))) * w
        r = ((X[K + up] - X[K + um]) * (X[H + vp] - X[H + vm]) -
             (X[K + vp] - X[K + vm]) * (X[H + up] - X[H + um])) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'Wein')

    # -------------------------------------------------------------------------
    #                             Isolines Fairness
    # -------------------------------------------------------------------------

    def squared_gradients_constraints(self):
        if self.get_weight('isolines_parallel') <= 0:
            return
        S = self.bspline.S
        k = self._N4
        h = self._N4 + S
        p, up, um, vp, vm = self.bspline.uv_central_differences_iterators()
        Hu, Hv, du, dv = self.bspline.uv_central_differences(self.mean(), True)
        Ku, Kv = self.bspline.uv_central_differences(self.gaussian())
        s = np.arange(S)
        one = np.ones(S)
        ku2 = self._N5 + s
        kukv = self._N5 + S + s
        kv2 = self._N5 + 2 * S + s
        hu2 = self._N5 + 3 * S + s
        huhv = self._N5 + 4 * S + s
        hv2 = self._N5 + 5 * S + s
        # ---------------------------------------------------------------------
        w = self.get_weight('squared_gradients')
        i1 = np.hstack((s, s, s))
        i2 = np.hstack((s, s, s, s, s))
        # ---------------------------------------------------------------------
        j = np.hstack((k + up, k + um, ku2))
        data = np.hstack((2 * Ku / du, - 2 * Ku / du, -one)) * w
        H = sparse.coo_matrix((data, (i1, j)), shape=(S, self.N))
        r = Ku ** 2 * w
        self.add_iterative_constraint(H, r, 'Ku^2')
        # ---------------------------------------------------------------------
        j = np.hstack((k + vp, k + vm, kv2))
        data = np.hstack((2 * Kv / dv, - 2 * Kv / dv, -one)) * w
        H = sparse.coo_matrix((data, (i1, j)), shape=(S, self.N))
        r = Kv ** 2 * w
        self.add_iterative_constraint(H, r, 'Kv^2')
        # ---------------------------------------------------------------------
        j = np.hstack((k + up, k + um, k + vp, k + vm, kukv))
        data = np.hstack((Kv / du, -Kv / du, Ku / dv, -Ku / dv, -one)) * w
        H = sparse.coo_matrix((data, (i2, j)), shape=(S, self.N))
        r = Ku * Kv * w
        self.add_iterative_constraint(H, r, 'KuKv')
        # ---------------------------------------------------------------------
        w = self.get_weight('squared_gradients')
        j = np.hstack((h + up, h + um, hu2))
        data = np.hstack((2 * Hu / du, - 2 * Hu / du, -one)) * w
        H = sparse.coo_matrix((data, (i1, j)), shape=(S, self.N))
        r = Hu ** 2 * w
        self.add_iterative_constraint(H, r, 'Hu^2')
        # ---------------------------------------------------------------------
        j = np.hstack((h + vp, h + vm, hv2))
        data = np.hstack((2 * Hv / dv, - 2 * Hv / dv, -one)) * w
        H = sparse.coo_matrix((data, (i1, j)), shape=(S, self.N))
        r = Hv ** 2 * w
        self.add_iterative_constraint(H, r, 'Hv^2')
        # ---------------------------------------------------------------------
        j = np.hstack((h + up, h + um, h + vp, h + vm, huhv))
        data = np.hstack((Hv / du, -Hv / du, Hu / dv, -Hu / dv, -one)) * w
        H = sparse.coo_matrix((data, (i2, j)), shape=(S, self.N))
        r = Hu * Hv * w
        self.add_iterative_constraint(H, r, 'HuHv')

    def gradients_norm_constraints(self):
        if self.get_weight('isolines_parallel') <= 0:
            return
        S = self.bspline.S
        s = np.arange(S)
        one = np.ones(S)
        X = self._X
        e = self._N2 + s
        f = e + S
        g = f + S
        det = X[g + S]
        ku2 = self._N5 + s
        kukv = self._N5 + S + s
        kv2 = self._N5 + 2 * S + s
        hu2 = self._N5 + 3 * S + s
        huhv = self._N5 + 4 * S + s
        hv2 = self._N5 + 5 * S + s
        dk = self._N5 + 6 * S + s
        dh = self._N5 + 7 * S + s
        # ---------------------------------------------------------------------
        # DK = (E*G-F**2)**(-1) * (E*Kv**2 - 2*F*Ku*Kv + G*Ku**2)
        # DH = (E*G-F**2)**(-1) * (E*Hv**2 - 2*F*Hu*Hv + G*Hu**2)
        # ---------------------------------------------------------------------
        i = np.hstack((s, s, s, s, s, s, s))
        # ---------------------------------------------------------------------
        w = self.get_weight('gradients_norms')
        j = np.hstack((e, f, g, kv2, kukv, ku2, dk))
        data = np.hstack((X[kv2] / det, -2 * X[kukv] / det, X[ku2] / det,
                          X[e] / det, -2 * X[f] / det, X[g] / det, -one)) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, self.N))
        r = (X[e] * X[kv2] - 2 * X[f] * X[kukv] + X[g] * X[ku2]) / det * w
        self.add_iterative_constraint(H, r, 'DK')
        # ---------------------------------------------------------------------
        w = self.get_weight('gradients_norms')
        j = np.hstack((e, f, g, hv2, huhv, hu2, dh))
        data = np.hstack((X[hv2] / det, -2 * X[huhv] / det, X[hu2] / det,
                          X[e] / det, -2 * X[f] / det, X[g] / det, -one)) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, self.N))
        r = (X[e] * X[hv2] - 2 * X[f] * X[huhv] + X[g] * X[hu2]) / det * w
        self.add_iterative_constraint(H, r, 'DH')

    def isolines_parallel_constraints2(self):
        if self.get_weight('isolines_parallel') <= 0:
            return
        S = self.bspline.S
        N = self.N
        X = self._X
        p, up, um, vp, vm = self.bspline.uv_central_differences_iterators()
        K = self._N4
        dK = self._N5 + 6 * S
        i = np.arange(S)
        w = self.get_weight('isolines_parallel') * 100
        i = np.hstack((i, i, i, i, i, i, i, i))
        j = np.hstack((K + up, K + um, dK + vp, dK + vm, K + vp, K + vm,
                       dK + up, dK + um))
        data = np.hstack(((X[dK + vp] - X[dK + vm]), -(X[dK + vp] - X[dK + vm]),
                          (X[K + up] - X[K + um]), -(X[K + up] - X[K + um]),
                          -(X[dK + up] - X[dK + um]), (X[dK + up] - X[dK + um]),
                          -(X[K + vp] - X[K + vm]), (X[K + vp] - X[K + vm]))) * w
        r = ((X[K + up] - X[K + um]) * (X[dK + vp] - X[dK + vm]) -
             (X[K + vp] - X[K + vm]) * (X[dK + up] - X[dK + um])) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'Kfair')
        w = self.get_weight('isolines_parallel')
        H = self._N4 + S
        dH = self._N5 + 7 * S
        i = np.arange(S)
        i = np.hstack((i, i, i, i, i, i, i, i))
        # print(np.mean(np.abs(X[dK+vp]-X[dK+vm])))
        # print(np.mean(np.abs(X[dH+vp]-X[dH+vm])))
        j = np.hstack((H + up, H + um, dH + vp, dH + vm, H + vp, H + vm, dH + up, dH + um))
        data = np.hstack(((X[dH + vp] - X[dH + vm]), -(X[dK + vp] - X[dH + vm]),
                          (X[H + up] - X[H + um]), -(X[H + up] - X[H + um]),
                          -(X[dH + up] - X[dH + um]), (X[dH + up] - X[dH + um]),
                          -(X[H + vp] - X[H + vm]), (X[H + vp] - X[H + vm]))) * w
        r = ((X[H + up] - X[H + um]) * (X[dH + vp] - X[dH + vm]) -
             (X[H + vp] - X[H + vm]) * (X[dH + up] - X[dH + um])) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'Hfair')

    def isolines_parallel_constraints(self):
        w = self.get_weight('isolines_parallel')
        if w <= 0:
            return
        N = self.N
        X = self._X
        norms = self.gradients_norms()
        p, up, um, vp, vm = self.bspline.uv_central_differences_iterators(
            include_boundary=False)
        S = len(p)
        i = np.arange(S)
        i = np.hstack((i, i, i, i, i, i, i, i))
        # ---------------------------------------------------------------------
        K = self._N4
        dK = self._N5 + 6 * self.bspline.S
        Ku, Kv = self.bspline.uv_central_differences(self.gaussian())
        dKu, dKv = self.bspline.uv_central_differences(norms[:, 0])
        Ku = Ku[p]
        Kv = Kv[p]
        dKu = dKu[p]
        dKv = dKv[p]
        Kn = (Ku ** 2 + Kv ** 2) ** .5 + 1e-8
        dKn = (dKu ** 2 + dKv ** 2) ** .5 + 1e-8
        nr = np.mean(Kn * dKn) / (Kn * dKn) * 1
        #nr = 0.1
        j = np.hstack((K + up, K + um, dK + vp, dK + vm, K + vp, K + vm,
                       dK + up, dK + um))
        data = np.hstack((dKv * nr, -dKv * nr, Ku * nr, -Ku * nr,
                          -dKu * nr, dKu * nr, -Kv * nr, Kv * nr)) * w
        r = (Ku * dKv - Kv * dKu) * nr * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'KNfair')
        # ---------------------------------------------------------------------
        H = self._N4 + S
        dH = self._N5 + 7 * S
        Hu, Hv = self.bspline.uv_central_differences(self.mean())
        dHu, dHv = self.bspline.uv_central_differences(norms[:, 1])
        Hu = Hu[p]
        Hv = Hv[p]
        dHu = dHu[p]
        dHv = dHv[p]
        Hn = (Hu ** 2 + Hv ** 2) ** .5 + 1e-8
        dHn = (dHu ** 2 + dHv ** 2) ** .5 + 1e-8
        nr = np.mean(Hn * dHn) / (Hn * dHn) * 10
        #nr = 1
        j = np.hstack((H + up, H + um, dH + vp, dH + vm, H + vp, H + vm,
                       dH + up, dH + um))
        data = np.hstack((dHv * nr, -dHv * nr, Hu * nr, -Hu * nr,
                          -dHu * nr, dHu * nr, -Hv * nr, Hv * nr)) * w
        r = (Hu * dHv - Hv * dHu) * nr * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, N))
        self.add_iterative_constraint(H, r, 'HNfair')

    # -------------------------------------------------------------------------
    #                              Linear Weingarten
    # -------------------------------------------------------------------------

    def linear_fitting_constraints(self):
        w = self.get_weight('linear_fitting')
        if w <= 0:
            return
        S = self.bspline.S
        s = np.arange(S)
        k = self._N4 + s
        h = self._N4 + S + s
        C = self.fit_linear_relation()
        a = np.repeat(C[0], S)
        b = np.repeat(C[1], S)
        c = np.repeat(C[2], S)
        i = np.hstack((s, s))
        j = np.hstack((k, h))
        data = np.hstack((a, b)) * w
        r = c * w
        H = sparse.coo_matrix((data, (i, j)), shape=(S, self.N))
        self.add_iterative_constraint(H, r, 'Lin')

    def curve_fitting_constraints0(self):
        w = self.get_weight('curve_fitting')
        if w <= 0:
            return
        for l in range(len(self._curves)):
            S = self.bspline.S
            s = np.arange(S)
            K = self.gaussian()
            H = self.mean()
            P = np.column_stack((K, H, np.zeros(len(K))))
            if self.adaptive_curve:
                n = self.n_curve_control_points
                try:
                    self._curve.fit_line_to_points(P, control_points_number=n)
                    self._curve.fit_to_points(P, straightening=0.1)
                except:
                    self.fit_curve()
            k = self._N4 + s
            h = self._N4 + S + s
            c = self._curve.closest_points(P)
            T, N = self._curve.frame(c)
            C = self._curve.points(c)[:, [0, 1]]
            N = N[:, [0, 1]]
            i = np.hstack((s, s))
            j = np.hstack((k, h))
            data = N.flatten('F') * w
            H = sparse.coo_matrix((data, (i, j)), shape=(S, self.N))
            r = np.einsum('ij,ij->i', N, C) * w
            self.add_iterative_constraint(H, r, 'Crv_t')
            i = np.hstack((s, S + s))
            data = np.ones(2 * S) * 0.01 * w
            H = sparse.coo_matrix((data, (i, j)), shape=(2 * S, self.N))
            r = C.flatten('F') * 0.01 * w
            self.add_iterative_constraint(H, r, 'Crv_{}'.format(l))

    # -------------------------------------------------------------------------
    #                                 Reference
    # -------------------------------------------------------------------------

    def reference_constraints(self):
        w = self.get_weight('reference') / 10
        C = 3 * self.bspline.C
        i = np.arange(C)
        H = sparse.coo_matrix((np.ones(C) * w, (i, i)), shape=(C, self.N))
        r = self.get_value('reference').flatten('F') * w
        self.add_constant_constraint(H, r, 'Ref')

    def fixed_points_constraints(self):
        w = self.get_weight('fixed')
        fix = np.unique(np.hstack((self.handle, self._fixed_points)))
        if len(fix) == 0:
            return
        C = 3 * len(fix)
        i = np.arange(C)
        j = np.hstack((fix, fix + self.bspline.C, fix + 2 * self.bspline.C))
        H = sparse.coo_matrix((np.ones(C) * w, (i, j)), shape=(C, self.N))
        r = self.bspline.control_points[fix].flatten('F') * w
        self.add_constant_constraint(H, r, 'Fix')

    def gliding_boundary_constraints(self):
        w = self.get_weight('gliding')
        if w <= 0:
            return
        bdrs = self.bspline.boundary_control_curves()
        for b in range(len(bdrs)):
            bdr = bdrs[b]
            crv = self._boundary_curves[b]
            c = crv.closest_vertices(self.bspline.control_points[bdr])
            T = crv.vertex_tangents(normalized=True)[c]
            V1 = utilities.orthogonal_vectors(T)
            V2 = np.cross(T, V1)
            C = len(c)
            nC = self.bspline.C
            i = np.arange(C)
            i = np.hstack((i, i, i))
            j = np.hstack((bdr, bdr + nC, bdr + 2 * nC))
            data = V1.flatten('F') * w
            r = np.einsum('ij,ij->i', self.bspline.control_points[bdr], V1) * w
            H = sparse.coo_matrix((data, (i, j)), shape=(C, self.N))
            self.add_iterative_constraint(H, r, 'Glid_{}_1'.format(b))
            data = V2.flatten('F') * w
            r = np.einsum('ij,ij->i', self.bspline.control_points[bdr], V2) * w
            H = sparse.coo_matrix((data, (i, j)), shape=(C, self.N))
            self.add_iterative_constraint(H, r, 'Glid_{}_2'.format(b))

    def control_lengths_constraints(self):
        w = self.get_weight('control_lengths')
        if w <= 0:
            return
        L = self.get_value('control_lengths')
        Lx = self.control_lengths()
        X = self.X
        v1, v2 = self.bspline.edge_vertices()
        E = len(v1)
        C = self.bspline.C
        v1 = np.hstack((v1, C + v1, 2 * C + v1))
        v2 = np.hstack((v2, C + v2, 2 * C + v2))
        e = np.arange(E)
        i = np.hstack((e, e, e, e, e, e))
        j = np.hstack((v1, v2))
        data = 2 * np.hstack((X[v1] - X[v2], X[v2] - X[v1])) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(E, self.N))
        r = (Lx ** 2 + L ** 2) * w
        self.add_iterative_constraint(H, r, 'Len')

    def control_diagonals_constraints(self):
        w = self.get_weight('control_lengths') / 2
        if w <= 0:
            return
        L = self.get_value('control_diagonals')
        Lx = self.control_diagonals()
        X = self.X
        v1, v2 = self.bspline.face_diagonals()
        E = len(v1)
        C = self.bspline.C
        v1 = np.hstack((v1, C + v1, 2 * C + v1))
        v2 = np.hstack((v2, C + v2, 2 * C + v2))
        e = np.arange(E)
        i = np.hstack((e, e, e, e, e, e))
        j = np.hstack((v1, v2))
        data = 2 * np.hstack((X[v1] - X[v2], X[v2] - X[v1])) * w
        H = sparse.coo_matrix((data, (i, j)), shape=(E, self.N))
        r = (Lx ** 2 + L ** 2) * w
        self.add_iterative_constraint(H, r, 'Diag')

    # -------------------------------------------------------------------------
    #                                 Fairness
    # -------------------------------------------------------------------------

    def control_fairness_constraints(self):
        f = self.bspline.S ** .5 / 1000
        w = self.get_weight('control_fairness') * f
        c, cp, cm = self.bspline.control_points_curves_iterators()
        L = len(c)
        one = self.bspline.control_points[cp] - self.bspline.control_points[cm]
        one = np.linalg.norm(one, axis=1) ** -1
        C = self.bspline.C
        # one = np.ones(L)
        i = np.arange(L)
        i = np.hstack((i, i, i))
        j = np.hstack((c, cp, cm))
        data = np.hstack((-2 * one, one, one)) * w
        i = np.hstack((i, L + i, 2 * L + i))
        j = np.hstack((j, C + j, 2 * C + j))
        data = np.hstack((data, data, data))
        K = sparse.coo_matrix((data, (i, j)), shape=(3 * L, self.N))
        s = np.zeros((3 * L))
        self.add_iterative_fairness(K, s, 'CFair')

    def curvature_fairness_constraints(self):
        c = self.get_value('ref_curvatures')
        p, up, um, vp, vm = self.bspline.uv_central_differences_iterators(
            include_boundary=False)
        S = len(p)
        k = self._N4
        h = self._N4 + self.bspline.S
        one = np.ones(S)
        i = np.hstack((p, p, p, p, p))
        s = np.zeros(self.bspline.S)
        data = np.hstack((-one, .25 * one, .25 * one, .25 * one, .25 * one))
        # ---------------------------------------------------------------------
        w = self.get_weight('curvature_fairness') * c[1] / c[0]
        j = np.hstack((k + p, k + up, k + um, k + vp, k + vm))
        K = sparse.coo_matrix((data * w, (i, j)), shape=(self.bspline.S, self.N))
        self.add_iterative_fairness(K, s, 'KFair')
        # ---------------------------------------------------------------------
        w = self.get_weight('curvature_fairness')
        j = np.hstack((h + p, h + up, h + um, h + vp, h + vm))
        K = sparse.coo_matrix((data * w, (i, j)), shape=(self.bspline.S, self.N))
        self.add_iterative_fairness(K, s, 'HFair')

    def curvature_minimization_constraints(self):
        c = self.get_value('ref_curvatures')
        S = self.bspline.S
        i = np.arange(S)
        k = self._N4 + i
        h = self._N4 + S + i
        w = self.get_weight('curvature_minimization') * c[1] / c[0]
        data = np.ones(S)
        K = sparse.coo_matrix((data * w, (i, k)), shape=(S, self.N))
        s = np.zeros(S)
        self.add_iterative_fairness(K, s, 'Kmin')
        w = self.get_weight('curvature_minimization')
        K = sparse.coo_matrix((data * w, (i, h)), shape=(S, self.N))
        self.add_iterative_fairness(K, s, 'Hmin')

    # -------------------------------------------------------------------------
    #                                 Build
    # -------------------------------------------------------------------------

    def build_iterative_constraints(self):
        self.forms_constraints()
        self.determinant_constraints()
        self.curvature_constraints()
        self.hk_constraints()
        self.squared_gradients_constraints()
        self.gradients_norm_constraints()
        self.isolines_parallel_constraints()
        self.control_lengths_constraints()
        self.control_diagonals_constraints()
        self.linear_fitting_constraints()
        self.gliding_boundary_constraints()

    def build_constant_constraints(self):
        self.reference_constraints()
        self.fixed_points_constraints()

    def build_constant_fairness(self):
        pass

    def build_iterative_fairness(self):
        self.control_fairness_constraints()
        self.curvature_fairness_constraints()



