#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

install_requireent = []

setup_requires = [
    'pandas',
    'config2',
    'notion',
    'notion_as_db',
    'ncloud_server'
]

install_requires = [
    'pandas',
    'config2',
    'notion',
    'notion_as_db',
    'ncloud_server'
]

setup(
    name='cloud_manager',
    author='Junsang Park',
    author_email='publichey@gmail.com',
    url='https://github.com/hoosiki/cloud_manager.git',
    version='0.0.5',
    long_description=readme,
    long_description_content_type="text/markdown",
    description='Package for managing cloud service using python. NCloud, AWS, AZURE, GCP',
    packages=find_packages(),
    license='BSD',
    include_package_date=False,
    setup_requires=setup_requires,
    install_requires=install_requires,
    download_url='https://github.com/hoosiki/cloud_manager/blob/master/dist/cloud_manager-0.0.5.tar.gz'
)
