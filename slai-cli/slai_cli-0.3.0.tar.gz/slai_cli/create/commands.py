import click

from slai.modules.runtime import detect_runtime, detect_credentials
from slai_cli import log
from slai_cli.create import project_generator
from slai_cli.exceptions import ProjectExistsException


@click.command()
@click.argument("name")
@click.option("--profile", required=False, default="default", help="Profile to use")
def create(name, profile):
    """Create a new slai project."""

    runtime = detect_runtime()
    credentials = detect_credentials(runtime=runtime, profile=profile)

    try:
        pg = project_generator.ProjectGenerator(
            project_name=name,
            aws_profile=credentials["aws_profile"],
            aws_region="us-east-1",
            client_id=credentials["client_id"],
            client_secret=credentials["client_secret"],
            profile=profile,
        )
    except ProjectExistsException:
        log.warn(f"Project '{name}' already exists.")
        return

    pg.create_new_project()
