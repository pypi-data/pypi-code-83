from setuptools import setuptools

long_description="FTTCrypt stands for File to Text Encryptor, it is a software library built for text encryption and Files converting & encryption to a small ciphertext purposely to enhance file upload and transfer. Imagine sending a file from User A to user B, the file has to be uploaded into a server or network then the receiver to downloads the file. According to FTTCrypt, you are not uploading a File, but a small, encrypted cipherText that represents the file which means you can store the cipher in a database level and access the file using the cipher anywhere the FTTCrypt runs. No need for a large file or blob storage for your next application. Save your files within your database as a cipher"
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FTTCrypt",
    version="1.0.1",
    author="FTTCrypt.io",
    author_email="support@fttcrypt.io",
    description="FTTCrypt, Encrypt a plain text to Cipher or any File to Cipher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="fttcrypt ecnryption fileencryption textencryption",
    url="https://github.com/aliyura/fttcrypt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'fttcrypt=fttcrypt_cli:main',
        ],
    },
)
