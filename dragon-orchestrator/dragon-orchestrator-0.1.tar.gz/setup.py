import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="dragon-orchestrator",
    version="0.1",
    author="Satheesh Kumar",
    author_email="mail@satheesh.dev",
    description="Orchestrator service which can be used to run containers and functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="License :: OSI Approved :: MIT License",
    packages=["dragon"],
    entry_points={"console_scripts": ["start_dragon_client=dragon.cli:run"]},
    zip_safe=False,
    python_requires=">=3",
    install_requires=["grpcio-tools", "docker"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
    ],
)
