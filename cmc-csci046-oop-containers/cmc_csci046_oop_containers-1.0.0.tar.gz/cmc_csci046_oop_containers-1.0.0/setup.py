import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_oop_containers",
    version="1.0.0",
    description="A library that utilizes oop to implement proper heap and unicode data structures",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/brandonsrho57/oop_containers",
    author="Brandon Rho",
    author_email="brandonsrho57@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True
)
