#!/usr/bin/env python3

from setuptools import setup

from flask_ckfinder3 import __version__

setup(
    name='Flask-CKFinder3',
    version=__version__,
    packages=['flask_ckfinder3'],
    author='Aristofor Kolomb',
    author_email='aristofor@gmail.com',
    description='Flask CKFinder3 connector',
    long_description=open('README.rst').read(),
    url='https://gitlab.com/aristofor/flask-ckfinder3',
    install_requires=['Flask','Pillow'],
    include_package_data=True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'License :: OSI Approved :: MIT License',
    ],
    license='MIT'
)
