import logging
import sys

import typer as typer

from holdingsparser.application import run

logger = logging.getLogger(__name__)


def configure_logging(verbose: int):
    level = verbose * 10
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=level)


def main(
    term: str = typer.Argument(..., help="Name, ticker or CIK"),
    verbose: int = typer.Option(0, "--verbose", "-v", count=True),
):
    configure_logging(verbose)
    try:
        run(term)
    except RuntimeError as e:
        print(str(e))
        logging.exception(str(e))
        sys.exit(2)


if __name__ == "__main__":
    typer.run(main)
