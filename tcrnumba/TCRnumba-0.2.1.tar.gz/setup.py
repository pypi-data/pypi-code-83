from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="TCRnumba",
    version='0.2.1',
    description="some description",
    url="https://github.com/Paul44444/capybaras_test",
    author='Paul',
    author_email='richtepp@physik.hu-berlin.de',
    license='BSD 2-clause',
    packages=['TCRnumba'],
    #install_requires=["mpi4py>=2.0","numpy", "numba", "scipy"], #TODO: finish this list
    install_requires=["mpi4py>=2.0","numpy", "numba", "scipy", "networkx", 
        "matplotlib", "time", "pandas", "math", "sys", "argparse", "os"], 
    #classifiers=[],
    
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
) 
