from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Getting Important World News'
LONG_DESCRIPTION = 'A package that allows user to get top world news from https://apnews.com/hub/ap-top-news.'

# Setting up
setup(
    name="PyWnews",
    version=VERSION,
    author="Niranjan Jain",
    author_email="<niranjainjain022@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['bs4', 'requests'],
    keywords=['python', 'worldnews', 'scrapper'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)