import setuptools

long_description = """
This is a very basic mensuration calculator that can calculate area, perimeter, volume, surface area and lateral surface area of a shape!
"""

setuptools.setup(
     name='mencalc',
     version='0.1',
     author="Snehashish Laskar",
     author_email="snehashish.laskar@gmail.com",
     description="A Simple Mensuration calculator",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )