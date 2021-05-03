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
    # data_files=[],#for data shared by multiple packages
    # setup_requires=['nltk']
    # Needed to silence warnings (and to be a worthwhile package)
    name='SynChron',
    # packages=['synchronicity','synchronicity.quotewidget'],
    packages = find_packages(),
    include_package_data = True,
    package_data={'': ['quotes-list.json','feeds.json']},
    url='https://github.com/sequencecentral/SynChron.git',
    author='Steve Ayers',
    author_email='steve@sequenccecentral.com',
    # Needed to actually package something
    # Needed for dependencies
    # install_requires=[''],
    # *strongly* suggested for sharing
    version='1',
    # The license can be anything you like
    license='MIT',
    # long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read(),
    # install_reqs = parse_requirements('requirements.txt', session='req')
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)

#to make an egg:
#python setup.py bdist_egg
#egg-info added

#make a dist: python setup.py sdist
# pip install twine
# twine upload dist/*
