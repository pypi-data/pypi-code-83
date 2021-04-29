import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_dwang862-containers",
    version="1.0.0",
    description="Contains fibonacci, range, unicode, BinaryTree, BST, AVLTree, Heap",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dwang862/containers-hw",
    author="Daniel Wang",
    author_email="dwang22@cmc.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["containers"],
    include_package_data=True,
)
