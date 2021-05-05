import setuptools

long_description = """
This is a very basic physics calulator! Atributes are
-> momentum
-> avg_speed
-> impulse
-> distance
-> distance_from_acceleration
-> accelertaion_with_velocity
-> accelertaion_with_force


"""

setuptools.setup(
     name='phycalc',
     version='0.2.1',
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
