#!/usr/bin/env python
from pathlib import Path

from setuptools import setup, find_packages

try: # for pip >= 10
	from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
	from pip.req import parse_requirements
pkg_name = "cvmodelz"

cwd = Path(__file__).parent.resolve()
# Get __version__ variable
exec(open(str(cwd / pkg_name / '_version.py')).read())

install_requires = [
	line.strip()
		for line in open(str(cwd / "requirements.txt")).readlines()
]

setup(
	name=pkg_name,
	version=__version__,
	python_requires=">3.6",
	description='Wrapper for various computer vision models (mostly provided by chainer, chainercv, and chainercv2)',
	log_description=open(str(cwd / "README.md")).read(),
	author='Dimitri Korsch',
	author_email='korschdima@gmail.com',
	license='MIT License',
	packages=find_packages(exclude=("tests",)),
	zip_safe=False,
	setup_requires=[],
	install_requires=install_requires,
	package_data={'': ['requirements.txt']},
	data_files=[('.',['requirements.txt'])],
	include_package_data=True,
)
