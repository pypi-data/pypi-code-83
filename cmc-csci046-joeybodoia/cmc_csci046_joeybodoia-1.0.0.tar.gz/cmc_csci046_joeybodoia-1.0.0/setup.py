import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_joeybodoia",
    version="1.0.0",
    description="Implementation of Binary Tree, BST, AVL, Heap Tree structures as well as Fibonacci, Range, and Unicode structres. ",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/joeybodoia/data_structures",
    author="joeybodoia",
    author_email="jbodoia21@cmc.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
    install_requires=["hypothesis", "pytest"],
)
