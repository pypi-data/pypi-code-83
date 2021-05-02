#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['cryptography>3.2,<4']

setup_requirements = []

test_requirements = []

setup(
    author="Sergey Panfilov",
    author_email='sergray@gmail.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="CLI tool for symmetric encryption/decryption using cryptography.fernet",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='crypto_fernet',
    name='crypto_fernet',
    packages=find_packages(include=['crypto_fernet', 'crypto_fernet.*']),
    setup_requires=setup_requirements,
    entry_points={
        'console_scripts': ['crypto_fernet=crypto_fernet.crypto_fernet:main'],
    },
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sergray/crypto_fernet',
    version='0.1.0',
    zip_safe=False,
)
