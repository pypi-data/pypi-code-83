import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

with open("./README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="medflux",
    version="0.0.2",
    author="w-is-h",
    author_email="w.kraljevic@gmail.com",
    description="Temporal modeling of patients and diseases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/w-is-h/medflux",
    packages=['medflux', 'medflux.datasets'],
    install_requires=[
        'datasets~=1.6.0',
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
