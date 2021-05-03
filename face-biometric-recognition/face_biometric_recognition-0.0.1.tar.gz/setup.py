#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'face_recognition_models>=0.3.0',
    'Click>=6.0',
    'dlib>=19.7,<=19.21.0',
    'numpy',
    'Pillow'
]

test_requirements = [
    'tox',
    'flake8'
]

setup(
    name='face_biometric_recognition',
    version='0.0.1',
    description="Recognize faces from Python",
    long_description=readme + '\n\n',
    long_description_content_type='text/markdown',
    author="Ransom Voke Anighoro",
    author_email='voke.anighoro@gmail.com',
    url='https://gitlab.com/vokeanighoro/facial_recognition',
    packages=[
        'face_biometric_recognition',
    ],
    package_dir={'face_biometric_recognition': 'face_biometric_recognition'},
    package_data={
        'face_biometric_recognition': ['models/*.dat']
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='face_biometric_recognition',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
