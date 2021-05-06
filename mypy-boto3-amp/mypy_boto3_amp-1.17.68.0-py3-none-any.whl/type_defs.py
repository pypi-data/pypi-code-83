"""
Type annotations for amp service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amp.type_defs import CreateWorkspaceResponseTypeDef

    data: CreateWorkspaceResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_amp.literals import WorkspaceStatusCode

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateWorkspaceResponseTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "ListWorkspacesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "WorkspaceDescriptionTypeDef",
    "WorkspaceStatusTypeDef",
    "WorkspaceSummaryTypeDef",
)


class CreateWorkspaceResponseTypeDef(TypedDict):
    arn: str
    status: "WorkspaceStatusTypeDef"
    workspaceId: str


class DescribeWorkspaceResponseTypeDef(TypedDict):
    workspace: "WorkspaceDescriptionTypeDef"


class _RequiredListWorkspacesResponseTypeDef(TypedDict):
    workspaces: List["WorkspaceSummaryTypeDef"]


class ListWorkspacesResponseTypeDef(_RequiredListWorkspacesResponseTypeDef, total=False):
    nextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredWorkspaceDescriptionTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    status: "WorkspaceStatusTypeDef"
    workspaceId: str


class WorkspaceDescriptionTypeDef(_RequiredWorkspaceDescriptionTypeDef, total=False):
    alias: str
    prometheusEndpoint: str


class WorkspaceStatusTypeDef(TypedDict):
    statusCode: WorkspaceStatusCode


class _RequiredWorkspaceSummaryTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    status: "WorkspaceStatusTypeDef"
    workspaceId: str


class WorkspaceSummaryTypeDef(_RequiredWorkspaceSummaryTypeDef, total=False):
    alias: str
