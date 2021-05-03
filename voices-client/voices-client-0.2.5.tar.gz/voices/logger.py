"""Logger for Voices integration."""

import logging
import os
from logging import Logger

LOG_LEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'WARN': logging.WARN,
    'ERROR': logging.ERROR,
    'FATAL': logging.FATAL,
    'CRITICAL': logging.CRITICAL,
}

LOGGER_ENV_VAR = 'LOG_LEVEL'
LOGGER_NAME = 'voices'


def build_logger(**kwargs) -> Logger:
    """Build repository logger from configuration.

    :param kwargs: Logger configurations forwarded from repository objects.
        :debug bool: Flag for enable debug level when a specific logger or level is not provided
        :logger Logger: Preconfigured logger instance
        :logger_name: Name of the logger that will be generated from config
        :logger_level: Leve of the logger that will be generated from config
    :return Logger: Logger instance
    """

    if 'logger' in kwargs.keys() and isinstance(kwargs['logger'], Logger):
        return kwargs['logger']

    level = _get_logging_level(
        debug=kwargs.get('debug', None),
        logger_level=kwargs.get('logger_level', None),
    )

    logger_name = kwargs.get('logger_name', LOGGER_NAME)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    return logger


def _get_logging_level(debug: bool = None, logger_level: int = None) -> int:
    """Obtain logging level for logger from configuration.

    :param debug: configured debug mode
    :param logger_level: Specific level from configuration
    :return int: Logging level code
    """

    level = ''
    logging_level = logging.INFO

    if os.getenv(LOGGER_ENV_VAR, None) is not None:
        level = os.getenv(LOGGER_ENV_VAR).upper()

    if level in LOG_LEVELS.keys():
        logging_level = LOG_LEVELS[level]

    if logger_level is not None and logger_level in LOG_LEVELS.values():
        logging_level = logger_level

    if debug is not None and debug:
        logging_level = logging.DEBUG

    return logging_level
