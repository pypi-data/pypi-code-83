import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(
    name='fit-tracker',
    version='0.0.0dev',
    description='A lightweight experiment tracker for numerical optimization problems.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/atraders/fit-tracker',
    author='@genziano',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='ml, operation research, optimization, logging',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=[],
    extras_require={'dev': ['pylint', 'pytest', 'mypy', 'isort'],},
)
