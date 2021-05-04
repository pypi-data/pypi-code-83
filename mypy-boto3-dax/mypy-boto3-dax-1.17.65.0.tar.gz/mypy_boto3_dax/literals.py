"""
Type annotations for dax service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/literals.html)

Usage::

    ```python
    from mypy_boto3_dax.literals import ChangeType

    data: ChangeType = "IMMEDIATE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ChangeType",
    "DescribeClustersPaginatorName",
    "DescribeDefaultParametersPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeParameterGroupsPaginatorName",
    "DescribeParametersPaginatorName",
    "DescribeSubnetGroupsPaginatorName",
    "IsModifiable",
    "ListTagsPaginatorName",
    "ParameterType",
    "SSEStatus",
    "SourceType",
)


ChangeType = Literal["IMMEDIATE", "REQUIRES_REBOOT"]
DescribeClustersPaginatorName = Literal["describe_clusters"]
DescribeDefaultParametersPaginatorName = Literal["describe_default_parameters"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeParameterGroupsPaginatorName = Literal["describe_parameter_groups"]
DescribeParametersPaginatorName = Literal["describe_parameters"]
DescribeSubnetGroupsPaginatorName = Literal["describe_subnet_groups"]
IsModifiable = Literal["CONDITIONAL", "FALSE", "TRUE"]
ListTagsPaginatorName = Literal["list_tags"]
ParameterType = Literal["DEFAULT", "NODE_TYPE_SPECIFIC"]
SSEStatus = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
SourceType = Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"]
