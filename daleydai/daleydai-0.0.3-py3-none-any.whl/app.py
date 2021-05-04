import click

from daleydai.commands import init, buyer, seller, show, add, remove


@click.group()
def cli():
    """
    karod bata road....
    """
    pass


cli.add_command(init)
cli.add_command(buyer)
cli.add_command(seller)
cli.add_command(show)
cli.add_command(add)
cli.add_command(remove)
