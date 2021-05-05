from setuptools import setup, find_packages
import os

find_version = '0.3'
if os.environ.get('CI_COMMIT_TAG'):
    find_version = os.environ['CI_COMMIT_TAG']

setup(
    name='mosaik-gridcontrollers',
    version=find_version,
    author='Reef Eilers',
    author_email='reef.eilers@offis.de',
    description='A suite of controllers for power grids implemented as mosaik simulators.',
    long_description_content_type='text/x-rst',
    long_description=(open('README.rst').read() + '\n\n' +
                      open('CHANGES.txt').read()),
    url='https://gitlab.com/mosaik/mosaik-gridcontrollers',
    install_requires=[
        'numpy>=1.2',
        'mosaik-api>=2.4',
        'mosaik>=2.6'
    ],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering',
    ],
    )
