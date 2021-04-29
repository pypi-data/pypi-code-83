"""
Main interface for cloudwatch service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudwatch import CloudWatchClient
    from mypy_boto3_cloudwatch.waiter import (
        AlarmExistsWaiter,
        CompositeAlarmExistsWaiter,
    )

    client: CloudWatchClient = boto3.client("cloudwatch")

    alarm_exists_waiter: AlarmExistsWaiter = client.get_waiter("alarm_exists")
    composite_alarm_exists_waiter: CompositeAlarmExistsWaiter = client.get_waiter("composite_alarm_exists")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_cloudwatch.literals import AlarmType, StateValue
from mypy_boto3_cloudwatch.type_defs import WaiterConfigTypeDef

__all__ = ("AlarmExistsWaiter", "CompositeAlarmExistsWaiter")


class AlarmExistsWaiter(Boto3Waiter):
    """
    [Waiter.AlarmExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Waiter.AlarmExists)
    """

    def wait(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        AlarmTypes: List[AlarmType] = None,
        ChildrenOfAlarmName: str = None,
        ParentsOfAlarmName: str = None,
        StateValue: StateValue = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [AlarmExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Waiter.AlarmExists.wait)
        """


class CompositeAlarmExistsWaiter(Boto3Waiter):
    """
    [Waiter.CompositeAlarmExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Waiter.CompositeAlarmExists)
    """

    def wait(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        AlarmTypes: List[AlarmType] = None,
        ChildrenOfAlarmName: str = None,
        ParentsOfAlarmName: str = None,
        StateValue: StateValue = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [CompositeAlarmExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Waiter.CompositeAlarmExists.wait)
        """
