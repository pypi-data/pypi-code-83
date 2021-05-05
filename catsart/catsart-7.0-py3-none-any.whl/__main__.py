  
import argparse
import sys

from catsart import __version__
import catsart.database


def run_print(parser, args, file=sys.stdout):
    cat = catsart.database.get_random()
    print(cat)

def run_help(parser, args):
    parser.print_help()


def run_version(parser, args):
    print(__version__)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    
    parser_print = subparsers.add_parser('print', help="Gives Random Cat Arts")
    parser_print.set_defaults(func=run_print)

    parser_help = subparsers.add_parser('help', help="Show This Menu")
    parser_help.set_defaults(func=run_help)

    parser_version = subparsers.add_parser('version', help="Gives Info About Current Version")
    parser_version.set_defaults(func=run_version)

    args = parser.parse_args()
    getattr(args, 'func', run_print)(parser, args)

if __name__ == '__main__':
    main()
