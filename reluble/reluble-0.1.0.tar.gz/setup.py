#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reluble",
    version="0.1.0",
    author="Nathan Drenkow, Catalina Gomez, and Benjamin D. Killeen",
    author_email="killeen@jhu.edu",
    description="Reliable deep network training, saving you hours.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["numpy", "torch", "termcolor", "scipy"],
    include_package_data=True,
    python_requires=">=3.8",
)
