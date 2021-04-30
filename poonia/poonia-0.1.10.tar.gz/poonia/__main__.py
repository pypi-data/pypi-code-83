import click



@click.group()
def main():
    pass

from .commands.encoding import encoding
main.add_command(encoding)
from .commands.esub import esub
main.add_command(esub)
from .commands.run import run, rune
main.add_command(run)
main.add_command(rune)
from .commands.sdel import sdel
main.add_command(sdel)
from .commands.which import which
main.add_command(which)
from .commands.pn import pn
main.add_command(pn)
from .commands.flatten import flatten
main.add_command(flatten)
from .commands.rename import rename
main.add_command(rename)
from .commands.duration import duration
main.add_command(duration)
from .commands.ffbook import ffbook
main.add_command(ffbook)
from .commands.ffsel import ffsel
main.add_command(ffsel)
from .commands.foldertag import foldertag
main.add_command(foldertag)
from .commands.moveup import moveup
main.add_command(moveup)

if __name__ == '__main__':
    main()
