#! /usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='P3MLens',
    version='1.0.0',
    author='Kun Xu',
    author_email='kunxu.sjtu15@foxmail.com',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data = True,
    url='https://github.com/kunxusjtu/P3MLens',
    license='MIT',
    description='An Accurate P3M Algorithm for Gravitational Lensing Studies in Simulations.',
    install_requires=['numpy', 'scipy>=1.6.0', 'numba', 'astropy'],
    tests_require=['pytest', 'pytest-xdist'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False
)
