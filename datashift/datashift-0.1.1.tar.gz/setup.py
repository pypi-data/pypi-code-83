import os.path
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="datashift",
    version="0.1.1",
    description="Lightweight and generic data processor that allows quickly filtering, balancing and processing a data set from one form to another.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MarcinStachowiak/datashift",
    author="Marcin Stachowiak",
    author_email="marcin@predictforce.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    keywords=['Pipeline', 'Data Processing', 'Preprocessing'],
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'python-dateutil',
        'pytz',
        'PyYAML',
        'six'
    ]
)
