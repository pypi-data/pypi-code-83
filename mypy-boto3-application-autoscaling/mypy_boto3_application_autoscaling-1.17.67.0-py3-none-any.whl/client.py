"""
Type annotations for application-autoscaling service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_application_autoscaling import ApplicationAutoScalingClient

    client: ApplicationAutoScalingClient = boto3.client("application-autoscaling")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_application_autoscaling.literals import (
    PolicyType,
    ScalableDimension,
    ServiceNamespace,
)
from mypy_boto3_application_autoscaling.paginator import (
    DescribeScalableTargetsPaginator,
    DescribeScalingActivitiesPaginator,
    DescribeScalingPoliciesPaginator,
    DescribeScheduledActionsPaginator,
)
from mypy_boto3_application_autoscaling.type_defs import (
    DescribeScalableTargetsResponseTypeDef,
    DescribeScalingActivitiesResponseTypeDef,
    DescribeScalingPoliciesResponseTypeDef,
    DescribeScheduledActionsResponseTypeDef,
    PutScalingPolicyResponseTypeDef,
    ScalableTargetActionTypeDef,
    StepScalingPolicyConfigurationTypeDef,
    SuspendedStateTypeDef,
    TargetTrackingScalingPolicyConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ApplicationAutoScalingClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentUpdateException: Type[BotocoreClientError]
    FailedResourceAccessException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ObjectNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ApplicationAutoScalingClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#can-paginate)
        """

    def delete_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: ServiceNamespace,
        ResourceId: str,
        ScalableDimension: ScalableDimension,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#delete-scaling-policy)
        """

    def delete_scheduled_action(
        self,
        ServiceNamespace: ServiceNamespace,
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: ScalableDimension,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scheduled_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#delete-scheduled-action)
        """

    def deregister_scalable_target(
        self,
        ServiceNamespace: ServiceNamespace,
        ResourceId: str,
        ScalableDimension: ScalableDimension,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.deregister_scalable_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#deregister-scalable-target)
        """

    def describe_scalable_targets(
        self,
        ServiceNamespace: ServiceNamespace,
        ResourceIds: List[str] = None,
        ScalableDimension: ScalableDimension = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeScalableTargetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scalable_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#describe-scalable-targets)
        """

    def describe_scaling_activities(
        self,
        ServiceNamespace: ServiceNamespace,
        ResourceId: str = None,
        ScalableDimension: ScalableDimension = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeScalingActivitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_activities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#describe-scaling-activities)
        """

    def describe_scaling_policies(
        self,
        ServiceNamespace: ServiceNamespace,
        PolicyNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: ScalableDimension = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeScalingPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#describe-scaling-policies)
        """

    def describe_scheduled_actions(
        self,
        ServiceNamespace: ServiceNamespace,
        ScheduledActionNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: ScalableDimension = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeScheduledActionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scheduled_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#describe-scheduled-actions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#generate-presigned-url)
        """

    def put_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: ServiceNamespace,
        ResourceId: str,
        ScalableDimension: ScalableDimension,
        PolicyType: PolicyType = None,
        StepScalingPolicyConfiguration: "StepScalingPolicyConfigurationTypeDef" = None,
        TargetTrackingScalingPolicyConfiguration: "TargetTrackingScalingPolicyConfigurationTypeDef" = None,
    ) -> PutScalingPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#put-scaling-policy)
        """

    def put_scheduled_action(
        self,
        ServiceNamespace: ServiceNamespace,
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: ScalableDimension,
        Schedule: str = None,
        Timezone: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        ScalableTargetAction: "ScalableTargetActionTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scheduled_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#put-scheduled-action)
        """

    def register_scalable_target(
        self,
        ServiceNamespace: ServiceNamespace,
        ResourceId: str,
        ScalableDimension: ScalableDimension,
        MinCapacity: int = None,
        MaxCapacity: int = None,
        RoleARN: str = None,
        SuspendedState: "SuspendedStateTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.register_scalable_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/client.html#register-scalable-target)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scalable_targets"]
    ) -> DescribeScalableTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalableTargets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators.html#describescalabletargetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_activities"]
    ) -> DescribeScalingActivitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingActivities)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators.html#describescalingactivitiespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_policies"]
    ) -> DescribeScalingPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators.html#describescalingpoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> DescribeScheduledActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScheduledActions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators.html#describescheduledactionspaginator)
        """
