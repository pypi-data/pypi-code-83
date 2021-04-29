from setuptools import find_packages, setup

setup(
    name='snowpiercer',
    version='1.0.1',
    author='snowpiercer',
    url='https://github.com/snowpiercer/snowpiercer',
    packages=['snowpiercer'],
    install_requires=['pycryptodome'],
    include_package_data=True,
)
