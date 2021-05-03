"""Package definition."""

from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='voices-client',
    version='0.2.6',
    packages=find_packages(),
    description='Voices client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Fondeadora/voices-client.git',
    package_data=dict(voices=['py.typed']),
    author='Fondeadora',
    author_email='tech@fondeadora.com',
    keywords=['client', 'voices', 'package'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
