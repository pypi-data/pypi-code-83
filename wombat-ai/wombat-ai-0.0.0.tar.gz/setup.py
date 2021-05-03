import wombat
import setuptools

setuptools.setup(
    name=f"{wombat.__name__}-ai",
    version=wombat.__version__,
    author=wombat.__author__,
    description=wombat.__doc__,
    long_description=open("readme.md", "r").read(),
    author_email="floris.laporte@gmail.com",
    long_description_content_type="text/markdown",
    url="http://github.com/flaport/wombat",
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
