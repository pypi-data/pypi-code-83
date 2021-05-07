import setuptools
from setuptools import find_packages
from setuptools.command.build_py import build_py as build_py_orig


class CustomBuildPy(build_py_orig):
    """
    subclass build_py so that we collect no .py files inside the built pip package
    this is done by overriding build_packages method with a noop
    """
    def build_packages(self):
        pass


with open("README.md", "r") as fh:
    long_description = fh.read()

#
# with open('./requirements.txt', 'r') as requirements:
#     requirements_buffer = requirements.read().split("\n")


directives = {
    'language_level': 3,
    'always_allow_keywords': True
}

setuptools.setup(
    name="monolithcaching",
    version="0.0.4",
    author="Maxwell Flitton",
    author_email="maxwell@gmail.com",
    description="Python package for monolithcaching",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MonolithAILtd/caching",
    install_requires=[
        "astroid==2.4.2",
        "boto3==1.14.38",
        "botocore==1.17.38",
        "docutils==0.15.2",
        "isort==5.4.2",
        "jmespath==0.10.0",
        "lazy-object-proxy==1.4.3",
        "mccabe==0.6.1",
        "mock==4.0.2",
        "pylint==2.6.0",
        "python-dateutil==2.8.1",
        "redis==3.5.3",
        "s3transfer==0.3.3",
        "six==1.15.0",
        "toml==0.10.1",
        "typed-ast==1.4.1",
        "urllib3==1.25.10",
        "wrapt==1.12.1"
    ],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'caching-hello = monolithcaching.console_commands.hello:print_logo',
        ],
    }
)
