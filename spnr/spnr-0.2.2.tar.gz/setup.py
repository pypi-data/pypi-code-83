# coding=utf-8

import setuptools

import spnr

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name=spnr.name,
    version=spnr.version,
    author='sea',
    author_email='simpleslight@icloud.com',
    description='A command line toolset',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache-2.0',
    url='https://github.com/suransea/spanner',
    packages=setuptools.find_packages(),
    install_requires=[
        'qrcode', 'pillow', 'opencv-python', 'pyscreenshot', 'pyzbar', 'pyperclip'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'console_scripts': [
            'spnr=spnr.cli:main',
        ]
    },
)
