import setuptools

with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smartmind_image", # Replace with your own PyPI username(id)
    version="0.0.3",
    author="Sangdae Nam",
    author_email="nsd26534613@gmail.com",
    description="sample package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/nicecoding1/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)