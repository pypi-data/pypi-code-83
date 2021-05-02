import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_tupperware",
    version="1.0.0",
    description="Containers from CMC's CSCI046 Data Structures Course",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/samcbogen/tupperware/tree/master",
    author="Samuel Bogen",
    author_email="samcbogen@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
)
