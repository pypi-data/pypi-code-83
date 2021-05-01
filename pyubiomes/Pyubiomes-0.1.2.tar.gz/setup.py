k=open("LONGDESC.md",'r').read()
from setuptools import setup, find_packages
setup(name = 'Pyubiomes', version = '0.1.2', description="a (probably bad wip) python wrapper for the C library Cubiomes", author="4gboframram", url="https://github.com/4gboframram/Pyubiomes",author_email="<zachawesomeness411@gmail.com>", long_description=k, include_package_data=True,
long_description_content_type='text/markdown',
packages=find_packages(),
package_data={'': ['searches.so']},)