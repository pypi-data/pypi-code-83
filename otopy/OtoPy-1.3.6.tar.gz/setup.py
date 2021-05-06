from setuptools import setup
import subprocess
import os

OtoPyVersion = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)
assert "." in OtoPyVersion

with open("README.md", "r", encoding="utf-8") as READMEfile:
    long_description = READMEfile.read()

setup(
    name='OtoPy',
    version=OtoPyVersion,    
    description='A Otoma Systems developed Lib Containing useful Tools and More',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Otoma-Systems/OtoPy.git',
    author='Otoma Systems',
    author_email='contact@otoma.com.br',
    license='BSD 2-clause',
    packages=['OtoPy'],
    install_requires=[],

    classifiers=[
        'Natural Language :: English',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Environment :: Win32 (MS Windows)',
        'Environment :: Console',        
        'Environment :: Other Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ]
)