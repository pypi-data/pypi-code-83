from setuptools import find_packages, setup

setup(
    name='wsurf',
    version='0.0.01',
    description='',
    long_description='',
    url='https://github.com/DavidePellis/wsurf',
    author='Davide Pellis',
    download_url='https://github.com/DavidePellis/wsurf/archive/0.0.01.tar.gz',
    author_email='davidepellis@gmail.com',
    packages=find_packages(),
    package_data={'': ['icons/*.png', '*.obj']},
    classifiers=['Development Status :: 1 - Planning'],
    license='MIT',
)