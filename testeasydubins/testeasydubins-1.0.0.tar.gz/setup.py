"""
Setup script for testeasydubins
"""

import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="testeasydubins",
    version="1.0.0",
    description="To generate dubin curves projection points.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Rishav",
    author_email="xyz@gmail.com",
    license="GPL3",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=["testeasydubins"],
    include_package_data=True,
    install_requires=["importlib_resources"],
    entry_points={"console_scripts": ["testeasydubins=testeasydubins.__main__:main"]},
)
