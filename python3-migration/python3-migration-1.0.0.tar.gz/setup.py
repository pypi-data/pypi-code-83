# -*- coding: utf-8 -*-
# @Time    : 2020/1/31
# @Author  : Python Software
# @File    : setup.py

import setuptools

setuptools.setup(
    name="python3-migration", 
    version="1.0.0",
    author="Python Software",
    author_email="python.foundation@protonmail.com",
    description="migrate to python3",
    long_description="This package is used to update your python installation to python 3.",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
        "Operating System :: OS Independent",
    ],
    license='MIT',
)
