from __future__ import annotations

import logging
import os
from shutil import which

import yamale
from yamale import YamaleError
from yaml.scanner import ScannerError

from rsync_tasks import exceptions
from rsync_tasks.exceptions import TaskFailed, SourcePathNotExist

_LOGGER = logging.getLogger(__package__)


class RsyncTasks:
    def __init__(self,
                 tasks: list[dict[str, str]],
                 flags: str,
                 base_path_source: str,
                 base_path_destination: str,
                 stop_on_failed_task: bool = False,
                 **kwargs):
        self._tasks = tasks

        self._flags = flags
        self._base_path_source = base_path_source
        self._base_path_destination = base_path_destination
        self._stop_on_failed_task = stop_on_failed_task

        # Checks if the necessary system tools are available
        RsyncTasks._check_tools()

    @classmethod
    def make_from_config(cls, config_path: str) -> RsyncTasks:
        # Loads the config schema to validate the config
        schema = yamale.make_schema(os.path.join(os.path.dirname(__file__), "resources/config.schema.yaml"))

        # Tries to load config file
        try:
            config = yamale.make_data(config_path)
        except FileNotFoundError:
            _LOGGER.error("Configuration file '{}' not found".format(config_path))
            raise exceptions.ConfigNotFound(config_path)
        except ScannerError as e:
            _LOGGER.error("Invalid configuration file '{}'\n{}".format(config_path, e))
            raise exceptions.InvalidConfig(e)

        # Tries to validate the configuration with the schema
        try:
            yamale.validate(schema, config)
        except YamaleError as e:
            _LOGGER.error("Invalid configuration file '{}'\n{}".format(config_path, e))
            raise exceptions.InvalidConfig(e)

        _LOGGER.info("Configuration loaded")

        # create instance form config
        config, _ = config[0]
        return cls(**config)

    @staticmethod
    def _check_tools() -> None:
        # Checks if 'rsync' is available
        if which("rsync") is None:
            e = exceptions.RsyncNotAvailable
            _LOGGER.error(e)
            raise e

        _LOGGER.info("All the needed tools are available")

    def start(self):
        for task in self._tasks:
            source = os.path.join(self._base_path_source, task["s"])
            destination = os.path.join(self._base_path_destination, task["d"])

            if not os.path.exists(source):
                _LOGGER.warning(f"Source path `{source}` does not exists")
                if self._stop_on_failed_task:
                    raise SourcePathNotExist(source)
                continue

            # creates the command for the current target
            command = self._mk_command(source, destination)
            _LOGGER.debug(f"Run command `{command}`")

            if os.system(command) != 0:
                _LOGGER.warning(f"Failed target `{command}`")
                if self._stop_on_failed_task:
                    raise TaskFailed(task["s"])

    def _mk_command(self, source: str, destination: str) -> str:
        command = ["rsync"]

        # adds necessary flag
        command += [self._flags]

        # adds the paths
        command += [f"\"{source}\"", f"\"{destination}\""]

        return " ".join(command)
