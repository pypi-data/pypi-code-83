from setuptools import setup, find_packages

setup(
    name="mbiscuit",
    version="1.6",
    author="wangxiaolei",
    packages=find_packages(),
    install_requires=[
        "certifi==2020.12.5",
        "chardet==4.0.0",
        "colorlog==5.0.1",
        "idna==2.10",
        "PyMySQL==1.0.2",
        "requests==2.25.1",
        "urllib3==1.26.4",
        "xlwt==1.3.0",
        "GitPython==3.1.14"
    ]
)
