#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='histpy',
      version="0.0.1",
      author='Israel Martinez',
      author_email='imc@umd.edu',
      install_requires = ['scipy',
                          'matplotlib!=3.4.0,!=3.4.0rc1,!=3.4.0rc2,!=3.4.0rc3,!=3.4.1',
                         ],
      url='https://gitlab.com/burstcube/histogram',
      packages = find_packages(include=["histpy","histpy.*"]),
      )
