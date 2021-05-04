from setuptools import setup

setup(
    name="TCRnumba",
    version='0.1.0',
    description="some description",
    url="https://github.com/Paul44444/capybaras_test",
    author='Paul',
    author_email='richtepp@physik.hu-berlin.de',
    license='BSD 2-clause',
    packages=['TCRnumba'],
    #install_requires=["mpi4py>=2.0","numpy", "numba", "scipy"], #TODO: finish this list
    install_requires=["mpi4py>=2.0","numpy", "numba", "scipy"], 
    #classifiers=[],
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
