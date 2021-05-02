#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import absolute_import

from __future__ import print_function

from __future__ import division

import numpy as np

from traits.api import HasTraits, Instance, Property, Enum, Button, String,\
                       on_trait_change, Float, Bool, Int,Constant, ReadOnly,\
                       List, Array, Range, File, observe

from traitsui.api import View, Item, HSplit, VSplit, InstanceEditor, HGroup,\
                         Group, ListEditor, Tabbed, VGroup, CheckListEditor,\
                         ArrayEditor, Action, ToolBar, Separator, Controller,\
                         FileEditor, RangeEditor

from pyface.image_resource import ImageResource

# -----------------------------------------------------------------------------

'''check.py: an interactive checker for mesh connectivity and normals'''

__author__ = 'Davide Pellis'


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#                                Tools Handler
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class T_Handler(Controller):

    def close(self, info, is_ok):
        info.object._closed = True
        Controller.close(self ,info, is_ok)
        return True


class Tool(HasTraits):

    def __init__(self):
        HasTraits.__init__(self)
        self._scenemanager = None

    @property
    def current_object(self):
        return self._scenemanager.current_object

    @property
    def geometry(self):
        return self._scenemanager.current_object.geometry

    @property
    def mesh(self):
        return self._scenemanager.current_object.geometry

    @property
    def meshmanager(self):
        if self._scenemanager.current_object.type != 'Mesh_plot_manager':
            return None
        return self._scenemanager.current_object

    @property
    def scenemanager(self):
        return self._scenemanager

    @property
    def geolab(self):
        return self._scenemanager

    @scenemanager.setter
    def scenemanager(self, scene_manager):
        self._scenemanager = scene_manager

    def close(self):
        try:
            self._closed = True
            self._handler.info.ui.dispose()
        except:
            pass


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#                                    B-spline
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class BsplineRebuilder(Tool):

    _closed = Bool(True)

    _handler = T_Handler()

    u_sampling = Int(0, label='sampling (U,V)')

    v_sampling = Int(0)

    u_degree = Int(0, label='degree (U,V)')

    v_degree = Int(0)

    u_points = Int(0, label='points (U,V)')

    v_points = Int(0)

    rebuild_button = Button(label='Rebuild')

    resample_button = Button(label='Resample')

    error_string = String('0', label='Deviation')

    view = View(VGroup(HGroup(Item('u_sampling', width=-100),
                                    Item('v_sampling', show_label=False,
                                         width=-100),),
                       HGroup(Item('u_points', width=-100),
                                    Item('v_points', show_label=False,
                                         width=-100),),
                       HGroup(Item('u_degree', width=-100),
                                    Item('v_degree', show_label=False,
                                         width=-100),),
                       HGroup(Item('rebuild_button', show_label=False),
                              Item('resample_button', show_label=False),
                              #'_',
                              #Item('error_string', style='readonly'),
                              ),
                       show_border=True),
                title='B-spline rebuilder',
                handler=_handler,
                width=350,
                icon=ImageResource('../icons/bspline_rebuild.png'))

    @property
    def bspline(self):
        return self.scenemanager.current_object.geometry


    def start(self):
        if not self._closed:
            self._handler.info.ui.dispose()
        if self.bspline.type != 'Bspline_Surface':
            return
        self.u_sampling = self.bspline.u_sampling
        self.v_sampling = self.bspline.v_sampling
        self.u_degree = self.bspline.u_degree
        self.v_degree = self.bspline.v_degree
        P = self.bspline.number_of_control_points
        self.u_points = P[0]
        self.v_points = P[1]
        self._closed = False
        self.configure_traits()

    @on_trait_change('rebuild_button')
    def rebuild_fired(self):
        self.bspline.rebuild(self.u_degree, self.v_degree, self.u_points,
                             self.v_points)
        self.scenemanager.object_changed()
        self.scenemanager.current_object.update_plot()

    @on_trait_change('resample_button')
    def resample_fired(self):
        self.bspline.u_sampling = self.u_sampling
        self.bspline.v_sampling = self.v_sampling
        self.scenemanager.object_changed()
        self.scenemanager.current_object.update_plot()

    @on_trait_change('update_button')
    def update_fired(self):
        self.scenemanager.update_plot()
        self.scenemanager.current_object.update_plot()


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#                                      Loads
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class Loads(Tool):

    _closed = Bool(True)

    _handler = T_Handler()

    area_load = Float(0, label='Area load')

    beam_load = Float(1, label='Beam load')

    vector = Array(np.float, (1, 3), editor=ArrayEditor(width=20))

    apply_force = Button(label='Apply force')

    reset_forces = Button(label='Reset forces')

    view = View(VGroup('area_load',
                       'beam_load',
                       'vector',
                       HGroup(
                              Item('apply_force',
                                   show_label=False,
                                   resizable=True),
                              Item('reset_forces',
                                   show_label=False,
                                   resizable=True),
                              ),
                       show_border=True),
                title='Loads',
                handler=_handler,
                width=300,
                icon=ImageResource('../icons/applyforce.png'))

    def start(self):
        if not self._closed:
            self._handler.info.ui.dispose()
        self.area_load = self.mesh.area_load
        self.beam_load = self.mesh.beam_load
        self.configure_traits()
        self._closed = False
        self.meshmanager.hide('forces')
        self.plot_loads()

    @on_trait_change('_closed')
    def hide_loads(self):
        self.meshmanager.hide('apply_loads')
        self.meshmanager.update_plot()

    @on_trait_change('area_load')
    def update_area_load(self):
        self.mesh.area_load = self.area_load
        self.plot_loads()

    @on_trait_change('beam_load')
    def update_beam_load(self):
        self.mesh.beam_load = self.beam_load
        self.plot_loads()

    @on_trait_change('apply_force')
    def apply_force_fired(self):
        selected = self.meshmanager.selected_vertices
        self.mesh.apply_force(self.vector[0,:], selected)
        self.plot_loads()

    @on_trait_change('reset_forces')
    def reset_forces_fired(self):
        self.mesh.reset_forces()
        self.plot_loads()

    def plot_loads(self):
        self.meshmanager.plot_vectors(vectors = self.mesh.loads(),
                                      color = 'blue-red',
                                      glyph_type = '3D-arrow',
                                      position = 'head',
                                      name = 'apply_loads')


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#                              Incremental Remesh
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

    def start(self):
        if not self._closed:
            self._handler.info.ui.dispose()
        self.configure_traits()
        self._closed = False

    @on_trait_change('corner_tolerance')
    def set_corner_tolerance(self):
        self.mesh.corner_tolerance = self.corner_tolerance

    @on_trait_change('remesh_button')
    def incremental_remesh(self):
        if self.meshmanager is not None:
            self.mesh.incremental_remesh(self.remesh_factor)
            self.geolab.fix_edges_bug()
            self.meshmanager.update_plot()
            self.geolab.object_changed()


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#                              Corner Tolerance
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class CornerTolerance(Tool):

    corner_tolerance = Range(0.0, 1.0, 0.3)

    _closed = Bool(True)

    _handler = T_Handler()

    view = View(Group(Item('corner_tolerance',
                            editor = RangeEditor(mode='slider'),),
                      show_border=True),
                title='Set corner tolerance',
                handler=_handler,
                icon=ImageResource('../icons/corners.png'))


    @property
    def scenemanager(self):
        return self._scenemanager

    @scenemanager.setter
    def scenemanager(self, scene_manager):
        self._scenemanager = scene_manager
        ct = (scene_manager.current_object.mesh.corner_tolerance + 1)/2
        self.corner_tolerance = ct

    def start(self):
        if not self._closed:
            self._handler.info.ui.dispose()
        self.configure_traits()
        self._closed = False
        self.plot_corners()
        self.scenemanager.current_object.add_plot_callback(self.plot_corners,
                                                           name='corners')

    def close(self):
        try:
            self._closed = True
            self._handler.info.ui.dispose()
        except:
            pass

    @on_trait_change('corner_tolerance')
    def set_corner_tolerance(self):
        self.mesh.corner_tolerance = self.corner_tolerance*2 - 1
        self.plot_corners()

    @on_trait_change('_closed')
    def hide_corners(self):
        self.scenemanager.current_object.hide('corners')
        self.scenemanager.current_object.remove_plot_callback('corners')

    def plot_corners(self):
        corners = self.mesh.mesh_corners()
        r = self.scenemanager.current_object.r
        self.scenemanager.current_object.plot_glyph(vertex_indices=corners,
                                                  glyph_type = 'sphere',
                                                  radius=2.2*r,
                                                  color='g',
                                                  name='corners')


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#                                   Save Mesh
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

class S_Handler(Controller):

    def close(self, info, is_ok):
        info.object._closed = True
        if info.initialized:
            info.object.current_object.highlight_off()
        Controller.close(self ,info, is_ok)
        return True


class SaveGeometry(Tool):

    _closed = Bool(True)

    _handler = S_Handler()

    label = String('opt')

    save_button = Button(label='Save')

    view = View(HGroup('label',
                       Item('save_button',
                            show_label=False),
                       show_border=True),
                title='Save geometry',
                handler=_handler,
                icon=ImageResource('../icons/save.png'))

    def start(self):
        if not self._closed:
            self._handler.info.ui.dispose()
        self.configure_traits()
        self._closed = False
        self.current_object.highlight()

    def close(self):     
        try:
            self._closed = True
            self._handler.info.ui.dispose()
        except:
            pass

    @observe('save_button')
    def save_file(self, event):
        name = ('{}_{}').format(self.geometry.name, self.label)
        self.scenemanager.object_save(None)
        path = self.geometry.make_obj_file(name)
        self.current_object.highlight_off()
        self.scenemanager.object_saved(path)
        self.close()




