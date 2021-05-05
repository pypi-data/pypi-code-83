from setuptools import setup, find_packages
from os import path

basedir = path.abspath(path.dirname(__file__))
with open(path.join(basedir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='catsart',
    description='Prints Random Cats Ascii Arts',
    author='nandydark',
    version='7.0',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: System"
    ],
    url='https://github.com/nandydark/catsart',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['cats', 'ascii'],
    packages=find_packages(),
    package_data={'catsart.database': ['*.json']},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'catsart = catsart.__main__:main',
        ],
    },
)
