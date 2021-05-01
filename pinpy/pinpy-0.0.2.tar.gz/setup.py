import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pinpy", # Replace with your own username
    version="0.0.2",
    author="Nikhilesh Yadav",
    author_email="nick.yadav@gmail.com",
    description="PINIR database package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "pinpy"},
    packages=setuptools.find_packages(where="pinpy"),
    python_requires=">=3.6",
)