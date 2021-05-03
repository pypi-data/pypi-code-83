"""
Type annotations for resource-groups service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/literals.html)

Usage::

    ```python
    from mypy_boto3_resource_groups.literals import GroupConfigurationStatus

    data: GroupConfigurationStatus = "UPDATE_COMPLETE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GroupConfigurationStatus",
    "GroupFilterName",
    "ListGroupResourcesPaginatorName",
    "ListGroupsPaginatorName",
    "QueryErrorCode",
    "QueryType",
    "ResourceFilterName",
    "ResourceStatusValue",
    "SearchResourcesPaginatorName",
)


GroupConfigurationStatus = Literal["UPDATE_COMPLETE", "UPDATE_FAILED", "UPDATING"]
GroupFilterName = Literal["configuration-type", "resource-type"]
ListGroupResourcesPaginatorName = Literal["list_group_resources"]
ListGroupsPaginatorName = Literal["list_groups"]
QueryErrorCode = Literal["CLOUDFORMATION_STACK_INACTIVE", "CLOUDFORMATION_STACK_NOT_EXISTING"]
QueryType = Literal["CLOUDFORMATION_STACK_1_0", "TAG_FILTERS_1_0"]
ResourceFilterName = Literal["resource-type"]
ResourceStatusValue = Literal["PENDING"]
SearchResourcesPaginatorName = Literal["search_resources"]
