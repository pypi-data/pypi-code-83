import io
import json

from shutil import copyfile
from pathlib import Path

from importlib import import_module
from pydrive.auth import GoogleAuth, RefreshError
from pydrive.drive import GoogleDrive
from slai.modules.parameters import from_config
from slai.clients.cli import get_cli_client
from slai.clients.project import get_project_client


def get_google_drive_client():
    import_path = from_config(
        "GOOGLE_DRIVE_CLIENT",
        "slai.clients.gdrive.GoogleDriveClient",
    )
    class_ = import_path.split(".")[-1]
    path = ".".join(import_path.split(".")[:-1])
    return getattr(import_module(path), class_)()


class GoogleDriveClient:
    def __init__(self):
        self.project_client = get_project_client(project_name=None)
        self.credentials = self.project_client.get_credentials()

        self.cli_client = get_cli_client(
            client_id=self.credentials["client_id"],
            client_secret=self.credentials["client_secret"],
        )

        gauth = self._authenticate()
        self.drive_client = GoogleDrive(gauth)

    def _local_auth_flow(self, gauth):
        gauth.GetFlow()
        gauth.flow.params.update({"access_type": "offline"})
        gauth.flow.params.update({"include_granted_scopes": "true"})

        gauth.LocalWebserverAuth()

    def _authenticate(self):
        user = self.cli_client.get_user()
        if user["gauth_creds"] is not None:
            with open(".slai/gauth/creds.json", "w") as f_out:
                json.dump(user["gauth_creds"], f_out)

        # copy client secrets file from gauth
        copyfile(".slai/gauth/client_secrets.json", Path.cwd() / "client_secrets.json")

        # TODO: handle failed auth
        gauth = GoogleAuth(settings_file=".slai/gauth/settings.yml")

        gauth.LoadCredentialsFile(".slai/gauth/creds.json")
        if gauth.credentials is None:
            self._local_auth_flow(gauth)
        elif gauth.access_token_expired:
            try:
                gauth.Refresh()
            except RefreshError:
                self._local_auth_flow(gauth)
        else:
            gauth.Authorize()

        gauth.SaveCredentialsFile(".slai/gauth/creds.json")
        if user["gauth_creds"] is None:
            with open(".slai/gauth/creds.json", "r") as f_in:
                gauth_creds = json.load(f_in)
                self.cli_client.update_user(email=None, gauth_creds=gauth_creds)

        # remove it once we are authenticated
        file_to_rem = Path.cwd() / "client_secrets.json"
        file_to_rem.unlink()

        return gauth

    def _format_parents(self, parent_ids):
        parents = []
        if parent_ids is not None:
            for _id in parent_ids:
                parents.append({"id": _id})
        return parents

    def upload_file(self, *, filename, local_path, parent_ids, file_id=None):
        parents = self._format_parents(parent_ids)

        _file = None
        if file_id is None:
            _file = self.drive_client.CreateFile(
                {"title": f"{filename}", "parents": parents}
            )
        else:
            _file = self.drive_client.CreateFile(
                {"title": f"{filename}", "parents": parents, "id": file_id}
            )

        _file.SetContentFile(local_path)
        _file.Upload()

        return _file["id"]

    def create_folder(self, *, name, parent_ids=None):
        parents = self._format_parents(parent_ids)
        folder_file = self.drive_client.CreateFile(
            {
                "title": name,
                "parents": parents,
                "mimeType": "application/vnd.google-apps.folder",
            }
        )
        folder_file.Upload()
        return folder_file["id"]

    def download_file(self, *, file_id, local_path):
        _file = self.drive_client.CreateFile({"id": file_id})
        _file.GetContentFile(local_path)
        return _file


class MockGoogleDriveClient:
    def __init__(self):
        pass

    def upload_file(self, *, filename, local_path, parent_ids):
        return "FILE_ABCDEFG"

    def create_folder(self, *, name, parent_ids=None):
        return "FOLDER_ABCDEFG"

    def download_file(self, *, file_id, local_path):
        _file = io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01")
        return _file
