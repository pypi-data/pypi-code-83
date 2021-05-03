import click
import logging
import os

from datafold.version import __version__
from datafold.cli import dbt
from datafold.cli import context
from datafold.cli.context import CliContext
from datafold.cli.context import DATAFOLD_HOST, DATAFOLD_APIKEY


FORMAT = '%(asctime)-15s:%(levelname)s:%(module)s: %(message)s'
logging.basicConfig(format=FORMAT)

logger = logging.getLogger(__file__)


@click.group()
@click.option('--host',
              default="https://app.datafold.com",
              help="The host where the datafold app is located, e.g. 'https://app.datafold.com'")
@click.pass_context
def manager(ctx, host: str, **kwargs):
    """Management script for Datafold CLI"""
    api_key = os.environ.get(DATAFOLD_APIKEY)
    if api_key is None:
        logger.error(f"The {DATAFOLD_APIKEY} environment variable is not set")
        ctx.exit(1)

    override_host = os.environ.get(DATAFOLD_HOST)
    if override_host is not None:
        logger.info(f"Overriding host {host} to {override_host}")
        host = override_host

    ctx.obj = CliContext(host=host, api_key=api_key)


@manager.command()
@click.pass_context
def version(ctx):
    """Displays Datafold CLI version."""
    print(__version__)


manager.add_command(dbt.manager, "dbt")
