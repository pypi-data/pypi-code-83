#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import absolute_import

from __future__ import print_function

from __future__ import division

from traits.api import Button, Str, Float, Bool, Int

from traits.api import on_trait_change

from traitsui.api import View, Item, HGroup, Group, VGroup, Tabbed

import numpy as np

# ------------------------------------------------------------------------------

from .geolab.gui.geolabcomponent import GeolabComponent

from .bspline_optimizer import WsurfOptimizer

from .geolab.geometry import Polyline

from .geolab.plotter.plotutilities import uv_wheel_lut_table

# ------------------------------------------------------------------------------

__author__ = 'Davide Pellis'


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
#                            Optimization GUI
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


class WeingartenGUI(GeolabComponent):
    # --------------------------------------------------------------------------
    #                                 Traits
    # --------------------------------------------------------------------------

    name = Str('Weingarten B-spline')

    iterations = Int(1, label='Iterations')

    epsilon = Float(0.001, label='Dumping')

    step = Float(1, label='Step')

    step_control = Bool(True)

    alignment = Float(0.1)

    reference_closeness = Float(0.1)

    shape_preservation = Float(0)

    gliding_boundary = Float(0.01)

    control_fairness = Float(0.2)

    isolines_parallel = Float(0)

    fitting = Float(0, label='Linear')

    scale = Float(1)

    curve_fitting = Button(label='Fit')

    reparametrize_points = Button(label='Reparametrize')

    reinitialize = Button(label='Initialize')

    optimize = Button(label='Optimize')

    geometric_error = Str('_', label='Geometric')

    interactive = Bool(False, label='Interactive')

    boundary = Bool(False, label='boundary')

    u_sampling = Int(0, label='Sampling (U,V)')

    v_sampling = Int(0)

    u_degree = Int(0, label='Degree (U,V)')

    v_degree = Int(0)

    u_points = Int(0, label='Points (U,V)')

    v_points = Int(0)

    rebuild_button = Button(label='Rebuild')

    resample_button = Button(label='Resample')

    plot_samples_check = Bool(False, label='Show samples')

    plot_clusters_check = Bool(False, label='Plot clusters')

    fix_button = Button(label='Fix', tooltip='Fix selected vertices')

    unfix_button = Button(label='Unfix', tooltip='Unfix selected vertices')

    reference_button = Button(label='Reference', tooltip=
    'Set the current shape as reference')

    color_view_check = Bool(False, label='Color')

    hk_view_check = Bool(True, label='H-K')

    k1k2_view_check = Bool(False, label='k1-k2')

    optimizer_values_check = Bool(False, label='Unknowns', tooltip=
    'Show values from unknowns vector')

    K_coeff = Float(0, label='a')

    H_coeff = Float(0, label='b')

    C_coeff = Float(0, label='c')

    linear_relation = Bool(True)

    # --------------------------------------------------------------------------
    #                              Component View
    # --------------------------------------------------------------------------

    view = View(
        VGroup(Group('alignment',
                     'fitting',
                     'reference_closeness',
                     'shape_preservation',
                     'isolines_parallel',
                     'control_fairness',
                     'gliding_boundary',
                     'boundary',
                     show_border=True,
                     label='Weights'),
               HGroup('K_coeff',
                      'H_coeff',
                      'C_coeff',
                      show_border=True,
                      label='Linear relation: aK + bH + c = 0'),
               VGroup(HGroup(Item('u_sampling', width=-100),
                             Item('v_sampling', show_label=False,
                                  width=-100), ),
                      HGroup(Item('u_points', width=-100),
                             Item('v_points', show_label=False,
                                  width=-100), ),
                      HGroup(Item('u_degree', width=-100),
                             Item('v_degree', show_label=False,
                                  width=-100), ),
                      HGroup('plot_samples_check',
                             '_',
                             Item('rebuild_button', show_label=False),
                             Item('resample_button', show_label=False),
                             ),
                      show_border=True,
                      label='B-spline'),
               VGroup(
                   HGroup('step', 'step_control',
                          show_border=True),
                   HGroup(Item('interactive',
                               tooltip='Interactive optimization',
                               show_label=False, ),
                          Item('_'),
                          'reinitialize',
                          'optimize',
                          show_labels=False,
                          show_border=True),
                   show_border=True,
                   label='Optimizer'),
               VGroup('geometric_error',
                      style='readonly',
                      label='errors [ mean | max ]',
                      show_border=True, ),
               show_border=True,
               show_labels=True),
        resizable=True,
    )

    # -------------------------------------------------------------------------
    #                                Attributes
    # -------------------------------------------------------------------------
    '''Define here all component standard attributes'''

    surface_lut = None

    optimizer = WsurfOptimizer()

    __reinitialize = False

    # -------------------------------------------------------------------------
    #                                 Properties
    # -------------------------------------------------------------------------

    @property
    def bspline(self):
        return self.geolab.current_object.geometry

    @property
    def current_object(self):
        return self.geolab.current_object

    # -------------------------------------------------------------------------
    #                            Special Methods
    # -------------------------------------------------------------------------
    '''These are overwriting of special methods, fired by geolab'''

    def geolab_settings(self):
        self.geolab.add_scene('3D')
        position = [0.010216647233753599, -1.1378681444403156,
                    4.796698057325836, 0.0, 1.0, 0.0, 0.010216647233753599,
                    -1.1378681444403156, 0.0, 50.0, 4.302506863495564,
                    5.430352877034375, False]
        self.geolab.add_scene('2D', interaction='locked',
                              position=position,
                              style='base')
        # self.geolab.add_scene('2D', position=position)
        self.geolab.height = 800
        self.geolab.width = 800
        self.geolab.side_width = 400

    def geolab_object_add(self):
        self.geolab.delete_selected_object()
        self.__reinitialize = True

    def geolab_object_added(self):
        obj = self.geolab.last_object
        bspline = obj.geometry
        self.optimizer.reset_scaling()
        P = bspline.number_of_control_points
        bspline.u_sampling = int(P[0] * 2)
        bspline.v_sampling = int(P[1] * 2)
        if self.__reinitialize:
            self.geolab.object_changed()
            self.__reinitialize = False
        
    def geolab_geometry_reset(self):
        P = self.bspline.number_of_control_points
        self.bspline.u_sampling = int(P[0] * 3)
        self.bspline.v_sampling = int(P[1] * 3)

    def geolab_object_change(self):
        self.current_object.surface_plot = 'color'

    def geolab_object_changed(self):
        if self.geolab.current_object is None:
            return
        self.optimizer.bspline = self.bspline
        self.current_object.update_size()
        self.u_degree = self.bspline.u_degree
        self.v_degree = self.bspline.v_degree
        P = self.bspline.number_of_control_points
        self.u_points = P[0]
        self.v_points = P[1]
        self.u_sampling = self.bspline.u_sampling
        self.v_sampling = self.bspline.v_sampling
        self.bspline.sampling = (self.u_sampling, self.v_sampling)
        P = self.bspline.points()
        self.surface_lut = uv_wheel_lut_table(P)
        self.optimizer.verbose = True
        self.geolab.current_object.update_size()
        self.optimizer.initialization()
        self.geolab.clear()
        self.initialize_bspline_plot_functions()
        self.plot_diagrams()
        self.plot_samples()
        self.plot_fixed_vertices()
        self.geolab.update_plot()

    def geolab_object_save(self, file_name):
        self.optimizer.resize_bspline()

    def geolab_object_saved(self, file_name):
        self.optimizer.unresize_bspline()

    def geolab_set_state(self, state):
        """Function called to set interactive states that should be
        switched off when other selections are enabled and vice-versa.
        Pre-set states - to do not use - are:
            - 'select_object'
            - 'split_edges':
            - 'collapse_edges':
            - 'move_vertices':
            - 'select_vertices':
            - 'select_faces':
            - 'select_edges':
            - 'select_boundary_vertices':
        """
        if state != 'bs-interactive':
            self.interactive = False

    def geolab_fix_vertices(self, selected):
        self.optimizer.fix_points(selected)

    def geolab_unfix_vertices(self, selected):
        self.optimizer.unfix_points(selected)

    def geolab_set_reference(self):
        self.optimizer.set_reference()

    # -------------------------------------------------------------------------
    #                              Plot Functions
    # -------------------------------------------------------------------------

    def initialize_bspline_plot_functions(self):
        obj = self.geolab.current_object

        def plot_surface_color():
            obj.plot_surface(color=self.surface_lut,
                             vertex_data=np.arange(len(self.surface_lut)))

        obj.add_surface_callback(plot_surface_color, name='surface rainbow')

        def plot_surface_hk_isolines():
            init = not self.optimizer_values_check
            if self.geolab.is_moving_vertex:
                K, H, k1, k2 = self.optimizer.bspline.curvatures()
            else:
                H = self.optimizer.mean(init)
                K = self.optimizer.gaussian(init)
            obj.plot_surface(vertex_data=H, color='r', iso_surface=True,
                             name='iso_h', tube_radius=0.2, shading=False)
            obj.plot_surface(vertex_data=K, color='b', iso_surface=True,
                             name='iso_k', tube_radius=0.2, shading=False)
            obj.plot_surface(color='w')

        obj.add_surface_callback(plot_surface_hk_isolines, name='HK isolines')

        def plot_surface_k1k2_isolines():
            init = not self.optimizer_values_check
            if self.geolab.is_moving_vertex:
                K, H, k1, k2 = self.optimizer.bspline.curvatures()
            else:
                k1, k2 = self.optimizer.principal_curvatures(init)
            obj.plot_surface(vertex_data=k1, color='cornflower',
                             iso_surface=True, name='iso_h', tube_radius=0.2,
                             shading=False)
            obj.plot_surface(vertex_data=k2, color='orange', iso_surface=True,
                             name='iso_k', tube_radius=0.2, shading=False)
            obj.plot_surface(color='w')

        obj.add_surface_callback(plot_surface_k1k2_isolines,
                                 name='k1-k2 isolines')

        obj.surface_plot = 'HK isolines'
        self.hk_view_check = True

    def plot_diagrams(self):

        def plot_diagrams_callback():
            init = not self.optimizer_values_check
            U = self.optimizer.bspline.u_sampling
            V = self.optimizer.bspline.v_sampling
            if self.geolab.is_moving_vertex:
                K, H, k1, k2 = self.optimizer.bspline.curvatures()
            else:
                k1, k2 = self.optimizer.principal_curvatures(init)
                H = self.optimizer.mean(init)
                K = self.optimizer.gaussian(init)
            Kmin = min(np.min(K), -0.05)
            Kmax = max(np.max(K), 0.05)
            Hmin = min(np.min(H), -0.05)
            Hmax = max(np.max(H), 0.05)
            k1min = min(np.min(k1), -0.05)
            k1max = max(np.max(k1), 0.05)
            k2min = min(np.min(k2), -0.05)
            k2max = max(np.max(k2), 0.05)
            cK = (Kmax + Kmin) / 2
            cH = (Hmax + Hmin) / 2
            ck1 = (k1max + k1min) / 2
            ck2 = (k2max + k2min) / 2
            Kc = K - cK
            Hc = H - cH
            k1c = k1 - ck1
            k2c = k2 - ck2
            Kn = np.max(abs(Kc))
            Hn = np.max(abs(Hc))
            k12n = max(np.max(np.abs(k1c)), np.max(np.abs(k2c)))
            HK = np.column_stack((Hc / Hn, Kc / Kn, np.zeros(U * V)))
            k1k2 = np.column_stack((k1c / k12n, k2c / k12n, np.zeros(U * V)))
            k1k2[:, 1] -= 2.2
            r = 0.012
            # C = [[-cH/Hn, -cK/Kn, 0],[-ck1/k12n, -ck2/k12n-2.2, 0]]
            Hax = (np.linspace(-10, 10, 201) - cH) / Hn
            Hax = Hax[Hax < 1.3]
            Hax = Hax[Hax > -1.3]
            Kax = (np.linspace(-10, 10, 201) - cK) / Kn
            Kax = Kax[Kax < 1.5]
            Kax = Kax[Kax > -1.2]
            Kax2 = (np.linspace(-10, 10, 2001) - cK) / Kn
            Kax2 = Kax2[Kax2 < 1.5]
            Kax2 = Kax2[Kax2 > -1.2]
            HKaxes = Axes(x=Hax, y=Kax, cx=-cH / Hn, cy=-cK / Kn)
            HKaxes2 = Axes(y=Kax2, cx=-cH / Hn, cy=-cK / Kn, d=0.01)
            k1ax = (np.linspace(-10, 10, 201) - ck1) / k12n
            k1ax = k1ax[k1ax < 1.3]
            k1ax = k1ax[k1ax > -1.3]
            k2ax = (np.linspace(-10, 10, 201) - ck2) / k12n - 2.2
            k2ax = k2ax[k2ax < -1.25]
            k2ax = k2ax[k2ax > -3.8]
            k1k2axes = Axes(x=k1ax, y=k2ax, cx=-ck1 / k12n, cy=-ck2 / k12n - 2.2)
            line = Polyline([[-3, -1.2, 0], [3, -1.2, 0]])
            self.geolab.plot_mesh_edges(HKaxes, color=(60, 60, 60), scene='2D',
                                        name='hk_axes')
            self.geolab.plot_mesh_edges(HKaxes2, color=(60, 60, 60), scene='2D',
                                        name='hk_axes2')
            self.geolab.plot_mesh_edges(k1k2axes, color=(60, 60, 60), scene='2D',
                                        name='k1k2_axes')

            self.geolab.plot_polyline(line, color=(240, 240, 240),
                                      line_width=6,
                                      scene='2D')
            if not self.plot_clusters_check:
                color = self.surface_lut
                self.geolab.plot_points(HK, radius=r,
                                        color=color,
                                        resolution=5,
                                        vertex_data=np.arange(len(HK)),
                                        shading=False,
                                        lut_range='-:+',
                                        scene='2D',
                                        name='HK')
                self.geolab.plot_points(k1k2, radius=r, color=color,
                                        resolution=5,
                                        vertex_data=np.arange(len(HK)),
                                        shading=False,
                                        lut_range='-:+',
                                        scene='2D',
                                        name='k1k2')
            else:
                data = self.optimizer.clusters
                self.geolab.plot_points(HK, radius=r,
                                        color='blue-red',
                                        resolution=5,
                                        vertex_data=data,
                                        shading=False,
                                        lut_range='-:+',
                                        scene='2D',
                                        name='HK')
                self.geolab.plot_points(k1k2,
                                        radius=r,
                                        color='blue-red',
                                        resolution=5,
                                        vertex_data=data,
                                        shading=False,
                                        lut_range='-:+',
                                        scene='2D',
                                        name='k1k2')

        self.geolab.current_object.add_plot_callback(plot_diagrams_callback)

    def plot_fixed_vertices(self):

        def plot_fixed_callback():
            v = self.optimizer.fixed_points
            self.geolab.current_object.plot_glyph(vertex_indices=v,
                                                  glyph_type='axes',
                                                  color='orange',
                                                  shading=False,
                                                  line_width=4,
                                                  scale_factor=0.3,
                                                  name='fixed')

        self.geolab.current_object.add_plot_callback(plot_fixed_callback)

    def plot_samples(self):

        def plot_samples_callback():
            if not self.plot_samples_check:
                self.geolab.current_object.remove('samples')
            else:
                P = self.bspline.points()
                self.geolab.current_object.plot_points(P,
                                                       color=self.surface_lut,
                                                       vertex_data=np.arange(len(P)),
                                                       lut_range='-:+',
                                                       radius=0.07,
                                                       shading=False,
                                                       name='samples')

        self.geolab.current_object.add_plot_callback(plot_samples_callback)

    @on_trait_change('plot_samples_check')
    def update_plot_fired(self):
        self.geolab.current_object.update_plot()

    # -------------------------------------------------------------------------
    #                              Settings
    # -------------------------------------------------------------------------

    def set_settings(self):
        self.optimizer.step_control = self.step_control
        self.optimizer.step = self.step
        self.optimizer.iterations = 1
        self.optimizer.epsilon = self.epsilon
        self.optimizer.step = self.step
        self.optimizer.include_boundary = self.boundary
        self.optimizer.linear_coefficients = (self.K_coeff, self.H_coeff,
                                              -self.C_coeff)
        self.optimizer.set_weight('linear_fitting', self.fitting)
        self.optimizer.set_weight('gliding', self.gliding_boundary)
        self.optimizer.set_weight('reference', self.reference_closeness)
        self.optimizer.set_weight('control_lengths', self.shape_preservation)
        self.optimizer.set_weight('hk', self.alignment)
        self.optimizer.set_weight('control_fairness', self.control_fairness)
        self.optimizer.set_weight('isolines_parallel', self.isolines_parallel)
        self.optimizer.adaptive_curve = False

    # -------------------------------------------------------------------------
    #                              Optimization
    # -------------------------------------------------------------------------

    def optimization_step(self):
        if not self.interactive:
            self.geolab.set_state(None)
        self.set_settings()
        self.optimizer.optimize()
        self.print_error()
        if True:
            if self.optimizer.geometric_error()[1] > 1:
                self.optimizer.reinitialize()
        self.current_object.update_plot()

    def print_error(self):
        self.geometric_error = self.optimizer.geometric_error_string()

    @on_trait_change('optimize')
    def optimize_fired(self):
        self.current_object.iterate(self.optimization_step, self.iterations)

    @on_trait_change('interactive')
    def interactive_optimize_fired(self):
        self.geolab.set_state('bs-interactive')
        if self.interactive:
            def start():
                self.optimizer.handle = self.current_object.selected_vertices

            def interact():
                self.current_object.iterate(self.optimization_step, 1)

            def end():
                self.current_object.iterate(self.optimization_step, 5)

            self.current_object.move_vertices(interact, start, end)
        else:
            self.optimizer.handle = None
            self.current_object.move_vertices_off()

    @on_trait_change('reinitialize')
    def reinitialize_fired(self):
        self.set_settings()
        self.optimizer.reinitialization()
        self.print_error()
        self.current_object.update_plot()

    # -------------------------------------------------------------------------
    #                              Traits
    # -------------------------------------------------------------------------

    @on_trait_change('rebuild_button')
    def rebuild_fired(self):
        if self.u_sampling < self.u_points:
            self.u_sampling = self.u_points + 1
        if self.v_sampling < self.v_points:
            self.v_sampling = self.v_points + 1
        self.bspline.u_sampling = self.u_sampling
        self.bspline.v_sampling = self.v_sampling
        self.bspline.rebuild(self.u_degree, self.v_degree, self.u_points,
                             self.v_points)
        self.geolab.object_changed()
        self.geolab.current_object.update_plot()

    @on_trait_change('resample_button')
    def resample_fired(self):
        self.bspline.u_sampling = self.u_sampling
        self.bspline.v_sampling = self.v_sampling
        self.geolab.object_changed()
        self.geolab.current_object.update_plot()

    def set_plot_state(self, state=None):
        if state != 'color':
            self.color_view_check = False
        if state != 'hk':
            self.hk_view_check = False
        if state != 'k1k2':
            self.k1k2_view_check = False

    @on_trait_change('color_view_check')
    def color_view_fired(self):
        if self.color_view_check:
            self.set_plot_state('color')
            self.geolab.current_object.surface_plot = 'surface rainbow'

    @on_trait_change('hk_view_check')
    def hk_view_fired(self):
        if self.hk_view_check:
            self.set_plot_state('hk')
            self.geolab.current_object.surface_plot = 'HK isolines'

    @on_trait_change('k1k2_view_check')
    def k1k2_view_fired(self):
        if self.k1k2_view_check:
            self.set_plot_state('k1k2')
            self.geolab.current_object.surface_plot = 'k1-k2 isolines'

    @on_trait_change('optimizer_values_check')
    def optimizer_values_fired(self):
        self.geolab.current_object.update_plot()

    @on_trait_change('scale')
    def scale_fired(self):
        self.optimizer.scale = self.scale
        self.current_object.update_size()
        self.optimizer.reinitialization()
        self.geolab.set_state(None)
        self.current_object.update_plot()


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class Axes(object):

    def __init__(self, x=[], y=[], cx=0, cy=0, d=0.03):
        self.d = d
        E = len(x) + len(y)
        self._Nx = len(x)
        self._Ny = len(y)
        self.V = E * 2
        self.E = E
        nx = len(x)
        ny = len(y)
        Xm = np.column_stack((x, np.repeat(cy - self.d, nx), np.zeros(nx)))
        Xp = np.column_stack((x, np.repeat(cy + self.d, nx), np.zeros(nx)))
        Ym = np.column_stack((np.repeat(cx - self.d, ny), y, np.zeros(ny)))
        Yp = np.column_stack((np.repeat(cx + self.d, ny), y, np.zeros(ny)))
        self.vertices = np.vstack((Xm, Ym, Xp, Yp))

    def edge_vertices(self):
        x = np.arange(self._Nx)
        y = np.arange(self._Ny) + self._Nx
        v1 = np.hstack((x, y))
        v2 = v1 + self.E
        return v1, v2


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


def WsurfGUI(file_name=None):

    from wsurf.geolab.gui.geolabgui import GeolabGUI

    component = WeingartenGUI()

    GUI = GeolabGUI()

    GUI.add_component(component)

    if file_name is not None:
        GUI.open_obj_file(file_name)

    GUI.start()
