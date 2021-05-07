# -*- coding: utf-8 -*-
""" Scrutinize setuptools command plugin. """

from typing import Final
import os
import sys
import setuptools
import configparser
import importlib.util
from distutils import log
from distutils.errors import DistutilsOptionError, DistutilsSetupError, DistutilsError

from setuptools_scrutinize import ScrutinizerConfigError, ScrutinizerRunError

SETUP_CONFIG_OPTION: Final[str] = 'scrutinize_config'
DEFAULT_CONFIG_FILEPATH: Final[str] = '.scrutinize'
CONFIG_SECTION: Final[str] = 'scrutinize'

def known_scrutinizers():
    return {
            'pylint': {
                'module': 'setuptools_scrutinize.pylint',
                'class': 'PylintScrutinizer',
                },
            'cmd': {
                'module': 'setuptools_scrutinize.cmd',
                'class': 'CmdScrutinizer',
                },
            }


def validate_config_file_exists(dist, attr, value):
    """ Validate the configuration file exists. """

    if not os.path.exists(value):
        raise DistutilsSetupError("Cannot find Scrutinize configuration file '%s'" % value)


class DistutilsCheckError(DistutilsError):
    pass


class Scrutinize(setuptools.Command):

    description = "Run scrutinizing quality assurance"

    user_options = [
            ('list', 'l', "List scrutinizers"),
            # ('lint-config', None, "Check that Scurinize configuration file is valid"),
            # ('lint-output=', None, "output report into this file"),
            ('config=', None, "Scrutinize configuration file, default: '" +
                                DEFAULT_CONFIG_FILEPATH +
                                "'. In setup.cfg/setup.py, use option '"  + SETUP_CONFIG_OPTION +
                                "'."),
            ]


    def initialize_options(self):
        self.list = None
        self.lint_config = None
        self.config = DEFAULT_CONFIG_FILEPATH if DEFAULT_CONFIG_FILEPATH else self.distribution.scrutinize_config
        self.scrutinizers = [ ]


    def finalize_options(self):
        cfg_file = self.config
        if not os.path.exists(cfg_file):
            raise DistutilsSetupError("Cannot find Scrutinize configuration file '%s'" % cfg_file)
        try:
            config = configparser.ConfigParser()
            config.read(cfg_file)
        except configparser.Error:
            raise DistutilsSetupError("Error in Scrutinize configuration file '%s': %s" % (cfg_file, sys.exc_info()[1]))

        # Get the global cfg_files, then remove the section
        # (so it doesn't count as a scrutinizer section later).
        packages = ''
        exclude_packages = 'tests test'
        if config.has_section(CONFIG_SECTION):
            for option in ['verbose', 'dry_run']:
                try:
                    if config.has_option(CONFIG_SECTION, option):
                        setattr(self, option, config.getboolean(CONFIG_SECTION, option))
                except ValueError:
                    raise DistutilsOptionError(f"Option {CONFIG_SECTION}.{option} in '{cfg_file}' is not boolean")

            # packages
            if config.has_option(CONFIG_SECTION, 'packages'):
                packages = config.get(CONFIG_SECTION, 'packages')
            if config.has_option(CONFIG_SECTION, 'exclude_packages'):
                exclude_packages = config.get(CONFIG_SECTION, 'exclude_packages')

            config.remove_section(CONFIG_SECTION)

        # Check that there is a class/module for each scrutinizer.
        for scrutinizer in config.sections():

            if config.has_option(CONFIG_SECTION, 'packages'):
                packages = config.get(CONFIG_SECTION, 'packages')
                config.remove_option(CONFIG_SECTION, 'packages')
            if config.has_option(CONFIG_SECTION, 'exclude_packages'):
                exclude_packages = config.get(CONFIG_SECTION, 'exclude_packages')
                config.remove_option(CONFIG_SECTION, 'exclude_packages')
            mod_cfg = config[scrutinizer]

            if scrutinizer not in known_scrutinizers():
                raise DistutilsOptionError("Scrutinizer '%s' not found" % scrutinizer)
            # TODO If the scrutinizer is an exe, check that it can be run.

            mod_name = known_scrutinizers().get(scrutinizer).get('module')
            class_name = known_scrutinizers().get(scrutinizer).get('class')
            try:
                spec = importlib.util.find_spec(mod_name)
                module = importlib.util.module_from_spec(spec)
                sys.modules[mod_name] = module
                spec.loader.exec_module(module)
                module.validate_configuration(mod_cfg)
                scru_class = getattr(module, class_name)
                scru = scru_class(self)  # N.B. We pass self, i.e. Command as param.

                # Configure for run
                scru.initialize_options()
                scru.verbose = self.verbose
                scru.dry_run = self.dry_run
                scru.config = mod_cfg
                scru.lint_packages = packages
                scru.lint_exclude_packages = exclude_packages
                scru.finalize_options()
                
                self.scrutinizers.append(scru)

            except ScrutinizerConfigError:
                err = sys.exc_info()[1]
                raise DistutilsOptionError(f"Error in config of Scrutinizer '{scrutinizer}' ({mod_name}): {err}")
            except ModuleNotFoundError:
                err = sys.exc_info()[1]
                raise DistutilsOptionError(f"Cannot load Scrutinizer '{scrutinizer}' ({mod_name}): {err}")


    def run(self):
        """ Run """

        # Make sure the dependencies are available
        if self.distribution.install_requires:
            self.distribution.fetch_build_eggs(self.distribution.install_requires)

        if self.distribution.tests_require:
            self.distribution.fetch_build_eggs(self.distribution.tests_require)

        # if self.lint_packages:
        #     # The user explicitly specified the paths/packages to send to lint
        #     files = self.lint_packages
        # else:
        #     # With no packages specified, find all of them and pass them
        #     # through the filter
        #     base = self.command.get_finalized_command("build_py")
        #     files = [
        #         filename
        #         for (package, module, filename) in base.find_all_modules()
        #         if package not in self.lint_exclude_packages
        #     ]

        for scru in self.scrutinizers:
            if self.verbose:
                log.debug("Scrutinizer: %s", scru.name)
            try:
                scru.run()
            except ScrutinizerRunError:
                raise DistutilsError(f"Scrutinizer {scru.name} discovered errors")
