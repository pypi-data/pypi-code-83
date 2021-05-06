import os
import sys
import pathlib
import setuptools


setuptools.setup(
    name="ts_IntegrationTests",
    description="TSSW integration test scripts.",
    version="0.0.1",
    package_dir={"": "python"},
    packages=setuptools.find_namespace_packages(where="python"),
    scripts=["bin/simple_script.py",],
    license="GPL",
    project_urls={
        "Bug Tracker": "https://jira.lsstcorp.org/secure/Dashboard.jspa",
        "Source Code": "https://github.com/lsst-ts/ts_IntegrationTests",
    },
)
