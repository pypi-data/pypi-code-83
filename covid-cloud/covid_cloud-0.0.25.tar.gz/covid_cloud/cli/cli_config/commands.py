import click
import yaml
import json

from covid_cloud.constants import *
from covid_cloud.cli.utils import *


class ConfigHelp(click.Command):
    def format_help(self, ctx, formatter):
        click.echo("Usage: covid-cloud config [OPTIONS] KEY VALUE")
        click.echo("Options:")
        click.echo(" --help  Show this message and exit.")
        click.echo("Accepted Keys: ")
        for key in ACCEPTED_CONFIG_KEYS:
            click.echo(f"\t{key}")


@click.command(cls=ConfigHelp)
@click.pass_context
@click.argument("key")
@click.argument("value", required=False, default=None,nargs=-1)
def config(ctx, key, value):
    if key == 'list' and not value:
        click.echo(json.dumps(ctx.obj, indent=4))
        return
    elif key not in ACCEPTED_CONFIG_KEYS:
        click.secho(f'{key} is not an accepted configuration key.', fg='red')
        return

    if len(value) == 1:
        value = value[0]
    if len(value) == 2:
        value = {value[0]: value[1]}

    set_config(ctx,key,value)

    with open(config_file_path, 'w') as config_file:
        yaml.dump(ctx.obj, config_file)

    click.echo(json.dumps(ctx.obj, indent=4))
