# -*- coding: utf-8 -*-
""" Scrutinizer: Cmd """

import os
from distutils import log

from . import Scrutinizer, ScrutinizerConfigError, ScrutinizerRunError


def validate_configuration(cfg):
    """ Validate configuration. """


class CmdScrutinizer(Scrutinizer):
    """ Cmd scrutinizer
        An example of how to implement a scrutinizer.
    """

    name = 'Command'

    description = "Execute an individual command"

    user_options = [
        ("cmd=", None, "Run this command"),
        ("time", None, "Measure execution time"),
    ]


    def initialize_options(self):
        """ Initialize object, really.
            Create the attributes and apply defaults, when available.
        """
        self.time = False
        self.cmd = None


    def finalize_options(self):
        """ Apply the configuration and prepare for running. """

        self.time = False
        log.debug("config: %s", self.config)
        self.cmd = self.config.get('cmd', None)


    def run(self):
        """ Run """

        if self.verbose:
            log.debug("Running command: '%s'", self.cmd)
        res = os.system(self.cmd)
        if self.verbose:
            log.debug("Command returned (code): '%d'", res)
