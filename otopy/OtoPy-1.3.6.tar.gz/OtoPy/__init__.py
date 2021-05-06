"""
OtoPy.

A Otoma Systems developed Lib, Containing useful Tools.
"""

import subprocess
import os

OtoPyVersion = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)
assert "." in OtoPyVersion

__version__ = OtoPyVersion
__author__ = 'Otoma Systems'
__name__="OtoPy"