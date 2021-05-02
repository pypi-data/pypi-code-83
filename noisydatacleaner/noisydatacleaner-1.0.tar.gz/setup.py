from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()



setup(
    name="noisydatacleaner",
    version="1.0",
    author="Teo Jao Ming",
    author_email="jaomingteo@gmail.com",
    description="Noise Detection and Label Correcting Package",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jaotheboss/NoisyDataCleaner",
    project_urls = {
        "Bug Tracker": "https://github.com/jaotheboss/NoisyDataCleaner/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
)