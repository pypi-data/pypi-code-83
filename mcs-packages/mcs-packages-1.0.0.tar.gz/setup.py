import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mcs-packages",
    version="1.0.0",
    description="Demo for creating packages on pypi.org",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/moderncoursesquare/pypi-packages/my_packages/",
    author="moderncoursesquare",
    author_email="moderncoursesquare@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["mcs_packages"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "mcs=samplepackage.__main__:main",
        ]
    },
)

