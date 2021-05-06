"""
Setup to create the package
"""
import sys
from pkg_resources import resource_filename
from setuptools import setup, find_packages
from setuptools.command.install import install
import distutils

import polidoro_cli

with open("README.md", "r") as fh:
    long_description = fh.read()


class PostInstallCommand(install):
    def run(self):
        install.run(self)

        import os
        from subprocess import run
        cli_dir = os.path.expanduser('~/.teste')
        print('---------------------\n\n\n\n\n')
        def find_module_path():
            for p in sys.path:
                if os.path.isdir(p):
                    print(p)
                    print(os.listdir(p))
                if os.path.isdir(p) and 'polidoro_cli' in os.listdir(p):
                    return os.path.join(p, 'polidoro_cli')
        install_path = find_module_path()
        print(1, install_path)
        import polidoro_cli

        print(2, polidoro_cli.__path__)
        # for k, v in vars(distutils.core).items():
        #     print(k, v)
        print('\n\n\n\n---------------------')
        # print(distutils.core.Distribution.package_dir)
        print('\n\n\n\n---------------------')
        # if os.path.exists(cli_dir):
        #     pass
        # else:
        #     os.link()


setup(
    name='polidoro-cli',
    version='3.0.0-RC4',
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
