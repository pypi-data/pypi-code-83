import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mcs_matplotlib",
    version="1.0.1",
    description="More utilities for matplotlib",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/moderncoursesquare/pythonlib",
    author="moderncoursesquare",
    author_email="moderncoursesquare@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["mcs_matplotlib"],
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)

