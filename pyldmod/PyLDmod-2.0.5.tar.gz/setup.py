# -*- coding: utf-8 -*-
"""
PyLDmod
====

PyLDmod_ is a  Python JSON-LD_ library. It has been modified to accept file://
URL's

.. _PyLDmod: https://github.com/hsolbrig/pyld
.. _JSON-LD: https://json-ld.org/
"""

from distutils.core import setup
import os

# get meta data
about = {}
with open(os.path.join(
        os.path.dirname(__file__), 'lib', 'pyld', '__about__.py')) as fp:
    exec(fp.read(), about)

with open('README.rst') as fp:
    long_description = fp.read()

setup(
    name='PyLDmod',
    version=about['__version__'],
    description='modified Python implementation of the JSON-LD API',
    long_description=long_description,
    author='Digital Bazaar',
    author_email='support@digitalbazaar.com',
    url='https://github.com/digitalbazaar/pyld',
    packages=[
        'c14n',
        'pyld',
        'pyld.documentloader',
    ],
    package_dir={'': 'lib'},
    license='BSD 3-Clause license',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'cachetools',
        'frozendict',
        'lxml',
    ],
    extras_require={
        'requests': ['requests'],
        'aiohttp': ['aiohttp'],
        'cachetools': ['cachetools'],
        'frozendict': ['frozendict'],
    }
)
