import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="firex",
    version="0.0.1",
    author="Sarmad Gulzar",
    author_email="sarmadgulzar@hotmail.com",
    description="Firebase with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarmadgulzar/firex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["firebase-admin==5.0.0"],
    python_requires='>=3.6',
)
