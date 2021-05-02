#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import absolute_import

from __future__ import print_function

from __future__ import division

# -----------------------------------------------------------------------------

from wsurf.geolab.plotter.plotmanager import PlotManager

from wsurf.geolab.gui.geolabbsplinesurface import GeolabBSplineSurface

# -----------------------------------------------------------------------------

'''plotmanager.py: The scene manager class'''

__author__ = 'Davide Pellis'

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#                                Scene Manager
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class SceneManager(PlotManager):

    def __init__(self, scene_model=None):
        PlotManager.__init__(self, scene_model)

        self._objects = {}

        self._selected = None

        self._last_object = None

        self._counter = 0

        self._handler = None

        self._geometry_change_callbacks = []

        self._object_changed_callbacks = []

        self._object_change_callbacks = []

        self._object_save_callbacks = []

        self._object_saved_callbacks = []

        self._object_added_callbacks = []

        self._object_add_callbacks = []

    # -------------------------------------------------------------------------
    #                                Properties
    # -------------------------------------------------------------------------

    @property
    def scene_model(self):
        return self._scene_model

    @scene_model.setter
    def scene_model(self, scene_model):
        self._scene_model = scene_model
        self._scene = scene_model.mayavi_scene
        for obj in self._objects:
            obj.scene_model = scene_model

    @property
    def current_object(self):
        if self._selected is None:
            try:
                return self._objects[self._objects.keys()[0]]
            except:
                return None
        try:
            return self._objects[self._selected]
        except:
            self._selected = None
            return self.current_object

    @property
    def objects(self):
        return self._objects[self._selected]

    @property
    def last_object(self):
        if self._last_object is None:
            try:
                return self._objects[self._objects.keys()[0]]
            except:
                return None
        try:
            return self._objects[self._last_object]
        except:
            self._last_object = None
            return self.last_object

    @property
    def engine(self):
        return self._scene_model.engine

    #--------------------------------------------------------------------------

    def add_callback(self, key, callback):
        if key == 'object_change':
            self._object_change_callbacks.append(callback)
        elif key == 'object_changed':
            self._object_changed_callbacks.append(callback)
        elif key == 'object_save':
            self._object_save_callbacks.append(callback)
        elif key == 'object_saved':
            self._object_saved_callbacks.append(callback)
        elif key == 'object_added':
            self._object_added_callbacks.append(callback)
        elif key == 'object_add':
            self._object_add_callbacks.append(callback)

    def object_changed(self):
        for callback in self._object_changed_callbacks:
            try:
                callback()
            except:
                pass

    def object_change(self):
        for callback in self._object_change_callbacks:
            try:
                callback()
            except:
                pass

    def object_save(self, file_name):
        for callback in self._object_save_callbacks:
            try:
                callback(file_name)
            except:
                pass

    def object_saved(self, file_name):
        for callback in self._object_saved_callbacks:
            try:
                callback(file_name)
            except:
                pass

    def object_added(self):
        for callback in self._object_added_callbacks:
            try:
                callback()
            except:
                pass

    def object_add(self):
        for callback in self._object_add_callbacks:
            try:
                callback()
            except:
                pass

    # -------------------------------------------------------------------------
    #                            Get from pipeline
    # -------------------------------------------------------------------------

    def update(self, **kwargs):
        obj = kwargs.get('object', None)
        if obj is not None:
            self._objects[obj].update(**kwargs)
        else:
            PlotManager.update(self, **kwargs)

    def clear(self):
        for key in self._objects:
            self._objects[key].clear()
        PlotManager.clear(self)

    def clear_scene(self):
        for scene in self.engine.scenes:
           if scene != self.scene_model:
               scene.remove()

    def add_object(self, geometry, name=None):
        self.object_add()
        if geometry.type == 'Bspline_Surface':
            GP = GeolabBSplineSurface(self.scene_model)
            GP.geometry = geometry
            obj = GP
        if name is not None:
            obj.name = name
        else:
            obj.name = 'obj_{}'.format(self._counter)
            self._counter += 1
        if len(self._objects) == 0:
            self._selected = obj.name
        self._last_object = obj.name
        self.remove(obj.name)
        self._objects[obj.name] = obj
        obj.scene_model = self.scene_model
        self.object_added()

    def remove(self, names=None):
        if names is None:
            if self._selected is None:
                names = [self._objects.keys()[0]]
            else:
                names = [str(self._selected)]
        if type(names) is str:
            names = [names]
        for key in names:
            try:
                self._objects[key].clear()
                del self._objects[key]
                self._selected = None
            except:
                pass
        PlotManager.remove(self, names)

    def core_plot(self):
        PlotManager.core_plot(self)
        for key in self._objects:
            obj = self._objects[key]
            obj.update_plot()

    def hide(self, **kwargs):
        name = kwargs.get('name', None)
        if name is None:
            super(SceneManager, self).hide()
            for key in self._objects:
                try:
                    self._objects[key].hide()
                except:
                    pass
        else:
            obj = kwargs.get('object', None)
            if obj is not None:
                self._objects[obj].hide(**kwargs)
            else:
                PlotManager.hide(self, **kwargs)

    def get_object(self, name):
        try:
            obj = self._objects[name]
        except:
            obj = None
        return obj

    # -------------------------------------------------------------------------
    #                                 Record
    # -------------------------------------------------------------------------

    def shoot(self, kink=False):
        for key in self._objects:
            obj = self._objects[key]
            obj.shoot(kink)

    def interpolate_frames(self, N, key_frames_number):
        for key in self._objects:
            obj = self._objects[key]
            obj.interpolate_frames(N, key_frames_number)

    def clear_records(self):
        for key in self._objects:
            obj = self._objects[key]
            obj.clear_records()

    def plot_frame(self, frame_number):
        for key in self._objects:
            obj = self._objects[key]
            obj.plot_frame(frame_number)

    def plot_key_frame(self, key_number):
        for key in self._objects:
            obj = self._objects[key]
            obj.plot_key_frame(key_number)

    # -------------------------------------------------------------------------
    #                                  Selection
    # -------------------------------------------------------------------------

    def select_object(self):
        if self.current_object == None:
            return
        self.current_object.highlight()
        ranges = {}
        count = 0
        for key in self._objects:
            obj = self._objects[key]
            N = obj.selection_on()
            ranges[key] = [count, count+N]
            count += N
        def picker_callback(picker):
            pick_id = picker.cell_id
            if pick_id >= 0:
                for key in self._objects:
                    try:
                        obj = self._objects[key]
                        if picker.actor in obj.object_selection_actors:
                            if key != self._selected:
                                self.current_object.highlight_off()
                                self.object_change()
                                self._selected = key
                                self.object_changed()
                                self.current_object.highlight()
                    except IndexError:
                        pass
        s = self.engine.current_scene
        p = s._mouse_pick_dispatcher.callbacks
        if len(p) == 0:
            s.on_mouse_pick(picker_callback,'cell')
        else:
            p[0] = (picker_callback,'cell','Left')
        a = s._mouse_pick_dispatcher._active_pickers['cell']
        a.tolerance = self.picker_tolerance


    def select_off(self):
        for key in self._objects:
            obj = self._objects[key]
            obj.select_off()
            try:
                obj.hilight_off()
            except:
                pass
        scene = self.engine.current_scene
        p = scene._mouse_pick_dispatcher.callbacks
        def picker_callback(picker):
            return
        for i in range(len(p)):
            p[i] = (picker_callback,'cell','Left')