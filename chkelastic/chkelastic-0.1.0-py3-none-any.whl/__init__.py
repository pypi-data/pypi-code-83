#!/usr/bin/env python3
"""
A command line tool to assert ElasticSearch index and document integrity.
"""
import argparse
import sys

from . import commands


def parse_args(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    # global options.
    parser.add_argument(
        "-v", "--verbose", action="count", help="increase output verbosity."
    )
    parser.add_argument(
            "-s", "--src-url", default="http://127.0.0.1:9200", help="source ES cluster URL. defaults to http://127.0.0.1:9200."
    )
    parser.add_argument(
            "-d", "--dst-url", default="http://127.0.0.1:9200", help="destination ES cluster URL. defaults to http://127.0.0.1:9200."
    )

    sub_parser = parser.add_subparsers(dest="subcommand")
    sub_parser.required = (
        True  # required to be done this way for py36 argparse compatibility.
    )

    commands.add_index(sub_parser)
    commands.add_doc(sub_parser)

    args = parser.parse_args(argv[1:])
    return args


def main(argv=None):
    if argv is None:
        argv = sys.argv
    args = parse_args(argv)
    try:
        args.command(args)
    except KeyboardInterrupt:
        sys.exit(-1)


if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
