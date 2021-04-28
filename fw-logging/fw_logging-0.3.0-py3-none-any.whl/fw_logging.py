"""Logging helper module standardizing logging and reducing boilerplate."""
import copy
import datetime
import fileinput
import functools
import logging
import logging.config
import pathlib
import re
import sys
import typing as t

import crayons
import orjson
from pydantic import BaseSettings, Field

__all__ = ["setup_logging", "get_log_config", "Filter"]


colors = {  # pylint: disable=no-member
    color: getattr(crayons, color)
    for color in ("white", "blue", "cyan", "green", "yellow", "red", "magenta")
}

level_colors = {
    "TRACE": colors["blue"],
    "DEBUG": colors["cyan"],
    "INFO": colors["green"],
    "WARNING": colors["yellow"],
    "ERROR": colors["red"],
    "CRITICAL": colors["magenta"],
}


def setup_logging(**kwargs) -> None:
    """Configure logging with settings from `get_log_config()`."""
    logging.config.dictConfig(get_log_config(**kwargs))


def get_log_config(**kwargs) -> dict:
    """Get log config dict based on kwargs and/or envvars."""
    # create log config using kwargs (~application defaults)
    config = LogConfig(**kwargs)
    if config.handler == "file":
        color = False
    elif config.color is None:
        color = getattr(sys, config.handler).isatty()
    else:
        color = config.color
    # merge any env-configured loggers/filters (~runtime overrides)
    config.loggers.update(LogConfig().loggers)
    config.filters.update(LogConfig().filters)
    # return the logconfig dict
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {"level": config.level, "handlers": [config.handler]},
        "loggers": {
            logger: {"level": level or config.level, "handlers": [config.handler]}
            for logger, level in config.loggers.items()
        },
        "filters": {
            filt: {"()": "fw_logging.Filter", "add_all": False, **kwargs}
            for filt, kwargs in config.filters.items()
        },
        "formatters": {
            "text": {
                "()": "fw_logging.Formatter",
                "fmt": config.fmt,
                "datefmt": config.datefmt,
                "color": color,
            },
            "json": {
                "()": "fw_logging.JSONFormatter",
                "tag": config.json_tag,
            },
        },
        "handlers": {
            "stdout": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "filters": list(config.filters),
                "formatter": config.formatter,
            },
            "stderr": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
                "filters": list(config.filters),
                "formatter": config.formatter,
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": str(config.filename),
                "delay": True,
                "maxBytes": config.max_bytes,
                "backupCount": config.backup_count,
                "filters": list(config.filters),
                "formatter": config.formatter,
            },
        },
    }


class LogConfig(BaseSettings):  # pylint: disable=too-few-public-methods
    """Logging config."""

    class Config:  # pylint: disable=too-few-public-methods
        """Enable envvars with prefix `FW_LOG_`."""

        env_prefix = "FW_LOG_"

    level: str = Field("INFO", regex=r"TRACE|DEBUG|INFO|WARNING|ERROR|CRITICAL")
    handler: str = Field("stdout", regex=r"stdout|stderr|file")
    formatter: str = Field("text", regex=r"text|json")
    loggers: t.Dict[str, t.Optional[str]] = {}
    filters: t.Dict[str, t.Dict[str, str]] = {}

    # options for the file handler
    filename: pathlib.Path = pathlib.Path("log.txt")
    max_bytes: int = 5 << 20
    backup_count: int = 10

    # options for the text formatter
    fmt: str = "{asctime}.{msecs:03.0f} {levelname} {caller} {message}"
    datefmt: str = "%Y-%m-%d %H:%M:%S"
    color: t.Optional[bool]

    # options for the json formatter
    json_tag: t.Optional[str]


class Filter(logging.Filter):
    """Log exclusion filter allowing temporary filtering as a context manager."""

    def __init__(self, *, name: str = "", msg: str = "", add_all: bool = True) -> None:
        """Add exclusion filter to all handlers attached to the root logger.

        Args:
            name (str): Logger name prefix to ignore messages from.
            msg (str): Log message pattern to ignore when matched via re.search.
            add_all (bool): Set to False to skip auto-adding on all handlers.
        """
        assert name or msg, "Filter record name and/or msg required"
        super().__init__(name)
        self.name = name
        self.msg_re = re.compile(msg) if msg else None
        if add_all:
            handlers = logging.root.handlers
            assert handlers, "No handlers found - run setup_logging() first"
            for handler in handlers:
                handler.addFilter(self)

    def __enter__(self) -> "Filter":
        """Enter 'with' context - return the filter object."""
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Exit 'with' context - remove filter from the root handlers."""
        for handler in logging.root.handlers:
            handler.removeFilter(self)

    def filter(self, record: logging.LogRecord) -> bool:
        """Return True if the record doesn't match all of the exclude filters."""
        exclude = []
        if self.name:
            exclude.append(super().filter(record))
        if self.msg_re:
            exclude.append(bool(self.msg_re.search(record.msg)))
        return not all(exclude)


class Formatter(logging.Formatter):
    """Log formatter with color support.

    See https://github.com/encode/uvicorn/blob/0.12.3/uvicorn/logging.py
    """

    def __init__(
        self,
        fmt: t.Optional[str] = None,
        datefmt: t.Optional[str] = None,
        color: bool = False,
    ) -> None:
        """Initialize Formatter."""
        super().__init__(fmt=fmt, datefmt=datefmt, style="{")
        self.color = color

    def formatMessage(self, record: logging.LogRecord) -> str:
        """Colorize levelname if color is enabled."""
        record_ = copy.copy(record)
        record_.__dict__["levelname"] = get_levelname(record.levelno, self.color)
        record_.__dict__["caller"] = get_caller(record, self.color)
        return super().formatMessage(record_)


@functools.lru_cache()
def get_levelname(levelno: int, color: bool = False) -> str:
    """Return 4 char long log level name, optionally colorized (cached)."""
    # pylint: disable=protected-access
    levelname = logging._levelToName.get(levelno, f"LV{levelno:02d}")[:4]
    if not color:
        return levelname
    color_fn = colors["white"]
    for level, color_fn in level_colors.items():
        if levelno <= getattr(logging, level):
            break
    return str(color_fn(levelname, always=True, bold=True))


def get_caller(record: logging.LogRecord, color: bool = False) -> str:
    """Return log record caller information, optionally colorized."""
    module_path = get_module_path(record.pathname)
    caller = f"{module_path}:{record.lineno:<4d}"
    # capture custom logger names not based on __name__
    if record.name != module_path:
        caller = f"{record.name}:{caller}"
    if not color:
        return caller
    return str(colors["blue"](caller, always=True))


@functools.lru_cache()
def get_module_path(filepath: str) -> str:
    """Return python module path from the given filepath (cached)."""
    path = pathlib.Path(filepath)
    module_path = path.stem
    while (path.parent / "__init__.py").exists():
        path = path.parent
        module_path = f"{path.name}.{module_path}"
    return module_path


class JSONFormatter(logging.Formatter):
    """JSON log formatter."""

    def __init__(self, tag: t.Optional[str] = None) -> None:
        """Initialize JSONFormatter."""
        self.tag = tag
        super().__init__()

    def format(self, record: logging.LogRecord) -> str:
        """Format the given LogRecord as a JSON string."""
        record_dict = {
            "msg": record.getMessage(),
            "lvl": record.levelname,
            "time": datetime.datetime.fromtimestamp(record.created),
            "caller": get_caller(record),
            "proc": record.process,
            "thrd": record.thread,
        }
        if record.exc_info:
            record_dict["exc"] = self.formatException(record.exc_info)
        if "tag" in record.__dict__ or self.tag:
            record_dict["tag"] = record.__dict__.get("tag") or self.tag
        # pylint: disable=c-extension-no-member
        return orjson.dumps(record_dict).decode()


def logformat() -> None:
    """Read JSON logs from an input file or stdin and print in text format."""
    for idx, line in enumerate(fileinput.input()):
        try:
            print(format_line(line))
        except Exception as exc:  # pylint: disable=broad-except
            msg = f"Error: {exc}".replace("line 1", f"line {idx + 1}", 1)
            print(colors["red"](msg), file=sys.stderr)
            print(line)


def format_line(line: str) -> str:
    """Return a human-readable log line from a JSON log record."""
    record = orjson.loads(line)
    # support keys of both fw-logging and flywheel-common
    msg = record.get("msg") or record["message"]
    lvl = (record.get("lvl") or record["severity"])[:4]
    time = (record.get("time") or record["timestamp"])[:23].replace("T", " ")
    caller = record.get("caller") or f"{record['filename']}:{record['lineno']:<4d}"
    for level, color_fn in level_colors.items():
        if level.startswith(lvl):
            lvl = color_fn(lvl)
            break
    prefix = f"{time} {lvl} {colors['blue'](caller)} "
    return f"{prefix}{msg}".replace("\n", "\n" + " " * len(prefix))  # multiline


def add_log_level(name: str, num: int) -> None:
    """Add a custom log level to the logging module.

    * add `name.upper()` attribute to the logging module with value num.
    * add `name.lower()` function/method to the logging module/logger class.
    """
    name = name.upper()
    func = name.lower()

    def _root_log(msg, *args, **kwargs):
        kwargs.setdefault("stacklevel", 3)
        logging.log(num, msg, *args, **kwargs)

    def _logger_log(self, msg, *args, **kwargs):
        if self.isEnabledFor(num):
            # pylint: disable=protected-access
            self._log(num, msg, args, **kwargs)

    _root_log.__doc__ = f"Log a message with severity '{name}' on the root logger."
    _logger_log.__doc__ = f"Log 'msg % args' with severity '{name}'."

    logging.addLevelName(num, name)
    setattr(logging, name, num)
    setattr(logging, func, _root_log)
    setattr(logging.getLoggerClass(), func, _logger_log)


add_log_level("TRACE", 5)
