#!/usr/bin/env python
from setuptools import setup, find_packages
from firefox_downloader import info

setup(
    name='firefox_downloader',
    version=info.VERSION,
    description=info.DESCRIPTION,
    author='Riccardo Scartozzi',
    author_email='',
    url='https://gitlab.com/firefox2/firefox-utils.git',
    license='MIT License',
    include_package_data=True,
    packages=find_packages(),
    scripts=(
        'bin/firefox_downloader',
    ),
    install_requires=(
        'requests',
    ),
)
