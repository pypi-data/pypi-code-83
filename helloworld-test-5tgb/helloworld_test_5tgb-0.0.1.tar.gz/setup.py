#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='helloworld_test_5tgb',
    version='0.0.1',
    author='yiming',
    author_email='test@test.com',
    description=u'helloworld',
    packages=['helloworld_test_5tgb'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'helloworld=helloworld_test_5tgb:helloworld'
        ]
    }
)
