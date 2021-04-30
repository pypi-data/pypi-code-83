from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


VERSION = '0.0.4'
DESCRIPTION = 'A package which can compute the spread of a disease in a population'

# Setting up
setup(
    name="demicestimator",
    version=VERSION,
    author="Aditya Narendra (ozzey)",
    author_email="<adityanarendra6@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas', 'scipy'],
    keywords=['python', 'pandemic', 'epidemic model', 'Machine Learning', 'Prediction', 'SIR','SEIR'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License"
    ]
)
