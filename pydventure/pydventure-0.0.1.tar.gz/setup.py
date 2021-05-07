from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pydventure',
    version='0.0.1',
    author='Sashito Mizuki',
    author_email='sashitomizuki@gmail.com',
    package_dir={"": "pydventure"},
    packages=find_packages('pydventure'),
    url='http://pypi.python.org/pypi/pydventure/',
    license='LICENSE.txt',
    description='Write your Text-Adventure game.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
    ],
)