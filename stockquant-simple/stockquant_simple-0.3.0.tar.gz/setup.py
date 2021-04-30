# -*- coding:utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


setup(
    name="stockquant_simple",
    version="0.3.0",
    packages=[
        "stockquant",
        "stockquant/source",
        "stockquant/utils"
    ],
    platforms="any",
    description="Professional quant framework",
    url="https://github.com/Gary-Hertel/StockQuant_simple",
    author="Gary-Hertel",
    author_email="hertelquant@foxmail.com",
    license="MIT",
    keywords=[
        "stocklquant", "quant", "framework"
    ],
    install_requires=[
        "numpy",
        "requests",
        "colorlog",
        "pandas",
        "tushare",
        "baostock",
    ]
)