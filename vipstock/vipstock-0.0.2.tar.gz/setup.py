import setuptools

# from os import path
# read the contents of your README file
# this_directory = path.abspath(path.dirname(__file__))
# filepath = path.join(this_directory, 'README.md')
# with open(filepath, encoding='utf-8') as f:
#     long_description = f.read()


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vipstock", # Replace with your own username
    version="0.0.2",
    author="Iseuwei",
    author_email="iseuwei@gmail.com",
    description="A small api package for vip.stock",
    keywords=("vipstock", "sinastock", "api", "web"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    # license="BSD",
    # platforms="any",
    url="https://github.com/Iseuwei",
    project_urls={
        "Bug Tracker": "https://github.com/Iseuwei/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # package_dir={"": ""},
    # install_requires=["requests"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    package_data={'': ['*.csv', '*.txt', '*.md']},
    data_files=(['README.md'])
)