import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_mjotsuka_trees",
    version="1.0.0",
    description="Class functions for CSCI046 implementing fibonacci, range, unicode, BAST, BinaryTree, AVLTree, and Heap",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mjotsuka/conts/",
    author="Megan Otsuka",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
)
