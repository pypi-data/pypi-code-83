import boto3
import yaml
import os

from slai.exceptions import ModelNotFound, ProjectNotFound
from slai.clients.cli import SlaiCliClient
from slai.modules.parameters import from_config
from slai.modules.runtime import detect_runtime, detect_credentials, ValidRuntimes

from pathlib import Path
from importlib import import_module


def get_project_client(*, project_name, client_id=None, client_secret=None):
    import_path = from_config(
        "PROJECT_CLIENT",
        "slai.clients.project.ProjectClient",
    )
    class_ = import_path.split(".")[-1]
    path = ".".join(import_path.split(".")[:-1])

    return getattr(import_module(path), class_)(
        project_name=project_name, client_id=client_id, client_secret=client_secret
    )


class ProjectClient:
    def __init__(self, *, project_name=None, client_id=None, client_secret=None):
        self.runtime = detect_runtime()

        self.project_name = project_name
        if client_id is None and client_secret is None:
            self.credentials = detect_credentials(runtime=self.runtime)
        else:
            self.credentials = {"client_id": client_id, "client_secret": client_secret}

        self.cli_client = SlaiCliClient(
            client_id=self.credentials["client_id"],
            client_secret=self.credentials["client_secret"],
        )

    def list_models(self):
        """ List models in a slai project. """
        project = self.get_project()
        return project["models"]

    def _load_config_from_disk(self):
        cwd = Path.cwd()
        config = None
        local_config_path = None

        if self.runtime == ValidRuntimes.Local:
            local_config_path = f"{cwd}/.slai/config.yml"
        elif self.runtime == ValidRuntimes.Collab:
            local_config_path = os.getenv("SLAI_CONFIG_FILE")

        with open(local_config_path, "r") as f_in:
            try:
                config = yaml.safe_load(f_in)
            except yaml.YAMLError:
                pass

        return config

    def get_credentials(self):
        return self.credentials

    def get_project_name(self):
        """ Retrieve project configuration values. """
        if self.project_name is None:
            config = self._load_config_from_disk()
            return config["project_name"]

        return self.project_name

    def get_project(self):
        """ Retrieve project configuration values. """
        project = self.cli_client.retrieve_project(project_name=self.get_project_name())

        return project


class MockProjectClient:
    def __init__(self):
        self.runtime = detect_runtime()
        self.project_id = "MOCK_PROJECT_ID"

    def list_models(self):
        project = {"models": []}
        return project["models"]

    def get_project_name(self):
        return "MOCK_PROJECT_NAME"

    def get_project(self):
        project = {
            "id": self.project_id,
            "name": "some_project",
            "project_folder_google_drive_file_id": None,
            "created": "2021-02-21T11:40:06.607882",
            "updated": "2021-02-21T11:40:06.653309",
            "models": [],
        }
        return project
