#!/usr/bin/env python
# pylint: disable = invalid-name, missing-docstring

"""Check classes are documented properly as per numpydoc requirements.

This currently checks:
  - constructor parameters are documented in the class docstring, not __init__
  - listed sections in docstrings are valid

Note: because this script imports finesse modules directly, it should be executed within the same
environment used to develop Finesse. In pre-commit, for example, this means setting the script
language as "system" and not "python".

Author: Sean Leavey
"""

import sys
import argparse
import inspect
from pathlib import Path
from importlib import import_module
import warnings
from numpydoc.docscrape import FunctionDoc, ClassDoc
import finesse


FINESSE_ROOT = Path(finesse.__file__.replace("__init__.py", ""))


def check_module(path):
    path = Path(path).resolve()

    try:
        module_path = path.relative_to(FINESSE_ROOT)
    except ValueError:
        # Specified file is not part of the finesse package.
        return 0

    module_name = "." + str(module_path.stem)
    package = str(finesse.__name__ + "." + str(module_path.parent).replace("/", "."))
    package = package.rstrip(".")

    try:
        module = import_module(module_name, package)
    except ModuleNotFoundError:
        return 0

    has_issue = False

    for _, obj in inspect.getmembers(module):
        if not inspect.isclass(obj):
            continue

        if obj.__module__ != module.__name__:
            # Reject imported modules.
            continue

        clsobj = f"{module_path}::{obj.__name__}"
        initmeth = None

        try:
            if obj.__init__.__module__ == obj.__module__:
                # There is an init method.
                initmeth = obj.__init__
        except AttributeError:
            # Probably a C parent.
            pass

        # Parse docstring.
        initdoc = None
        with warnings.catch_warnings(record=True) as warnlist:
            # Import classdoc so that it triggers warnings caught by the context manager.
            try:
                ClassDoc(obj)

                if initmeth:
                    initdoc = FunctionDoc(initmeth)
            except Exception as e:
                print(f"error while processing docstring for {obj}: {e}")

                has_issue = True

            if warnlist:
                for wrng in warnlist:
                    print(f"{clsobj}: numpydoc warning: {wrng.message}")

                has_issue = True

        if initdoc and initdoc.get("Parameters"):
            print(
                f"{clsobj}: constructor parameters should be documented in the class "
                "docstring, not __init__ (see https://finesse.readthedocs.io/en/latest/developer/documenting.html#writing-sphinx-compatible-docstrings)."
            )

            has_issue = True

    return 1 if has_issue else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(sys.argv)

    retv = 0

    for filename in args.filenames:
        retv |= check_module(filename)

    sys.exit(retv)
