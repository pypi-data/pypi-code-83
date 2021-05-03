import json
import setuptools
from setuptools import setup, find_packages

from pathlib import Path
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
loc = Path(__location__)

PACKAGE_NAME = "qazc"

with open(f"{PACKAGE_NAME}/pypkg.json", "r") as f:
    info = json.loads(f.read())

with open("requirements.txt") as fid:
    requires = [line.strip() for line in fid]


setup(
    name=PACKAGE_NAME,
    version=info["version"],
    install_requires=requires,
    include_package_data=True,
    packages=find_packages(),
    package_data={"": ["*.json", "./test.json"]},
)
