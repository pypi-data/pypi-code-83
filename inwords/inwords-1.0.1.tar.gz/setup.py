import re
from setuptools import setup

version = '1.0.1'

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def parse_requirements(file_name):
    requirements = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'(\s*#)|(\s*$)', line):
            continue
        if re.match(r'\s*-e\s+', line):
            requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
        elif re.match(r'\s*-f\s+', line):
            pass
        else:
            requirements.append(line)

    return requirements

package_name='inwords'
base_url = 'https://github.com/s18k/inwords/'
setup(
    name='inwords',
    version=version,
    description='A Python package to spell out a number',
    author='Shreyas Kamath',
    author_email='shreyaskamath18@gmail.com',
    license='GNU General Public License v3.0',
	long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/s18k/inwords',
    
	download_url='{0}/archive/{1}-{2}'.format(base_url, package_name,version),
    packages=['inwords'],
    include_package_data=True,
    zip_safe=False,
    install_requires=parse_requirements("requirements.txt"),
   
)