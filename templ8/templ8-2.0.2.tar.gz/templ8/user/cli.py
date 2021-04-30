import os
from argparse import ArgumentParser
from configparser import ConfigParser
from typing import Tuple

from templ8.user.flags import Flags
from templ8.user.inputs import Inputs
from templ8.utils.dataclasses import map_to_signature


def parse_version() -> str:
    parser = ConfigParser()
    parser.read(os.path.normpath(os.path.join(__file__, "..", "..", "..", "setup.cfg")))
    return parser.get("metadata", "version")


def parse_cli() -> Tuple[Inputs, Flags]:
    cli = ArgumentParser("templ8", description=f"Templ8 cli version: {parse_version()}")
    cli.add_argument("input", help="input file path")
    cli.add_argument(
        "-v",
        "--verbose",
        help="increase the verbosity level",
        action="append_const",
        const=1,
    )
    cli.add_argument(
        "-d", "--dry-run", help="don't generate anything", action="store_true"
    )
    cli.add_argument(
        "-s", "--silent", help="don't output any logs", action="store_true"
    )

    args = cli.parse_args()
    args.verbosity = sum(args.verbose) if args.verbose else 0

    flags = Flags(**map_to_signature(Flags, args.__dict__))
    inputs = Inputs.from_file(args.input)
    return (inputs, flags)
