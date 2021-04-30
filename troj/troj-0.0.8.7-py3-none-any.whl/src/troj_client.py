import requests
import json
import os
from typing import Optional, Dict, List
from utils import (
    assert_valid_name,
    raise_resp_exception_error
    # requests_retry
)


class TrojClient:
    '''
    api endpoint is gonna be the main endpoint I think, not really sure
    '''

    def __init__(
        self,
        *,
        # api_endpoint: str = 'http://localhost:8080/api/v1',
        api_endpoint: str = 'https://wuw1nar7mf.execute-api.ca-central-1.amazonaws.com/dev/api/v1',
        **kwargs,
    ) -> "Client":
        self._creds_api_key = None
        self._creds_token = None
        self._creds_app_id = None
        self._creds_app_key = None
        self.api_endpoint = api_endpoint

    def _get_creds_headers(self) -> Dict[str, str]:
        """
        Get appropriate request headers for the currently set credentials.

        Raises:
            Exception: No credentials set.

        Returns:
            dict: Dictionary of headers
        """
        if self._creds_token:
            return {"Authorization": f"Bearer {self._creds_token}"}
        else:
            raise Exception("No credentials set.")

    def set_credentials(
        self,
        *,
        api_key: Optional[str] = None,
        token: Optional[str] = None,
        app_id: Optional[str] = None,
        app_key: Optional[str] = None,
    ) -> None:
        """Set credentials for the client.

        Args:
            api_key (str, optional): A string for a long lived API key. Defaults to None.
            token (str, optional): A JWT providing auth credentials. Defaults to None.
            app_id (str, optional): Application ID string. Defaults to None.
            app_key (str, optional): Application secret key. Defaults to None.

        Raises:
            Exception: Invalid credential combination provided.
        """
        if api_key is not None:
            self._creds_api_key = api_key
        elif token is not None:
            self._creds_token = token
        elif app_id is not None and app_key is not None:
            self._creds_app_id = app_id
            self._creds_app_key = app_key
        else:
            raise Exception(
                "Please provide either an api_key, token, or app_id and app_key"
            )

    def test_api_endpoint(self):
        try:
            r = requests.get(
                'https://wuw1nar7mf.execute-api.ca-central-1.amazonaws.com/dev/ping')
            if (r.status_code == 200):
                return 200
        except Exception as exc:
            raise Exception(f'test_api_endpoint error: {exc}')

    # TODO: Create a project class, then dataset class
    # Users can name projects/datasets hatever they want
    # We store the hashed name in db instead of uuid
    # switch out uuids for names and compare hash in db instead of using uuids
    # profit??

    def create_project(self, project_name: str):
        """
        Create a new project via the REST API.

        Args:
            project_name (str): Name you want to give your project
        """

        assert_valid_name(project_name)

        data = {
            "project_name": project_name
        }
        r = requests.post(
            # f'{self.api_endpoint}/projects',
            f'{self.api_endpoint}/projects',
            headers=self._get_creds_headers(),
            data=json.dumps(data),
        )

        # No header = Exception: HTTP Error received: Forbidden: 403 | Not authenticated
        raise_resp_exception_error(r)
        return {"status_code": r.status_code, "data": r.json()}
        # End of create_project()

    def get_projects(self):
        """
        Get data about the users projects
        """

        r = requests.get(
            f'{self.api_endpoint}/projects',
            headers=self._get_creds_headers(),
        )

        raise_resp_exception_error(r)
        return {"status_code": r.status_code, "data": r.json()}

    def get_project(self, project_name: str):
        """
        Get data about a users specific project

        Args: 
            project_name (str): Name of the project to be gotten
        """

        r = requests.get(
            f'{self.api_endpoint}/projects/{project_name}',
            headers=self._get_creds_headers(),
        )

        raise_resp_exception_error(r)
        return {"status_code": r.status_code, "data": r.json()}

    def delete_project(self, project_name: str):
        """
        Try to delete a project

        Args: 
            project_name (str): Name of the project to be deleted
        """

        # Check if project exists
        # If no: raise exception saying it doesn't exist
        # if not self.get_project(project_name):
        #     raise Exception(f'Project \'{project_name}\' does not exist.')
        # If yes:
        # Check if project has datasets
        # If yes: raise exception saying datasets must be deleted first
        # if not self.get_project_datasets(project_name):
        #     raise Exception(
        #         f'Project \'{project_name}\' has existing datasets and cannot be deleted. Delete datasets and try again.')
        # If no: do delete

        r = requests.delete(
            f'{self.api_endpoint}/projects/{project_name}',
            headers=self._get_creds_headers(),
        )

        raise_resp_exception_error(r)
        return {"status_code": r.status_code, "data": r.json()}

    def create_dataset(self, project_name: str, dataset_name: str):
        assert_valid_name(dataset_name)
        project_data = self.get_project(project_name)

        data = {
            "project_uuid": project_data['data']['project_uuid'],
            "dataset_name": dataset_name
        }

        r = requests.post(
            f'{self.api_endpoint}/datasets',
            headers=self._get_creds_headers(),
            data=json.dumps(data),
        )

        raise_resp_exception_error(r)
        return {"status_code": r.status_code, "data": r.json()}
        # End of create_dataset()

    def get_project_datasets(self, project_name: str):
        """
        Get info about existing datasets for a specific project

        Args: 
            project_name (str): Name of the project you want to find datasets under
        """

        r = requests.get(
            f'{self.api_endpoint}/projects/{project_name}/datasets',
            headers=self._get_creds_headers(),
        )

        raise_resp_exception_error(r)
        return {"status_code": r.status_code, "data": r.json()}

    def dataset_exists(self, project_name: str, dataset_name: str):
        print("dataset check")

    def delete_dataset(self, project_name: str, dataset_name: str):
        r = requests.delete(
            f'{self.api_endpoint}/projects/{project_name}/datasets/{dataset_name}',
            headers=self._get_creds_headers(),
        )

        raise_resp_exception_error(r)
        return {"status_code": r.status_code, "data": r.json()}

    # Change arguments to take in project & dataset name instead of uuids
    # Do a get_dataset(dataset_name) and get uuids for dataset and project

    def post_dataframe(self, project_uuid=None, dataset_uuid=None, dataframe=None):
        if (project_uuid is None):
            raise Exception("Project UUID is needed.")
        if (dataset_uuid is None):
            raise Exception("Dataset UUID is needed.")
        if (dataframe is None):
            raise Exception("Dataframe is needed.")

        try:
            params = {
                'project_uuid': project_uuid,
                'dataset_uuid': dataset_uuid
            }

            r = requests.post(
                f'{self.api_endpoint}/send_output',
                params=params,
                data=json.dumps(dataframe),
                headers=self._get_creds_headers(),
            )
            print("post res:", r, r.text)
            # https://www.geeksforgeeks.org/response-methods-python-requests/
            if (r.status_code == 200):
                return True
            print('reason:', r.reason)
            return False
        except Exception as exc:
            raise Exception(f'post_dataframe error: {exc}')
