from setuptools import setup

setup(
    name='itsdevtime',
    version='0.0.2',
    url='https://gitlab.com/vladcalin/itsdevtime',
    author='Vlad Călin',
    author_email='contact@vladcalin.ro',
    install_requires=[
        'click',
        'pyyaml',
        'requests',
        'colorlog'
    ],
    entry_points={
        'console_scripts': [
            'itsdevtime = itsdevtime.cli:main'
        ]
    },
    extras_require={
        'dev': [
            'bump2version',
            'twine',
            'pytest',
        ]
    }
)
