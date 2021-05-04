import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_narula",
    version="1.0.0",
    description="Fibonacci numbers, Binary Trees, Binary Search Trees, and more",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dnarula22/containers_week8",
    author="Dhruv Narula",
    author_email="dnarula22@cmc.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["containers"],
    include_package_data=True,
)
