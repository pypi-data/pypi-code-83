import os
import yaml

from pathlib import Path
from slai.exceptions import NoCredentialsFound

LOCAL_CREDENTIALS_PATHS = {
    "project": ".slai/config.yml",
    "global": f"{Path.home()}/.slai/credentials.yml",
}


class ValidRuntimes:
    Local = "local"
    Collab = "collab"


def detect_runtime():
    try:
        import google.colab

        return "collab"
    except ImportError:
        return "local"


def detect_credentials(*, runtime, profile="default"):
    credentials = None
    if runtime == ValidRuntimes.Local:

        if os.path.exists(LOCAL_CREDENTIALS_PATHS["project"]):
            credentials = _load_credentials(
                path=LOCAL_CREDENTIALS_PATHS["project"], credentials_type="project"
            )
        elif os.path.exists(LOCAL_CREDENTIALS_PATHS["global"]):
            credentials = _load_credentials(
                path=LOCAL_CREDENTIALS_PATHS["global"], credentials_type="global"
            )
            credentials = credentials.get(profile)
        else:
            raise NoCredentialsFound("slai_config_not_found")

    elif runtime == ValidRuntimes.Collab:
        _mount_google_drive()
        credentials = _load_credentials(
            path=f"{os.getenv('SLAI_PROJECT_PATH')}/config.yml"
        )

    return credentials


def _load_credentials(*, path, credentials_type="global"):
    credentials = {}

    with open(path, "r") as f_in:
        try:
            credentials = yaml.safe_load(f_in)
        except yaml.YAMLError:
            raise NoCredentialsFound("slai_invalid_config")

    if credentials_type == "global":
        return credentials
    elif credentials_type == "project":
        return {
            "client_id": credentials["client_id"],
            "client_secret": credentials["client_secret"],
            "aws_profile": credentials["aws_profile"],
        }

    return credentials


def _mount_google_drive():
    try:
        from google.colab import drive

        drive.mount("/content/drive", force_remount=True)
    except ImportError:
        raise
