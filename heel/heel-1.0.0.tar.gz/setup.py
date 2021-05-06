import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="heel",  # Replace with your own username
    version="1.0.0",
    author="秦",
    author_email="571169713@qq.com",
    description="这是一个测试打包上传的包！",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qcdh1234/python",
    project_urls={
        "Bug Tracker": "https://github.com/qcdh1234/python/tree/master/pack_test_lib",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
