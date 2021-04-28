from setuptools import setup
from setuptools import find_packages
from os import path

install_requires = [
    "txaio",
    "h5py",
    "autobahn",
    "twisted[tls]",
    "autobahn_sync",
    "jupyter",
    "pyOpenSSL",
    "seaborn",
    "requests",
    "dataclasses; python_version<'3.7'",
    "msgpack",
    "msgpack-numpy",
    "neuroballad",
    "service_identity",
    "crochet",
    "matplotlib",
    "fastcluster",
    "networkx",
    "pandas",
    "scipy",
    "sympy",
    "nose",
    "jupyterlab>=2.2.8, <=3.0.10",
    "pywin32; platform_system=='Windows'"
]

extras_require_utilities = {
        "graspy<=0.1.1",
        "umap-learn",
        "tensorflow",
        "graphviz",
        "sklearn",
        "cdlib",
        "pyclustering",
    }

extras_require_full = extras_require_utilities

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name="FlyBrainLab",
    version="1.1.5",
    description="Main Client of the FlyBrainLab Project",
    author="Mehmet Kerem Turkcan",
    author_email="mkt2126@columbia.edu",
    url="https://flybrainlab.fruitflybrain.org",
    download_url="",
    license="BSD-3-Clause",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    extras_require = {
        "full": extras_require_full,
        "utilities": extras_require_utilities,
    },
    dependency_links=["https://github.com/flybrainlab/neuroballad/tarball/master#egg=neuroballad-0.1.0",
                      "https://github.com/mkturkcan/autobahn-sync/tarball/master#egg=autobahn_sync-0.3.2",
                      "https://github.com/palash1992/GEM/tarball/master#egg=gem-1.0.0",
                      "https://github.com/mkturkcan/nxcontrol/tarball/master#egg=nxcontrol-0.2"],
    packages=find_packages(),
)
