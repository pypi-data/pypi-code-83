import os.path
from setuptools import find_packages, setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="cmc_csci046_cristywei",
    version="1.0.0",
    description="Implementation of binary tree, binary search tree, AVL tree, heap, fibonacci, range, and unicode.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cristywei/containers-hw",
    author="Cristy Wei",
    author_email="cwei23@cmc.edu",
    license="GNU General Public License v3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True, 
)
