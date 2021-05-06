import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aliyun-citybrain-sdk", # Replace with your own username
    version="0.0.2",
    author="fanyubin",
    author_email="fanyubin@jiagouyun.com",
    description="阿里云交通云控平台SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://gitlab.jiagouyun.com/cloudcare-data/api-citybrain.aliyun.com",
    project_urls={
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