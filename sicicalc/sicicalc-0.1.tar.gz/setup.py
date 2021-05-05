import setuptools

long_description = """
This is a package to calculate Simple and Compund Intrest!
"""

setuptools.setup(
     name='sicicalc',
     version='0.1',
     author="Snehashish Laskar",
     author_email="snehashish.laskar@gmail.com",
     description="A Simple and Compound Intrest calculator",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )