"""
Main interface for devicefarm service type definitions.

Usage::

    ```python
    from mypy_boto3_devicefarm.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_devicefarm.literals import (
    ArtifactType,
    BillingMethod,
    CurrencyCode,
    DeviceAttribute,
    DeviceAvailability,
    DeviceFilterAttribute,
    DeviceFormFactor,
    DevicePlatform,
    DevicePoolType,
    ExecutionResult,
    ExecutionResultCode,
    ExecutionStatus,
    InstanceStatus,
    InteractionMode,
    NetworkProfileType,
    OfferingTransactionType,
    OfferingType,
    RecurringChargeFrequency,
    RuleOperator,
    SampleType,
    TestGridSessionArtifactType,
    TestGridSessionStatus,
    TestType,
    UploadCategory,
    UploadStatus,
    UploadType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountSettingsTypeDef",
    "ArtifactTypeDef",
    "CPUTypeDef",
    "CountersTypeDef",
    "CustomerArtifactPathsTypeDef",
    "DeviceFilterTypeDef",
    "DeviceInstanceTypeDef",
    "DeviceMinutesTypeDef",
    "DevicePoolCompatibilityResultTypeDef",
    "DevicePoolTypeDef",
    "DeviceSelectionResultTypeDef",
    "DeviceTypeDef",
    "IncompatibilityMessageTypeDef",
    "InstanceProfileTypeDef",
    "JobTypeDef",
    "LocationTypeDef",
    "MonetaryAmountTypeDef",
    "NetworkProfileTypeDef",
    "OfferingPromotionTypeDef",
    "OfferingStatusTypeDef",
    "OfferingTransactionTypeDef",
    "OfferingTypeDef",
    "ProblemDetailTypeDef",
    "ProblemTypeDef",
    "ProjectTypeDef",
    "RadiosTypeDef",
    "RecurringChargeTypeDef",
    "RemoteAccessSessionTypeDef",
    "ResolutionTypeDef",
    "RuleTypeDef",
    "RunTypeDef",
    "SampleTypeDef",
    "SuiteTypeDef",
    "TagTypeDef",
    "TestGridProjectTypeDef",
    "TestGridSessionActionTypeDef",
    "TestGridSessionArtifactTypeDef",
    "TestGridSessionTypeDef",
    "TestTypeDef",
    "TrialMinutesTypeDef",
    "UniqueProblemTypeDef",
    "UploadTypeDef",
    "VPCEConfigurationTypeDef",
    "CreateDevicePoolResultTypeDef",
    "CreateInstanceProfileResultTypeDef",
    "CreateNetworkProfileResultTypeDef",
    "CreateProjectResultTypeDef",
    "CreateRemoteAccessSessionConfigurationTypeDef",
    "CreateRemoteAccessSessionResultTypeDef",
    "CreateTestGridProjectResultTypeDef",
    "CreateTestGridUrlResultTypeDef",
    "CreateUploadResultTypeDef",
    "CreateVPCEConfigurationResultTypeDef",
    "DeviceSelectionConfigurationTypeDef",
    "ExecutionConfigurationTypeDef",
    "GetAccountSettingsResultTypeDef",
    "GetDeviceInstanceResultTypeDef",
    "GetDevicePoolCompatibilityResultTypeDef",
    "GetDevicePoolResultTypeDef",
    "GetDeviceResultTypeDef",
    "GetInstanceProfileResultTypeDef",
    "GetJobResultTypeDef",
    "GetNetworkProfileResultTypeDef",
    "GetOfferingStatusResultTypeDef",
    "GetProjectResultTypeDef",
    "GetRemoteAccessSessionResultTypeDef",
    "GetRunResultTypeDef",
    "GetSuiteResultTypeDef",
    "GetTestGridProjectResultTypeDef",
    "GetTestGridSessionResultTypeDef",
    "GetTestResultTypeDef",
    "GetUploadResultTypeDef",
    "GetVPCEConfigurationResultTypeDef",
    "InstallToRemoteAccessSessionResultTypeDef",
    "ListArtifactsResultTypeDef",
    "ListDeviceInstancesResultTypeDef",
    "ListDevicePoolsResultTypeDef",
    "ListDevicesResultTypeDef",
    "ListInstanceProfilesResultTypeDef",
    "ListJobsResultTypeDef",
    "ListNetworkProfilesResultTypeDef",
    "ListOfferingPromotionsResultTypeDef",
    "ListOfferingTransactionsResultTypeDef",
    "ListOfferingsResultTypeDef",
    "ListProjectsResultTypeDef",
    "ListRemoteAccessSessionsResultTypeDef",
    "ListRunsResultTypeDef",
    "ListSamplesResultTypeDef",
    "ListSuitesResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestGridProjectsResultTypeDef",
    "ListTestGridSessionActionsResultTypeDef",
    "ListTestGridSessionArtifactsResultTypeDef",
    "ListTestGridSessionsResultTypeDef",
    "ListTestsResultTypeDef",
    "ListUniqueProblemsResultTypeDef",
    "ListUploadsResultTypeDef",
    "ListVPCEConfigurationsResultTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseOfferingResultTypeDef",
    "RenewOfferingResultTypeDef",
    "ScheduleRunConfigurationTypeDef",
    "ScheduleRunResultTypeDef",
    "ScheduleRunTestTypeDef",
    "StopJobResultTypeDef",
    "StopRemoteAccessSessionResultTypeDef",
    "StopRunResultTypeDef",
    "UpdateDeviceInstanceResultTypeDef",
    "UpdateDevicePoolResultTypeDef",
    "UpdateInstanceProfileResultTypeDef",
    "UpdateNetworkProfileResultTypeDef",
    "UpdateProjectResultTypeDef",
    "UpdateTestGridProjectResultTypeDef",
    "UpdateUploadResultTypeDef",
    "UpdateVPCEConfigurationResultTypeDef",
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "awsAccountNumber": str,
        "unmeteredDevices": Dict[DevicePlatform, int],
        "unmeteredRemoteAccessDevices": Dict[DevicePlatform, int],
        "maxJobTimeoutMinutes": int,
        "trialMinutes": "TrialMinutesTypeDef",
        "maxSlots": Dict[str, int],
        "defaultJobTimeoutMinutes": int,
        "skipAppResign": bool,
    },
    total=False,
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {"arn": str, "name": str, "type": ArtifactType, "extension": str, "url": str},
    total=False,
)

CPUTypeDef = TypedDict(
    "CPUTypeDef", {"frequency": str, "architecture": str, "clock": float}, total=False
)

CountersTypeDef = TypedDict(
    "CountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

CustomerArtifactPathsTypeDef = TypedDict(
    "CustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)

DeviceFilterTypeDef = TypedDict(
    "DeviceFilterTypeDef",
    {"attribute": DeviceFilterAttribute, "operator": RuleOperator, "values": List[str]},
    total=False,
)

DeviceInstanceTypeDef = TypedDict(
    "DeviceInstanceTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": InstanceStatus,
        "udid": str,
        "instanceProfile": "InstanceProfileTypeDef",
    },
    total=False,
)

DeviceMinutesTypeDef = TypedDict(
    "DeviceMinutesTypeDef", {"total": float, "metered": float, "unmetered": float}, total=False
)

DevicePoolCompatibilityResultTypeDef = TypedDict(
    "DevicePoolCompatibilityResultTypeDef",
    {
        "device": "DeviceTypeDef",
        "compatible": bool,
        "incompatibilityMessages": List["IncompatibilityMessageTypeDef"],
    },
    total=False,
)

DevicePoolTypeDef = TypedDict(
    "DevicePoolTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": DevicePoolType,
        "rules": List["RuleTypeDef"],
        "maxDevices": int,
    },
    total=False,
)

DeviceSelectionResultTypeDef = TypedDict(
    "DeviceSelectionResultTypeDef",
    {"filters": List["DeviceFilterTypeDef"], "matchedDevicesCount": int, "maxDevices": int},
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": DeviceFormFactor,
        "platform": DevicePlatform,
        "os": str,
        "cpu": "CPUTypeDef",
        "resolution": "ResolutionTypeDef",
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List["DeviceInstanceTypeDef"],
        "availability": DeviceAvailability,
    },
    total=False,
)

IncompatibilityMessageTypeDef = TypedDict(
    "IncompatibilityMessageTypeDef", {"message": str, "type": DeviceAttribute}, total=False
)

InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TestType,
        "created": datetime,
        "status": ExecutionStatus,
        "result": ExecutionResult,
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "device": "DeviceTypeDef",
        "instanceArn": str,
        "deviceMinutes": "DeviceMinutesTypeDef",
        "videoEndpoint": str,
        "videoCapture": bool,
    },
    total=False,
)

LocationTypeDef = TypedDict("LocationTypeDef", {"latitude": float, "longitude": float})

MonetaryAmountTypeDef = TypedDict(
    "MonetaryAmountTypeDef", {"amount": float, "currencyCode": CurrencyCode}, total=False
)

NetworkProfileTypeDef = TypedDict(
    "NetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": NetworkProfileType,
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

OfferingPromotionTypeDef = TypedDict(
    "OfferingPromotionTypeDef", {"id": str, "description": str}, total=False
)

OfferingStatusTypeDef = TypedDict(
    "OfferingStatusTypeDef",
    {
        "type": OfferingTransactionType,
        "offering": "OfferingTypeDef",
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)

OfferingTransactionTypeDef = TypedDict(
    "OfferingTransactionTypeDef",
    {
        "offeringStatus": "OfferingStatusTypeDef",
        "transactionId": str,
        "offeringPromotionId": str,
        "createdOn": datetime,
        "cost": "MonetaryAmountTypeDef",
    },
    total=False,
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": OfferingType,
        "platform": DevicePlatform,
        "recurringCharges": List["RecurringChargeTypeDef"],
    },
    total=False,
)

ProblemDetailTypeDef = TypedDict("ProblemDetailTypeDef", {"arn": str, "name": str}, total=False)

ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "run": "ProblemDetailTypeDef",
        "job": "ProblemDetailTypeDef",
        "suite": "ProblemDetailTypeDef",
        "test": "ProblemDetailTypeDef",
        "device": "DeviceTypeDef",
        "result": ExecutionResult,
        "message": str,
    },
    total=False,
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {"arn": str, "name": str, "defaultJobTimeoutMinutes": int, "created": datetime},
    total=False,
)

RadiosTypeDef = TypedDict(
    "RadiosTypeDef", {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool}, total=False
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {"cost": "MonetaryAmountTypeDef", "frequency": RecurringChargeFrequency},
    total=False,
)

RemoteAccessSessionTypeDef = TypedDict(
    "RemoteAccessSessionTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": ExecutionStatus,
        "result": ExecutionResult,
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": "DeviceTypeDef",
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": BillingMethod,
        "deviceMinutes": "DeviceMinutesTypeDef",
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": InteractionMode,
        "skipAppResign": bool,
    },
    total=False,
)

ResolutionTypeDef = TypedDict("ResolutionTypeDef", {"width": int, "height": int}, total=False)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {"attribute": DeviceAttribute, "operator": RuleOperator, "value": str},
    total=False,
)

RunTypeDef = TypedDict(
    "RunTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TestType,
        "platform": DevicePlatform,
        "created": datetime,
        "status": ExecutionStatus,
        "result": ExecutionResult,
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": BillingMethod,
        "deviceMinutes": "DeviceMinutesTypeDef",
        "networkProfile": "NetworkProfileTypeDef",
        "parsingResultUrl": str,
        "resultCode": ExecutionResultCode,
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": "RadiosTypeDef",
        "location": "LocationTypeDef",
        "customerArtifactPaths": "CustomerArtifactPathsTypeDef",
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": "DeviceSelectionResultTypeDef",
    },
    total=False,
)

SampleTypeDef = TypedDict(
    "SampleTypeDef", {"arn": str, "type": SampleType, "url": str}, total=False
)

SuiteTypeDef = TypedDict(
    "SuiteTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TestType,
        "created": datetime,
        "status": ExecutionStatus,
        "result": ExecutionResult,
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "deviceMinutes": "DeviceMinutesTypeDef",
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TestGridProjectTypeDef = TypedDict(
    "TestGridProjectTypeDef",
    {"arn": str, "name": str, "description": str, "created": datetime},
    total=False,
)

TestGridSessionActionTypeDef = TypedDict(
    "TestGridSessionActionTypeDef",
    {"action": str, "started": datetime, "duration": int, "statusCode": str, "requestMethod": str},
    total=False,
)

TestGridSessionArtifactTypeDef = TypedDict(
    "TestGridSessionArtifactTypeDef",
    {"filename": str, "type": TestGridSessionArtifactType, "url": str},
    total=False,
)

TestGridSessionTypeDef = TypedDict(
    "TestGridSessionTypeDef",
    {
        "arn": str,
        "status": TestGridSessionStatus,
        "created": datetime,
        "ended": datetime,
        "billingMinutes": float,
        "seleniumProperties": str,
    },
    total=False,
)

TestTypeDef = TypedDict(
    "TestTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TestType,
        "created": datetime,
        "status": ExecutionStatus,
        "result": ExecutionResult,
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "deviceMinutes": "DeviceMinutesTypeDef",
    },
    total=False,
)

TrialMinutesTypeDef = TypedDict(
    "TrialMinutesTypeDef", {"total": float, "remaining": float}, total=False
)

UniqueProblemTypeDef = TypedDict(
    "UniqueProblemTypeDef", {"message": str, "problems": List["ProblemTypeDef"]}, total=False
)

UploadTypeDef = TypedDict(
    "UploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": UploadType,
        "status": UploadStatus,
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": UploadCategory,
    },
    total=False,
)

VPCEConfigurationTypeDef = TypedDict(
    "VPCEConfigurationTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)

CreateDevicePoolResultTypeDef = TypedDict(
    "CreateDevicePoolResultTypeDef", {"devicePool": "DevicePoolTypeDef"}, total=False
)

CreateInstanceProfileResultTypeDef = TypedDict(
    "CreateInstanceProfileResultTypeDef", {"instanceProfile": "InstanceProfileTypeDef"}, total=False
)

CreateNetworkProfileResultTypeDef = TypedDict(
    "CreateNetworkProfileResultTypeDef", {"networkProfile": "NetworkProfileTypeDef"}, total=False
)

CreateProjectResultTypeDef = TypedDict(
    "CreateProjectResultTypeDef", {"project": "ProjectTypeDef"}, total=False
)

CreateRemoteAccessSessionConfigurationTypeDef = TypedDict(
    "CreateRemoteAccessSessionConfigurationTypeDef",
    {"billingMethod": BillingMethod, "vpceConfigurationArns": List[str]},
    total=False,
)

CreateRemoteAccessSessionResultTypeDef = TypedDict(
    "CreateRemoteAccessSessionResultTypeDef",
    {"remoteAccessSession": "RemoteAccessSessionTypeDef"},
    total=False,
)

CreateTestGridProjectResultTypeDef = TypedDict(
    "CreateTestGridProjectResultTypeDef", {"testGridProject": "TestGridProjectTypeDef"}, total=False
)

CreateTestGridUrlResultTypeDef = TypedDict(
    "CreateTestGridUrlResultTypeDef", {"url": str, "expires": datetime}, total=False
)

CreateUploadResultTypeDef = TypedDict(
    "CreateUploadResultTypeDef", {"upload": "UploadTypeDef"}, total=False
)

CreateVPCEConfigurationResultTypeDef = TypedDict(
    "CreateVPCEConfigurationResultTypeDef",
    {"vpceConfiguration": "VPCEConfigurationTypeDef"},
    total=False,
)

DeviceSelectionConfigurationTypeDef = TypedDict(
    "DeviceSelectionConfigurationTypeDef",
    {"filters": List["DeviceFilterTypeDef"], "maxDevices": int},
)

ExecutionConfigurationTypeDef = TypedDict(
    "ExecutionConfigurationTypeDef",
    {
        "jobTimeoutMinutes": int,
        "accountsCleanup": bool,
        "appPackagesCleanup": bool,
        "videoCapture": bool,
        "skipAppResign": bool,
    },
    total=False,
)

GetAccountSettingsResultTypeDef = TypedDict(
    "GetAccountSettingsResultTypeDef", {"accountSettings": "AccountSettingsTypeDef"}, total=False
)

GetDeviceInstanceResultTypeDef = TypedDict(
    "GetDeviceInstanceResultTypeDef", {"deviceInstance": "DeviceInstanceTypeDef"}, total=False
)

GetDevicePoolCompatibilityResultTypeDef = TypedDict(
    "GetDevicePoolCompatibilityResultTypeDef",
    {
        "compatibleDevices": List["DevicePoolCompatibilityResultTypeDef"],
        "incompatibleDevices": List["DevicePoolCompatibilityResultTypeDef"],
    },
    total=False,
)

GetDevicePoolResultTypeDef = TypedDict(
    "GetDevicePoolResultTypeDef", {"devicePool": "DevicePoolTypeDef"}, total=False
)

GetDeviceResultTypeDef = TypedDict(
    "GetDeviceResultTypeDef", {"device": "DeviceTypeDef"}, total=False
)

GetInstanceProfileResultTypeDef = TypedDict(
    "GetInstanceProfileResultTypeDef", {"instanceProfile": "InstanceProfileTypeDef"}, total=False
)

GetJobResultTypeDef = TypedDict("GetJobResultTypeDef", {"job": "JobTypeDef"}, total=False)

GetNetworkProfileResultTypeDef = TypedDict(
    "GetNetworkProfileResultTypeDef", {"networkProfile": "NetworkProfileTypeDef"}, total=False
)

GetOfferingStatusResultTypeDef = TypedDict(
    "GetOfferingStatusResultTypeDef",
    {
        "current": Dict[str, "OfferingStatusTypeDef"],
        "nextPeriod": Dict[str, "OfferingStatusTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetProjectResultTypeDef = TypedDict(
    "GetProjectResultTypeDef", {"project": "ProjectTypeDef"}, total=False
)

GetRemoteAccessSessionResultTypeDef = TypedDict(
    "GetRemoteAccessSessionResultTypeDef",
    {"remoteAccessSession": "RemoteAccessSessionTypeDef"},
    total=False,
)

GetRunResultTypeDef = TypedDict("GetRunResultTypeDef", {"run": "RunTypeDef"}, total=False)

GetSuiteResultTypeDef = TypedDict("GetSuiteResultTypeDef", {"suite": "SuiteTypeDef"}, total=False)

GetTestGridProjectResultTypeDef = TypedDict(
    "GetTestGridProjectResultTypeDef", {"testGridProject": "TestGridProjectTypeDef"}, total=False
)

GetTestGridSessionResultTypeDef = TypedDict(
    "GetTestGridSessionResultTypeDef", {"testGridSession": "TestGridSessionTypeDef"}, total=False
)

GetTestResultTypeDef = TypedDict("GetTestResultTypeDef", {"test": "TestTypeDef"}, total=False)

GetUploadResultTypeDef = TypedDict(
    "GetUploadResultTypeDef", {"upload": "UploadTypeDef"}, total=False
)

GetVPCEConfigurationResultTypeDef = TypedDict(
    "GetVPCEConfigurationResultTypeDef",
    {"vpceConfiguration": "VPCEConfigurationTypeDef"},
    total=False,
)

InstallToRemoteAccessSessionResultTypeDef = TypedDict(
    "InstallToRemoteAccessSessionResultTypeDef", {"appUpload": "UploadTypeDef"}, total=False
)

ListArtifactsResultTypeDef = TypedDict(
    "ListArtifactsResultTypeDef",
    {"artifacts": List["ArtifactTypeDef"], "nextToken": str},
    total=False,
)

ListDeviceInstancesResultTypeDef = TypedDict(
    "ListDeviceInstancesResultTypeDef",
    {"deviceInstances": List["DeviceInstanceTypeDef"], "nextToken": str},
    total=False,
)

ListDevicePoolsResultTypeDef = TypedDict(
    "ListDevicePoolsResultTypeDef",
    {"devicePools": List["DevicePoolTypeDef"], "nextToken": str},
    total=False,
)

ListDevicesResultTypeDef = TypedDict(
    "ListDevicesResultTypeDef", {"devices": List["DeviceTypeDef"], "nextToken": str}, total=False
)

ListInstanceProfilesResultTypeDef = TypedDict(
    "ListInstanceProfilesResultTypeDef",
    {"instanceProfiles": List["InstanceProfileTypeDef"], "nextToken": str},
    total=False,
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef", {"jobs": List["JobTypeDef"], "nextToken": str}, total=False
)

ListNetworkProfilesResultTypeDef = TypedDict(
    "ListNetworkProfilesResultTypeDef",
    {"networkProfiles": List["NetworkProfileTypeDef"], "nextToken": str},
    total=False,
)

ListOfferingPromotionsResultTypeDef = TypedDict(
    "ListOfferingPromotionsResultTypeDef",
    {"offeringPromotions": List["OfferingPromotionTypeDef"], "nextToken": str},
    total=False,
)

ListOfferingTransactionsResultTypeDef = TypedDict(
    "ListOfferingTransactionsResultTypeDef",
    {"offeringTransactions": List["OfferingTransactionTypeDef"], "nextToken": str},
    total=False,
)

ListOfferingsResultTypeDef = TypedDict(
    "ListOfferingsResultTypeDef",
    {"offerings": List["OfferingTypeDef"], "nextToken": str},
    total=False,
)

ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef", {"projects": List["ProjectTypeDef"], "nextToken": str}, total=False
)

ListRemoteAccessSessionsResultTypeDef = TypedDict(
    "ListRemoteAccessSessionsResultTypeDef",
    {"remoteAccessSessions": List["RemoteAccessSessionTypeDef"], "nextToken": str},
    total=False,
)

ListRunsResultTypeDef = TypedDict(
    "ListRunsResultTypeDef", {"runs": List["RunTypeDef"], "nextToken": str}, total=False
)

ListSamplesResultTypeDef = TypedDict(
    "ListSamplesResultTypeDef", {"samples": List["SampleTypeDef"], "nextToken": str}, total=False
)

ListSuitesResultTypeDef = TypedDict(
    "ListSuitesResultTypeDef", {"suites": List["SuiteTypeDef"], "nextToken": str}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

ListTestGridProjectsResultTypeDef = TypedDict(
    "ListTestGridProjectsResultTypeDef",
    {"testGridProjects": List["TestGridProjectTypeDef"], "nextToken": str},
    total=False,
)

ListTestGridSessionActionsResultTypeDef = TypedDict(
    "ListTestGridSessionActionsResultTypeDef",
    {"actions": List["TestGridSessionActionTypeDef"], "nextToken": str},
    total=False,
)

ListTestGridSessionArtifactsResultTypeDef = TypedDict(
    "ListTestGridSessionArtifactsResultTypeDef",
    {"artifacts": List["TestGridSessionArtifactTypeDef"], "nextToken": str},
    total=False,
)

ListTestGridSessionsResultTypeDef = TypedDict(
    "ListTestGridSessionsResultTypeDef",
    {"testGridSessions": List["TestGridSessionTypeDef"], "nextToken": str},
    total=False,
)

ListTestsResultTypeDef = TypedDict(
    "ListTestsResultTypeDef", {"tests": List["TestTypeDef"], "nextToken": str}, total=False
)

ListUniqueProblemsResultTypeDef = TypedDict(
    "ListUniqueProblemsResultTypeDef",
    {"uniqueProblems": Dict[ExecutionResult, List["UniqueProblemTypeDef"]], "nextToken": str},
    total=False,
)

ListUploadsResultTypeDef = TypedDict(
    "ListUploadsResultTypeDef", {"uploads": List["UploadTypeDef"], "nextToken": str}, total=False
)

ListVPCEConfigurationsResultTypeDef = TypedDict(
    "ListVPCEConfigurationsResultTypeDef",
    {"vpceConfigurations": List["VPCEConfigurationTypeDef"], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PurchaseOfferingResultTypeDef = TypedDict(
    "PurchaseOfferingResultTypeDef",
    {"offeringTransaction": "OfferingTransactionTypeDef"},
    total=False,
)

RenewOfferingResultTypeDef = TypedDict(
    "RenewOfferingResultTypeDef", {"offeringTransaction": "OfferingTransactionTypeDef"}, total=False
)

ScheduleRunConfigurationTypeDef = TypedDict(
    "ScheduleRunConfigurationTypeDef",
    {
        "extraDataPackageArn": str,
        "networkProfileArn": str,
        "locale": str,
        "location": "LocationTypeDef",
        "vpceConfigurationArns": List[str],
        "customerArtifactPaths": "CustomerArtifactPathsTypeDef",
        "radios": "RadiosTypeDef",
        "auxiliaryApps": List[str],
        "billingMethod": BillingMethod,
    },
    total=False,
)

ScheduleRunResultTypeDef = TypedDict("ScheduleRunResultTypeDef", {"run": "RunTypeDef"}, total=False)

_RequiredScheduleRunTestTypeDef = TypedDict("_RequiredScheduleRunTestTypeDef", {"type": TestType})
_OptionalScheduleRunTestTypeDef = TypedDict(
    "_OptionalScheduleRunTestTypeDef",
    {"testPackageArn": str, "testSpecArn": str, "filter": str, "parameters": Dict[str, str]},
    total=False,
)


class ScheduleRunTestTypeDef(_RequiredScheduleRunTestTypeDef, _OptionalScheduleRunTestTypeDef):
    pass


StopJobResultTypeDef = TypedDict("StopJobResultTypeDef", {"job": "JobTypeDef"}, total=False)

StopRemoteAccessSessionResultTypeDef = TypedDict(
    "StopRemoteAccessSessionResultTypeDef",
    {"remoteAccessSession": "RemoteAccessSessionTypeDef"},
    total=False,
)

StopRunResultTypeDef = TypedDict("StopRunResultTypeDef", {"run": "RunTypeDef"}, total=False)

UpdateDeviceInstanceResultTypeDef = TypedDict(
    "UpdateDeviceInstanceResultTypeDef", {"deviceInstance": "DeviceInstanceTypeDef"}, total=False
)

UpdateDevicePoolResultTypeDef = TypedDict(
    "UpdateDevicePoolResultTypeDef", {"devicePool": "DevicePoolTypeDef"}, total=False
)

UpdateInstanceProfileResultTypeDef = TypedDict(
    "UpdateInstanceProfileResultTypeDef", {"instanceProfile": "InstanceProfileTypeDef"}, total=False
)

UpdateNetworkProfileResultTypeDef = TypedDict(
    "UpdateNetworkProfileResultTypeDef", {"networkProfile": "NetworkProfileTypeDef"}, total=False
)

UpdateProjectResultTypeDef = TypedDict(
    "UpdateProjectResultTypeDef", {"project": "ProjectTypeDef"}, total=False
)

UpdateTestGridProjectResultTypeDef = TypedDict(
    "UpdateTestGridProjectResultTypeDef", {"testGridProject": "TestGridProjectTypeDef"}, total=False
)

UpdateUploadResultTypeDef = TypedDict(
    "UpdateUploadResultTypeDef", {"upload": "UploadTypeDef"}, total=False
)

UpdateVPCEConfigurationResultTypeDef = TypedDict(
    "UpdateVPCEConfigurationResultTypeDef",
    {"vpceConfiguration": "VPCEConfigurationTypeDef"},
    total=False,
)
