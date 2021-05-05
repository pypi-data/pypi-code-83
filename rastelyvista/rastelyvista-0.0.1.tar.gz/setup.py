#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='rastelyvista',
    version='0.0.1',
    description='3D model building',
    long_description='Create models from meshes and surfaces of 3D data using shapefiles to manipulate models',
    long_description_content_type="text/markdown",
    author='Ed Harrison',
    author_email='eh@emrld.no',
    url='https://github.com/emerald-geomodelling/rastelyvista',
    packages=setuptools.find_packages(),
    install_requires=[
        "pyvista",
        "geopandas",
        "numpy",
        "pandas",
        "emerald-shapeutils"
    ],
)
