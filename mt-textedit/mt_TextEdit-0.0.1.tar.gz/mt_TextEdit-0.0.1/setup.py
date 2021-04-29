import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="mt_TextEdit",
    version="0.0.1",
    author="mole1000",
    author_email="mole1000@protonmail.com",
    description="A text editor to work with MetTrack and MetCal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['PyQt5>=5', 'mt_FileMan>=0.0.2'],
    test_suite='tests',
    extras_require={
        'testing': ['pytest']
    },
)
    
