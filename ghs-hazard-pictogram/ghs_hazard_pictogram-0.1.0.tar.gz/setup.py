#!/usr/bin/env python3
import os
import subprocess
from datetime import date
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

module = 'ghs_hazard_pictogram'

setup(
    name='ghs_hazard_pictogram',
    description='GHS hazard descriptions and pictograms.',
    python_requires='>3.7.0',
    version='0.1.0',
    author='Frédéric MEUROU',
    author_email='fm@peabytes.me',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fmeurou/ghs_hazard_pictograms',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Information Technology",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Chemistry"
    ],
    py_modules=[
        'ghs_hazard_pictogram',
    ],
)
