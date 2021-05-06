"""Configuration for hdev commands."""
import os

import toml

DEFAULT_CONFIG_FILENAME = "pyproject.toml"


class Configuration(dict):
    """A dict which lets you access it's keys via dot separated strings."""

    def get(self, key, default=None):
        """Get nested dict keys using "key" with dot as separator.

           config.get("key", {}).get("nested", DEFAULT)

        becomes:

            config.get("key.nested", DEFAULT)
        """
        value = self
        for sub_key in key.split("."):
            try:
                value = value[sub_key]
            except KeyError:
                return default

        return value


def load_configuration(config_path=None):
    """Load hdev configuration based on `config_path`."""
    if not config_path:
        config_path = os.path.join(os.getcwd(), DEFAULT_CONFIG_FILENAME)

    try:
        toml_config = toml.load(config_path)
    except FileNotFoundError:
        # No project file, use defaults
        toml_config = {}
    except ValueError:
        print(f"Invalid syntax on toml file '{config_path}'")
        return None

    return Configuration(toml_config)
