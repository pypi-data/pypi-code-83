# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="donb-custom-widget",
    version="1.0",
    author="Don Beberto",
    author_email="bebert64@gmail.com",
    description="Custom widget for Pyside6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    package_data={"": ["py.typed"]},
    packages=setuptools.find_packages(where="."),
    install_requires=[
        "Pyside6",
        "donb-tools",
    ],
)
