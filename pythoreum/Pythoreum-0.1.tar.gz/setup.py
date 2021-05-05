import setuptools

long_description = """
This is a package to calculate The Pythagoreas theoreum!
"""

setuptools.setup(
     name='Pythoreum',
     version='0.1',
     author="Snehashish Laskar",
     author_email="snehashish.laskar@gmail.com",
     description="A simpple Pythogoreus theorum calculator!",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )