import logging
import os
import stat
from .config import CONFIG

ROOT_LOGGER_NAME = "iamzero"
LOG_FORMAT = (
    "[%(levelname)s][%(asctime)s #%(process)d.%(threadName)s]"
    " %(name)s:%(lineno)s \t%(message)s"
)


def configure_root_logger(name, log_level=CONFIG["LOG_LEVEL"], log_location=CONFIG["LOG_LOCATION"]):
    """
    configure iamzero logger
    """
    logger = logging.getLogger(name)

    # Don't propagate messages to upper loggers
    logger.propagate = False
    logger.handlers = []

    formatter = logging.Formatter(LOG_FORMAT)

    # Configure the stderr handler configured on CRITICAL level
    stderr_handler = logging.StreamHandler()
    stderr_handler.setFormatter(formatter)
    logger.addHandler(stderr_handler)

    try:
        logger.setLevel(log_level)
    except ValueError:
        logger.error("Unknown log_level %r, default log level is CRITICAL", log_level)
        logger.setLevel(logging.CRITICAL)

    if log_location is not None:
        try:
            filehandler = logging.FileHandler(log_location)
            os.chmod(log_location, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP)
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)
        except (OSError, IOError):
            msg = "Couldn't use %s as iamzero log location, fallback to stderr."
            logger.error(msg, log_location, exc_info=True)
        else:
            stderr_handler.setLevel(logging.CRITICAL)

    return logger