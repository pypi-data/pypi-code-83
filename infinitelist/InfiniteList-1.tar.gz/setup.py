from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='InfiniteList',
    version='1',
    packages=['InfiniteList'],
    url='https://github.com/GlobalCreativeCommunityFounder/InfiniteList',
    license='MIT',
    author='GlobalCreativeCommunityFounder',
    author_email='globalcreativecommunityfounder@gmail.com',
    description='This package contains implementation of the library "InfiniteList". InfiniteList is a data type '
                'supporting lists of any lengths by using class attributes storing small sublists.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "InfiniteList=InfiniteList.InfiniteList_versus_list:main",
        ]
    }
)