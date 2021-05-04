import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dariap_cine",
    version="1.0.5",
    author="daria",
    author_email="y1159554_t@iespoblenou.org",
    description="Proyecto UF4",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "dariap_cine=dariap_cine.__main__:main",
        ]
    },
) 
