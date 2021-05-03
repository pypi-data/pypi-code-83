import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION.txt", "r") as fh:
    version = fh.read().strip()

setuptools.setup(
     name='pysqltemplate',
     version=version,
     author="Kevin Crouse",
     author_email="krcrouse@gmail.com",
     description="A package to write composable, generic SQL objects that can be flexibly reused and combined. Like an ORM, but not an ORM.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://gitlab.com/krcrouse/sqltemplate",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3.7",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
         "Development Status :: 3 - Alpha"
     ],
 )
