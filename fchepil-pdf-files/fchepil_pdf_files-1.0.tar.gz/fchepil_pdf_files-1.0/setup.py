import setuptools
from pathlib import Path

setuptools.setup(
    name="fchepil_pdf_files",
    version=1.0,
    long_description=Path("README.md").read_text(),
    # list which packages/folders to exclude
    packages=setuptools.find_packages(exclude=["tests", "data"])
)
