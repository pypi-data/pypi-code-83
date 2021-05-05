from os import read
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as f:
    readme = f.read()


setup(
    name='flaskspot',
    version='0.1.0',
    description="FlaskSpot provides Starter Kits for Flask.",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Abhijeet Sonawane",
    author_email="abhijeet.sonawane001@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "flaskspot = flaskspot:cli"
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='flaskspot flaskproject flaskstarterkit'
)