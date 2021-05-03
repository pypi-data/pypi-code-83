from setuptools import setup
from pathlib import Path

codeDirectory = Path(__file__).parent
readme = (codeDirectory / "README.markdown").read_text()

setup(
    name = "ashmail",
    version = "v2.1.0",
    description = "the free and simple mass emailing system",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/0x44RU5H/ashmail",
    author = "Aarush Gupta",
    author_email = "aarush@theaarushgupta.com",
    license = "AGPLv3+",
    classifiers = [
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    packages = ["ashmail"],
    package_data = {},
    install_requires = ["jinja2", "pyyaml"],
    entry_points = {
        "console_scripts": ["ashmail = ashmail.ashmail:main"]
    }
)