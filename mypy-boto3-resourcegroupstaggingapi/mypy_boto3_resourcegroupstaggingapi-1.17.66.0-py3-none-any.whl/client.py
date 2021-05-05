"""
Type annotations for resourcegroupstaggingapi service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_resourcegroupstaggingapi import ResourceGroupsTaggingAPIClient

    client: ResourceGroupsTaggingAPIClient = boto3.client("resourcegroupstaggingapi")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_resourcegroupstaggingapi.literals import GroupByAttribute
from mypy_boto3_resourcegroupstaggingapi.paginator import (
    GetComplianceSummaryPaginator,
    GetResourcesPaginator,
    GetTagKeysPaginator,
    GetTagValuesPaginator,
)
from mypy_boto3_resourcegroupstaggingapi.type_defs import (
    DescribeReportCreationOutputTypeDef,
    GetComplianceSummaryOutputTypeDef,
    GetResourcesOutputTypeDef,
    GetTagKeysOutputTypeDef,
    GetTagValuesOutputTypeDef,
    TagFilterTypeDef,
    TagResourcesOutputTypeDef,
    UntagResourcesOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ResourceGroupsTaggingAPIClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConstraintViolationException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    PaginationTokenExpiredException: Type[BotocoreClientError]
    ThrottledException: Type[BotocoreClientError]


class ResourceGroupsTaggingAPIClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client.html#can-paginate)
        """

    def describe_report_creation(self) -> DescribeReportCreationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.describe_report_creation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client.html#describe-report-creation)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client.html#generate-presigned-url)
        """

    def get_compliance_summary(
        self,
        TargetIdFilters: List[str] = None,
        RegionFilters: List[str] = None,
        ResourceTypeFilters: List[str] = None,
        TagKeyFilters: List[str] = None,
        GroupBy: List[GroupByAttribute] = None,
        MaxResults: int = None,
        PaginationToken: str = None,
    ) -> GetComplianceSummaryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_compliance_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client.html#get-compliance-summary)
        """

    def get_resources(
        self,
        PaginationToken: str = None,
        TagFilters: List[TagFilterTypeDef] = None,
        ResourcesPerPage: int = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[str] = None,
        IncludeComplianceDetails: bool = None,
        ExcludeCompliantResources: bool = None,
        ResourceARNList: List[str] = None,
    ) -> GetResourcesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client.html#get-resources)
        """

    def get_tag_keys(self, PaginationToken: str = None) -> GetTagKeysOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_tag_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client.html#get-tag-keys)
        """

    def get_tag_values(self, Key: str, PaginationToken: str = None) -> GetTagValuesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_tag_values)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client.html#get-tag-values)
        """

    def start_report_creation(self, S3Bucket: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.start_report_creation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client.html#start-report-creation)
        """

    def tag_resources(
        self, ResourceARNList: List[str], Tags: Dict[str, str]
    ) -> TagResourcesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.tag_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client.html#tag-resources)
        """

    def untag_resources(
        self, ResourceARNList: List[str], TagKeys: List[str]
    ) -> UntagResourcesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.untag_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client.html#untag-resources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_compliance_summary"]
    ) -> GetComplianceSummaryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/paginators.html#getcompliancesummarypaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_resources"]) -> GetResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/paginators.html#getresourcespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_tag_keys"]) -> GetTagKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/paginators.html#gettagkeyspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_tag_values"]) -> GetTagValuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/paginators.html#gettagvaluespaginator)
        """
