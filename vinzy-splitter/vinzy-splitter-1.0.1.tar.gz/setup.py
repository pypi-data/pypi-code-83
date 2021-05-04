from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="vinzy-splitter",
    version="1.0.1",
    description="A package will help you to split your data frame into training, validation and testing subsets",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/vinayak-97/Training-Validation-and-Testing-dataframe-splitter-package.git",
    author="Vinayak Bhosale",
    author_email="vinubhosale.cj@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["vinzy_splitter"],
    include_package_data=True,
    install_requires=["numpy","pandas"],
    )
    