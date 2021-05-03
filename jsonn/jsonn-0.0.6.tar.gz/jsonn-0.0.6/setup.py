from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["numpy>=1.14.5","pandas==0.25"]

setup(
    name="jsonn",
    version="0.0.6",
    author="Jaroslaw Szkola",
    author_email="jjsman@gmail.com",
    description="A package for process large json files",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jjsman/jsonn/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
