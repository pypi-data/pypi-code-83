"""
Type annotations for emr service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/literals.html)

Usage::

    ```python
    from mypy_boto3_emr.literals import ActionOnFailure

    data: ActionOnFailure = "CANCEL_AND_WAIT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionOnFailure",
    "AdjustmentType",
    "AuthMode",
    "AutoScalingPolicyState",
    "AutoScalingPolicyStateChangeReasonCode",
    "CancelStepsRequestStatus",
    "ClusterRunningWaiterName",
    "ClusterState",
    "ClusterStateChangeReasonCode",
    "ClusterTerminatedWaiterName",
    "ComparisonOperator",
    "ComputeLimitsUnitType",
    "ExecutionEngineType",
    "IdentityType",
    "InstanceCollectionType",
    "InstanceFleetState",
    "InstanceFleetStateChangeReasonCode",
    "InstanceFleetType",
    "InstanceGroupState",
    "InstanceGroupStateChangeReasonCode",
    "InstanceGroupType",
    "InstanceRoleType",
    "InstanceState",
    "InstanceStateChangeReasonCode",
    "JobFlowExecutionState",
    "ListBootstrapActionsPaginatorName",
    "ListClustersPaginatorName",
    "ListInstanceFleetsPaginatorName",
    "ListInstanceGroupsPaginatorName",
    "ListInstancesPaginatorName",
    "ListNotebookExecutionsPaginatorName",
    "ListSecurityConfigurationsPaginatorName",
    "ListStepsPaginatorName",
    "ListStudioSessionMappingsPaginatorName",
    "ListStudiosPaginatorName",
    "MarketType",
    "NotebookExecutionStatus",
    "OnDemandCapacityReservationPreference",
    "OnDemandCapacityReservationUsageStrategy",
    "OnDemandProvisioningAllocationStrategy",
    "PlacementGroupStrategy",
    "RepoUpgradeOnBoot",
    "ScaleDownBehavior",
    "SpotProvisioningAllocationStrategy",
    "SpotProvisioningTimeoutAction",
    "Statistic",
    "StepCancellationOption",
    "StepCompleteWaiterName",
    "StepExecutionState",
    "StepState",
    "StepStateChangeReasonCode",
    "Unit",
)


ActionOnFailure = Literal["CANCEL_AND_WAIT", "CONTINUE", "TERMINATE_CLUSTER", "TERMINATE_JOB_FLOW"]
AdjustmentType = Literal["CHANGE_IN_CAPACITY", "EXACT_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY"]
AuthMode = Literal["IAM", "SSO"]
AutoScalingPolicyState = Literal[
    "ATTACHED", "ATTACHING", "DETACHED", "DETACHING", "FAILED", "PENDING"
]
AutoScalingPolicyStateChangeReasonCode = Literal[
    "CLEANUP_FAILURE", "PROVISION_FAILURE", "USER_REQUEST"
]
CancelStepsRequestStatus = Literal["FAILED", "SUBMITTED"]
ClusterRunningWaiterName = Literal["cluster_running"]
ClusterState = Literal[
    "BOOTSTRAPPING",
    "RUNNING",
    "STARTING",
    "TERMINATED",
    "TERMINATED_WITH_ERRORS",
    "TERMINATING",
    "WAITING",
]
ClusterStateChangeReasonCode = Literal[
    "ALL_STEPS_COMPLETED",
    "BOOTSTRAP_FAILURE",
    "INSTANCE_FAILURE",
    "INSTANCE_FLEET_TIMEOUT",
    "INTERNAL_ERROR",
    "STEP_FAILURE",
    "USER_REQUEST",
    "VALIDATION_ERROR",
]
ClusterTerminatedWaiterName = Literal["cluster_terminated"]
ComparisonOperator = Literal[
    "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL"
]
ComputeLimitsUnitType = Literal["InstanceFleetUnits", "Instances", "VCPU"]
ExecutionEngineType = Literal["EMR"]
IdentityType = Literal["GROUP", "USER"]
InstanceCollectionType = Literal["INSTANCE_FLEET", "INSTANCE_GROUP"]
InstanceFleetState = Literal[
    "BOOTSTRAPPING", "PROVISIONING", "RESIZING", "RUNNING", "SUSPENDED", "TERMINATED", "TERMINATING"
]
InstanceFleetStateChangeReasonCode = Literal[
    "CLUSTER_TERMINATED", "INSTANCE_FAILURE", "INTERNAL_ERROR", "VALIDATION_ERROR"
]
InstanceFleetType = Literal["CORE", "MASTER", "TASK"]
InstanceGroupState = Literal[
    "ARRESTED",
    "BOOTSTRAPPING",
    "ENDED",
    "PROVISIONING",
    "RECONFIGURING",
    "RESIZING",
    "RUNNING",
    "SHUTTING_DOWN",
    "SUSPENDED",
    "TERMINATED",
    "TERMINATING",
]
InstanceGroupStateChangeReasonCode = Literal[
    "CLUSTER_TERMINATED", "INSTANCE_FAILURE", "INTERNAL_ERROR", "VALIDATION_ERROR"
]
InstanceGroupType = Literal["CORE", "MASTER", "TASK"]
InstanceRoleType = Literal["CORE", "MASTER", "TASK"]
InstanceState = Literal[
    "AWAITING_FULFILLMENT", "BOOTSTRAPPING", "PROVISIONING", "RUNNING", "TERMINATED"
]
InstanceStateChangeReasonCode = Literal[
    "BOOTSTRAP_FAILURE",
    "CLUSTER_TERMINATED",
    "INSTANCE_FAILURE",
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
]
JobFlowExecutionState = Literal[
    "BOOTSTRAPPING",
    "COMPLETED",
    "FAILED",
    "RUNNING",
    "SHUTTING_DOWN",
    "STARTING",
    "TERMINATED",
    "WAITING",
]
ListBootstrapActionsPaginatorName = Literal["list_bootstrap_actions"]
ListClustersPaginatorName = Literal["list_clusters"]
ListInstanceFleetsPaginatorName = Literal["list_instance_fleets"]
ListInstanceGroupsPaginatorName = Literal["list_instance_groups"]
ListInstancesPaginatorName = Literal["list_instances"]
ListNotebookExecutionsPaginatorName = Literal["list_notebook_executions"]
ListSecurityConfigurationsPaginatorName = Literal["list_security_configurations"]
ListStepsPaginatorName = Literal["list_steps"]
ListStudioSessionMappingsPaginatorName = Literal["list_studio_session_mappings"]
ListStudiosPaginatorName = Literal["list_studios"]
MarketType = Literal["ON_DEMAND", "SPOT"]
NotebookExecutionStatus = Literal[
    "FAILED",
    "FAILING",
    "FINISHED",
    "FINISHING",
    "RUNNING",
    "STARTING",
    "START_PENDING",
    "STOPPED",
    "STOPPING",
    "STOP_PENDING",
]
OnDemandCapacityReservationPreference = Literal["none", "open"]
OnDemandCapacityReservationUsageStrategy = Literal["use-capacity-reservations-first"]
OnDemandProvisioningAllocationStrategy = Literal["lowest-price"]
PlacementGroupStrategy = Literal["CLUSTER", "NONE", "PARTITION", "SPREAD"]
RepoUpgradeOnBoot = Literal["NONE", "SECURITY"]
ScaleDownBehavior = Literal["TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"]
SpotProvisioningAllocationStrategy = Literal["capacity-optimized"]
SpotProvisioningTimeoutAction = Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"]
Statistic = Literal["AVERAGE", "MAXIMUM", "MINIMUM", "SAMPLE_COUNT", "SUM"]
StepCancellationOption = Literal["SEND_INTERRUPT", "TERMINATE_PROCESS"]
StepCompleteWaiterName = Literal["step_complete"]
StepExecutionState = Literal[
    "CANCELLED", "COMPLETED", "CONTINUE", "FAILED", "INTERRUPTED", "PENDING", "RUNNING"
]
StepState = Literal[
    "CANCELLED", "CANCEL_PENDING", "COMPLETED", "FAILED", "INTERRUPTED", "PENDING", "RUNNING"
]
StepStateChangeReasonCode = Literal["NONE"]
Unit = Literal[
    "BITS",
    "BITS_PER_SECOND",
    "BYTES",
    "BYTES_PER_SECOND",
    "COUNT",
    "COUNT_PER_SECOND",
    "GIGA_BITS",
    "GIGA_BITS_PER_SECOND",
    "GIGA_BYTES",
    "GIGA_BYTES_PER_SECOND",
    "KILO_BITS",
    "KILO_BITS_PER_SECOND",
    "KILO_BYTES",
    "KILO_BYTES_PER_SECOND",
    "MEGA_BITS",
    "MEGA_BITS_PER_SECOND",
    "MEGA_BYTES",
    "MEGA_BYTES_PER_SECOND",
    "MICRO_SECONDS",
    "MILLI_SECONDS",
    "NONE",
    "PERCENT",
    "SECONDS",
    "TERA_BITS",
    "TERA_BITS_PER_SECOND",
    "TERA_BYTES",
    "TERA_BYTES_PER_SECOND",
]
