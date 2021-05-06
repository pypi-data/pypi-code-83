"""
Type annotations for devicefarm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/type_defs.html)

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
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountSettingsTypeDef",
    "ArtifactTypeDef",
    "CPUTypeDef",
    "CountersTypeDef",
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
    "CustomerArtifactPathsTypeDef",
    "DeviceFilterTypeDef",
    "DeviceInstanceTypeDef",
    "DeviceMinutesTypeDef",
    "DevicePoolCompatibilityResultTypeDef",
    "DevicePoolTypeDef",
    "DeviceSelectionConfigurationTypeDef",
    "DeviceSelectionResultTypeDef",
    "DeviceTypeDef",
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
    "IncompatibilityMessageTypeDef",
    "InstallToRemoteAccessSessionResultTypeDef",
    "InstanceProfileTypeDef",
    "JobTypeDef",
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
    "LocationTypeDef",
    "MonetaryAmountTypeDef",
    "NetworkProfileTypeDef",
    "OfferingPromotionTypeDef",
    "OfferingStatusTypeDef",
    "OfferingTransactionTypeDef",
    "OfferingTypeDef",
    "PaginatorConfigTypeDef",
    "ProblemDetailTypeDef",
    "ProblemTypeDef",
    "ProjectTypeDef",
    "PurchaseOfferingResultTypeDef",
    "RadiosTypeDef",
    "RecurringChargeTypeDef",
    "RemoteAccessSessionTypeDef",
    "RenewOfferingResultTypeDef",
    "ResolutionTypeDef",
    "RuleTypeDef",
    "RunTypeDef",
    "SampleTypeDef",
    "ScheduleRunConfigurationTypeDef",
    "ScheduleRunResultTypeDef",
    "ScheduleRunTestTypeDef",
    "StopJobResultTypeDef",
    "StopRemoteAccessSessionResultTypeDef",
    "StopRunResultTypeDef",
    "SuiteTypeDef",
    "TagTypeDef",
    "TestGridProjectTypeDef",
    "TestGridSessionActionTypeDef",
    "TestGridSessionArtifactTypeDef",
    "TestGridSessionTypeDef",
    "TestTypeDef",
    "TrialMinutesTypeDef",
    "UniqueProblemTypeDef",
    "UpdateDeviceInstanceResultTypeDef",
    "UpdateDevicePoolResultTypeDef",
    "UpdateInstanceProfileResultTypeDef",
    "UpdateNetworkProfileResultTypeDef",
    "UpdateProjectResultTypeDef",
    "UpdateTestGridProjectResultTypeDef",
    "UpdateUploadResultTypeDef",
    "UpdateVPCEConfigurationResultTypeDef",
    "UploadTypeDef",
    "VPCEConfigurationTypeDef",
)


class AccountSettingsTypeDef(TypedDict, total=False):
    awsAccountNumber: str
    unmeteredDevices: Dict[DevicePlatform, int]
    unmeteredRemoteAccessDevices: Dict[DevicePlatform, int]
    maxJobTimeoutMinutes: int
    trialMinutes: "TrialMinutesTypeDef"
    maxSlots: Dict[str, int]
    defaultJobTimeoutMinutes: int
    skipAppResign: bool


ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {"arn": str, "name": str, "type": ArtifactType, "extension": str, "url": str},
    total=False,
)


class CPUTypeDef(TypedDict, total=False):
    frequency: str
    architecture: str
    clock: float


class CountersTypeDef(TypedDict, total=False):
    total: int
    passed: int
    failed: int
    warned: int
    errored: int
    stopped: int
    skipped: int


class CreateDevicePoolResultTypeDef(TypedDict, total=False):
    devicePool: "DevicePoolTypeDef"


class CreateInstanceProfileResultTypeDef(TypedDict, total=False):
    instanceProfile: "InstanceProfileTypeDef"


class CreateNetworkProfileResultTypeDef(TypedDict, total=False):
    networkProfile: "NetworkProfileTypeDef"


class CreateProjectResultTypeDef(TypedDict, total=False):
    project: "ProjectTypeDef"


class CreateRemoteAccessSessionConfigurationTypeDef(TypedDict, total=False):
    billingMethod: BillingMethod
    vpceConfigurationArns: List[str]


class CreateRemoteAccessSessionResultTypeDef(TypedDict, total=False):
    remoteAccessSession: "RemoteAccessSessionTypeDef"


class CreateTestGridProjectResultTypeDef(TypedDict, total=False):
    testGridProject: "TestGridProjectTypeDef"


class CreateTestGridUrlResultTypeDef(TypedDict, total=False):
    url: str
    expires: datetime


class CreateUploadResultTypeDef(TypedDict, total=False):
    upload: "UploadTypeDef"


class CreateVPCEConfigurationResultTypeDef(TypedDict, total=False):
    vpceConfiguration: "VPCEConfigurationTypeDef"


class CustomerArtifactPathsTypeDef(TypedDict, total=False):
    iosPaths: List[str]
    androidPaths: List[str]
    deviceHostPaths: List[str]


DeviceFilterTypeDef = TypedDict(
    "DeviceFilterTypeDef",
    {"attribute": DeviceFilterAttribute, "operator": RuleOperator, "values": List[str]},
    total=False,
)


class DeviceInstanceTypeDef(TypedDict, total=False):
    arn: str
    deviceArn: str
    labels: List[str]
    status: InstanceStatus
    udid: str
    instanceProfile: "InstanceProfileTypeDef"


class DeviceMinutesTypeDef(TypedDict, total=False):
    total: float
    metered: float
    unmetered: float


class DevicePoolCompatibilityResultTypeDef(TypedDict, total=False):
    device: "DeviceTypeDef"
    compatible: bool
    incompatibilityMessages: List["IncompatibilityMessageTypeDef"]


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


class DeviceSelectionConfigurationTypeDef(TypedDict):
    filters: List["DeviceFilterTypeDef"]
    maxDevices: int


class DeviceSelectionResultTypeDef(TypedDict, total=False):
    filters: List["DeviceFilterTypeDef"]
    matchedDevicesCount: int
    maxDevices: int


class DeviceTypeDef(TypedDict, total=False):
    arn: str
    name: str
    manufacturer: str
    model: str
    modelId: str
    formFactor: DeviceFormFactor
    platform: DevicePlatform
    os: str
    cpu: "CPUTypeDef"
    resolution: "ResolutionTypeDef"
    heapSize: int
    memory: int
    image: str
    carrier: str
    radio: str
    remoteAccessEnabled: bool
    remoteDebugEnabled: bool
    fleetType: str
    fleetName: str
    instances: List["DeviceInstanceTypeDef"]
    availability: DeviceAvailability


class ExecutionConfigurationTypeDef(TypedDict, total=False):
    jobTimeoutMinutes: int
    accountsCleanup: bool
    appPackagesCleanup: bool
    videoCapture: bool
    skipAppResign: bool


class GetAccountSettingsResultTypeDef(TypedDict, total=False):
    accountSettings: "AccountSettingsTypeDef"


class GetDeviceInstanceResultTypeDef(TypedDict, total=False):
    deviceInstance: "DeviceInstanceTypeDef"


class GetDevicePoolCompatibilityResultTypeDef(TypedDict, total=False):
    compatibleDevices: List["DevicePoolCompatibilityResultTypeDef"]
    incompatibleDevices: List["DevicePoolCompatibilityResultTypeDef"]


class GetDevicePoolResultTypeDef(TypedDict, total=False):
    devicePool: "DevicePoolTypeDef"


class GetDeviceResultTypeDef(TypedDict, total=False):
    device: "DeviceTypeDef"


class GetInstanceProfileResultTypeDef(TypedDict, total=False):
    instanceProfile: "InstanceProfileTypeDef"


class GetJobResultTypeDef(TypedDict, total=False):
    job: "JobTypeDef"


class GetNetworkProfileResultTypeDef(TypedDict, total=False):
    networkProfile: "NetworkProfileTypeDef"


class GetOfferingStatusResultTypeDef(TypedDict, total=False):
    current: Dict[str, "OfferingStatusTypeDef"]
    nextPeriod: Dict[str, "OfferingStatusTypeDef"]
    nextToken: str


class GetProjectResultTypeDef(TypedDict, total=False):
    project: "ProjectTypeDef"


class GetRemoteAccessSessionResultTypeDef(TypedDict, total=False):
    remoteAccessSession: "RemoteAccessSessionTypeDef"


class GetRunResultTypeDef(TypedDict, total=False):
    run: "RunTypeDef"


class GetSuiteResultTypeDef(TypedDict, total=False):
    suite: "SuiteTypeDef"


class GetTestGridProjectResultTypeDef(TypedDict, total=False):
    testGridProject: "TestGridProjectTypeDef"


class GetTestGridSessionResultTypeDef(TypedDict, total=False):
    testGridSession: "TestGridSessionTypeDef"


class GetTestResultTypeDef(TypedDict, total=False):
    test: "TestTypeDef"


class GetUploadResultTypeDef(TypedDict, total=False):
    upload: "UploadTypeDef"


class GetVPCEConfigurationResultTypeDef(TypedDict, total=False):
    vpceConfiguration: "VPCEConfigurationTypeDef"


IncompatibilityMessageTypeDef = TypedDict(
    "IncompatibilityMessageTypeDef", {"message": str, "type": DeviceAttribute}, total=False
)


class InstallToRemoteAccessSessionResultTypeDef(TypedDict, total=False):
    appUpload: "UploadTypeDef"


class InstanceProfileTypeDef(TypedDict, total=False):
    arn: str
    packageCleanup: bool
    excludeAppPackagesFromCleanup: List[str]
    rebootAfterUse: bool
    name: str
    description: str


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


class ListArtifactsResultTypeDef(TypedDict, total=False):
    artifacts: List["ArtifactTypeDef"]
    nextToken: str


class ListDeviceInstancesResultTypeDef(TypedDict, total=False):
    deviceInstances: List["DeviceInstanceTypeDef"]
    nextToken: str


class ListDevicePoolsResultTypeDef(TypedDict, total=False):
    devicePools: List["DevicePoolTypeDef"]
    nextToken: str


class ListDevicesResultTypeDef(TypedDict, total=False):
    devices: List["DeviceTypeDef"]
    nextToken: str


class ListInstanceProfilesResultTypeDef(TypedDict, total=False):
    instanceProfiles: List["InstanceProfileTypeDef"]
    nextToken: str


class ListJobsResultTypeDef(TypedDict, total=False):
    jobs: List["JobTypeDef"]
    nextToken: str


class ListNetworkProfilesResultTypeDef(TypedDict, total=False):
    networkProfiles: List["NetworkProfileTypeDef"]
    nextToken: str


class ListOfferingPromotionsResultTypeDef(TypedDict, total=False):
    offeringPromotions: List["OfferingPromotionTypeDef"]
    nextToken: str


class ListOfferingTransactionsResultTypeDef(TypedDict, total=False):
    offeringTransactions: List["OfferingTransactionTypeDef"]
    nextToken: str


class ListOfferingsResultTypeDef(TypedDict, total=False):
    offerings: List["OfferingTypeDef"]
    nextToken: str


class ListProjectsResultTypeDef(TypedDict, total=False):
    projects: List["ProjectTypeDef"]
    nextToken: str


class ListRemoteAccessSessionsResultTypeDef(TypedDict, total=False):
    remoteAccessSessions: List["RemoteAccessSessionTypeDef"]
    nextToken: str


class ListRunsResultTypeDef(TypedDict, total=False):
    runs: List["RunTypeDef"]
    nextToken: str


class ListSamplesResultTypeDef(TypedDict, total=False):
    samples: List["SampleTypeDef"]
    nextToken: str


class ListSuitesResultTypeDef(TypedDict, total=False):
    suites: List["SuiteTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class ListTestGridProjectsResultTypeDef(TypedDict, total=False):
    testGridProjects: List["TestGridProjectTypeDef"]
    nextToken: str


class ListTestGridSessionActionsResultTypeDef(TypedDict, total=False):
    actions: List["TestGridSessionActionTypeDef"]
    nextToken: str


class ListTestGridSessionArtifactsResultTypeDef(TypedDict, total=False):
    artifacts: List["TestGridSessionArtifactTypeDef"]
    nextToken: str


class ListTestGridSessionsResultTypeDef(TypedDict, total=False):
    testGridSessions: List["TestGridSessionTypeDef"]
    nextToken: str


class ListTestsResultTypeDef(TypedDict, total=False):
    tests: List["TestTypeDef"]
    nextToken: str


class ListUniqueProblemsResultTypeDef(TypedDict, total=False):
    uniqueProblems: Dict[ExecutionResult, List["UniqueProblemTypeDef"]]
    nextToken: str


class ListUploadsResultTypeDef(TypedDict, total=False):
    uploads: List["UploadTypeDef"]
    nextToken: str


class ListVPCEConfigurationsResultTypeDef(TypedDict, total=False):
    vpceConfigurations: List["VPCEConfigurationTypeDef"]
    nextToken: str


class LocationTypeDef(TypedDict):
    latitude: float
    longitude: float


class MonetaryAmountTypeDef(TypedDict, total=False):
    amount: float
    currencyCode: Literal["USD"]


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


class OfferingTransactionTypeDef(TypedDict, total=False):
    offeringStatus: "OfferingStatusTypeDef"
    transactionId: str
    offeringPromotionId: str
    createdOn: datetime
    cost: "MonetaryAmountTypeDef"


OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": Literal["RECURRING"],
        "platform": DevicePlatform,
        "recurringCharges": List["RecurringChargeTypeDef"],
    },
    total=False,
)


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ProblemDetailTypeDef(TypedDict, total=False):
    arn: str
    name: str


class ProblemTypeDef(TypedDict, total=False):
    run: "ProblemDetailTypeDef"
    job: "ProblemDetailTypeDef"
    suite: "ProblemDetailTypeDef"
    test: "ProblemDetailTypeDef"
    device: "DeviceTypeDef"
    result: ExecutionResult
    message: str


class ProjectTypeDef(TypedDict, total=False):
    arn: str
    name: str
    defaultJobTimeoutMinutes: int
    created: datetime


class PurchaseOfferingResultTypeDef(TypedDict, total=False):
    offeringTransaction: "OfferingTransactionTypeDef"


class RadiosTypeDef(TypedDict, total=False):
    wifi: bool
    bluetooth: bool
    nfc: bool
    gps: bool


class RecurringChargeTypeDef(TypedDict, total=False):
    cost: "MonetaryAmountTypeDef"
    frequency: Literal["MONTHLY"]


class RemoteAccessSessionTypeDef(TypedDict, total=False):
    arn: str
    name: str
    created: datetime
    status: ExecutionStatus
    result: ExecutionResult
    message: str
    started: datetime
    stopped: datetime
    device: "DeviceTypeDef"
    instanceArn: str
    remoteDebugEnabled: bool
    remoteRecordEnabled: bool
    remoteRecordAppArn: str
    hostAddress: str
    clientId: str
    billingMethod: BillingMethod
    deviceMinutes: "DeviceMinutesTypeDef"
    endpoint: str
    deviceUdid: str
    interactionMode: InteractionMode
    skipAppResign: bool


class RenewOfferingResultTypeDef(TypedDict, total=False):
    offeringTransaction: "OfferingTransactionTypeDef"


class ResolutionTypeDef(TypedDict, total=False):
    width: int
    height: int


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


class ScheduleRunConfigurationTypeDef(TypedDict, total=False):
    extraDataPackageArn: str
    networkProfileArn: str
    locale: str
    location: "LocationTypeDef"
    vpceConfigurationArns: List[str]
    customerArtifactPaths: "CustomerArtifactPathsTypeDef"
    radios: "RadiosTypeDef"
    auxiliaryApps: List[str]
    billingMethod: BillingMethod


class ScheduleRunResultTypeDef(TypedDict, total=False):
    run: "RunTypeDef"


_RequiredScheduleRunTestTypeDef = TypedDict("_RequiredScheduleRunTestTypeDef", {"type": TestType})
_OptionalScheduleRunTestTypeDef = TypedDict(
    "_OptionalScheduleRunTestTypeDef",
    {"testPackageArn": str, "testSpecArn": str, "filter": str, "parameters": Dict[str, str]},
    total=False,
)


class ScheduleRunTestTypeDef(_RequiredScheduleRunTestTypeDef, _OptionalScheduleRunTestTypeDef):
    pass


class StopJobResultTypeDef(TypedDict, total=False):
    job: "JobTypeDef"


class StopRemoteAccessSessionResultTypeDef(TypedDict, total=False):
    remoteAccessSession: "RemoteAccessSessionTypeDef"


class StopRunResultTypeDef(TypedDict, total=False):
    run: "RunTypeDef"


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


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TestGridProjectTypeDef(TypedDict, total=False):
    arn: str
    name: str
    description: str
    created: datetime


class TestGridSessionActionTypeDef(TypedDict, total=False):
    action: str
    started: datetime
    duration: int
    statusCode: str
    requestMethod: str


TestGridSessionArtifactTypeDef = TypedDict(
    "TestGridSessionArtifactTypeDef",
    {"filename": str, "type": TestGridSessionArtifactType, "url": str},
    total=False,
)


class TestGridSessionTypeDef(TypedDict, total=False):
    arn: str
    status: TestGridSessionStatus
    created: datetime
    ended: datetime
    billingMinutes: float
    seleniumProperties: str


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


class TrialMinutesTypeDef(TypedDict, total=False):
    total: float
    remaining: float


class UniqueProblemTypeDef(TypedDict, total=False):
    message: str
    problems: List["ProblemTypeDef"]


class UpdateDeviceInstanceResultTypeDef(TypedDict, total=False):
    deviceInstance: "DeviceInstanceTypeDef"


class UpdateDevicePoolResultTypeDef(TypedDict, total=False):
    devicePool: "DevicePoolTypeDef"


class UpdateInstanceProfileResultTypeDef(TypedDict, total=False):
    instanceProfile: "InstanceProfileTypeDef"


class UpdateNetworkProfileResultTypeDef(TypedDict, total=False):
    networkProfile: "NetworkProfileTypeDef"


class UpdateProjectResultTypeDef(TypedDict, total=False):
    project: "ProjectTypeDef"


class UpdateTestGridProjectResultTypeDef(TypedDict, total=False):
    testGridProject: "TestGridProjectTypeDef"


class UpdateUploadResultTypeDef(TypedDict, total=False):
    upload: "UploadTypeDef"


class UpdateVPCEConfigurationResultTypeDef(TypedDict, total=False):
    vpceConfiguration: "VPCEConfigurationTypeDef"


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


class VPCEConfigurationTypeDef(TypedDict, total=False):
    arn: str
    vpceConfigurationName: str
    vpceServiceName: str
    serviceDnsName: str
    vpceConfigurationDescription: str
