# -*- coding: utf-8 -*-
from .attributable import Attributable

import logging
# create logger
logger = logging.getLogger(__name__)
#logger.debug('level %d' %  (logger.getEffectiveLevel()))


class AttributableMeta(Attributable):
    """ Attributes are also meta data. """

    def __init__(self, meta=None, **kwds):

        super(Attributable, self).__init__(meta=meta, **kwds)
