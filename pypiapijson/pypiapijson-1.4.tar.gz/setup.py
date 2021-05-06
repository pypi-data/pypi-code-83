from setuptools import setup, find_packages
 
classifiers = []
 
setup(
  name='pypiapijson',
  version='1.4',
  description='A client for connect to pypi.org api to retrieve the python packages!',
  long_description=open('README.txt').read() + "Changelog\nVersion 1\nFirst release\nVersion 1.2\nAdd getbyv() and status\nVersion 1.3\nFix some bugs\nVersion 1.4\nAdded help",
  url='',  
  author='Rukchad Wongprayoon',
  author_email='mooping3roblox@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Tools', 
  packages=find_packages(),
  install_requires=['requests','aiohttp']
)