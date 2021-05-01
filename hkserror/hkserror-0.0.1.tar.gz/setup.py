import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="hkserror",
    version="0.0.1",
    author="huykingsofm",
    author_email="huykingsofm@gmail.com",
    description="The module defines some popular errors of hks python modulesystems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/huykingsofm/hkserror",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3",
    install_requires=[]
)