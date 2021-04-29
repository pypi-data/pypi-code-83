#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst", encoding="utf-8") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.1.2",
    "requests>=2.25.1",
    "pandas>=1.2.4",
]

setup(
    author="Yunseong Hwang",
    author_email="kika1492@gmail.com",
    python_requires=">=3.7.1",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Korean",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="KASI Open API interface implemented in Python.",
    entry_points={
        "console_scripts": [
            "kasi=kasi.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="kasi",
    name="kasi",
    packages=find_packages(include=["kasi", "kasi.*"]),
    test_suite="tests",
    url="https://github.com/elbakramer/kasi",
    version="0.1.0",
    zip_safe=False,
)
