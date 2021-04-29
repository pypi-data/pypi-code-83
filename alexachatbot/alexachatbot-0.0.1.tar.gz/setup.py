import setuptools
import os

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setuptools.setup(
	name="alexachatbot",
	version="0.0.1",
	author="Karan Prasad",
	author_email="alteromiiller@gmail.com",
	packages=["alexachatbot"],
	discription="Simple alexa chatbot api python package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/A-l-t-e-r-o/Alexa-chatbot",
	licence="MIT",
	python_requires=">=3.8",
	keywords=["chatbot","alexa chatbot","chatbot api","alexa api"],
	install_requires=[
		"urllib3>=1.25"

	],
	extras_require ={
		"dev":[
			"pytest>=6.2.3",
		],
	},
	classifires=[
		"Operating System :: Microsoft :: Windows",
		'License :: OSI Approved :: MIT License',
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 3",
		'Programming Language :: Python :: Implementation :: CPython',
		"Topic :: Alexa Chatbot :: api",
	]
)