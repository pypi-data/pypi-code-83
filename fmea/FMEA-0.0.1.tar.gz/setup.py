import setuptools

def readme():
    with open('readme.md') as f:
        return f.read()
    
setuptools.setup(
    name="FMEA", # Replace with your own username
    version="0.0.1",
    author="Apratim Ray",
    author_email="apratimr55@gmail.com",
    description="A flexible Mutable Symmetric Encryption algorithm",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ApratimR/FMEA",
    project_urls={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="FMEA"),
    py_modules=["FMEA"],
    install_requires = ["numpy","FNNH"],
    python_requires=">=3.6",
)