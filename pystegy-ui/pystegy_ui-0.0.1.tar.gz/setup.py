import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pystegy_ui", # Replace with your own username
    version="0.0.1",
    author="d.char",
    author_email="d.charentus@gmail.com",
    description="small steganography utility tkinter interface",
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
    # package_dir={"": "stegy_ui"},
    # packages=setuptools.find_packages(where="pystegy"),
    # py_modules=['stegyImage'],
    packages=["stegy_ui", "stegy_ui.tkinterdnd2", "stegy_ui.ui"],
    include_package_data=True,
    # package_data={
    #     # If any package contains *.txt files, include them:
    #     "": ["*.txt"],
    #     # And include any *.dat files found in the "data" subdirectory
    #     # of the "mypkg" package, also:
    #     "stegy_ui": ["TitleBar.lck", "data/result.png", "ress/src.png", "ress/stegy.ico", "ress/stegy.bmp", "ress/share32.png"],
    # },
    install_requires=[
          "pystegy>=0.0.2"
      ],
    python_requires=">=3.6",
)
