import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_vb_trees",
    version="1.0.0",
    description="Implementations of Binary Tree, BST, AVL Tree, and Heap Tree",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/vbopardi/Week8Containers",
    author="Varun Bopardikar",
    author_email="vbopardi@students.pitzer.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
    install_requires=["pytest", "hypothesis"],
)
