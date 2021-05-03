import camfr
import setuptools

setuptools.setup(
    name=camfr.__name__,
    version=camfr.__version__,
    author=camfr.__author__,
    description=camfr.__doc__,
    long_description=open("README.md", "r").read(),
    author_email="floris.laporte@gmail.com",
    long_description_content_type="text/markdown",
    url="http://github.com/flaport/camfr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
    ],
)
