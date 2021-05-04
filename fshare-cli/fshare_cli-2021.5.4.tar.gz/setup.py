from setuptools import setup

# Get the version from fshare_cli/version.py without importing the package
exec(compile(open('fshare_cli/version.py').read(), 'fshare_cli/version.py', 'exec'))

DESCRIPTION = '[Unofficial] Fshare command-line interface',
LONG_DESCRIPTION = 'An unofficial command-line program to download files from Fshare.vn'

setup(
    name='fshare_cli',
    version=__version__,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url='https://github.com/pltchuong/fshare-cli',
    author='Phan Chuong',
    author_email='pltchuong@gmail.com',
    maintainer='Phan Chuong',
    maintainer_email='pltchuong@gmail.com',
    license='Unlicense',

    packages=[
        'fshare_cli',
    ],

    install_requires = [
        'easysettings==4.0.0',
        'colorlog==5.0.1',
        'requests==2.25.1',
        'pycurl==7.43.0.5',
        'tqdm==4.60.0',
    ],

    classifiers=[
        'Topic :: Software Development :: Build Tools',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    entry_points={
        'console_scripts': [
            'fshare = fshare_cli.__main__:main',
        ],
    },
)
