import sys
from mlfix import cli


def main() -> int:
    cli.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
