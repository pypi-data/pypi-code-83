from setuptools import setup, Extension
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='split_layer',
    version='0.1.1',
    author='swordfate',
    author_email='1317732065@qq.com',
    url='',
    description=u'Print each layer forward and backward time of PyTorch models.',
    long_description_content_type='text/markdown',
    long_description = long_description,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[],
    entry_points={
        'console_scripts': [
        ]
    }
)
