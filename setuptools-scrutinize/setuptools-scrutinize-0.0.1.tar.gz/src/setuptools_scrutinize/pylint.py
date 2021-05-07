# -*- coding: utf-8 -*-
""" Scrutinizer: Pylint """

from typing import Final, Tuple, Any
import os
import re
import sys
from distutils import log
from pylint import lint  # type: ignore
from pylint.__pkginfo__ import numversion as pylint_version  # type: ignore
from pkg_resources import *

from . import Scrutinizer
from setuptools_scrutinize import ScrutinizerConfigError, ScrutinizerRunError


_opts: Final[Tuple[str, Any]] = lint.Run.LinterClass.make_options()


def user_options():
    parsed = []

    for longopt, params in _opts:
        desc = params.get("help", None)

        parsed.append(("lint-" + longopt + "=", None, desc))
    return parsed


def validate_configuration(cfg):
    """ Validate configuration.
    """
    pass

class PylintScrutinizer(Scrutinizer):
    """ Pylint scrutinizer """

    name = 'Pylint'

    description = "Pylint code checker"

    user_options = user_options() + [
        (
            "lint-packages=",
            None,
            "Report on just these packages. These arguments are passed straight "
            "through to pylint as the module_or_package arguments. As such, they "
            "can be paths to files or packages",
        ),
        ("lint-exclude-packages=", None, "exclude these packages"),
        ("lint-output=", None, "output report into this file"),
        ("lint-rcfile=", None, "pylint configuration file"),
    ]


    def initialize_options(self):
        """ Initialize object, really.
            Create the attributes and apply defaults, when available.
        """
        self.lint_packages = ""
        self.lint_exclude_packages = "tests test"
        self.lint_output = None
        # self.lint_rcfile = self.distribution.scrutinize_rcfile
        self.lint_rcfile = None
        self.distribution = self.command.distribution
        # self.command = None
        for longopt, params in _opts:
            key = "lint_" + longopt.replace("-", "_").rstrip("=")
            setattr(self, key, None)


    def finalize_options(self):
        """ Apply the configuration and prepare for running.
        """
        self.lint_rcfile = self.config
        self.lint_packages = [package.strip() for package in re.split(r"[\s,]+", self.lint_packages) if package != ""]  # pylint disable=line-too-long
        self.lint_exclude_packages = [module.strip() for module in re.split(r"[\s,]+", self.lint_exclude_packages)]  # pylint disable=line-too-long
        if self.lint_output:
            out_dir = os.path.dirname(self.lint_output)
            if out_dir:
                if sys.version_info >= (3, 2):
                    os.makedirs(out_dir, exist_ok=True)
                elif not os.path.exists(out_dir):
                    os.makedirs(out_dir)
            self.lint_output = open(self.lint_output, "w")

    def with_project_on_sys_path(self, func, func_args, func_kwargs):
        """ Fix the project path to include the eggs.
            Now you include also the build dependencies which are
            installed locally.
            Supports both Python 2 and Python 3.
        """
        if sys.version_info >= (3,) and getattr(self.distribution, "use_2to3", False):
            # If we run 2to3 we can not do this inplace:

            # Ensure metadata is up-to-date
            self.command.reinitialize_command("build_py", inplace=0)
            self.command.run_command("build_py")
            bpy_cmd = self.command.get_finalized_command("build_py")
            build_path = normalize_path(bpy_cmd.build_lib)

            # Build extensions
            self.command.reinitialize_command("egg_info", egg_base=build_path)
            self.command.run_command("egg_info")

            self.command.reinitialize_command("build_ext", inplace=0)
            self.command.run_command("build_ext")
        else:
            # Without 2to3 inplace works fine:
            self.command.run_command("egg_info")

            # Build extensions in-place
            self.command.reinitialize_command("build_ext", inplace=1)
            self.command.run_command("build_ext")

        ei_cmd = self.command.get_finalized_command("egg_info")

        old_path = sys.path[:]
        old_modules = sys.modules.copy()

        try:
            sys.path.insert(0, normalize_path(ei_cmd.egg_base))
            working_set.__init__()
            add_activation_listener(lambda dist: dist.activate())
            require("%s==%s" % (ei_cmd.egg_name, ei_cmd.egg_version))
            if self.verbose:
                log.debug("Running with args: %s; %s", func_args, func_kwargs)
            return func(*func_args, **func_kwargs)
        finally:
            sys.path[:] = old_path
            sys.modules.clear()
            sys.modules.update(old_modules)
            working_set.__init__()

    def run(self):
        options = []
        for longopt, params in _opts + (("rcfile", None),):
            # value = getattr(self, "lint_" + longopt.replace("-", "_"))
            value = self.config.get("lint_" + longopt.replace("-", "_"))
            if value is not None:
                if " " in value:
                    value = '"' + value + '"'
                options.append("--{0}={1}".format(longopt, value))

        # if self.verbose:
        #     print("Config:")
        #     print(options)

        # # Make sure the dependencies are available
        # if self.distribution.install_requires:
        #     self.distribution.fetch_build_eggs(self.distribution.install_requires)
        #
        # if self.distribution.tests_require:
        #     self.distribution.fetch_build_eggs(self.distribution.tests_require)

        if self.lint_packages:
            # The user explicitly specified the paths/packages to send to lint
            files = self.lint_packages
        else:
            # With no packages specified, find all of them and pass them
            # through the filter
            base = self.command.get_finalized_command("build_py")
            files = [
                filename
                for (package, module, filename) in base.find_all_modules()
                if package not in self.lint_exclude_packages
            ]

        if self.lint_output:
            stdout, sys.stdout = sys.stdout, self.lint_output
            stderr, sys.stderr = sys.stderr, self.lint_output
        try:
            kwargs = {}
            if pylint_version < (2, 0, 0):
                kwargs.update({"exit": False})
            else:
                kwargs.update({"do_exit": False})
            lint_runner = self.with_project_on_sys_path(lint.Run, [options + files], kwargs)
            if lint_runner.linter.msg_status:
                raise ScrutinizerRunError("lint error %s." % lint_runner.linter.msg_status)
        finally:
            if self.lint_output:
                sys.stdout = stdout
                sys.stderr = stderr
