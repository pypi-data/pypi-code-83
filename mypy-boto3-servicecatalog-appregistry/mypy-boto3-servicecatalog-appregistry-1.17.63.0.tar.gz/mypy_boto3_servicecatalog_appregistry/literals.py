"""
Type annotations for servicecatalog-appregistry service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/literals.html)

Usage::

    ```python
    from mypy_boto3_servicecatalog_appregistry.literals import ListApplicationsPaginatorName

    data: ListApplicationsPaginatorName = "list_applications"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListApplicationsPaginatorName",
    "ListAssociatedAttributeGroupsPaginatorName",
    "ListAssociatedResourcesPaginatorName",
    "ListAttributeGroupsPaginatorName",
    "ResourceType",
    "SyncAction",
)


ListApplicationsPaginatorName = Literal["list_applications"]
ListAssociatedAttributeGroupsPaginatorName = Literal["list_associated_attribute_groups"]
ListAssociatedResourcesPaginatorName = Literal["list_associated_resources"]
ListAttributeGroupsPaginatorName = Literal["list_attribute_groups"]
ResourceType = Literal["CFN_STACK"]
SyncAction = Literal["NO_ACTION", "START_SYNC"]
