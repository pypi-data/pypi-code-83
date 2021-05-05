import os
import subprocess
import sys

import click
from cookiecutter import exceptions
from cookiecutter.main import cookiecutter
from .helper import windows_success_msg, common_success_msg

# CONTANTS
__version__ = "0.1.0"


@click.group()
@click.version_option(__version__)
def cli():
    pass


@cli.command()
@click.argument("project_name")
def create_project(project_name):
    """Creates a new Flask project"""

    # parse project info
    project_slug = project_name.lower().replace("-", "_")

    # Check for directory exists or not
    if os.path.exists(project_name):
        click.secho(
            "\nError! Directory with {} name already exists!\n".format(project_name),
            fg="red",
        )
        exit()

    click.secho("\nCreating a new Flask app in {}.".format(os.getcwd()))

    try:
        cookiecutter(
            "https://github.com/flaskspot/simple-flask-boilerplate.git",
            no_input=True,
            extra_context={"project_name": project_name, "project_slug": project_slug},
        )
        # After successfull Installation
        click.secho(
            "\nSuccess! Created {project_name} at {cwd}/{project_name}.".format(
                project_name=project_name, cwd=os.getcwd()
            ),
            fg="green",
        )
        if sys.platform == 'win32' or sys.platform == 'cygwin':
            message = windows_success_msg.format(project_name=project_name)
        else:
            message = common_success_msg.format(project_name=project_name)

        click.secho(message)

    except (
        exceptions.NonTemplatedInputDirException,
        exceptions.UnknownTemplateDirException,
        exceptions.ContextDecodingException,
        exceptions.ConfigDoesNotExistException,
        exceptions.OutputDirExistsException,
    ):
        click.secho("Unknown Exception!", fg="red")
    except exceptions.VCSNotInstalled:
        click.secho(
            "\nGit not installed, Please install git to use FlaskSpot!", fg="red"
        )
