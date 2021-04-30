"""Setup script for monument"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="monument",
    version="0.1.0",
    description="Python Interface to MonumentAI Model Serving",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/monumentAI/monument_python",
    author="MonumentAI",
    author_email="bliu@monuemnt.ai",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    keywords=[
        "monument",
        "monumentAI",
    ],
    packages=["monument"],
    package_dir={"monument": "src/monument"},
    include_package_data=True,
    install_requires=[
        "numpy",
    ],
)
