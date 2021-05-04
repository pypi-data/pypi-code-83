import os
import shutil


import click
import docker

from yamlflow.cli.manifest import Manifest
from yamlflow.cli.constants import(
    BASE_DIR,
    MANIFEST_FILE
    )


client = docker.from_env()

_copy_ignore = shutil.ignore_patterns('*.pyc', "__pycache__", "objects")

@click.command()
def build():
    """Build a deployable unit, based on initialization"""
    manifest = Manifest(MANIFEST_FILE)
    build_info = manifest.build_info()
    click.echo(
        click.style(
            f"Building image {build_info['tag']}",
            fg="blue"
        )
    )
    try:
        client.images.build(path=build_info["path"],
                            dockerfile=build_info["dockerfile"],
                            tag=build_info["tag"],
                            buildargs=build_info["buildargs"],
                            rm=True)
    except (TypeError, docker.errors.APIError, docker.errors.BuildError) as err:
        click.echo(
            click.style(
                f"Failed building image: {err}",
                fg="red"
            )
        )
