from pathlib import Path
from setuptools import setup, find_packages
import sys
from pathlib import Path

module_path = Path(__file__).resolve().parent / "src/py3status_jenkins_status"
sys.path.insert(0, str(module_path))
from version import version
sys.path.remove(str(module_path))

def make_long_description():
    here = Path(__file__).parent
    readme = (here / "README.md").read_text()
    changelog = (here / "CHANGELOG.md").read_text()
    return f"{readme}\n\n{changelog}"


setup(
    name="py3status-jenkins-status",
    version=version,
    description="py3status module to display the current jenkins job status",
    long_description=make_long_description(),
    long_description_content_type="text/markdown",
    author="Andreas Schmidt",
    author_email="mail@schmidt-andreas.de",
    packages=find_packages(where="src"),
    install_requires=["py3status>=3.20", "jenkins", "pypass"],
    package_dir={"": "src"},
    extras_require={"lint": ["pre-commit"], "test": ["pytest", "py3status"]},
    entry_points={"py3status": ["module = py3status_jenkins_status.jenkins_status"]},
    url="https://gitlab.com/schmidtandreas/py3status-jenkins",
    download_url="https://gitlab.com/schmidtandreas/py3status-jenkins/tags",
    project_urls={
      "Documentation":"https://py3status-jenkins.readthedocs.io/en/latest/"
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
