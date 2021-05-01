# Third party package
import click

# pass_gen packages
from . import generate

@click.command()
@click.option('-l', '--length', type=int, default=12, metavar='', help='Password length [8 - 16]')
def cli(length):
    if length in range(8, 17):
        password = generate(length)
        click.echo(password)
    else:
        click.echo('Password length must be between 8-16.')

if __name__ == '__main__':
    cli(12)