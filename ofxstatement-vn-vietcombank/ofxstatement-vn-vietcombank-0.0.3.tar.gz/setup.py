#!/usr/bin/python3
"""Setup
"""
from setuptools import find_packages
from distutils.core import setup

version = "0.0.3"

setup(
    name="ofxstatement-vn-vietcombank",
    version=version,
    author="Mikhail Umnov",
    author_email="darkms5+github@gmail.com",
    url="https://github.com/darkms/ofxstatement-vn-vietcombank",
    description=("Vietcombank plugin for ofxstatement"),
    license="MIT License",
    keywords=["ofx", "vietcombank"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Utilities",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["ofxstatement", "ofxstatement.plugins"],
    entry_points={
        "ofxstatement": ["vietcombank_excel = ofxstatement.plugins.vietcombank_excel:VietcombankExcelPlugin"]
    },
    install_requires=["ofxstatement"],
    include_package_data=True,
    zip_safe=True,
)
