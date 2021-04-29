import pathlib
from setuptools import setup


cwd = pathlib.Path(__file__).parent
long_description = (cwd / 'README.md').read_text()

setup(
	name = 'funnelmap',
	packages = ['funnelmap'],
	description = (
		"creating and saving many-to-one maps of memorable aliases to "
		"'official' identifiers"
	),
	version = '0.1',
	license = 'MIT',
	long_description_content_type = 'text/markdown',
	long_description = long_description,
	author = 'hotzsauce',
	author_email = 'githotz@gmail.com',
	url = 'https://www.github.com/hotzsauce/funnel-dev',
	keywords = ['json', 'surjective', 'aliases', 'renaming'],
	extras_require = {
		'dataframe': ['pandas']
	},
	include_package_data = True,
	classifiers = [
		'Development Status :: 3 - Alpha',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.7'
	]
)
