import click
from bluetooth.main import (
    pair_device,
    pair_device_name,
    remove_device,
    remove_device_name,
)


@click.group()
def cli():
    """Bluetooth Command"""
    pass


@cli.command("pair", help="Pairs Bluetooth device, give Device ID.")
@click.option("-i", "--device_id", type=str, default=None)
@click.option("-d", "--device_name", type=str, default=None)
def cli_pair_device(device_id, device_name):
    if device_id is not None:
        pair_device(device_id)
    elif device_name is not None:
        pair_device_name(device_name)
    else:
        click.echo("No input is provided")


@cli.command("unpair", help="UnPairs Bluetooth device, give Device ID.")
@click.option("-i", "--device_id", type=str, default=None)
@click.option("-d", "--device_name", type=str, default=None)
def cli_unpair_device(device_id, device_name):
    if device_id is not None:
        remove_device(device_id)
    elif device_name is not None:
        remove_device_name(device_name)
    else:
        click.echo("No input is provided")
