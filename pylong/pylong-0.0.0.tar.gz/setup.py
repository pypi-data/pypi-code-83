import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylong",
    version="0.0.0",
    author="jiukun",
    author_email="jiukun9291@gmail.com",
    description="use yaml to combination params for pytest collect test cases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    package_data={
            "": ["*.yml"],
    },
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "pytest",
        "allure-pytest",
        "requests",
        "PyYAML",
        "xlwt",
        "xlrd",
        "mysql-connector-python",
        "jmespath",
        "selenium",
        "Faker",
        "Pillow",
        "pypng",
        "numpy",
        "sqlmap",
        "pytest-xdist",
        "Flask",
        "Jinja2",
        "flask_migrate",
        "flask_cors",
        "Flask-SQLAlchemy",
        "flask_migrate",
        "flask_restful",
        "fnv",
    ]
)
