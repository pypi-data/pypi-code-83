import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pystegy", # Replace with your own username
    version="0.0.2",
    author="d.char",
    author_email="d.charentus@gmail.com",
    description="small steganography utility ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # package_dir={"": "pystegy"},
    # packages=setuptools.find_packages(where="pystegy"),
    # py_modules=['stegyImage'],
    packages=["pystegy", "pystegy.utils"],
    install_requires=[
          "matplotlib>=3.4.1",
          "requests>=2.25.1"
      ],
    python_requires=">=3.6",
)
