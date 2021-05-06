import os
import setuptools
from glasswall_visual_comparison_tool_cli import __version__


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="glasswall-visual-layer-comparison-tool-cli",
    version=__version__,
    author="ahewitt",
    author_email="ahewitt@glasswallsolutions.com",
    description="CLI Tool that makes requests to the glasswall-visual-layer-comparison API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/filetrust/glasswall-visual-layer-comparison-tool-cli",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "glasswall_visual_comparison_tool_cli = glasswall_visual_comparison_tool_cli.__main__:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Click>=7.0",
        "requests>=2.23.0"
    ],
)