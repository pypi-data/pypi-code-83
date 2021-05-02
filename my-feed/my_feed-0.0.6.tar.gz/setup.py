import subprocess
import os
from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

packages = find_packages(exclude=['tests*'])

remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

assert "." in remote_version
assert os.path.isfile("my_feed/version.py")

with open("my_feed/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{remote_version}\n")

setup(
    name='my_feed',
    version=remote_version,
    license='LGPLv3',

    author='HoodyH',
    description='A single service to get all your feed',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/HoodyH/My-Feed',

    packages=packages,
    package_data={"my_feed": ["VERSION"]},
    include_package_data=True,

    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],

    python_requires='>=3.7',
    install_requires=[
        'requests',
        'bs4'
    ],
)
