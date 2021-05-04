from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name = 'visdm',
    version = '0.0.2',
    description = 'A Python package arraning methods for Data Mining Visualization.',
    long_description = readme(),
    long_description_content_type = 'text/markdown',
    # url = 'https://gitlab.com/popolinneto/exmatrix',
    author = 'Mario Popolin Neto',
    license = 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International',
    classifiers = [
        'License :: Free for non-commercial use',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],
    package_dir = { '': 'src' },
    packages = [ 'visdm' ],
    python_requires = '>=3.6',
    install_requires = [ 'numpy>=1.16.0', 'scikit-learn>=0.20.0' ],
)