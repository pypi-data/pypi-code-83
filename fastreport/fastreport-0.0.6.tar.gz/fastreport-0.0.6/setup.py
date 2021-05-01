# -*- coding: utf-8 -*-
"""
Created on Sat May 1 19:45:08 2021

@author: kishore S
"""

from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


VERSION = '0.0.6'
DESCRIPTION = 'Easy report with almost no coding'


setup(
    name="fastreport",
    version=VERSION,
    author="Kishore",
    author_email="<kishoresshankar@gmail.com>",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kishore-s-gowda/fastreport",
    license="MIT",
    keywords=['python', 'regression', 'classification', 'algorithm'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    py_modules = ['report']
)
