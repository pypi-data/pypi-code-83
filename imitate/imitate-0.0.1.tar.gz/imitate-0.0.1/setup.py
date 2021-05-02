#!/usr/bin/env python

import argparse
import os
import shutil
import subprocess
import sys

import numpy
import setuptools.command.build_py
import setuptools.command.develop

from setuptools import find_packages, setup
from setuptools import setup, Extension
from Cython.Build import cythonize

# parameters for wheeling server.
parser = argparse.ArgumentParser(add_help=False, allow_abbrev=False)
parser.add_argument('--checkpoint',
                    type=str,
                    help='Path to checkpoint file to embed in wheel.')
parser.add_argument('--model_config',
                    type=str,
                    help='Path to model configuration file to embed in wheel.')
args, unknown_args = parser.parse_known_args()

# Remove our arguments from argv so that setuptools doesn't see them
sys.argv = [sys.argv[0]] + unknown_args

version = '0.0.1'
cwd = os.path.dirname(os.path.abspath(__file__))

# Handle Cython code
# def find_pyx(path='.'):
#     pyx_files = []
#     for root, _, filenames in os.walk(path):
#         for fname in filenames:
#             if fname.endswith('.pyx'):
#                 pyx_files.append(os.path.join(root, fname))
#     return pyx_files


# def find_cython_extensions(path="."):
#     exts = cythonize(find_pyx(path), language_level=3)
#     for ext in exts:
#         ext.include_dirs = [numpy.get_include()]

#     return exts


class build_py(setuptools.command.build_py.build_py):  # pylint: disable=too-many-ancestors
    def run(self):
        self.create_version_file()
        setuptools.command.build_py.build_py.run(self)

    @staticmethod
    def create_version_file():
        print('-- Building version ' + version)
        version_path = os.path.join(cwd, 'version.py')
        with open(version_path, 'w') as f:
            f.write("__version__ = '{}'\n".format(version))


class develop(setuptools.command.develop.develop):
    def run(self):
        build_py.create_version_file()
        setuptools.command.develop.develop.run(self)


# The documentation for this feature is in server/README.md
package_data = ['imitatetts/server/templates/*']

if 'bdist_wheel' in unknown_args and args.checkpoint and args.model_config:
    print('Embedding model in wheel file...')
    model_dir = os.path.join('imitatetts', 'server', 'model')
    tts_dir = os.path.join(model_dir, 'tts')
    os.makedirs(tts_dir, exist_ok=True)
    embedded_checkpoint_path = os.path.join(tts_dir, 'checkpoint.pth.tar')
    shutil.copy(args.checkpoint, embedded_checkpoint_path)
    embedded_config_path = os.path.join(tts_dir, 'config.json')
    shutil.copy(args.model_config, embedded_config_path)
    package_data.extend([embedded_checkpoint_path, embedded_config_path])


def pip_install(package_name):
    subprocess.call([sys.executable, '-m', 'pip', 'install', package_name])


requirements = open(os.path.join(cwd, 'requirements.txt'), 'r').readlines()
with open('README.md', "r", encoding="utf-8") as readme_file:
    README = readme_file.read()

exts = [Extension(name='imitatetts.imitate.layers.glow_tts.monotonic_align.core',
                  sources=["H:\ImitateTTS\TTS\imitatetts\imitate\layers\glow_tts\monotonic_align\core.pyx"])]
setup(
    name='imitate',
    version=version,
    url='https://github.com/AdityaCyberSafe/ImitateTTS',
    author='Aditya Sunil Patil',
    author_email='admin@cybersafe.ezyro.com',
    description='An open-source deep learning TTS Engine for people with speech disoders',
    license='MIT',
    # cython
    include_dirs=numpy.get_include(),
    ext_modules=cythonize(exts, language_level=3),
    # ext_modules=find_cython_extensions(),
    # package
    include_package_data=True,
    packages=find_packages(include=['imitatetts*']),
    project_urls={
        'Documentation': 'https://github.com/mozilla/TTS/wiki',
        'Tracker': 'https://github.com/AdityaCyberSafe/ImitateTTS/issues',
        'Repository': 'https://github.com/AdityaCyberSafe/ImitateTTS',
        'Discussions': 'https://github.com/AdityaCyberSafe/ImitateTTS/discussions',
    },
    cmdclass={
        'build_py': build_py,
        'develop': develop,
        # 'build_ext': build_ext
    },
    install_requires=requirements,
    python_requires='>=3.6.0, <3.9',
    entry_points={
        'console_scripts': [
            'imitate = imitatetts.bin.synthesize:main',
            'imitate-server = imitatetts.server.server:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Development Status :: 3 - Alpha',
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    zip_safe=False
)
