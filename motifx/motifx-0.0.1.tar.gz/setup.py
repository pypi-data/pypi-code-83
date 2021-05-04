import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="motifx",
    version="0.0.1",
    author="Ethan",
    author_email="ethan_vn@outlook.com",
    description="用于发现复杂网络中潜在的三角形模体结构(高阶组织); Find triangular motifs of complex networks; Find higher-order organization of complex networks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EthanVn/MotifX",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy>=1.19.2',
        'scipy>=1.6.2'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
