import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
        name="cmc_csci046_Pothis",
        version="1.0.0",
        description="Implementation of fundamental data structures and unicode normalization",
        long_description=README,
        long_description_content_type="text/markdown",
        url="https://github.com/Tonnpo/csci-046",
        author="Ton Pothisawang",
        author_email="Tpothis@students.pitzer.edu",
        license="BSD 3-Clause",
        packages=find_packages(exclude=("tests")),
        include_package_data=True,
)
