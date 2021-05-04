import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

requirements = ["requests", "pandas", "click", "rich"]

setuptools.setup(
    name="daleydai",
    version="0.0.3",
    author="Suman Shrestha",
    url="https://github.com/sumansta/daleydai",
    description="karod bata road...",
    license="MIT",
    packages=setuptools.find_packages(exclude=["dist", "build", "*.egg-info", "tests"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    entry_points={"console_scripts": ["daleydai = daleydai.app:cli"]},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
