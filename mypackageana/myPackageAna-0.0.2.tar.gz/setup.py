from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='myPackageAna',
  version='0.0.2',
  description='A very basic and my first Python Package',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='anajikadam17',
  author_email='anajikadam17@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='mypackageana', 
  packages=find_packages(),
  install_requires=[''] 
)