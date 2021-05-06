from setuptools import setup

setup(
    name='awesome-caching',
    version='0.0.1',
    packages=['awesome_caching'],
    url='https://github.com/DewMaple/awesome-caching',
    description='Convenient functions that help to process images',
    author='dew.maple',
    author_email='dew.maple@gmail.com',
    license='BSD',
    keywords=['cache', 'python'],
    classifiers=['Programming Language :: Python :: 3.6'],
    project_urls={
        'Bug Reports': 'https://github.com/DewMaple/awesome-caching/issues',
        'Source': 'https://github.com/DewMaple/awesome-caching',
    },
    tests_require=[
        "pytest",
        "pytest-cov",
        "pytest-xprocess",
        "redis",
    ],
    zip_safe=True
)
