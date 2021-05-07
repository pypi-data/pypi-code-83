import setuptools

setuptools.setup(
    name="flake8-efm",
    license="ISC",
    description="Plugin for EFM-compatible output.",
    author="Hugo Osvaldo Barrera",
    author_email="hugo@barrera.io",
    url="https://git.sr.ht/~whynothugo/flake8-efm",
    py_modules=["flake8_efm"],
    install_requires=["flake8 > 3.0.0"],
    long_description=open("README.rst").read(),
    entry_points={"flake8.report": ["efm = flake8_efm:Errorformat"]},
    classifiers=[
        "Environment :: Console",
        "Framework :: Flake8",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
)
