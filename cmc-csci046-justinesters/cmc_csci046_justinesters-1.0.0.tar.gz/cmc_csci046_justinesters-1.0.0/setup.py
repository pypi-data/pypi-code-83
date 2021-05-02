import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_justinesters",
    version="1.0.0",
    description="unicode and heap",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/JustinEsters/contiainers_justin",
    author="Justin Esters",
    author_email="jesters23@cmc.edu",
    license="GNU GPLv3",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
    install_requires=["feedparser", "html2text"]
   # entry_points={
    #    "console_scripts": [
     #       "realpython=reader.__main__:main",
#        ]
 #   },
)
