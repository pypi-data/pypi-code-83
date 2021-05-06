"""
Type annotations for identitystore service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/type_defs.html)

Usage::

    ```python
    from mypy_boto3_identitystore.type_defs import DescribeGroupResponseTypeDef

    data: DescribeGroupResponseTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DescribeGroupResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "FilterTypeDef",
    "GroupTypeDef",
    "ListGroupsResponseTypeDef",
    "ListUsersResponseTypeDef",
    "UserTypeDef",
)


class DescribeGroupResponseTypeDef(TypedDict):
    GroupId: str
    DisplayName: str


class DescribeUserResponseTypeDef(TypedDict):
    UserName: str
    UserId: str


class FilterTypeDef(TypedDict):
    AttributePath: str
    AttributeValue: str


class GroupTypeDef(TypedDict):
    GroupId: str
    DisplayName: str


class _RequiredListGroupsResponseTypeDef(TypedDict):
    Groups: List["GroupTypeDef"]


class ListGroupsResponseTypeDef(_RequiredListGroupsResponseTypeDef, total=False):
    NextToken: str


class _RequiredListUsersResponseTypeDef(TypedDict):
    Users: List["UserTypeDef"]


class ListUsersResponseTypeDef(_RequiredListUsersResponseTypeDef, total=False):
    NextToken: str


class UserTypeDef(TypedDict):
    UserName: str
    UserId: str
