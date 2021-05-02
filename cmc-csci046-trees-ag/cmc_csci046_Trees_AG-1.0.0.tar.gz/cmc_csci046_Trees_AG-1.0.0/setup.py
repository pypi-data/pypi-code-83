import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_Trees_AG",
    version="1.0.0",
    description="Trees Data Structures Assignments",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/agulati18/week08",
    author="Aryaman Gulati",
    author_email="agulati22@cmc.edu",
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
