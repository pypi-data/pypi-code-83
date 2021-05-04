from slai.modules.parameters import from_config
from slai.modules.runtime import detect_runtime, detect_credentials, ValidRuntimes
from slai.clients.inference import get_inference_client


class Model:
    def __init__(
        self,
        *,
        model_name,
        project_name,
        version="latest",
        client_id=None,
        client_secret=None
    ):
        self.inference_client = get_inference_client(
            model_name=model_name,
            project_name=project_name,
            version=version,
            client_id=client_id,
            client_secret=client_secret,
        )

    def __call__(self, **inputs):
        return self.inference_client.call(payload=inputs)

    def info(self):
        pass
