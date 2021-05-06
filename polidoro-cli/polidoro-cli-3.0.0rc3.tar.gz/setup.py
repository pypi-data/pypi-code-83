"""
Setup to create the package
"""
from setuptools import setup, find_packages
from setuptools.command.install import install

import polidoro_cli

with open("README.md", "r") as fh:
    long_description = fh.read()


class PostInstallCommand(install):
    def run(self):
        install.run(self)

        import os
        os.mkdir('~/.teste')
        from subprocess import run
        run('mkdir ~/.teste2', check=True)
        print("oi")


setup(
    name='polidoro-cli',
    version='3.0.0-RC3',
    # version=polidoro_cli.VERSION,
    description='Generic CLI.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/heitorpolidoro/cli',
    author='Heitor Polidoro',
    scripts=['bin/cli'],
    license='unlicense',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    install_requires=['polidoro-argument==3.*'],
    cmdclass={
        'install': PostInstallCommand
    }
)
