import logging
import os

from configparser import Error as ConfigError, RawConfigParser
from typing import Any, Mapping, Optional


LOGGER = logging.getLogger(__name__)

CONFIG_DEFAULT_VALUES = {
    # Instrumentation is disabled when true
    "DISABLE": False,
    # The backend URL
    "URL": "https://app.iamzero.dev",
    # Log configuration
    "LOG_LEVEL": "CRITICAL",
    # Whether to save logs to a file
    "LOG_LOCATION": None,
    # The authentication token
    "TOKEN": None,
}


HOME_FILE_PATH = os.path.expanduser("~/.iamzero.ini")


class Config(object):
    """
    Loads config with the following priorities:

    1. env variables (IAMZERO_ + the name of the config variable - eg IAMZERO_URL)
    2. config file (by default ~/.iamzero.ini, or whatever the value of IAMZERO_CONFIG_FILE env var is, falling back to iamzero.ini in the local project directory)
    3. Default values as per CONFIG_DEFAULT_VALUE
    """

    FILE_ENV_VAR = "IAMZERO_CONFIG_FILE"
    HOME_FILE_PATH = HOME_FILE_PATH

    def __init__(self, default_values=None):
        # type: (Optional[Mapping[str, Any]]) -> None
        self.config = {}  # type: (Mapping[str, Any])

        if default_values is None:
            default_values = CONFIG_DEFAULT_VALUES

        self.default_values = default_values

        self.loaders = [
            self.load_from_default_values,
            self.load_from_file,
            self.load_from_env,
        ]

        self.config_path = None

    def load(self):
        """Call each loader and update the config variable at the end"""
        base_config = {}

        for loader in self.loaders:
            loaded = loader()

            if loaded:
                base_config.update(loaded)

        self.config = base_config

    def load_from_default_values(self):
        """Returns default values"""
        return self.default_values

    def load_from_file(self):
        """
        Load from config file
        """

        file_path = (
            self.config_path
            or self._file_path_from_env()
            or self._file_path_from_home()
            or self._file_path_from_local()
        )

        if not file_path:
            return {}

        config = RawConfigParser()

        try:
            config.read(file_path)

            config_dict = {}
            for option in config.options("iamzero"):
                upper_option = option.upper()
                config_dict[upper_option] = self._coerce_value(
                    upper_option, config.get("iamzero", option)
                )

            return config_dict
        except ConfigError:
            LOGGER.debug("Error parsing config file %s", file_path)
            return {}

    def load_from_env(self):
        """Load configuration from os environment variables, variables
        must be prefixed with IAMZERO_ to be detected.
        """
        env_config = {}
        for env_var, value in os.environ.items():
            if env_var.startswith("IAMZERO_"):
                key = env_var[8:].upper()
                env_config[key] = self._coerce_value(key, value)
        return env_config

    def _coerce_value(self, name, value):  # type: (str, Any) -> Any
        default_value = self.default_values.get(name)
        # best effort conversion to boolean
        if isinstance(default_value, bool):
            value = value.lower().strip() in ("1", "true", "yes", "y")
        elif isinstance(default_value, (int, float)):
            try:
                value = type(default_value)(value)
            except ValueError:
                LOGGER.error(
                    "Invalid config value for %s, using default value", name.lower()
                )
                value = default_value
        return value

    def _file_path_from_env(self):
        """Return file path if os environement was set and file exists"""
        path = os.getenv(self.FILE_ENV_VAR, default=None)

        if path and os.path.isfile(path):
            return path

    def _file_path_from_home(self):
        """Return file path if file exists in home directory"""
        if self.HOME_FILE_PATH and os.path.isfile(self.HOME_FILE_PATH):
            return self.HOME_FILE_PATH

    def _file_path_from_local():
        """Return file path if file exists locally on the project"""
        if os.path.isfile("iamzero.ini"):
            return os.path.join(os.getcwd(), "iamzero.ini")

    def __getitem__(self, name):  # type: (str) -> Any
        return self.config[name]


CONFIG = Config()
CONFIG.load()
