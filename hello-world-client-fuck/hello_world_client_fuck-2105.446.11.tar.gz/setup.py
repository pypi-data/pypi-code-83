#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
import datetime


def GetVersion():
    now_time = datetime.datetime.now()
    version = "%s.%s.%s" % (now_time.strftime('%y') + now_time.strftime('%m'),
                            now_time.strftime('%H') + now_time.strftime('%M'),
                            now_time.strftime('%S'))
    return version


setup(name='hello_world_client_fuck',
      version=GetVersion(),
      author='hello world',
      include_package_data=True,
      zip_safe=False,
      url="https://pypi.org/",
      author_email='',
      python_requires=">=3.3",
      packages=['src'],
      license="MIT",
      install_requires=[])
