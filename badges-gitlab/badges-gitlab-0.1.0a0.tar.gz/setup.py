import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="badges-gitlab",
    version="0.1.0-alpha",
    author="Felipe P. Silva",
    author_email="felipefoz@gmail.com",
    description="Generate badges for Gitlab Projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    url="https://gitlab.com/felipe_public/badges-gitlab",
    project_urls={
        "Bug Tracker": "https://gitlab.com/felipe_public/badges-gitlab/-/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=['anybadge', 'iso8601', 'python-gitlab'],
    entry_points={
        'console_scripts': ['badges-gitlab=badges_gitlab:main']
    },
    python_requires=">=3.9",
)
