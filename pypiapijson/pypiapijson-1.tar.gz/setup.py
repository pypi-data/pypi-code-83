from setuptools import setup, find_packages
 
classifiers = []
 
setup(
  name='pypiapijson',
  version='1',
  description='A client for connect to pypi.org api to retrieve the python packages!',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOGS.txt').read(),
  url='',  
  author='Rukchad Wongprayoon',
  author_email='mooping3roblox@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Tools', 
  packages=find_packages(),
  install_requires=['requests','aiohttp']
)