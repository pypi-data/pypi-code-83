"""
Type annotations for appconfig service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/literals.html)

Usage::

    ```python
    from mypy_boto3_appconfig.literals import DeploymentEventType

    data: DeploymentEventType = "BAKE_TIME_STARTED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DeploymentEventType",
    "DeploymentState",
    "EnvironmentState",
    "GrowthType",
    "ReplicateTo",
    "TriggeredBy",
    "ValidatorType",
)


DeploymentEventType = Literal[
    "BAKE_TIME_STARTED",
    "DEPLOYMENT_COMPLETED",
    "DEPLOYMENT_STARTED",
    "PERCENTAGE_UPDATED",
    "ROLLBACK_COMPLETED",
    "ROLLBACK_STARTED",
]
DeploymentState = Literal[
    "BAKING", "COMPLETE", "DEPLOYING", "ROLLED_BACK", "ROLLING_BACK", "VALIDATING"
]
EnvironmentState = Literal["DEPLOYING", "READY_FOR_DEPLOYMENT", "ROLLED_BACK", "ROLLING_BACK"]
GrowthType = Literal["EXPONENTIAL", "LINEAR"]
ReplicateTo = Literal["NONE", "SSM_DOCUMENT"]
TriggeredBy = Literal["APPCONFIG", "CLOUDWATCH_ALARM", "INTERNAL_ERROR", "USER"]
ValidatorType = Literal["JSON_SCHEMA", "LAMBDA"]
