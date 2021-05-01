#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

long_description = '''
# readme:

this is a package to create html with python language
though it will be used by myself, also you can use it.
'''

setup(
    name='html_builder',
    version='0.0.2',
    author='normidar',
    author_email='normidar7@gmail.com',
    url='https://normidar.com',
    description=u'this package is use for creating html by python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[
        'HtmlCreator',
        'HtmlCreator.Body',
        'HtmlCreator.Head',
        'HtmlCreator.Body.Input'
    ],
    install_requires=[],
    entry_points={
        'console_scripts': []
    }
)