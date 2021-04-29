import os
from setuptools import setup, find_packages

VERSION = '0.1.0'


setup(
    name = 'mpltw',
    packages = find_packages(exclude=['contrib', 'docs', 'tests']),
    license = 'MIT',
    version = VERSION,
    description = 'Using matplotlib with tranditional Chinese word more easily.',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    install_requires = ['matplotlib'],
    include_package_data=True,
    author = 'scku208',
    author_email = 'scku208@gmail.com',
    url = 'https://gitlab.com/scku208/matplotlib-taiwan-font',
    download_url = 'https://gitlab.com/scku208/matplotlib-taiwan-font/-/archive/master/matplotlib-taiwan-font-master.zip'\
        .format(v=VERSION),
    keywords = ['matplotlib', 'tranditional', 'Chinese'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        ]
    )
