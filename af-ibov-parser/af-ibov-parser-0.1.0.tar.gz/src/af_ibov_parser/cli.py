import sys
import argparse

from . import errors, handlers


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='available sub-commands')

parser_global = argparse.ArgumentParser(add_help=False)
parser_global.add_argument('--output', '-o',
                           type=str,
                           choices=['text', 'json'],
                           default='text')

parser_version = subparsers.add_parser('version',
                                       help='shows program version',
                                       parents=[parser_global])
parser_version.set_defaults(_handler=handlers.version)

parser_parse = subparsers.add_parser('parse',
                                     help='shows program version',
                                     parents=[parser_global])
parser_parse.add_argument('--src', '-s', type=str,
                          help='folder to read archives from')
parser_parse.add_argument('--dest', '-d', type=str,
                          help='folder to store parsed records')
parser_parse.add_argument('--workers', '-w', type=int,
                          help='amount of workers to use')
parser_parse.set_defaults(_handler=handlers.parse)


def run(*args: str, **kwargs: str) -> str:
    '''
    Run ArgumentParser and returns a string
    containing the command result.
    '''
    ns = parser.parse_args(*args, **kwargs)
    params = {k: v for k, v in vars(ns).items() if k != '_handler'}
    return str(ns._handler(**params))


def main(*args: str, **kwargs: str) -> None:
    '''
    Prints result of ArgumentParser to stdout.

    Writes a str containing `errors.AFError'
    to stderr in case of an error.
    '''
    try:
        print(run(*args, **kwargs))
    except errors.AFError as e:
        sys.stderr.write(f'{e}\n')
        sys.exit(e.code)
