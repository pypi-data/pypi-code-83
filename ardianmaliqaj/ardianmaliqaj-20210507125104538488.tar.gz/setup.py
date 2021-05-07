from setuptools import setup, find_packages
from datetime import datetime

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]


version_format = "".join([char for char in str(datetime.now()) if char.isdigit()])

setup(
  name='ardianmaliqaj',
  version= version_format,
  description='building first pip',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Ardian Maliqaj',
  author_email='ardianmaliqaj0@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='pip installable module',
  packages=find_packages(),
  install_requires=['']
)
