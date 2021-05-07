from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='calculator-anarim1',
	version='0.0.1',
	description='Simple Calculator with memory',
	py_modules=["calculator"],
	package_dir={'': 'src'},
	long_description=long_description,
	long_description_content_type="text/markdown",
	extras_require = {
		"dev": [
			"pytest>=3.7",
			],
	},
	url="https://github.com/NaUrovne/calculator",
	author="Albert Narimanov",
	author_email="albertnarimanov@gmail.com"
)