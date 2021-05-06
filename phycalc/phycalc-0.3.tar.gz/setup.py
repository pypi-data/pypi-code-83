import setuptools

long_description = """
This is a very basic physics calulator! There are three classes: \n 
-> acceleration:\n
-> motion\n
-> momentum\n
"""

setuptools.setup(
     name='phycalc',
     version='0.3',
     author="Snehashish Laskar",
     author_email="snehashish.laskar@gmail.com",
     description="A Simple Physics calculator",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
