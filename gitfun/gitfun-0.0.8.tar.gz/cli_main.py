import subprocess
from github import Github
import click
import argparse
from gitfun import GitFun as gf
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
@click.option('-url', type=str, help='Paste your link of the repo')

def fungit(url):
    click.echo(gf.remote(url))