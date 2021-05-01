from setuptools import find_packages
from setuptools import setup

with open("README.md", "r", encoding='utf-8') as fh:  
    long_description = fh.read()

setup(
    name="serendipy",
    author="jqy",
    version="0.1.5",
    author_email="jiaqiyuejqy@gmail.com",
    packages=find_packages(exclude=('test',)),
    description="Bi-level optimization for gurobi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    license='Apache2.0',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)