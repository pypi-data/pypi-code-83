from setuptools import find_packages, setup
from my_pip_pkg import __version__
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
#his call to setup() does all the work
setup(
    name='cs253_demotry_pip',
    version="1.0.1",

    description="A demo peoject for CS253 presentation",
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://demo_project.com/dummy.xml',
    author='Navya',
    author_email='navyaa@iitk.ac.in',
    packages=find_packages(),
    install_requires=["numpy"],
)
