# -*- coding: utf-8 -*-

from __future__ import absolute_import

from __future__ import print_function

from __future__ import division

from traits.api import HasTraits, Instance, on_trait_change, Int

from traitsui.api import View, Item

from tvtk.pyface.scene_editor import SceneEditor

from mayavi.tools.mlab_scene_model import MlabSceneModel

from pyface.image_resource import ImageResource

# -----------------------------------------------------------------------------

from wsurf.geolab import utilities

from wsurf.geolab.plotter.geolabscene import GeolabScene

from wsurf.geolab.plotter.plotmanager import PlotManager

# -----------------------------------------------------------------------------

'''viewer.py: The viewer for plotter souce classes'''

__author__ = 'Davide Pellis'

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#                                    Viewer
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class Viewer(HasTraits):

    # -------------------------------------------------------------------------
    #                                  Traits
    # -------------------------------------------------------------------------

    scene = Instance(MlabSceneModel, ())

    editor = SceneEditor(scene_class=GeolabScene)

    # -------------------------------------------------------------------------
    #                                 Initialize
    # -------------------------------------------------------------------------

    def __init__(self, objects, **kwargs):
        HasTraits.__init__(self)

        self._plotmanager = PlotManager(scene_model=self.scene)

        self._generate_data(objects)

        self._size = kwargs.get('size', (800, 800))

        self._position = kwargs.get('position', None)

        self._background = kwargs.get('background', None)

        self._resizable = kwargs.get('resizable', True)
        
        self.magnification = kwargs.get('magnification', 4)

    @property
    def position(self):
        return self.scene._position

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, background):
        self._background = background

    # -------------------------------------------------------------------------
    #                                 Methods
    # -------------------------------------------------------------------------

    def start(self):

        view = View(Item('scene',
                         editor=SceneEditor(scene_class=GeolabScene),
                         show_label=False,
                         resizable=self._resizable,
                         height=self._size[1],
                         width=self._size[0],
                         ),
                    resizable=self._resizable,
                    title='GeoLab viewer',
                    icon=ImageResource('../icons/geolab_logo.png')
                    )

        self.configure_traits(view=view)

    def _generate_data(self, objects):
        self._plotmanager.add(objects, rename=True)
        
    @on_trait_change('scene.activated')
    def _scene_settings(self):
        if self._position is not None:
            self._plotmanager.set_view(self._position)
        if self.background is not None:
            self._plotmanager.background = self._background
        self.scene.magnification = self.magnification

# -----------------------------------------------------------------------------
#                                 View Function
# -----------------------------------------------------------------------------

def view(objects, **kwargs):
    viewer = Viewer(objects, **kwargs)
    viewer.start()
    
# -----------------------------------------------------------------------------
#                                 Save Function
# -----------------------------------------------------------------------------
