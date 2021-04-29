import setuptools
from pathlib import Path

setuptools.setup(
    name="mehulpdf",
    version=1.0,
    long_descreption=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"])
)