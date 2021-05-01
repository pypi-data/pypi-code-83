import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="covidtrackershubraj", # Replace with your own username
    version="1.0.3",
    author="Shub Raj Lama",
    author_email="me@shubraj.com",
    description="Commandline Covid-19 Tracker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shubraj/covidTracker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="covidtracker",
    packages=setuptools.find_packages(),
    install_requires = [
        "colorama==0.4.4",
        "pyfiglet==0.8.post1",
        "requests==2.25.1",
    ],

    python_requires=">=3.6",
)