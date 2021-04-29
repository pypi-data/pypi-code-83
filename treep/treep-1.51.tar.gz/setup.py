from pathlib import Path
import re
from setuptools import setup

version_string = "unknown"
try:
    version_string_line = open(
        str(Path(__file__).resolve().parent / "treep" / "version.py"), "rt"
    ).read()
except EnvironmentError:
    pass  # Okay, there is no version file.
else:
    version_regex_pattern = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(version_regex_pattern, version_string_line, re.M)
    if mo:
        version_string = mo.group(1)
    else:
        raise RuntimeError("unable to find version in yourpackage/_version.py")

setup(
    name="treep",
    version=version_string,
    description="managing git projects structured in tree in python",
    long_description="see https://git-amd.tuebingen.mpg.de/amd-clmc/treep",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
    keywords="project git tree",
    url="https://git-amd.tuebingen.mpg.de/amd-clmc/treep",
    author="Vincent Berenz",
    author_email="vberenz@tuebingen.mpg.de",
    license="GPL",
    packages=["treep"],
    install_requires=[
        "lightargs",
        "colorama",
        "gitpython",
        "argcomplete",
        "pyyaml",
        "future",
    ],
    scripts=["bin/treep", "bin/treep_to_yaml"],
    package_data={"treep": ["setup_treepcd.sh"]},
    include_package_data=True,
    zip_safe=False,
)
