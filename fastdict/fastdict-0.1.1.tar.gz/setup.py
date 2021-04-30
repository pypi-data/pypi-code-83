# from __future__ import absolute_import
import os
import sys
from setuptools import setup

NAME = "fastdict"
INSTALL_REQUIRES = [
]

dirname = os.path.dirname(os.path.abspath(__file__))
if dirname not in sys.path:
    sys.path.insert(0, dirname)
try:
    import fastdict
    version = fastdict.__version__
except Exception:
    print("import project error")
    exit(-1)

readme = os.path.join(dirname, "README")

setup(
    name=NAME,
    version=fastdict.__version__,
    description="Python fastdict with attribute",
    long_description=open(readme).read(),
    packages=[NAME],
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    author="StevenKang",
    author_email="kangweibaby@163.com",
    url="https://github.com/StevenBaby/fastdict",
    license="MIT",
    include_package_data=True,
    zip_safe=True,
    platforms="any",
)


# python setup.py sdist bdist_wheel --universal
# twine upload dist/*
# pip2 install fastdict --upgrade -i https://pypi.python.org/simple
# pip3 install fastdict --upgrade -i https://pypi.python.org/simple
