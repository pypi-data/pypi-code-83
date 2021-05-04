"""Packaging script for Science Data Challenge (SDC) 2 scoring utilities.

https://packaging.python.org/tutorials/packaging-projects/
"""
from setuptools import setup, find_packages

with open("README.md", "r") as file:
    README = file.read()

package_version = {}
with open("src/ska_sdc2_scoring_utils/__version__.py") as file:
    exec(file.read(), package_version)


setup(
    name="ska_sdc2_scoring_utils",
    version=package_version["__version__"],
    author="SKA Organisation",
    description="Utility scripts for interacting with SKA SDC2 scoring service.",
    url="https://gitlab.com/ska-telescope/sdc/sdc2-scoring-utils",
    license="License :: OSI Approved :: BSD License",
    long_description=README,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=["docopt", "python-keycloak", "requests"],
    package_dir={"": "src"},
    packages=find_packages("src"),
    entry_points={
        "console_scripts": [
            "sdc2-score=ska_sdc2_scoring_utils.sdc2_score:main",
            "sdc2-score-admin=ska_sdc2_scoring_utils.sdc2_score_admin:main",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
)
