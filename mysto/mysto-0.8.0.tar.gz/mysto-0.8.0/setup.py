import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mysto",
    version="0.8.0",
    author="Schoening Consulting, LLC",
    author_email="bschoeni+llc@gmail.com",
    description="A data anonymization toolkit ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bschoeni/fpe",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Security",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license_files = ('LICENSE.txt',),
    packages=find_packages(exclude=["tests", "tests.*"]),
#    packages=find_packages(include=['ff3']),
    python_requires='>=3.6',
)
