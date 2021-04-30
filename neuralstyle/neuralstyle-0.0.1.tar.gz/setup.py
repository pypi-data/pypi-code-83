# pylint: disable-all
import setuptools

setuptools.setup(
    name="neuralstyle",
    version="0.0.1",
    author="Marmik Shah",
    author_email="marmikshah@icloud.com",
    description="Implementations of Neural Style transfer algorithms in PyTorch",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/marmikshah/neuralstyle",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=setuptools.find_packages(),
)
