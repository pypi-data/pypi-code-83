from setuptools import setup, find_packages

classifires = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='e.calc',
    version='1.0.0',
    description='Small calculator package',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Wiktor Skrzynecki',
    author_email='errorflin@gmail.com',
    license='MIT',
    classifires=classifires,
    keywords='calculator',
    packages=find_packages(),
    install_requires=['']
)