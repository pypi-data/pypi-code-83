import pathlib
from setuptools import setup, find_packages
from mlfix import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

requirements = [
    "pyyaml == 5.4.1",
]

setup(
    name="mlfix",
    version=__version__,
    url="https://github.com/konradmalik/mlfix.git",
    author="Konrad Malik",
    author_email="konrad.malik@gmail.com",
    license="MIT",
    description="mlflow artifact store migration fix tool",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": ["mlfix = mlfix.__main__:main"],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
