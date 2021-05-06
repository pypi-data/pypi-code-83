"""Setup file for the Cachier package."""

# This file is part of Cachier.
# https://github.com/shaypal5/chardif

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Shay Palachy <shaypal5@gmail.com>

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import versioneer


TEST_REQUIRES = ['pytest', 'coverage', 'pytest-cov']

README_RST = ''
with open('README.rst') as f:
    README_RST = f.read()


setup(
    name='chardif',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description=('Print per-character string diffs to terminal w/ Python'),
    long_description=README_RST,
    license='MIT',
    author='Shay Palachy',
    author_email='shay.palachy@gmail.com',
    url='https://github.com/shaypal5/chardif',
    packages=['chardif'],
    # entry_points='''
    #     [console_scripts]
    #     chardif=chardif.scripts.cli:cli
    # ''',
    install_requires=['wasabi'],
    extras_require={
        'test': TEST_REQUIRES,
    },
    platforms=['linux', 'osx', 'windows'],
    keywords=['diff', 'wasabi', 'chardiff'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Other/Nonlisted Topic',
        'Intended Audience :: Developers',
    ],
)
