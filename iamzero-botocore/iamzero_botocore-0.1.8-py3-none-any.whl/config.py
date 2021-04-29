import logging
import os

from configparser import Error as ConfigError, RawConfigParser
from typing import Any, Mapping, Optional


LOGGER = logging.getLogger(__name__)

CONFIG_DEFAULT_VALUE = {
    # Instrumentation is disabled when true
    "DISABLE": False,
    # The backend URL
    "URL": "https://app.iamzero.dev",
    # Log configuration
    "LOG_LEVEL": "CRITICAL",
    # Whether to save logs to a file
    "LOG_LOCATION": None,
}

class Config(object):

    def __init__(self, default_values=None):
        # type: (Optional[Mapping[str, Any]]) -> None
        self.config = {}  # type: (Mapping[str, Any])

        if default_values is None:
            default_values = CONFIG_DEFAULT_VALUE

        self.default_values = default_values

        self.loaders = [
            self.load_from_default_values,
            self.load_from_env,
        ]

        self.config_path = None

    def load(self):
        """ Call each loader and update the config variable at the end
        """
        base_config = {}

        for loader in self.loaders:
            loaded = loader()

            if loaded:
                base_config.update(loaded)

        self.config = base_config

    def load_from_default_values(self):
        """ Returns default values
        """
        return self.default_values

    def load_from_env(self):
        """ Load configuration from os environment variables, variables
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
                    "Invalid config value for %s, using default value",
                    name.lower()
                )
                value = default_value
        return value

    def __getitem__(self, name):  # type: (str) -> Any
        return self.config[name]


CONFIG = Config()
CONFIG.load()