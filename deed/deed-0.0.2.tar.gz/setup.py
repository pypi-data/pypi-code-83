from setuptools import find_packages, setup


setup(
    name='deed',
    version='0.0.2',
    description='ActivityFormatter for object changes (auditlog)',
    author='TruckPad',
    url='https://github.com/TruckPad/deed-py',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    install_requires=['jsonpatch>=1.32'],
    license="Apache License 2.0",
    python_requires=">= 2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
)
