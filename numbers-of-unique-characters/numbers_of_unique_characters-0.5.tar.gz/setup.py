import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="numbers_of_unique_characters",
    version="0.5",
    author="Yuliia_Kuzminska",
    author_email="yuliia.nikolaevna86@gmail.com",
    description="Python module is used to find unique characters.",
    long_description="The application that takes a string and returns the number of unique characters in the string.",
    long_description_content_type="text/markdown",
    url="https://git.foxminded.com.ua/Yuliia_Nikolaevna/foxminded/",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Framework :: Pytest",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=['']
)
