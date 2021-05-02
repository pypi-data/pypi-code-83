from setuptools import setup, find_packages

setup(
    name="mmcrypto",
    author="Manas Mishra",
    author_email="manas.m22@gmail.com",
    description="Package to give crypto trading signals in wazirx",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/manasm11/mmcrypto",
    version="0.0.0",
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),
    python_requires=">=3.7",
)
