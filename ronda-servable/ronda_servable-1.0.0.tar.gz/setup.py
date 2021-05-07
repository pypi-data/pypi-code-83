import os
import re

from setuptools import find_packages
from setuptools import setup


def read_version():
    regexp = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")
    init_py = os.path.join(os.path.dirname(__file__), "ronda_servable", "__init__.py")
    with open(init_py) as f_in:
        for line in f_in:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)
        raise RuntimeError("Cannot find version in {}".format(init_py))


setup(
    name="ronda_servable",
    version=read_version(),
    url="https://git.woa.com/RondaServing/RondaServable/RondaPythonServable",
    project_urls={
        "Documentation": "https://git.woa.com/RondaServing/RondaServable/RondaPythonServable/wikis/home",
        "Code": "https://git.woa.com/RondaServing/RondaServable/RondaPythonServable",
        "Issue tracker": "https://git.woa.com/RondaServing/RondaServable/RondaPythonServable/issues",
    },
    maintainer="Ronda Serving Group",
    description="Ronda Python Servable",
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "automaxprocs",
        "pynvml"
    ],
    packages=find_packages(include=("ronda_servable", "ronda_servable.*")),
    package_data={'': ['*.so']},
)
