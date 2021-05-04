import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="remotedb",
    version="0.0.1",
    author="Hosting HQ LLC",
    author_email="justyn.c.freeman@gmail.com",
    description="Official Python API Wrapper for Hosting HQ RemoteDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hosting-HQ/remotedb-py",
    project_urls={
        "Bug Tracker": "https://github.com/Hosting-HQ/remotedb-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)