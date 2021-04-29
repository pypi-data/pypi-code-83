import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='cortx_jupyter',
    version='0.1.135',
    author='Sumanth Reddy Muni & Priyadarshini Murugan',
    description='Jupyter Notebook Manager for Cortx',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['traitlets',
                      'tornado',
                      'boto3',
                      'joblib',
                      'pandas',
                      'numpy',
                      'notebook',
                      'nbformat',
                      'asyncio'],
    url='https://github.com/sumanthreddym/cortx_jupyter',
    packages=setuptools.find_packages()
)
