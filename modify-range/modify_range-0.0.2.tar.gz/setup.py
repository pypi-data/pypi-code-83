from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name = 'modify_range',
    author = 'bakharia',
    author_email = 'bakharia1@gmail.com',
    version = '0.0.2',
    description = 'Modify the range of collection of numbers on scale of log5 for better visualization. It works best between 0-100. max,min is the max and min value from the present list and, a and b are the max and min values you want. It will set values between a and b. Then convert it to the scale of log5',
    py_modules = ['modify_range'],
    package_dir={"":"src"},
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires = [],
    extra_require = {
        "dev": [
            "pytest >= 3.6",
        ]
    }
)