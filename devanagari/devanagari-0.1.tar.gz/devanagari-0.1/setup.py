import setuptools
from setuptools import setup,find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devanagari",
    version="0.1",
    author="Shushant Pudasaini, Nitesh Ghimire , Sagar Lamichhane, Aakash Dumjan, Sujan Adhikari, Sajjan Adhikari, Janardan Karki",
    author_email="shusrulz@gmail.com",
    description="Package for applying NLP to devanagari datasets",
    packages = find_packages(where="devanagari"),
    zip_safe = False,
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data = True,
    url="https://gitlab.com/shusrulz/everest_nlp/-/archive/0.1/everest_nlp-0.1.tar.gz",
    install_requires = ["gensim==3.7.3","sklearn","jellyfish==0.8.2","pandas"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "devanagari"},
    python_requires=">=3.6",
)
