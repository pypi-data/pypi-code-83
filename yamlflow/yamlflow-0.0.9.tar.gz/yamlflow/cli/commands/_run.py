import os
import sys
import time
import shutil

import click
import docker

from yamlflow.cli.manifest import Manifest
from yamlflow.cli.constants import MANIFEST_FILE


client = docker.from_env()


@click.command()
def run():
    """Run the deployable unit."""
    manifest = Manifest(MANIFEST_FILE)
    run_info = manifest.run_info()
    click.echo(click.style(
            f"""
            Running container {run_info["name"]} with configurations
            image  {run_info["image"]}
            -n     {run_info["name"]}
            -e     {run_info["environment"]}
            -p     {run_info["ports"]}
            """,
            fg="blue"
        )
    )
    try:
        client.containers.run(image=run_info["image"],
                              name=run_info["name"],
                              environment=run_info["environment"],
                              ports=run_info["ports"],
                              detach=True,
                              auto_remove=True)
    except (docker.errors.ImageNotFound, docker.errors.APIError) as err:
        print(f"Failed running container: {err}")
        sys.exit(1)
    time.sleep(5)
    is_up_and_running = False
    try:
        client.containers.get(run_info["name"])
        is_up_and_running = True
    except (docker.errors.NotFound, docker.errors.APIError) as err:
        pass

    if is_up_and_running:
        click.echo(click.style(
                f"""
                Container {run_info["name"]} is up and running in 0.0.0.0:{run_info["ports"]}
                """,
                fg="blue"
            )
        )
    else:
        click.echo(click.style(
                f"""
                Container {run_info["name"]} was up but excited.
                """,
                fg="red"
            )
        )