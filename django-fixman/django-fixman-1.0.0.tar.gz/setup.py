# See https://packaging.python.org/en/latest/distributing.html
# and https://docs.python.org/2/distutils/setupscript.html
# and https://pypi.python.org/pypi?%3Aaction=list_classifiers

from setuptools import setup, find_packages


def read(path):
    with open(path, "r") as f:
        contents = f.read()
        f.close()
    return contents


setup(
    name='django-fixman',
    version=read("VERSION.txt"),
    description=read("DESCRIPTION.txt"),
    long_description=read("README.markdown"),
    long_description_content_type="text/markdown",
    author='Shawn Davis',
    author_email='shawn@develmaycare.com',
    url='https://github.com/develmaycare/django-fixman/',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pygments",
        # "commonkit @ git+https://github.com/develmaycare/python-commonkit",
        "python-commonkit",
    ],
    # dependency_links=[
    #     "https://github.com/develmaycare/python-commonkit",
    # ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    zip_safe=False,
    tests_require=[
        "coverage",
        "pytest",
    ],
    test_suite='runtests.runtests',
    entry_points={
        'console_scripts': [
            'fixman = fixman.cli:main_command',
        ],
    },
)
