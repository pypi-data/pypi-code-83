import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="codeforces-cli",
    version="1.0",
    description="Command line interface for Codeforces",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/aakashdinkar/codeforces-cli",
    author="Aakash Dinkar",
    author_email="aakashdinkar1307@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    # packages=find_packages(),
    packages = ['codeforces'],
    install_requires=['requests', 'tabulate', 'beautifulsoup4'],
    keyword = ['cf-cli'],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "codeforeces=codeforeces.__main__:codeforces",
        ]
    },
)