from setuptools import find_packages, setup
from my_pip_pkg import __version__
import pathlib

#The directory containing this file

HERE = pathlib.Path(__file__).parent


#The text to the README file
README = (HERE / "README.md").read_text()

setup(
	name='CS253A_try_new',
	version = "1.0.3",
	description= "Demo/ revision for the endsem of CS253",
	url='https://demo_project.com/dummy.xml',
	long_description=README,
	long_description_content_type="text/markdown",
	author='Vishesh',
	author_email='visheshkaushik.99@gmail.com',
	install_requires=["numpy"],
	packages=find_packages(),
)
