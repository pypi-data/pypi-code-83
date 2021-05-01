import setuptools
from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
	name='jslfirebaseutil',  # How you named your package folder (MyLib)
	packages=setuptools.find_packages(),  # Chose the same as "name"
	version='1.0.6',  # Start with a small number and increase it with every change you make
	license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
	description='JSoftwareLabs Utils for Firebase',  # Give a short description about your library
	long_description=long_description,
    long_description_content_type='text/markdown',
	author='JSoftwareLabs.com',  # Type in your name
	author_email='info@jsoftwarelabs.com',  # Type in your E-Mail
	url='https://github.com/JSoftwareLabs/JSLFireBaseUtils',
	# Provide either the link to your github or to your website
	download_url='https://github.com/JSoftwareLabs/JSLFireBaseUtils/archive/refs/tags/V1_0_6.tar.gz',
	# I explain this later on
	keywords=['Firebase', 'JSoftwareLabs', 'Cloudstore', 'Firestore', 'Firebase Utility'],
	# Keywords that define your package best
	install_requires=[  # I get to this in a second
		'firebase-admin',
		'google-cloud',
	],
	include_package_data=True,
	classifiers=[
		'Development Status :: 4 - Beta',
		# Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
		'Intended Audience :: Developers',  # Define that your audience are developers
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: Apache Software License',  # Again, pick a license
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
	],
)
