from setuptools import setup, find_packages
 
with open('README.md') as readme_file:
    readme = readme_file.read()


setup(
     version='0.1.1',
     name='quick_hull',
     author="Nathan Martino and Tanvi Thummar",
     url='https://github.com/ntm0110/quick_hull',
     description="A python library for the quick hull algorithm and visualization.",
     install_requires=['matplotlib==3.4.1', 'numpy==1.20.0', 'scipy==1.6.3'],
     license="MIT license",
     long_description=readme,
     packages=find_packages(),
)