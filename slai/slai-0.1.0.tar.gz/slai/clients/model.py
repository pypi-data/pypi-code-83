import yaml
import io

from pathlib import Path

from slai.exceptions import ModelNotFound
from slai.clients.s3 import get_s3_client
from slai.clients.gdrive import get_google_drive_client
from slai.clients.project import get_project_client
from slai.clients.cli import get_cli_client
from slai.modules.parameters import from_config
from slai.modules.runtime import detect_runtime
from importlib import import_module


def get_model_client(*, model_name, project_name, client_id=None, client_secret=None):
    import_path = from_config(
        "MODEL_CLIENT",
        "slai.clients.model.ModelClient",
    )
    class_ = import_path.split(".")[-1]
    path = ".".join(import_path.split(".")[:-1])
    return getattr(import_module(path), class_)(
        model_name=model_name,
        project_name=project_name,
        client_id=client_id,
        client_secret=client_secret,
    )


class ModelClient:
    def __init__(
        self, *, model_name=None, project_name=None, client_id=None, client_secret=None
    ):
        self.runtime = detect_runtime()
        if self.runtime == "local":
            try:
                # we only need the google client when we're running locally
                self.gdrive_client = get_google_drive_client()
            except FileNotFoundError:
                # TODO: separate clients into a 'local model usage' and 'local model creation' client
                pass

        self.project_client = get_project_client(
            project_name=project_name, client_id=client_id, client_secret=client_secret
        )

        if client_id is None and client_secret is None:
            self.credentials = self.project_client.get_credentials()
        else:
            self.credentials = {"client_id": client_id, "client_secret": client_secret}

        self.api_client = get_cli_client(
            client_id=self.credentials["client_id"],
            client_secret=self.credentials["client_secret"],
        )

        self.model_name = model_name
        self.model = self.get_model()

    def get_project_name(self):
        return self.project_client.get_project_name()

    def create_model_folder(self, *, project_google_drive_folder_id):
        model_google_drive_folder_id = self.gdrive_client.create_folder(
            name=f"{self.model['name']}",
            parent_ids=[project_google_drive_folder_id],
        )
        return model_google_drive_folder_id

    def create_model_artifact(
        self, *, model_data, artifact_type, artifact_requirements, model_version_id=None
    ):
        if model_version_id is None:
            model_version_id = self.model["model_version_id"]

        model_artifact = self.api_client.create_model_artifact(
            model_version_id=model_version_id,
            model_data=model_data,
            artifact_type=artifact_type,
            artifact_requirements=artifact_requirements,
        )
        return model_artifact

    def create_model_deployment(
        self,
        *,
        model_artifact_id,
        model_handler_data,
        requirements,
    ):
        model_deployment = self.api_client.create_model_deployment(
            model_artifact_id=model_artifact_id,
            model_handler_data=model_handler_data,
            requirements=requirements,
        )
        return model_deployment

    def upload_model_notebook(
        self, *, model_google_drive_folder_id, notebook_path, file_id=None
    ):
        model_data = self.get_model()

        model_notebook_google_drive_file_id = self.gdrive_client.upload_file(
            filename=f"{model_data['name']}.ipynb",
            local_path=notebook_path,
            parent_ids=[
                model_google_drive_folder_id,
            ],
            file_id=file_id,
        )

        return model_notebook_google_drive_file_id

    def update_model(self, *, key, value):
        model_data = self.get_model()
        model_data[key] = value
        model_data = self.api_client.update_model(model_data=model_data)
        return model_data

    def get_model(self):
        model_data = self.api_client.retrieve_model(
            project_name=self.project_client.get_project_name(),
            name=self.model_name,
        )
        return model_data

    def get_latest_model_artifact(self, model_version_id=None):
        model_data = self.get_model()

        if model_version_id is None:
            model_version_id = model_data["model_version_id"]

        model_artifact = self.api_client.retrieve_model_artifact(
            model_version_id=model_version_id,
            model_artifact_id=None,
        )
        return model_artifact

    def download_latest_model_notebook(
        self, local_path, model_notebook_google_drive_file_id
    ):
        self.gdrive_client.download_file(
            file_id=model_notebook_google_drive_file_id,
            local_path=local_path,
        )


class MockModelClient:
    def __init__(self, *, model_name, project_name):
        pass

    def get_project_name(self):
        return "MOCK_PROJECT_NAME"

    def create_model_folder(self):
        return

    def create_model_artifact(
        self, *, model_data, artifact_type, artifact_requirements
    ):
        return {
            "id": "60329220dd191a68cfb474ec",
            "model_version_id": "60328ce6dd191a6608bb7da9",
            "artifact_type": artifact_type,
            "artifact_requirements": {"torch": "==1.70.0a0"},
            "created": "2021-02-21T12:02:24.503850",
        }

    def upload_template_model_notebook(self, template_notebook_path):
        return

    def update_model(self, *, key, value):
        model_data = {
            "id": "60329220dd191a68cfb474ec",
            "project_name": "something",
            "project_id": "60328ce6dd191a6608bb7da9",
            "name": "something1",
            "model_s3_data_bucket_name": None,
            "notebook_uri": None,
            "model_version_id": "60329220dd191a68cfb474ed",
            "created": "2021-02-21T12:02:24.503850",
            "updated": "2021-02-21T12:02:24.635203",
        }
        model_data[key] = value
        return model_data

    def get_model(self):
        return {
            "id": "60329220dd191a68cfb474ec",
            "project_name": "something",
            "project_id": "60328ce6dd191a6608bb7da9",
            "name": "something1",
            "model_s3_data_bucket_name": None,
            "notebook_uri": None,
            "model_version_id": "60329220dd191a68cfb474ed",
            "created": "2021-02-21T12:02:24.503850",
            "updated": "2021-02-21T12:02:24.635203",
        }

    def download_latest_model_notebook(self, local_path):
        return
