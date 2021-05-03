#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='shangyu_pypi',  # How you named your package folder (MyLib)
    version='0.0.4',  # Start with a small number and increase it with every change you make
    author='ShangYu Chiang',  # Type in your name
    author_email='d07945011@ntu.edu.tw',   # Type in your E-Mail
    url='',  # Provide either the link to your github or to your website
    long_description=long_description,  # description - Give a short description about your library
    long_description_content_type='text/markdown',
    packages=['shangyu_pypi'],  # packages - Chose the same as "name"
    install_requires=[],
    python_requires='>=3.5'
)
