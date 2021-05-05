from slai.modules.parameters import from_config
from slai.modules.runtime import detect_runtime, detect_credentials
from slai.clients.model import get_model_client

from requests.auth import HTTPBasicAuth
from importlib import import_module

import requests

REQUESTS_TIMEOUT = 15


def get_inference_client(
    *, model_name, project_name, version, client_id=None, client_secret=None
):
    import_path = from_config(
        "MODEL_INFERENCE_CLIENT",
        "slai.clients.inference.ModelInferenceClient",
    )
    class_ = import_path.split(".")[-1]
    path = ".".join(import_path.split(".")[:-1])

    return getattr(import_module(path), class_)(
        model_name=model_name,
        project_name=project_name,
        version=version,
        client_id=client_id,
        client_secret=client_secret,
    )


class ModelInferenceClient:
    BASE_URL = from_config(
        key="BASE_URL",
        default="https://6zacu5yc29.execute-api.us-east-1.amazonaws.com/development",
    )

    def __init__(
        self,
        *,
        model_name,
        project_name,
        version="latest",
        client_id=None,
        client_secret=None,
    ):
        self.runtime = detect_runtime()

        if client_id is None or client_secret is None:
            credentials = detect_credentials(runtime=self.runtime)
            self.client_id = credentials["client_id"]
            self.client_secret = credentials["client_secret"]
        else:
            self.client_id = client_id
            self.client_secret = client_secret

        self.model_name = model_name
        self.project_name = project_name
        self.version = version

        self._load_model()

    def _load_model(self):
        self.model_client = get_model_client(
            model_name=self.model_name,
            project_name=self.project_name,
            client_id=self.client_id,
            client_secret=self.client_secret,
        )
        self.model = self.model_client.get_model()

    def call(self, payload):
        body = {
            "model_id": self.model["id"],
            "model_version_id": self.version,
            "payload": payload,
        }

        res = requests.post(
            f"{self.BASE_URL}/model/call",
            auth=HTTPBasicAuth(self.client_id, self.client_secret),
            json=body,
            timeout=REQUESTS_TIMEOUT,
        )
        res.raise_for_status()
        return res.json()

    def info(self):
        pass
