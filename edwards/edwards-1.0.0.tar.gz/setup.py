import os

from setuptools import setup, find_packages


setup(
    name="edwards",
    version="1.0.0",
    author="Cobo Tech Engineers",
    author_email="engineers@cobo.com",
    description="rust curve25519 libs",
    long_description="rust curve25519 libs ",
    license="Cobo Copyright Reserved",
    url="https://cobo.com",
    packages=find_packages(
        include=["*"]
    ),
    include_package_data=True,
    # zip_safe=False,
)
