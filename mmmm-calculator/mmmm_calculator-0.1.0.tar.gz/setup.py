from setuptools import setup, find_packages

BASE_DIR = "/home/manas/Codes/uploading_to_pypi/"

setup(
    name="mmmm_calculator",
    version="0.1.0",
    author="Manas Mishra",
    author_email="manas.m22@gmail.com",
    description=("Basic calculator to test uploading packages to pypi"),
    license="MIT",
    keywords="",
    url="https://github.com/manasm11/uploading_to_pypi",
    packages=find_packages(include=["mmmm_calculator", "mmmm_calculator.*"]),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Other Audience",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=open(BASE_DIR + "requirements.txt").readlines(),
)
