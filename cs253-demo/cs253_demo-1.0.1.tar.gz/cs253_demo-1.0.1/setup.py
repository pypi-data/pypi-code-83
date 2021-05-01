from setuptools import find_packages, setup
from my_pip_pkg import __version__
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(
    name='cs253_demo',
    version=__version__,
    description='Demo Project',
    url='https://demo_project.com/dummy.xml',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Sathvik Bhagavan',
    author_email='sathvikb@iitk.ac.in',
    install_requires=['numpy'],
    packages=find_packages()
)