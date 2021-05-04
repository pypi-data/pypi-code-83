from setuptools import setup

setup(
    name='scd_courses',
    version='0.1',
    description='currency exchange rates',
    packages=['scd_courses'],
    author_email='ivanbalashov2019@gmail.com',
    zip_safe=False, install_requires=['requests', 'bs4']
)