from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='piseptron',
  version='0.0.1',
  description='A Perceptron model',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Andrey Pisarevsky',
  author_email='pisarevskiy1977@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='perceptron', 
  packages=find_packages(),
  install_requires=[''] 
)