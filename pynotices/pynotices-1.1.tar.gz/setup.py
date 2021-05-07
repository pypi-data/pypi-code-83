# coding: utf-8
import setuptools
"""
打包的用的setup必须引入，
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
if sys.version_info < (2, 5):
    sys.exit('Python 2.5 or greater is required.')

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", 'r') as f:
    long_description = f.read()

# 版本号，自己随便写
VERSION = "1.0.1"

LICENSE = "MIT"


setup(
    name='pynotices',
    version=1.1,
    description='The information notification module developed by python3 includes nailing, email, enterprise wechat and flybook',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='SpiderZhong',
    author_email='5805461@qq.com',
    maintainer='zhongqinghao',
    maintainer_email='root@ihack.cc',
    license=LICENSE,
    packages=setuptools.find_packages(),
    platforms=["all"],
    url='https://github.com/ZhongQingHao/pynotice',
    install_requires=["requests",],
    classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ],
)


# URL 你这个包的项目地址，如果有，给一个吧，没有你直接填写在PyPI你这个包的地址也是可以的
# INSTALL_REQUIRES 模块所依赖的python模块
# 以上字段不需要都包含
