import os
import logging
import sys
import argparse
from pathlib import Path
from mlfix import fix


def configure_logging():
    level = os.environ.get("LOG_LEVEL", "error").upper()
    logging.basicConfig(level=logging.getLevelName(level))


def _main_parser() -> argparse.ArgumentParser:
    """
    main application parser
    """
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    p.add_argument("path_to_store", help="Local path to the artifact store to fix")

    p.add_argument(
        "--mlruns-name",
        type=str,
        default="mlruns",
        help="Name of the mlruns folder (default: %(default)s)",
    )

    return p


def cmd_fix(ns: argparse.Namespace):
    path = Path(ns.path_to_store).resolve().absolute()
    mlruns_name = ns.mlruns_name
    print(
        f"fixing artifact store in path: '{path}', former mlruns name: '{mlruns_name}'..."
    )
    fix.fix_meta(path, mlruns_name)
    print("done!")


def run():
    configure_logging()
    if sys.version_info < (3, 6, 0):
        sys.stderr.write("You need python 3.6 or later to run this script\n")
        sys.exit(1)

    parser = _main_parser()
    namespace = parser.parse_args()
    if namespace.path_to_store is not None:
        cmd_fix(namespace)
    else:
        parser.print_help()
