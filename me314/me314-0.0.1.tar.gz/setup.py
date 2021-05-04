import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='me314',
    version='0.0.1',
    author='Muchen Sun',
    description='Northwestern ME314 toolbox',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'numpy',
        'sympy',
    ],
    url='https://github.com/MuchenSun/me314',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)

