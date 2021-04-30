#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import sys
import subprocess

# Regular import isn't working so we open the version py and evaluate it
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, '__version__.py')) as version_file:
    version_data = version_file.read()
exec(version_data)

INSTALL_URL = f"git+ssh://git@github.bus.zalan.do/DSI/zlab-cli.git@{__version__}#egg=zlab"


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        subprocess.run(["pip", "install", INSTALL_URL])
        print("zlab successfully installed!")
        sys.exit()


setup(
    author="Zalando SE",
    author_email='zlab-team@gmail.com',
    description="Zalando zlab installer",
    install_requires=[],
    license="MIT license",
    cmdclass={
        'install': PostInstallCommand,
    },
    include_package_data=True,
    keywords='zlab',
    name='zlab',
    py_modules=['__version__'],
    setup_requires=[],
    tests_require=[],
    url='https://github.bus.zalan.do/DSI/zlab-cli',
    version=__version__,
    zip_safe=False,
)
