

from __future__ import absolute_import

from __future__ import print_function

from __future__ import division

#------------------------------------------------------------------------------

from traits.api import HasTraits

#------------------------------------------------------------------------------

__author__ = 'Davide Pellis'


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#                                  Component
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class GeolabComponent(HasTraits):

    name = 'component'

    def __init__(self):
        HasTraits.__init__(self)
        self.__geolab = None

    @property
    def geolab(self):
        return self.__geolab

    @geolab.setter
    def geolab(self, geolab):
        self.__geolab = geolab
        self.__geolab.add_callback('object_change', self.geolab_object_change)
        self.__geolab.add_callback('object_changed', self.geolab_object_changed)
        self.__geolab.add_callback('object_save', self.geolab_object_save)
        self.__geolab.add_callback('object_saved', self.geolab_object_saved)
        self.__geolab.add_callback('object_added', self.geolab_object_added)
        self.__geolab.add_callback('object_add', self.geolab_object_add)

        #self.__geolab.handler.add_state_callback(self.geolab_set_state)

    #@property
    #def handler(self):
        #return self.geolab.handler

    def geolab_settings(self):
        pass

    def initialize_plot(self):
        pass

    def geolab_set_state(self, name):
        pass

    def geolab_object_change(self):
        pass

    def geolab_object_changed(self):
        pass

    def geolab_object_save(self, file_name):
        pass

    def geolab_object_saved(self, file_name):
        pass

    def geolab_object_added(self):
        pass

    def geolab_object_add(self):
        pass
    
    def geolab_closing(self):
        pass





