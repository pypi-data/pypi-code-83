#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import absolute_import

from __future__ import print_function

from __future__ import division

import numpy as np

from pyface.image_resource import ImageResource

from traits.api import HasTraits, Instance, Property, Enum, Button,String,\
                       on_trait_change, Float, Bool, Int,Constant, ReadOnly,\
                       List, Array, Range, Str, Color

from traitsui.api import View, Item, HSplit, VSplit, InstanceEditor, HGroup,\
                         Group, ListEditor, Tabbed, VGroup, CheckListEditor,\
                         ArrayEditor, Action, ToolBar, Separator,EnumEditor,\
                         ListStrEditor, ColorEditor, Controller

#------------------------------------------------------------------------------

from wsurf.geolab.plotter.bsplinesurfaceplotmanager import BsplineSurfacePlotManager

#------------------------------------------------------------------------------

__author__ = 'Davide Pellis'

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#                               Geolab Mesh
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class GMHandler(Controller):

    def close(self, info, is_ok):
        info.object._closed = True
        Controller.close(self, info, is_ok)
        return True


class GeolabBSplineSurface(BsplineSurfacePlotManager):

    _handler = GMHandler()

    _closed = Bool(True)

    plot_scale = Range(-10, 10, 0)

    surface_glossy_range = Range(0., 1., 0.5)

    control_color_select = Color((10, 10, 10), width=20, label='control_color')

    surface_color_select = Color((122, 163, 230), width=20, label='surface_color')

    control_plot = Str('wireframe', label='Control polygon')

    control_callbacks = ['color', 'wireframe', 'none']

    surface_plot = Str('color', label='Surface')

    surface_callbacks = ['color', 'gaussian curv.', 'mean curv.', 'none']

    surface_data_range = Range(0.00, 1.00, 0.80)

    show_edge_legend = Bool(False, label='legend')

    show_face_legend = Bool(False, label='legend')

    view = View(
                VGroup(VGroup(
                       Item('plot_scale',
                            resizable=True),
                       show_border=True),
                       VGroup(
                       HGroup(VGroup(Item('control_plot',
                                          resizable=True,
                                          editor=CheckListEditor(values=
                                                          control_callbacks),),
                                     Item('surface_plot',
                                          resizable=True,
                                          editor=CheckListEditor(values=
                                                          surface_callbacks),),
                                     ),
                              VGroup(Item('control_color_select',
                                          show_label=False,
                                          resizable=False,
                                          enabled_when='control_plot == "color"',
                                          editor=ColorEditor(),),
                                     Item('surface_color_select',
                                          show_label=False,
                                          resizable=False,
                                          enabled_when='surface_plot == "color"',
                                          editor=ColorEditor(),),
                                     ),
                              VGroup('show_edge_legend',
                                     '_',
                                     'show_face_legend',
                                     ),
                               ),
                       show_border=True),
                       VGroup(
                       HGroup(Item('surface_glossy_range',
                                   resizable=True),
                              ),
                       HGroup(Item('surface_data_range',
                                   resizable=True),
                               ),
                       show_border=True),
                       show_border=True),
                handler=_handler,
                title='B-spline surface plot settings',
                icon=ImageResource('../icons/plotmanager.png'),)

    def __init__(self, *args):
        BsplineSurfacePlotManager.__init__(self, *args)

        self._control_callbacks = {'color': self.plot_plain_edges,
                                'wireframe': self.plot_wireframe_control_polygon,
                                'none': self.hide_control_polygon}

        self._surface_callbacks = {'color': self.plot_plain_surface,
                                'gaussian curv.': self.plot_gaussian_curvature,
                                'mean curv.': self.plot_mean_curvature,
                                'none': self.hide_surface}

    def start(self):
        if not self._closed:
            pass
            self._handler.info.ui.dispose()
        self.configure_traits()
        self._closed = False

    def close(self):
        try:
            self._closed = True
            self._handler.info.ui.dispose()
        except:
            pass

    #--------------------------------------------------------------------------
    #                                    Plot
    #--------------------------------------------------------------------------

    def add_surface_callback(self, callback, name):
        self._surface_callbacks[name] = callback
        if name not in self.surface_callbacks:
            self.surface_callbacks.append(name)

    def add_edge_callback(self, callback, name):
        self._edge_callbacks[name] = callback
        if name not in self.edge_callbacks:
            self.edge_callbacks.append(name)

    @on_trait_change('control_plot')
    def edge_plot_change(self):
        self.remove_control_polygon()
        self.remove_edge_sources()
        self.update_plot()

    @on_trait_change('surface_plot, smooth_surface')
    def face_plot_changed(self):
        self.remove_surface()
        self.remove_face_sources()
        self.update_plot()

    def core_plot(self, **kwargs):
        control_plot = self._control_callbacks[self.control_plot]
        control_plot()
        surface_plot = self._surface_callbacks[self.surface_plot]
        surface_plot()
        self.make_face_legend()
        BsplineSurfacePlotManager.core_plot(self)


    #--------------------------------------------------------------------------
    #                             Predefined Plots
    #--------------------------------------------------------------------------

    def plot_plain_edges(self):
        self.plot_control_polygon()

    def plot_wireframe_control_polygon(self):
        self.plot_control_polygon(color='k', tube_radius=None)

    def plot_plain_surface(self):
        self.plot_surface(glossy=self.surface_glossy_range)

    def plot_gaussian_curvature(self):
        K, H, k1, k2 = self.bspline.curvatures()
        vertex_data = K
        val = np.max(np.abs(vertex_data)) * self.surface_data_range
        self.plot_surface(vertex_data = vertex_data,
                          glossy=self.surface_glossy_range,
                          color='turbo',
                          lut_range=[-val, val])

    def plot_mean_curvature(self):
        K, H, k1, k2 = self.bspline.curvatures()
        vertex_data = H
        val = np.max(np.abs(vertex_data)) * self.surface_data_range
        self.plot_surface(vertex_data=vertex_data,
                          glossy=self.surface_glossy_range,
                          color='turbo',
                          lut_range=[-val, val])

    @on_trait_change('show_face_legend')
    def make_face_legend(self):
        try:
            if self.show_face_legend:
                self.get_source('faces').show_legend(label=self.face_plot)
            else:
                self.get_source('faces').hide_legend()
        except:
            pass

    # -------------------------------------------------------------------------
    #                                 Select
    # -------------------------------------------------------------------------

    def select_off(self):
        super(GeolabBSplineSurface, self).select_off()

    # -------------------------------------------------------------------------
    #                                 Scales
    # -------------------------------------------------------------------------

    @on_trait_change('surface_data_range, surface_glossy_range')
    def plot_updated(self):
        self.update_plot()

    @on_trait_change('plot_scale')
    def set_scale(self):
        #self.handler.set_state(None)
        self.scale = 4**(0.1*self.plot_scale)
        self.glyph_scale = 4**(0.1*self.plot_scale)
        self.update_plot()

    @on_trait_change('surface_color_select, control_color_select')
    def set_color(self):
        ec = self.control_color_select.getRgb()
        fc = self.surface_color_select.getRgb()
        self.control_color = (ec[0], ec[1], ec[2])
        self.surface_color = (fc[0], fc[1], fc[2])
        self.update_plot()
