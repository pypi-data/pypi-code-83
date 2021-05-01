import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_aaronxie",
    version="1.0.0",
    description="CSCI046 class work. Implementation of Heap, AVLTree, BinaryTree, BST and more.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/aaronxie0000/containers_assignment/",
    author="Aaron Xie",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
)
