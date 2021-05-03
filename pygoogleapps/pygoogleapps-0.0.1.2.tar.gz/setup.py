import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION.txt", "r") as fh:
    version = fh.read().strip()

setuptools.setup(
    name='pygoogleapps',
    version=version,
    author="Kevin Crouse",
    author_email="krcrouse@gmail.com",
    description='A module to provide a stateful wrapper around the Google App system',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/krcrouse/pygoogleapps",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],    
    install_requires=[
        'dateutil.parser',
        'google.auth',
        'googleapiclient',
        'http2lib',
    ],
)
