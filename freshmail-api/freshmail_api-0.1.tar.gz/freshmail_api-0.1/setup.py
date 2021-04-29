import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="freshmail_api",
    version="0.1",
    author="FreshMail",
    author_email="pomoc@freshmail.pl",
    description="FreshMail Python Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FreshMail/Python-Api-Client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
