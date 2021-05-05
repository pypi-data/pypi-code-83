#!/usr/bin/env python3

import logging
import logging.config
from typing import Union
from pathlib import Path

__name__ = 'alogs'
__version__ = '3.3'
__author__ = 'Marcellus Amadeus'
__email__ = 'marcellus@alana.ai'
__url__ = 'https://bitbucket.org/alana-ai/alogs'


logging_settings = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": ('%(levelname)s %(asctime)s '
                       '%(processName)s:%(process)d '
                       '%(module)s:%(funcName)s() '
                       '%(filename)s:%(lineno)d '
                       '[%(name)s] = %(message)s'),
            "datefmt": "%d/%b/%Y:%H:%M:%S %z"
        }
    },

    "handlers": {
        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "info.log",
            "maxBytes": 10485760,
            "backupCount": 10,
            "encoding": "utf8"
        }
    },

    "root": {
        "handlers": ["info_file_handler"]
    }
}


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors"""

    grey = "\x1b[38;21m"
    green = "\x1b[32;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = ('%(levelname)s %(asctime)s '
              '%(processName)s:%(process)d '
              '%(module)s:%(funcName)s() '
              '%(filename)s:%(lineno)d '
              '[%(name)s] = %(message)s')

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger(module_name: str = None,
               log_file: Union[str, Path] = None,
               disable_existing_loggers: bool = False,
               root_level: str = 'debug') -> logging.Logger:
    """Create a Logger object with given module name.

    :param module_name: Logger name
    :param log_file: log file name
    :param disable_existing_loggers: whether to disable existing logs or not
    :param root_level: log level {debug, info, warning, error, critical}
    :return: Logger object
    """

    levels = {
        "CRITICAL": 50,
        "ERROR": 40,
        "WARNING": 30,
        "INFO": 20,
        "DEBUG": 10
    }

    if log_file is not None:
        log_settings = logging_settings.copy()
        log_settings['disable_existing_loggers'] = disable_existing_loggers
        log_settings["handlers"]['info_file_handler']['filename'] = log_file

        logging.config.dictConfig(log_settings)

    logger = logging.getLogger(module_name or __name__)

    for handler in logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            break
    else:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(CustomFormatter())
        logger.addHandler(stream_handler)

    logger.setLevel(levels.get(root_level.upper(), 10))

    return logger

