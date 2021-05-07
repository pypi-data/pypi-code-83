from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="HashFunction",
    version="0.0.1",
    author="Matheus Nobre Gomes",
    author_email="matt-gomes@live.com",
    description="Hashing module",
    license="GPLv3+",
    keywords="hashing, hash, function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ccr5/hashing-python-module",
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
