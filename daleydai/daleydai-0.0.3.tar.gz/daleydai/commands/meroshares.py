import click
import json
import sys
import os


from daleydai import console

from daleydai.constants import CONFIG_FILE
from daleydai.utils import create_required_files, add_mero_shares, remove_mero_shares
from daleydai.scraper import fetch_stocks_and_dump_to_file, read_stocks_from_file


@click.command()
def init():
    """
    Initialize App
    """
    console.print("[blue]Initializing App")
    create_required_files()
    fetch_stocks_and_dump_to_file()
    console.print("[green]App initialization complete")


@click.command()
def show():
    """
    Show my shares
    """
    with open(CONFIG_FILE, "r+") as file:
        data = file.readline()

        if not data:
            console.print(
                "[yellow]Your shares are empty. Use [green]add <stock> [yellow]to add shares"
            )
            sys.exit()

        read_stocks_from_file()


@click.command()
@click.argument("stock")
def add(stock: str):
    """
    Add My Shares
    """
    add_mero_shares(stock)


@click.command()
@click.argument("stock")
def remove(stock: str):
    """
    Remove My Shares
    """
    remove_mero_shares(stock)
