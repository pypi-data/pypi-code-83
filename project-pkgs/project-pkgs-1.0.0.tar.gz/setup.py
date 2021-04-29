'''
Date: 2020-12-22 11:29:49
LastEditors: Rustle Karl
LastEditTime: 2021.04.29 19:31:21
'''
import os.path

from setuptools import setup

# Import the README and use it as the long-description.
cwd = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(cwd, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='project-pkgs',
    # py_modules=['color'],
    packages=['pkgs'],
    version='1.0.0',
    license='BSD',
    author='Rustle Karl',
    author_email='fu.jiawei@outlook.com',
    description='Common libraries for personal projects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['color', 'logger', 'pkgs'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
