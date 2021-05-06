from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='progressbar_easy',
    version='1.0.1.1',
    description='A simple progressbar to track progress',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Braxton Brown',
    author_email='braxton.brown@outlook.com',
    license='MIT',
    classifiers=classifiers,
    keywords='progressbar, progressbar_easy, easy progressbar, easy progress bar',
    packages=find_packages(),
    install_requires=['']
)