from distutils.core import setup

with open('README.md') as handle:
    long_description = handle.read()

setup(
    name='querycolumns',
    version='0.1.0',
    packages=['querycolumns'],
    description='Pandas utility for handling very wide DataFrames',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Yaniv Aknin',
    author_email='yaniv@aknin.name',
    url="https://github.com/yaniv-aknin/querycolumns",
    license='MIT',
    install_requires=['pandas'],
    extras_require={'dev': ['pytest']},
)
