from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Other Audience',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9'
]

setup(
    name = 'SRApi_Wrapper',
    version = '0.0.1',
    description = 'An easy to use, async and sync ready, feature-rich wrapper for the API some-random-api.ml.',
    long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url = 'https://github.com/Nimboss2411/SRApiWrapper',
    author = 'Nimit Grover',
    author_email = 'nimbossthegreat@gmail.com',
    license = 'MIT',
    classifiers = classifiers,
    keywords = 'apiwrapper',
    packages = ['package-subfolder'],
    install_requires = ['requests', 'aiohttp']
)