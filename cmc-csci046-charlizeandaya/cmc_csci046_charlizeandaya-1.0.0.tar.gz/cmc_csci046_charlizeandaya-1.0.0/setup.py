import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_charlizeandaya",
    version="1.0.0",
    description="Implementations of a binary tree, binary search tree, avl tree,\
         heap, unicode, range, and fibonacci",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/charlizeandaya/containers_homework",
    author="Charlize Andaya",
    author_email="charlize.andaya@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True
)
