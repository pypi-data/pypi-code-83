from setuptools import setup
from setuptools import find_packages
from pathlib import Path

here = Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(
    name='nv21',
    version='1.0.0',
    description='Functions for reading and decoding the data of frames in NV21 format.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/denisovap2013/nv21',
    author='Andrey Denisov',
    classifiers=[
        'Topic :: Scientific/Engineering :: Image Processing',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='nv21, yuv420sp, yuv',
    packages=find_packages(),
    python_requires='>=3.6, <4',
    install_requires=['opencv-python', 'numpy'],
    project_urls={
        'Bug Reports': 'https://github.com/denisovap2013/nv21/issues',
        'Source': 'https://github.com/denisovap2013/nv21/',
    },
)
