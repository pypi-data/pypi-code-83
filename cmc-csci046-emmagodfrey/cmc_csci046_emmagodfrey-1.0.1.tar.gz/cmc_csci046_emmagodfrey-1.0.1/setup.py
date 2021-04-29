import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_emmagodfrey",
    version="1.0.1",
    description="Implementations of a binary tree, binary search tree, avl tree, and a heap. Additional small projects included.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/emmacgodfrey/containers2",
    author="Emma Godfrey",
    author_email="emma.godfrey@pomona.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True
)
