import setuptools

with open("readme.txt", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="scriptnorm",
    version="4.0",
    author="Ramy Eskander",
    author_email="rnd2110@columbia.edu",
    description="A library for text normalization for a set of languages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rnd2110/SCRIPTS_Normalization",
    packages=["scriptnorm"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
