import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
 name="cmc_csci046_.yilinli_trees",
 version="1.0.0",
 description="Implement efficent data structures",
 long_description=README,
 url="https://github.com/yilinli22/homework8/",
 author="Yilin Li",
 author_email="yilli@students.pitzer.edu",
 license="MIT",
 classifiers=[
     "License :: OSI Approved :: MIT License",
     "Programming Language :: Python :: 3",
     "Programming Language :: Python :: 3.7",
],
 packages=find_packages(exclude=("tests")),
 include_package_data=True,
 long_description_content_type='text/markdown',
 install_requires=["pytest", "attrs", "hypothesis"])
 