import click

from daleydai.scraper import fetch_broker_data


@click.command()
@click.argument("id")
def buyer(id: int):
    """
    Fetch bought shares by broker id
    """
    fetch_broker_data(id, isBuy=True)
