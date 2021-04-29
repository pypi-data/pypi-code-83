#!/usr/bin/env python3
import argparse
import logging
import sys

from rsync_tasks import RsyncTasks, __version__
from rsync_tasks.exceptions import ConfigError
from .log import logger_setup

_LOGGER = logging.getLogger(__package__)


def main() -> int:
    # gets inline arguments
    parser = argparse.ArgumentParser(prog="rsync_tasks")

    parser.add_argument("-c", "--config", dest="config_path", default="/etc/rsync_tasks/config.yaml",
                        help="configuration file path")
    parser.add_argument("-v", dest="log_level", action="count", default=0,
                        help="number of -v defines level of verbosity")

    parser.add_argument("--version", action="version", version="rsync_tasks {}".format(__version__))

    # parses args
    args = vars(parser.parse_args())

    # sets verbosity level
    logger_setup(args["log_level"])

    # removes no longer necessary log level from args
    del args["log_level"]

    # creates an instance of RsyncTasks
    try:
        rt = RsyncTasks.make_from_config(**args)
    except ConfigError as e:
        _LOGGER.critical("Configuration issue: I give up")
        return 1

    _LOGGER.info("RsyncTasks is ready to start")

    # starts backup operations
    rt.start()

    return 0


if __name__ == "__main__":
    sys.exit(main())
