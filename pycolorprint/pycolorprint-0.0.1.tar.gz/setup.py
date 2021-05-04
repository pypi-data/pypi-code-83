from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Colorful pretty printer for python!'
LONG_DESCRIPTION = 'A python pretty printer that uses ANSI characters to make terminal output colorful.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="pycolorprint",
        version=VERSION,
        author="Alexander Steffen",
        author_email="alexsteffen55@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package.
        
        keywords=['python', 'pretty printer', 'print', 'colorful', 'color', 'color printer', 'color print'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)