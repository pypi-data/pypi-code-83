from setuptools import setup, find_packages
import pathlib

# recupero il path assoluto di setup.py e si suppone che sia anche la root del progetto
s_here = pathlib.Path(__file__).parent.resolve()

# resupero il testo del file README.md che presenta il progetto
s_prj_long_description = (s_here / 'README.md').read_text(encoding='utf-8')

setup(
    name='xenia_generic',
    version='0.0.0',
    description='Xenia Generic Utilities',
    long_description=s_prj_long_description,
    url='https://github.com/xenia2023/xenia_generic',
    packages=['xenia_generic'],  # packages=find_packages(where='xenia_generic')
    author='Stefano Gigli',
    author_email='xenia-dev@programmer.net',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='colored text, id generator, debugging, parameters check, strings functions',
    project_urls={
        # 'Bug Reports': '',  # 'https://github.com/pypa/sampleproject/issues',
        # 'Funding': '',  # 'https://donate.pypi.org',
        # 'Say Thanks!': '',  # 'http://saythanks.io/to/example',
        'Source': 'https://github.com/xenia2023/xenia_generic'  # 'https://github.com/pypa/sampleproject/',
    }
)
