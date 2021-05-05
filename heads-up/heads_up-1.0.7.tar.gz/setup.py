import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="heads_up",
    version="1.0.7",
    description="Receive alerts locally and remotely at certain stages of your code execution.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/heads-up-org/heads-up",
    author="Deniz Iren",
    author_email="deniziren@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["headsup"],
    include_package_data=True,
    install_requires=["requests", "pynput", "playsound", "qrcode[pil]", "numpy", "matplotlib"],
    entry_points={
        "console_scripts": [
            "headsup=headsup.__main__:main",
        ]
    },
)