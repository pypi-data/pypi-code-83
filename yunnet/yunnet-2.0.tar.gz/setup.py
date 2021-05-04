# coding: UTF-8
from setuptools import setup

setup(
    name="yunnet",
    version="2.0",
    description="Wrapper for yunnet.ru",
    packages=["yunnet"],
    install_requires=["httpx"],
    author_email="noreply@yunnet.ru",
    zip_safe=False,
)
