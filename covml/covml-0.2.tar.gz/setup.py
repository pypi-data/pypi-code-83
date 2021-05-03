# import pathlib
from setuptools import setup

# This call to setup() does all the work
setup(
    name="covml",
    version="0.2",
    description="Corona ML predictor",
    author="Shaurya Pratap Singh",
    author_email="shaurya.p.singh21@gmail.com",
    license="MIT",
    packages=["covml"],
    include_package_data=True,
    # scripts=['bin/pyserved', 'bin/pyserved-c'],
)


