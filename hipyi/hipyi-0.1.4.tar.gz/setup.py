from setuptools import setup, find_packages
import os

setup(
    name='hipyi',
    use_scm_version={"write_to": os.path.join("hipypi", "_version.py")},
    packages=find_packages(),
    install_requires=[
        'setuptools_scm',
    ],
    url='',
    license='',
    author='Daniel Morcuende',
    author_email='dmorcuende@gmail.com',
    description='Test pypi deploy'
)
