import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_containers_nick",
    version="1.0.0",
    description="Have access to codes that properly implement unicode and heap functions",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nickwilson3/containers_nick",
    author="Nick Wilson",
    author_email="nwilson23@cmc.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "cmc_csci046_containers_nick=reader.__main__:main",
        ]
    },
)
