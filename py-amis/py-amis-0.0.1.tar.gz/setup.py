import setuptools

tests_require = [
    'flask',
]
with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-amis",
    version="0.0.1",
    author="yujieshui",
    author_email="a1178615156@gmail.com",
    description="python gen amis json options",
    url="https://github.com/1178615156/pyamis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    tests_require=tests_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
