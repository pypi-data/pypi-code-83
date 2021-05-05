import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_Bhutoria",
    version="1.0.0",
    description="A collection of data structures and classes by R. Bhutoria in CMC CSCI046 SP21",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rajbhutoria/homework-csci046",
    author="Raj Bhutoria",
    author_email="rbhutoria22@cmc.edu",
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
