from setuptools import find_packages, setup

setup(
    name='mldatatools',
    packages=find_packages(include=['mldatatools']),
    version='0.0.2',
    description='Automated missing value imputation, outlier handling, feature scaling, feature discretization, and categorical feature encoding for machine learning datasets.',
    author='Matt Kearns',
    license='MIT',
    url='https://github.com/mattkearns/mldatatools',
    download_url='https://github.com/mattkearns/mldatatools/archive/refs/tags/0.0.1.tar.gz',
    install_requires=['pandas>=1.2.3', 'numpy>=1.20.1', 'scipy>=1.6.1'],
    keywords = ['data science', 'machine learning', 'data preparation', 'data preprocessing'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest>=4.4.1'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',  
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
  ],
)