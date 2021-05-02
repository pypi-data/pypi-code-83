from setuptools import setup

setup(
    name="QuickCite",
    version="0.0.3",
    description="Pure Python wrapper for the Formatically Citation Website.",
    py_modules=["QuickCite"],
    package_dir={'':'src'},
    install_requires = [
        "requests==2.25.1"
    ],
    url="https://github.com/http-samc/citer",
    author="Samarth Chitgopekar",
    author_email="sam@chitgopekar.tech"
)