import setuptools
import sys
from setuptools.dist import Distribution

sdk_version = "0.0.2"


setuptools.setup(
    name="trueface_utils",
    version=sdk_version,
    author="Trueface",
    author_email="support@trueface.ai",
    description="Trueface utils package",
    long_description="Trueface SDK",
    long_description_content_type="text/markdown",
    url="https://docs.trueface.ai",
    project_urls={
        "Bug Tracker": "https://support.trueface.ai",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
)

