from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding = 'utf-8') as f:
    long_description = f.read()

setup(
    name = 'find_primes',
    version = '1.2.0',
    author = 'JamesJ',
    author_email = 'GGJamesQQ@yeah.net',
    description = 'A module for finding primes.',
    classifiers = [
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta'
    ],
    packages = ['find_primes'],
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    python_requires = '>=3.6'
)