# Copyright 2021 Nicene Nerd <email@calebdixonsmith.top>
# Licensed under GPLv3+

from setuptools import setup
from uking_saves import VERSION

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="uking-saves",
    version=VERSION,
    author="NiceneNerd",
    author_email="email@calebdixonsmith.top",
    description="Parse and modify BOTW save files",
    license="GPLv3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NiceneNerd/uking-saves/",
    include_package_data=True,
    packages=["uking_saves"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.7"
)
