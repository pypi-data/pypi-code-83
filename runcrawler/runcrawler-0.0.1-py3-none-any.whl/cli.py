#!/usr/bin/env python
"""
cli.py

Command line interface for tools in pyavbp

Please delay the importation, to speed up the responsiveness of the CLI.
"""


# pylint: disable=import-outside-toplevel

import click


@click.group()

def main_cli():
    """---------------    RUNCRAWLER  ------------------

You are now using the Command line interface of Runcrawler package.
a Python3 helper for the parsing the error log files of AVBP software,
created at CERFACS (https://cerfacs.fr).

This is a python package currently installed in your python environment.
See the full documentation on nitrox.

"""
    pass


@click.command()
@click.argument('dir_path', type=click.Path(exists=True))
#@click.option("--scan_log", type=click.Path(exists=True), default=None, help="Error parser")

def scan_log(dir_path):
    """
    Takes as input an AVBP log file and returns an error code,
    depending on what error was found in the log file.
    """
    from runcrawler.logclassify import parse_avbp_o
    import os

    print('Error_log function', dir_path)

    code = parse_avbp_o(os.path.join(dir_path, "avbp.o"),
         logclassify_rc=None)

    print('code', code)

main_cli.add_command(scan_log)
