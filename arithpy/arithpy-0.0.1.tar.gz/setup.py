import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arithpy",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Suresh Mishra",                     # Full name of the author
    description="ArithPy is a simple and easy to use python moduloe made for basic arithmetic operations. The main purpose of creating such python module is to help developers to do calculations quickly in their programs made made by two school going students Suresh Mishra and Sai Binayak Biswal.",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["arithpy"],             # Name of the python package
    package_dir={'':'arithpy/src'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)