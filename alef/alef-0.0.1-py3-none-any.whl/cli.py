import fire

from .logging import getLogger, initLogging

logging = getLogger("bbox")


def _main():
    print("hello")


def main():
    fire.Fire(_main)
