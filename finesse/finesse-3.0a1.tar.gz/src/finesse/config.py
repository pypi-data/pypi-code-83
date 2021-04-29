"""Configuration tools."""

# NOTE: this module gets imported by `finesse` directly, so cannot itself import from
# `finesse` and cannot import packages that themselves import from `finesse`.
import os
from pathlib import Path
import importlib.resources
from configparser import RawConfigParser
import logging
from fnmatch import fnmatch

from . import datastore
from .utilities import option_list


_PACKAGE_LOGGER = logging.getLogger(__package__)


def config_instance():
    """The Finesse configuration object for the current session.

    Returns
    -------
    :class:`configparser.RawConfigParser`
        The Finesse configuration object.
    """
    return datastore.init_singleton(_FinesseConfig)


def configure(
    plotting=False, log_level=None, log_exclude=None, jupyter_tracebacks=None
):
    """Configure Finesse runtime options.

    Parameters
    ----------
    plotting : bool, optional
        Initialise Finesse plot theme for display.

    log_level : str, optional
        Configure a special :mod:`finesse` log handler to print log messages emitted at
        this level or higher to the error stream. The Python log levels "debug", "info",
        "warning", "error" and "critical" are supported, as are their corresponding
        level numbers (see :mod:`logging`). The logger is only created once, but
        subsequent calls to this function will update the log level.

    log_exclude : list of :class:`str`, optional
        Names of log channels to suppress, if a Finesse log handler can be configured
        (see notes).

    jupyter_tracebacks : bool, optional
        Show full tracebacks in Finesse errors when using Finesse in IPython. This
        setting does not work reliably in other environments.

    Notes
    -----
    The `log_level` and `log_exclude` parameters are only set if the root `finesse` log
    handler is a `_FinesseStreamHandler`. This is the case when the user has not
    configured any other `finesse` log handler prior to running this function for the
    first time in the current session, which allows this function to safely create one.
    If another log handler does exist and `log_level` and/or `log_exclude` are set, they
    are ignored and a warning is emitted.

    See Also
    --------
    :func:`finesse.plotting.tools.init`
    """
    # NOTE: Before modifying this function, note that it may be called multiple times
    # during the execution of Finesse and should therefore remain idempotent.

    if plotting:
        from .plotting import init as init_plotting

        init_plotting(mode="display")

    # Remove any existing handlers configured by this function.
    _clear_log_handler_instance()

    if log_level is not None or log_exclude is not None:
        try:
            handler = log_handler_instance()
        except ExistingLogHandlerError:
            import warnings

            warnings.warn(
                f"an existing log handler was configured for '{__package__}' prior to "
                f"the first call to this function; refusing to set log level or "
                f"excludes"
            )
        else:
            try:
                log_level = log_level.upper()
            except AttributeError:
                # Probably a number.
                pass

            if log_level:
                # Set the root logger's level, not the handler.
                _PACKAGE_LOGGER.setLevel(log_level)

            if log_exclude:
                for exclude in log_exclude:
                    handler.exclude(exclude)

    if jupyter_tracebacks is not None:
        from .environment import show_tracebacks

        show_tracebacks(jupyter_tracebacks)


def autoconfigure():
    """Automatically configure runtime options based on the environment."""
    from .environment import is_interactive

    if is_interactive():
        # The user has imported Finesse inside a notebook or similar interactive
        # session. Configure some aspects of Finesse automatically: pretty plots,
        # suppress tracebacks and set logging to emit warnings and above to stderr if
        # the user hasn't already configured a logger prior to importing.
        log_level = "warning" if not _PACKAGE_LOGGER.handlers else None
        configure(plotting=False, log_level=log_level, jupyter_tracebacks=False)
    else:
        # Use the defaults.
        configure()


def log_handler_instance():
    """Get the Finesse stream handler instance, creating and adding it to the root
    logger if necessary.

    Raises
    ------
    :class:`.ExistingLogHandlerError`
        If an existing log handler is set for the `finesse` logger by the time this
        function is first called in the current session.
    """

    def instance():
        """The root Finesse log handler for the current session."""
        return datastore.init_singleton(_FinesseStreamHandler)

    # Get the Finesse stream handler, if necessary.
    if not datastore.has_singleton(_FinesseStreamHandler):
        if _PACKAGE_LOGGER.handlers:
            raise ExistingLogHandlerError()
        else:
            # Configure the Finesse stream handler.
            handler = instance()
            handler.setFormatter(
                logging.Formatter(config_instance()["logging"]["log_format"])
            )
            _PACKAGE_LOGGER.addHandler(handler)

    return instance()


def _clear_log_handler_instance():
    """Remove existing :class:`._FinesseStreamHandler` from the root Finesse logger if
    present."""

    for handler in list(_PACKAGE_LOGGER.handlers):
        if type(handler) is _FinesseStreamHandler:
            # Remove.
            _PACKAGE_LOGGER.removeHandler(handler)

    try:
        datastore.invalidate_singleton(_FinesseStreamHandler)
    except KeyError:
        # No existing instance.
        pass


class _FinesseStreamHandler(logging.StreamHandler):
    """Finesse stream handler.

    This class provides a mechanism to exclude displayed log channels by wildcard. It is
    otherwise identical to :py:class:`logging.StreamHandler`.

    Do not use this class directly. It is an internal class handled by :func:`configure`
    and instances may be managed and deleted at its whim.
    """

    def __init__(self):
        super().__init__()
        self.__excluded_channels = None
        self.reset_exclude_patterns()

    def exclude(self, pattern):
        self.__excluded_channels.add(pattern)

    def reset_exclude_patterns(self):
        """Empty the configured log channel exclude patterns, and return what was
        there."""
        old_excludes = set(self.__excluded_channels or [])
        self.__excluded_channels = set()
        return old_excludes

    def filter(self, record):
        for pattern in self.__excluded_channels:
            if fnmatch(record.name, pattern):
                # Skip the record.
                return
        return record


class _FinesseConfig(RawConfigParser):
    """The built-in and user configuration for Finesse.

    Do not instantiate this class directly; use :func:`config_instance`.
    """

    # Order in which user configs are loaded.
    _USER_CONFIG_LOAD_ORDER = ["user_config_path", "cwd_config_path"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.write_user_config()
        self._load_finesse_configs()

    @classmethod
    def user_config_paths(cls):
        return {
            config: getattr(cls, config)() for config in cls._USER_CONFIG_LOAD_ORDER
        }

    @classmethod
    def user_config_path(cls):
        return cls.user_config_dir() / "usr.ini"

    @classmethod
    def cwd_config_path(cls):
        return Path.cwd() / "finesse.ini"

    @classmethod
    def user_config_dir(cls):
        r"""The path to the user's config directory for Finesse.

        The exact path is determined by the current platform and the presence of certain
        environment variables:

        .. rubric:: Windows

        A folder called ``finesse`` in the folder pointed to by the environment variable
        ``%APPDATA`` (usually ``%HOMEPATH%\AppData\Roaming``).

        .. rubric:: POSIX (including Mac OS X and WSL)

        A directory called ``finesse`` inside either the path pointed to by the
        environment variable ``XDG_CONFIG_HOME`` or, if that value cannot be found or is
        empty, ``~/.config``.

        Returns
        -------
        :py:class:`pathlib.Path` or None
            The path to the Finesse config directory.

        Raises
        ------
        :py:class:`RuntimeError`
            If no config directory can be determined.
        """
        from .environment import IS_WINDOWS

        if IS_WINDOWS:
            try:
                config_dir = Path(os.environ["APPDATA"])
            except KeyError:
                # NOTE: we assume %APPDATA% always exists on any normal Windows machine,
                # which should be the case. If it's not, we might need to change Finesse
                # to handle having no user config path.
                raise RuntimeError(
                    r"The %APPDATA% environment variable is required for Finesse to "
                    r"store user configuration, but it was not found. Please ensure "
                    r"this environment variable exists in the environment in which "
                    r"Finesse is being run."
                )
        else:
            # Path.home() raises RuntimeError if no home is found.
            config_dir = Path(
                os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")
            )

        return config_dir / "finesse"

    @classmethod
    def write_user_config(cls, force=False):
        """Copy the default config files to the user's config directory."""
        logger = logging.getLogger(__name__)
        user_config_path = cls.user_config_path()

        if force or not user_config_path.is_file():
            # Copy barebone user config file contents into user's user config path.
            logger.info(f"Writing user config file to {user_config_path}.")

            user_config_path.parent.mkdir(parents=True, exist_ok=True)
            with user_config_path.open("wb") as fobj:
                fobj.write(importlib.resources.read_binary(__package__, "usr.ini.dist"))

    def _load_finesse_configs(self):
        """Read the built-in and any user configuration files.

        The built-in configuration is loaded first, then the user configuration files
        are loaded in the order specified in :attr:`.USER_PATHS`. This means user
        configuration options can overwrite built-in options, and options from later
        paths in :attr:`.USER_PATHS` can overwrite options from earlier paths.
        """
        user_config_paths = self.user_config_paths().values()

        # Load the bundled configuration.
        self.read_string(
            importlib.resources.read_text(__package__, "finesse.ini"),
            source="<bundled finesse.ini>",
        )

        # Parse all configurations, from lowest to highest priority.
        parsed = self.read(user_config_paths)

        if not parsed:
            paths = option_list(user_config_paths)

            raise ConfigNotFoundError(f"Could not find user config files at {paths}.")


class ConfigNotFoundError(Exception):
    """Indicates a Finesse configuration could not be loaded."""


class ExistingLogHandlerError(Exception):
    """Indicates an existing non-Finesse log handler was found registered for the
    Finesse package."""
