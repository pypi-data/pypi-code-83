import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent


def parse_requirements(file):
    required = []
    with open(file) as f:
        for req in f.read().splitlines():
            if not req.strip().startswith("#"):
                required.append(req)
    return required


version = "0.1.2"
requires = parse_requirements("requirements.txt")
tests_requires = parse_requirements("requirements.tests.txt")
README = (HERE / "README.md").read_text()

setup(
    name="google-sheets-to-csv",
    version=version,
    description="Convert Google SpreadSheet document to CSV files",
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
    author="Pierre Verkest",
    author_email="pierreverkest84@gmail.com",
    url="https://gitlab.com/micro-entreprise/google-sheets-to-csv",
    packages=find_packages(exclude=["ez_setup", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires + tests_requires,
    entry_points="""
    [console_scripts]
    gs-to-csv=gs_to_csv.cli:main
    """,
)
