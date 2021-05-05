import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="azure-integration",  # Replace with your own username
    version="0.0.3",
    author="Mehran Zolghadr",
    author_email="mehran@keyleadhealth.com",
    description="Microsoft Azure Integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IOMehran/azure-integration",
    download_url="https://github.com/IOMehran/azure-integration/archive/refs/tags/v0.0.3.tar.gz",
    project_urls={
        "Bug Tracker": "https://github.com/IOMehran/azure-integration/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",

    install_requires=[
        "azure-common==1.1.27",
        "azure-core==1.13.0",
        "azure-identity==1.5.0",
        "azure-keyvault==4.1.0",
        "azure-keyvault-certificates==4.2.1",
        "azure-keyvault-keys==4.3.1",
        "azure-keyvault-secrets==4.2.0",
        "build==0.3.1.post1",
        "certifi==2020.12.5",
        "cffi==1.14.5",
        "chardet==4.0.0",
        "cryptography==3.4.7",
        "idna==2.10",
        "isodate==0.6.0",
        "msal==1.11.0",
        "msal-extensions==0.3.0",
        "msrest==0.6.21",
        "oauthlib==3.1.0",
        "packaging==20.9",
        "pep517==0.10.0",
        "portalocker==1.7.1",
        "pycparser==2.20",
        "PyJWT==2.0.1",
        "pyparsing==2.4.7",
        "python-dotenv==0.17.0",
        "requests==2.25.1",
        "requests-oauthlib==1.3.0",
        "six==1.15.0",
        "toml==0.10.2",
        "urllib3==1.26.4",
        "gobject"
    ],
)
