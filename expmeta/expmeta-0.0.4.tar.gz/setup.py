import os
import setuptools
import sys

## README for long description
with open('README.md', encoding='utf-8') as rdme:
	_readme = rdme.read()

_mydir = os.path.abspath(os.path.dirname(sys.argv[0]))
_requires = [ r for r in open('requirements.txt', "r").read().split('\n') if len(r)>1 ]
_version = open("expmeta/_version.py", "r").read().split("=")[-1].strip("\"")

setuptools.setup(
	name='expmeta',
	version=_version,
	description="Python classes for working with measurement metadata for scientific experiments",
	long_description=_readme+"\n\n",
	long_description_content_type="text/markdown",
	url="https://github.com/SamWolski/ExpMeta",
	author="Sam Wolski",
	author_email="wolski.samp@gmail.com",
	python_requires=">=3.7.*",
	license="MIT",
	classifiers=[
		"Development Status :: 2 - Pre-Alpha",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3.7",
		"Topic :: Scientific/Engineering",
	],
	packages=["expmeta"],
	install_requires=_requires,
)
