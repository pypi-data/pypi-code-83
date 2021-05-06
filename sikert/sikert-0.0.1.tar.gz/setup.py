
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = "Sikert let's you do subdomain enumeration"
LONG_DESCRIPTION = 'A package that allows to enumerate subdomain from different sources'

# Setting up
setup(
    name="sikert",
    version=VERSION,
    author="Deepanjal kumar (Operation Falcon)",
    author_email="operationfalcon6@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['certifi==2020.12.5', 'chardet==4.0.0', 'idna==2.10', 'requests==2.25.1', 'termcolor==1.1.0', 'urllib3==1.26.4'],
    keywords=['python', 'sikert', 'subdomain enumeration', 'sources'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix"
    ]
)