from setuptools import setup, setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dsmscp",
    version="0.0.3",
    author="Tom Marti",
    author_email="dev@dassym.com",
    keywords = ['Dassym', 'motor', 'api', 'dapi'],
    description="The dsmscp application offer a simple way to debug dassym motor.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = ['PyDapi2', 'PyQt5', 'pyserial'],
    url="https://github.com/dassym/dsmscp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ], 
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)