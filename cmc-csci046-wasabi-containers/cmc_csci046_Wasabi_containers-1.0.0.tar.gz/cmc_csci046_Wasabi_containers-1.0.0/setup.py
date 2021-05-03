import io
import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        README = f.read()
except FileNotFoundError:
    README = "Containers from my Data Structures class"

setup(
    name="cmc_csci046_Wasabi_containers",
    version="1.0.0",
    description="Containers from my Data Structures class, including Binary Tree, Binary Search Tree, the AVL Tree, and Heap!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/WasabiWabiSabi/container_dev",
    author="WasabiWabiSabi",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
)
