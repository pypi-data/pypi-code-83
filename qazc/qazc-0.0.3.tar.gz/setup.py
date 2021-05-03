import json
import setuptools
from setuptools import setup, find_packages

PACKAGE_NAME = "qazc"

with open(f"{PACKAGE_NAME}/pypkg.json", "r") as f:
    info = json.loads(f.read())

setup(
    name=PACKAGE_NAME,
    version=info["version"],
    include_package_data=True,
    packages=find_packages(),
    package_data={"": ["*.json"]},
)
