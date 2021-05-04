import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qutorch",
    version="0.0.4",
    author="Mario Duran-Vega",
    author_email="mario.duran.vega@gmail.com",
    description="Quantum circuit simulator based in PyTorch.",
    long_description=long_description,
    url="https://github.com/MarioDuran/qutorch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
