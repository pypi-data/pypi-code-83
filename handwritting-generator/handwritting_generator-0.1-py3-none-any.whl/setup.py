import os
import setuptools

setuptools.setup(
     name='handwritting_generator',  
     version='0.1',
     license='MIT',
     author="Constantin Werner",
     author_email="const.werner@gmail.com",
     description="Generates images of handwritten text",
     include_package_data=True,
     keywords=['data','computer vision', 'augmentation', 'handwritting','generator'],
     url="https://github.com/constantin50/handwritting_generator",
     packages=setuptools.find_packages(),
     install_requires=["Pillow"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
