import os
import shutil
import sys

import click

from aicrowd.notebook.exceptions import NotebookException
from aicrowd.utils import AliasedGroup


def print_exception(e: NotebookException):
    click.echo(click.style(f"{type(e).__name__}: {e.message}", fg="red"))
    if e.fix:
        click.echo(click.style(e.fix, fg="yellow"))
    sys.exit(e.exit_code)


@click.group(name="notebook", cls=AliasedGroup)
def notebook_command():
    """
    Notebook specific operations
    """
    pass


@click.command(name="clean")
@click.option(
    "-f",
    "--file",
    type=click.Path(exists=True),
    required=True,
    help="Path to the notebook",
)
def clean_subcommand(file: str):
    """
    Remove sensitive information from the notebook

    The default behaviour is to match `AICROWD_API_KEY(\\s+)?=(\\s+)?".+"` and
    remove the lines containing the regex. To match custom expressions, set a
    list of regex in `AICROWD_CLEAN_EXPRESSIONS` environment variable.
    """
    from aicrowd.notebook.clean import clean_notebook

    try:
        clean_notebook(file_path=file)
    except NotebookException as e:
        print_exception(e)


@click.command(name="split")
@click.option(
    "-f",
    "--file",
    type=click.Path(exists=True),
    required=True,
    help="Path to the notebook",
)
@click.option(
    "-o",
    "--output-dir",
    default="submission",
    help="Directory to place the split notebooks",
)
def split_subcommand(file: str, output_dir: str):
    """
    Split the notebook into training and prediction notebooks
    """
    from aicrowd.notebook.split import split_notebook

    try:
        split_notebook(file, output_dir)
    except NotebookException as e:
        print_exception(e)


@click.command(name="submit")
@click.option(
    "-c", "--challenge", required=True, help="Challenge to submit the file for"
)
@click.option("--description", default="", help="Description for the submission")
@click.option("-a", "--assets-dir", required=True, help="Path to assets dir")
@click.option("-o", "--output", default="submission.zip", help="Output file")
@click.option("-n", "--notebook-name", default=None, help="Name of the notebook to use")
@click.option("--no-verify", is_flag=True, help="Skip submission verification")
@click.option("--dry-run", is_flag=True, help="Verify submission but don't submit")
def submit_subcommand(
    challenge: str,
    description: str,
    assets_dir: str,
    output: str = "submission.zip",
    notebook_name: str = None,
    no_verify: bool = False,
    dry_run: bool = False,
):
    """
    Submit the notebook to AIcrowd
    """
    from aicrowd.notebook.submit import create_submission

    try:
        create_submission(
            challenge,
            description,
            assets_dir,
            output,
            notebook_name,
            no_verify,
            dry_run,
        )
    except NotebookException as e:
        print_exception(e)


@click.command(name="extract")
@click.option("-f", "--file", type=click.Path(exists=True), help="Path to the notebook")
@click.option("--start", help="Extract/Remove cells from this block")
@click.option("--end", help="Extract/Remove cells till this block")
@click.option(
    "--remove",
    is_flag=True,
    help="Removes the content between start and end instead of extracting them",
)
def extract_subcommand(file: str, start: str, end: str, remove: bool = False):
    """
    Extract/Remove cells from notebook between start and end
    """
    from aicrowd.notebook.split import extract_partial_notebook
    from aicrowd.notebook.helpers import read_notebook, write_notebook

    try:
        nb = read_notebook(file)
        partial_nb = extract_partial_notebook(
            nb=nb, start_block=start, end_block=end, remove=remove
        )
        write_notebook(file_path=os.path.join(os.getcwd(), file), nb=partial_nb)
    except NotebookException as e:
        print_exception(e)


@click.command(name="copy")
@click.option("-o", "--output", required=True, help="Path to copy the notebook to")
@click.option(
    "--clean", is_flag=True, help="Remove sensitive information from notebook"
)
def copy_subcommand(output: str, clean: bool = False):
    """
    Copies the active notebook to a path
    """
    from aicrowd.notebook.helpers import get_notebook_path
    from aicrowd.notebook.clean import clean_notebook

    try:
        shutil.copy2(get_notebook_path(), output)
        if clean:
            clean_notebook(output)
    except NotebookException as e:
        print_exception(e)


notebook_command.add_command(clean_subcommand)
notebook_command.add_command(split_subcommand)
notebook_command.add_command(submit_subcommand)
notebook_command.add_command(extract_subcommand)
notebook_command.add_command(copy_subcommand)
