import setuptools
def readme():
    with open("README.md") as f:
        return f.read()

setuptools.setup(
  name='chebxroots',
  version='0.1.5',
  author='Anna Clara Wendler, Mira Kristin Juergens, Lars Lammers',
  author_email = 'lars.lammers@stud.uni-goettingen.de' ,
  packages=["chebxroots"],
  url='https://gitlab.gwdg.de/annaclara.wendler/scientific-computing-chebychev-roots/',
  license='MIT',
  description='A package for computing roots of generic smooth functions.',
  #long_description=open('README.txt').read(),
  install_requires=[
       "scipy",
       "numpy",
       "pytest",
       "matplotlib"
   ],
)
