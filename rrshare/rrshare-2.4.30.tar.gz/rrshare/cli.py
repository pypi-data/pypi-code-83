"""This is a script which is run when the Streamlit package is executed."""

import os
import re
from typing import Optional

import click

import rrshare

ACCEPTED_FILE_EXTENSIONS = ("py", "py3")

LOG_LEVELS = ("error", "warning", "info", "debug")


@click.group(context_settings={"auto_envvar_prefix": "RRSHARE"})
@click.option("--log_level", show_default=True, type=click.Choice(LOG_LEVELS))
@click.pass_context
def main(ctx, log_level="info"):
    """Use the line below to run your own script:
        $ rrshare run your_script.py
    """
    if log_level:
        import streamlit.logger
        streamlit.logger.set_log_level(log_level.upper())


@main.command("help")
@click.pass_context
def help(ctx):
    """Print this help message."""
    # Pretend user typed 'rrshare --help' instead of 'rrshare help'.
    import sys

    assert len(sys.argv) == 2  # This is always true, but let's assert anyway.
    sys.argv[1] = "--help"
    #main()

@main.group("config")
def config():
    """Manage rrshare's config settings."""
    pass


if __name__ == '__main__':
    main()