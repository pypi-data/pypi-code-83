# template is from https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
# another thanks to python + pypi docs and qutebrowser

from distutils.core import setup

setup(
    name = 'AscentAurora',
    packages = ['AscentAurora'],
    version = '0.0.1.4',
    license = 'GPL v3',
    description = 'A library with the goal of simplifying the development of PyQt/PySide apps.',
    author = 'DespawnedDiamond',
    author_email = 'despawnedd@acrazytown.com',
    url = 'https://github.com/despawnedd/AscentAurora/',
    download_url = 'https://github.com/despawnedd/AscentAurora/dist/AscentAurora-0.0.1.4.tar.gz',
    keywords = ['qtpy', "PyQt", "PyQt5", "PySide", "PySide2"],
    install_requires = [
        'qtpy'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
