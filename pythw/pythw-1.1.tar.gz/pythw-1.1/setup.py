from setuptools import setup

setup(
    name = 'pythw',
    version = '1.1',
    description = 'Pyth Console',
    py_modules = ['pyth'],
    package_dir = {'': 'src'},
    install_requires = [
        "pyfiglet",
    ],
)