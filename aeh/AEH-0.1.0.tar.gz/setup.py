from setuptools import setup, find_packages
import os
import codecs

VERSION = '0.1.0'
DESCRIPTION = 'A New Encryption Algorithim'
# Setting up
setup(
    name="AEH",
    version=VERSION,
    author="Ali Al Hadi Al-Husseini",
    author_email="<alihadi.alhusseini@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'encryption', 'decrypting',
              ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
