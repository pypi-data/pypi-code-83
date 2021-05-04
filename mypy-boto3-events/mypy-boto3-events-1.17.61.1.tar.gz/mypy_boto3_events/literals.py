"""
Type annotations for events service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_events/literals.html)

Usage::

    ```python
    from mypy_boto3_events.literals import ApiDestinationHttpMethod

    data: ApiDestinationHttpMethod = "DELETE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ApiDestinationHttpMethod",
    "ApiDestinationState",
    "ArchiveState",
    "AssignPublicIp",
    "ConnectionAuthorizationType",
    "ConnectionOAuthHttpMethod",
    "ConnectionState",
    "EventSourceState",
    "LaunchType",
    "ListRuleNamesByTargetPaginatorName",
    "ListRulesPaginatorName",
    "ListTargetsByRulePaginatorName",
    "ReplayState",
    "RuleState",
)


ApiDestinationHttpMethod = Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
ApiDestinationState = Literal["ACTIVE", "INACTIVE"]
ArchiveState = Literal[
    "CREATE_FAILED", "CREATING", "DISABLED", "ENABLED", "UPDATE_FAILED", "UPDATING"
]
AssignPublicIp = Literal["DISABLED", "ENABLED"]
ConnectionAuthorizationType = Literal["API_KEY", "BASIC", "OAUTH_CLIENT_CREDENTIALS"]
ConnectionOAuthHttpMethod = Literal["GET", "POST", "PUT"]
ConnectionState = Literal[
    "AUTHORIZED", "AUTHORIZING", "CREATING", "DEAUTHORIZED", "DEAUTHORIZING", "DELETING", "UPDATING"
]
EventSourceState = Literal["ACTIVE", "DELETED", "PENDING"]
LaunchType = Literal["EC2", "FARGATE"]
ListRuleNamesByTargetPaginatorName = Literal["list_rule_names_by_target"]
ListRulesPaginatorName = Literal["list_rules"]
ListTargetsByRulePaginatorName = Literal["list_targets_by_rule"]
ReplayState = Literal["CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "RUNNING", "STARTING"]
RuleState = Literal["DISABLED", "ENABLED"]
