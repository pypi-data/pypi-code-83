import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ch_nn",
    version="1.0.0",
    author="CH Wong",
    author_email="wchh81@gmail.com",
    description="This is a simple but function completed neural networks framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KINGSEIY/build_neural_framework_by_hand",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)