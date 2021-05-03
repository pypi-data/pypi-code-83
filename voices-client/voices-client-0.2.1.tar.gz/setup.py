"""Package definition."""

from setuptools import find_packages, setup

setup(
    name='voices-client',
    version='0.2.1',
    packages=find_packages(),
    description='Voices client',
    url='https://github.com/Fondeadora/voices-client.git',
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
