import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_sangyoon_containers",
    version="1.1.0",
    description="Tree project for CSCI046 data structures course at CMC.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sam9807/containers-project",
    author="Sam Sangyoon Kim",
    author_email="skim21@cmc.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
)
