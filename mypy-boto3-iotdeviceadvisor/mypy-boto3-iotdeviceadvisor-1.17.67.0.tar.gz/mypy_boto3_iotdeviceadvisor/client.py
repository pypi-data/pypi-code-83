"""
Type annotations for iotdeviceadvisor service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotdeviceadvisor import IoTDeviceAdvisorClient

    client: IoTDeviceAdvisorClient = boto3.client("iotdeviceadvisor")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_iotdeviceadvisor.type_defs import (
    CreateSuiteDefinitionResponseTypeDef,
    GetSuiteDefinitionResponseTypeDef,
    GetSuiteRunReportResponseTypeDef,
    GetSuiteRunResponseTypeDef,
    ListSuiteDefinitionsResponseTypeDef,
    ListSuiteRunsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTestCasesResponseTypeDef,
    StartSuiteRunResponseTypeDef,
    SuiteDefinitionConfigurationTypeDef,
    SuiteRunConfigurationTypeDef,
    UpdateSuiteDefinitionResponseTypeDef,
)

__all__ = ("IoTDeviceAdvisorClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class IoTDeviceAdvisorClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#can-paginate)
        """

    def create_suite_definition(
        self,
        suiteDefinitionConfiguration: "SuiteDefinitionConfigurationTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateSuiteDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.create_suite_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#create-suite-definition)
        """

    def delete_suite_definition(self, suiteDefinitionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.delete_suite_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#delete-suite-definition)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#generate-presigned-url)
        """

    def get_suite_definition(
        self, suiteDefinitionId: str, suiteDefinitionVersion: str = None
    ) -> GetSuiteDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.get_suite_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#get-suite-definition)
        """

    def get_suite_run(self, suiteDefinitionId: str, suiteRunId: str) -> GetSuiteRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.get_suite_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#get-suite-run)
        """

    def get_suite_run_report(
        self, suiteDefinitionId: str, suiteRunId: str
    ) -> GetSuiteRunReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.get_suite_run_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#get-suite-run-report)
        """

    def list_suite_definitions(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListSuiteDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_suite_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#list-suite-definitions)
        """

    def list_suite_runs(
        self,
        suiteDefinitionId: str = None,
        suiteDefinitionVersion: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSuiteRunsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_suite_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#list-suite-runs)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#list-tags-for-resource)
        """

    def list_test_cases(
        self, intendedForQualification: bool = None, maxResults: int = None, nextToken: str = None
    ) -> ListTestCasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_test_cases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#list-test-cases)
        """

    def start_suite_run(
        self,
        suiteDefinitionId: str,
        suiteDefinitionVersion: str = None,
        suiteRunConfiguration: "SuiteRunConfigurationTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> StartSuiteRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.start_suite_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#start-suite-run)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#tag-resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#untag-resource)
        """

    def update_suite_definition(
        self,
        suiteDefinitionId: str,
        suiteDefinitionConfiguration: "SuiteDefinitionConfigurationTypeDef" = None,
    ) -> UpdateSuiteDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.update_suite_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/client.html#update-suite-definition)
        """
