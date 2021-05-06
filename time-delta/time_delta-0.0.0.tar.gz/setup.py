from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='time_delta',
  version='0.0.0',
  description='Calculate your time by entering the delta between your time and UTC time',
  long_description=open('README.txt').read() + '\n',
  url='',  
  author='mohammed yasser',
  author_email='muhammedyasser85@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='time_delta', 
  packages=find_packages(),
  install_requires=['datetime'] 
)