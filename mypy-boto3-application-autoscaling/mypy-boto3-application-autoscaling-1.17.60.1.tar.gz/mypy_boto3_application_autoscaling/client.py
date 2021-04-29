"""
Main interface for application-autoscaling service client

Usage::

    ```python
    import boto3
    from mypy_boto3_application_autoscaling import ApplicationAutoScalingClient

    client: ApplicationAutoScalingClient = boto3.client("application-autoscaling")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_application_autoscaling.literals import (
    DescribeScalableTargetsPaginatorName,
    DescribeScalingActivitiesPaginatorName,
    DescribeScalingPoliciesPaginatorName,
    DescribeScheduledActionsPaginatorName,
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
    [ApplicationAutoScaling.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.can_paginate)
        """

    def delete_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: ServiceNamespace,
        ResourceId: str,
        ScalableDimension: ScalableDimension,
    ) -> Dict[str, Any]:
        """
        [Client.delete_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scaling_policy)
        """

    def delete_scheduled_action(
        self,
        ServiceNamespace: ServiceNamespace,
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: ScalableDimension,
    ) -> Dict[str, Any]:
        """
        [Client.delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scheduled_action)
        """

    def deregister_scalable_target(
        self,
        ServiceNamespace: ServiceNamespace,
        ResourceId: str,
        ScalableDimension: ScalableDimension,
    ) -> Dict[str, Any]:
        """
        [Client.deregister_scalable_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.deregister_scalable_target)
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
        [Client.describe_scalable_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scalable_targets)
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
        [Client.describe_scaling_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_activities)
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
        [Client.describe_scaling_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_policies)
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
        [Client.describe_scheduled_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scheduled_actions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.generate_presigned_url)
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
        [Client.put_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scaling_policy)
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
        [Client.put_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scheduled_action)
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
        [Client.register_scalable_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.register_scalable_target)
        """

    @overload
    def get_paginator(
        self, operation_name: DescribeScalableTargetsPaginatorName
    ) -> DescribeScalableTargetsPaginator:
        """
        [Paginator.DescribeScalableTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalableTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: DescribeScalingActivitiesPaginatorName
    ) -> DescribeScalingActivitiesPaginator:
        """
        [Paginator.DescribeScalingActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingActivities)
        """

    @overload
    def get_paginator(
        self, operation_name: DescribeScalingPoliciesPaginatorName
    ) -> DescribeScalingPoliciesPaginator:
        """
        [Paginator.DescribeScalingPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: DescribeScheduledActionsPaginatorName
    ) -> DescribeScheduledActionsPaginator:
        """
        [Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScheduledActions)
        """
