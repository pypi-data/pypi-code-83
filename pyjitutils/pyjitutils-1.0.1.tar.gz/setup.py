import os
from setuptools import setup, find_packages


def readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


with open('requirements.txt', "r", encoding="utf-8") as rd:
    requirements = rd.read().splitlines()

setup(name='pyjitutils',
      version='1.0.1',
      author="PichaiLim",
      author_email='Pichai.Limpanitivat@gmail.com',
      description='timestamp convert to datetime',
      long_description=readme(),
      long_description_content_type="text/markdown",
      url='https://PichaiLimpanitivat@bitbucket.org/python-package/pyjitutils.git',
      package_dir={ "": "src" },
      packages=find_packages(where="src"),
      install_requires=requirements,
      python_requires='>=3.6',
      keywords='pyJitUtils jitutils src convert timestamp datetime',
      )
