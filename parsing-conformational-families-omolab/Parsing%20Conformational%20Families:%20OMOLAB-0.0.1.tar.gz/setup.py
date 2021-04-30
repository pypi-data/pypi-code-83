from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name= "Parsing Conformational Families: OMOLAB",
    version="0.0.1",
    description="Uses PCA and K-means clustering to separate conformational ensembles. (xyz-files only)",
    py_modules=["clustering","main","pymol","xyz","pca","elements"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Framework :: Matplotlib",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: Free For Educational Use",
        "License :: Free For Home Use",
        "License :: Free for non-commercial use",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Information Analysis"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    # install_requires= [
    #     "datetime",
    #     # "os",
    #     # "stat",
    #     "sklearn>=0.21.0",
    #     "plotly>=4.7.0",
    #     "numpy>=1.18.0",
    #     "pandas>=0.25.0",
    #     # "shutil"
    #     # "subprocess"
    # ],
    url = "https://github.com/mattnw1/Conformational_Analysis",
    author="Matthew Nwerem",
    author_email="nwere100@mail.chapman.edu"

)

#mGenerate_PyMOL_Session.sh cannot be included here because it is not a .py file, must find another way to add it
