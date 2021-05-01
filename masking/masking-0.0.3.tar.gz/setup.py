import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='masking',
    version='0.0.3',
    author='Sangram Mohanty',
    author_email='odisha532@hotmail.com',
    description='This package contains a function \'maskstring\' to mask a given input string based on the index positions passed as arguments.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sangram11/MASKING',
    project_urls={'BUG Tracker':'https://github.com/sangram11/MASKING',},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)