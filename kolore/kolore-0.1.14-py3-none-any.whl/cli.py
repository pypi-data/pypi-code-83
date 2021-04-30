import click
import kolore.palette as palette
from kolore import __version__


@click.command()
@click.option('--in', 'in_', help='input file', required=True)
@click.option('--out', help='output path', required=True)
@click.option('--from', 'from_', help='format of the input file, normally infered from extension')
@click.option('--to', help='format of output file, normally infered from extension')
@click.option('--width', default=400, type=int, help="image width size in pixels")
@click.option('--height', default=200, type=int, help="image height size in pixels")
@click.version_option(__version__)
def parse(in_: str, out: str, from_: str, to: str, width: int, height: int):
    palette.create(from_, to, width, height, in_, out)
