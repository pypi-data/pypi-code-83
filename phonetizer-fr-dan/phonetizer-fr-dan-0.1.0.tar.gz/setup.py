import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="phonetizer-fr-dan", # Replace with your own username
    version="0.1.0",
    author="Dan Ringwald",
    author_email="dan.ringwald12@gmail.com",
    description="Translates French words to phonetics. Checks phonetization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/biggoron/phonetizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pandas >= 1.2.4',
        'numpy >= 1.20.2',
        'transformers>=4.5.1',
        'biopython>=1.78',
        'torch>=1.8.1',
    ],
    scripts=[
        './scripts/check_phonetisation',
    ],
    python_requires='>=3.6',
    download_url='https://github.com/biggoron/phonetizer/archive/0.0.4.tar.gz'
)
