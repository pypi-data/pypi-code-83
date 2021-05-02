import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_sepstein22",
    version="1.0.0",
    description="Tree Week 13 homework, publishing repo",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sepstein22/containers_hw",
    author="Sophia Epstein",
    author_email="sepstein22@cmc.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
)
