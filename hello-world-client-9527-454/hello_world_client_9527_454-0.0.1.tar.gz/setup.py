#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(name='hello_world_client_9527_454',
      version='0.0.1',
      author='hello world',
      include_package_data=True,
      zip_safe=False,
      url="https://pypi.org/",
      author_email='',
      python_requires=">=3.3",
      packages=['uif_client'],
      license="MIT",
      install_requires=['requests', 'psutil', 'aiohttp'])
