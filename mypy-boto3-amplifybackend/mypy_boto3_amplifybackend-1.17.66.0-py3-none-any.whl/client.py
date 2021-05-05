"""
Type annotations for amplifybackend service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_amplifybackend import AmplifyBackendClient

    client: AmplifyBackendClient = boto3.client("amplifybackend")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_amplifybackend.paginator import ListBackendJobsPaginator
from mypy_boto3_amplifybackend.type_defs import (
    BackendAPIResourceConfigTypeDef,
    CloneBackendResponseTypeDef,
    CreateBackendAPIResponseTypeDef,
    CreateBackendAuthResourceConfigTypeDef,
    CreateBackendAuthResponseTypeDef,
    CreateBackendConfigResponseTypeDef,
    CreateBackendResponseTypeDef,
    CreateTokenResponseTypeDef,
    DeleteBackendAPIResponseTypeDef,
    DeleteBackendAuthResponseTypeDef,
    DeleteBackendResponseTypeDef,
    DeleteTokenResponseTypeDef,
    GenerateBackendAPIModelsResponseTypeDef,
    GetBackendAPIModelsResponseTypeDef,
    GetBackendAPIResponseTypeDef,
    GetBackendAuthResponseTypeDef,
    GetBackendJobResponseTypeDef,
    GetBackendResponseTypeDef,
    GetTokenResponseTypeDef,
    ListBackendJobsResponseTypeDef,
    LoginAuthConfigReqObjTypeDef,
    RemoveAllBackendsResponseTypeDef,
    RemoveBackendConfigResponseTypeDef,
    UpdateBackendAPIResponseTypeDef,
    UpdateBackendAuthResourceConfigTypeDef,
    UpdateBackendAuthResponseTypeDef,
    UpdateBackendConfigResponseTypeDef,
    UpdateBackendJobResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AmplifyBackendClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    GatewayTimeoutException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class AmplifyBackendClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#can-paginate)
        """

    def clone_backend(
        self, AppId: str, BackendEnvironmentName: str, TargetEnvironmentName: str
    ) -> CloneBackendResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.clone_backend)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#clone-backend)
        """

    def create_backend(
        self,
        AppId: str,
        AppName: str,
        BackendEnvironmentName: str,
        ResourceConfig: Dict[str, Any] = None,
        ResourceName: str = None,
    ) -> CreateBackendResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#create-backend)
        """

    def create_backend_api(
        self,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceConfig: "BackendAPIResourceConfigTypeDef",
        ResourceName: str,
    ) -> CreateBackendAPIResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#create-backend-api)
        """

    def create_backend_auth(
        self,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceConfig: "CreateBackendAuthResourceConfigTypeDef",
        ResourceName: str,
    ) -> CreateBackendAuthResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#create-backend-auth)
        """

    def create_backend_config(
        self, AppId: str, BackendManagerAppId: str = None
    ) -> CreateBackendConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#create-backend-config)
        """

    def create_token(self, AppId: str) -> CreateTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.create_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#create-token)
        """

    def delete_backend(
        self, AppId: str, BackendEnvironmentName: str
    ) -> DeleteBackendResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_backend)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#delete-backend)
        """

    def delete_backend_api(
        self,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceName: str,
        ResourceConfig: "BackendAPIResourceConfigTypeDef" = None,
    ) -> DeleteBackendAPIResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_backend_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#delete-backend-api)
        """

    def delete_backend_auth(
        self, AppId: str, BackendEnvironmentName: str, ResourceName: str
    ) -> DeleteBackendAuthResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_backend_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#delete-backend-auth)
        """

    def delete_token(self, AppId: str, SessionId: str) -> DeleteTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#delete-token)
        """

    def generate_backend_api_models(
        self, AppId: str, BackendEnvironmentName: str, ResourceName: str
    ) -> GenerateBackendAPIModelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.generate_backend_api_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#generate-backend-api-models)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#generate-presigned-url)
        """

    def get_backend(
        self, AppId: str, BackendEnvironmentName: str = None
    ) -> GetBackendResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get-backend)
        """

    def get_backend_api(
        self,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceName: str,
        ResourceConfig: "BackendAPIResourceConfigTypeDef" = None,
    ) -> GetBackendAPIResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get-backend-api)
        """

    def get_backend_api_models(
        self, AppId: str, BackendEnvironmentName: str, ResourceName: str
    ) -> GetBackendAPIModelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_api_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get-backend-api-models)
        """

    def get_backend_auth(
        self, AppId: str, BackendEnvironmentName: str, ResourceName: str
    ) -> GetBackendAuthResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get-backend-auth)
        """

    def get_backend_job(
        self, AppId: str, BackendEnvironmentName: str, JobId: str
    ) -> GetBackendJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get-backend-job)
        """

    def get_token(self, AppId: str, SessionId: str) -> GetTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.get_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get-token)
        """

    def list_backend_jobs(
        self,
        AppId: str,
        BackendEnvironmentName: str,
        JobId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Operation: str = None,
        Status: str = None,
    ) -> ListBackendJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.list_backend_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#list-backend-jobs)
        """

    def remove_all_backends(
        self, AppId: str, CleanAmplifyApp: bool = None
    ) -> RemoveAllBackendsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.remove_all_backends)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#remove-all-backends)
        """

    def remove_backend_config(self, AppId: str) -> RemoveBackendConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.remove_backend_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#remove-backend-config)
        """

    def update_backend_api(
        self,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceName: str,
        ResourceConfig: "BackendAPIResourceConfigTypeDef" = None,
    ) -> UpdateBackendAPIResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#update-backend-api)
        """

    def update_backend_auth(
        self,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceConfig: UpdateBackendAuthResourceConfigTypeDef,
        ResourceName: str,
    ) -> UpdateBackendAuthResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#update-backend-auth)
        """

    def update_backend_config(
        self, AppId: str, LoginAuthConfig: "LoginAuthConfigReqObjTypeDef" = None
    ) -> UpdateBackendConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#update-backend-config)
        """

    def update_backend_job(
        self,
        AppId: str,
        BackendEnvironmentName: str,
        JobId: str,
        Operation: str = None,
        Status: str = None,
    ) -> UpdateBackendJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#update-backend-job)
        """

    def get_paginator(
        self, operation_name: Literal["list_backend_jobs"]
    ) -> ListBackendJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/amplifybackend.html#AmplifyBackend.Paginator.ListBackendJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/paginators.html#listbackendjobspaginator)
        """
