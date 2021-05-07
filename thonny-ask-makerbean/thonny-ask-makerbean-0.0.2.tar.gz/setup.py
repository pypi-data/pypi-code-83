# -*- coding: utf-8 -*-
# @Author: ander
# @Date:   2021-03-29 16:59:00
# @Last Modified by:   Anderson
# @Last Modified time: 2021-05-07 18:06:01
import setuptools


setuptools.setup(
    name="thonny-ask-makerbean",
    version="0.0.2",
    author="Maker Bi",
    author_email="by@zaowanwu.com",
    description="",
    url="https://makerbean.com",
    packages=setuptools.find_namespace_packages(),
    package_data={
        "thonnycontrib.ask-makerbean": ['res/*'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "thonny >= 3.0.0",
        'requests',
        'pyperclip'
    ],
    python_requires='>=3.7',
)
