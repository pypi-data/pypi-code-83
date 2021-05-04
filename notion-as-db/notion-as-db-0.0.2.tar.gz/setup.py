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
        'notion'
        ]

install_requires = [
    'pandas',
    'config2',
    'notion'
]

setup(
    name='notion-as-db',
    author='Junsang Park',
    author_email='publichey@gmail.com',
    url='https://github.com/hoosiki/notion-as-db.git',
    version='0.0.2',
    long_description=readme,
    long_description_content_type="text/markdown",
    description='Package for convenient Notion usage. Once you set default.yaml file, You don\'t need to find v2token.',
    packages=find_packages(),
    license='BSD',
    include_package_date=False,
    setup_requires=setup_requires,
    install_requires=install_requires,
    download_url='https://github.com/hoosiki/notion-as-db/blob/master/dist/notion-as-db-0.0.2.tar.gz'
)
