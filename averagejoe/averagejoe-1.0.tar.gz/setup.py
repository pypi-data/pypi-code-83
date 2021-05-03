import setuptools.command.build_py
from setuptools import setup, find_packages
from setuptools.command.install import install as _install

#custom post-installation steps go here:
class Install(_install):
    def run(self):
        _install.do_egg_install(self)
        #nothing else to do

setup(
    cmdclass={
        'install': Install,
    },
    name='averagejoe',
    packages=find_packages(),
    description='averagejoe',
    author='Steve Ayers, Ph.D.',
    author_email='steve@sequenccecentral.com',
    version='1.0',
    include_package_data = True,
    package_data={'': []},
    url='https://github.com/sequencecentral/averagejoe.git',
    # git+https://github.com/sequencecentral/averagejoe.git@main#egg=averagejoe
    # Needed to actually package something
    # Needed for dependencies
    # install_requires=[''],
    # *strongly* suggested for sharing
    # The license can be anything you like
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=['DateTime==4.3', 'numpy==1.20.2', 'pytz==2021.1', 'zope.interface==5.3.0'],
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
#to make an egg:
#python setup.py bdist_egg
