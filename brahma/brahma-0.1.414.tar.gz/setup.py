#!/usr/bin/env python

from setuptools import setup, find_packages

long_description = ""

with open("README.md", "r") as fh:
    long_description = fh.read()



setup(
    name="brahma", 
    version="0.1.414",
    author="Rahul Tandon",
    author_email="rahul@vixenintelligence.com",
    description="BrahmA Aritificial Intelligence Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/vixencapital/brahma/releases/tag/1.0",
    packages=['brahma', 'brahma.bots', 'brahma.dna', 'brahma.genes', 'brahma.genome', 'brahma.world'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
