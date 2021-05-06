"""
Type annotations for backup service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/type_defs.html)

Usage::

    ```python
    from mypy_boto3_backup.type_defs import AdvancedBackupSettingTypeDef

    data: AdvancedBackupSettingTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_backup.literals import (
    BackupJobState,
    BackupVaultEvent,
    CopyJobState,
    RecoveryPointStatus,
    RestoreJobStatus,
    StorageClass,
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
    "AdvancedBackupSettingTypeDef",
    "BackupJobTypeDef",
    "BackupPlanInputTypeDef",
    "BackupPlanTemplatesListMemberTypeDef",
    "BackupPlanTypeDef",
    "BackupPlansListMemberTypeDef",
    "BackupRuleInputTypeDef",
    "BackupRuleTypeDef",
    "BackupSelectionTypeDef",
    "BackupSelectionsListMemberTypeDef",
    "BackupVaultListMemberTypeDef",
    "CalculatedLifecycleTypeDef",
    "ConditionTypeDef",
    "CopyActionTypeDef",
    "CopyJobTypeDef",
    "CreateBackupPlanOutputTypeDef",
    "CreateBackupSelectionOutputTypeDef",
    "CreateBackupVaultOutputTypeDef",
    "DeleteBackupPlanOutputTypeDef",
    "DescribeBackupJobOutputTypeDef",
    "DescribeBackupVaultOutputTypeDef",
    "DescribeCopyJobOutputTypeDef",
    "DescribeGlobalSettingsOutputTypeDef",
    "DescribeProtectedResourceOutputTypeDef",
    "DescribeRecoveryPointOutputTypeDef",
    "DescribeRegionSettingsOutputTypeDef",
    "DescribeRestoreJobOutputTypeDef",
    "ExportBackupPlanTemplateOutputTypeDef",
    "GetBackupPlanFromJSONOutputTypeDef",
    "GetBackupPlanFromTemplateOutputTypeDef",
    "GetBackupPlanOutputTypeDef",
    "GetBackupSelectionOutputTypeDef",
    "GetBackupVaultAccessPolicyOutputTypeDef",
    "GetBackupVaultNotificationsOutputTypeDef",
    "GetRecoveryPointRestoreMetadataOutputTypeDef",
    "GetSupportedResourceTypesOutputTypeDef",
    "LifecycleTypeDef",
    "ListBackupJobsOutputTypeDef",
    "ListBackupPlanTemplatesOutputTypeDef",
    "ListBackupPlanVersionsOutputTypeDef",
    "ListBackupPlansOutputTypeDef",
    "ListBackupSelectionsOutputTypeDef",
    "ListBackupVaultsOutputTypeDef",
    "ListCopyJobsOutputTypeDef",
    "ListProtectedResourcesOutputTypeDef",
    "ListRecoveryPointsByBackupVaultOutputTypeDef",
    "ListRecoveryPointsByResourceOutputTypeDef",
    "ListRestoreJobsOutputTypeDef",
    "ListTagsOutputTypeDef",
    "ProtectedResourceTypeDef",
    "RecoveryPointByBackupVaultTypeDef",
    "RecoveryPointByResourceTypeDef",
    "RecoveryPointCreatorTypeDef",
    "ResponseMetadata",
    "RestoreJobsListMemberTypeDef",
    "StartBackupJobOutputTypeDef",
    "StartCopyJobOutputTypeDef",
    "StartRestoreJobOutputTypeDef",
    "UpdateBackupPlanOutputTypeDef",
    "UpdateRecoveryPointLifecycleOutputTypeDef",
)


class AdvancedBackupSettingTypeDef(TypedDict, total=False):
    ResourceType: str
    BackupOptions: Dict[str, str]


class BackupJobTypeDef(TypedDict, total=False):
    AccountId: str
    BackupJobId: str
    BackupVaultName: str
    BackupVaultArn: str
    RecoveryPointArn: str
    ResourceArn: str
    CreationDate: datetime
    CompletionDate: datetime
    State: BackupJobState
    StatusMessage: str
    PercentDone: str
    BackupSizeInBytes: int
    IamRoleArn: str
    CreatedBy: "RecoveryPointCreatorTypeDef"
    ExpectedCompletionDate: datetime
    StartBy: datetime
    ResourceType: str
    BytesTransferred: int
    BackupOptions: Dict[str, str]
    BackupType: str


class _RequiredBackupPlanInputTypeDef(TypedDict):
    BackupPlanName: str
    Rules: List["BackupRuleInputTypeDef"]


class BackupPlanInputTypeDef(_RequiredBackupPlanInputTypeDef, total=False):
    AdvancedBackupSettings: List["AdvancedBackupSettingTypeDef"]


class BackupPlanTemplatesListMemberTypeDef(TypedDict, total=False):
    BackupPlanTemplateId: str
    BackupPlanTemplateName: str


class _RequiredBackupPlanTypeDef(TypedDict):
    BackupPlanName: str
    Rules: List["BackupRuleTypeDef"]


class BackupPlanTypeDef(_RequiredBackupPlanTypeDef, total=False):
    AdvancedBackupSettings: List["AdvancedBackupSettingTypeDef"]


class BackupPlansListMemberTypeDef(TypedDict, total=False):
    BackupPlanArn: str
    BackupPlanId: str
    CreationDate: datetime
    DeletionDate: datetime
    VersionId: str
    BackupPlanName: str
    CreatorRequestId: str
    LastExecutionDate: datetime
    AdvancedBackupSettings: List["AdvancedBackupSettingTypeDef"]


class _RequiredBackupRuleInputTypeDef(TypedDict):
    RuleName: str
    TargetBackupVaultName: str


class BackupRuleInputTypeDef(_RequiredBackupRuleInputTypeDef, total=False):
    ScheduleExpression: str
    StartWindowMinutes: int
    CompletionWindowMinutes: int
    Lifecycle: "LifecycleTypeDef"
    RecoveryPointTags: Dict[str, str]
    CopyActions: List["CopyActionTypeDef"]
    EnableContinuousBackup: bool


class _RequiredBackupRuleTypeDef(TypedDict):
    RuleName: str
    TargetBackupVaultName: str


class BackupRuleTypeDef(_RequiredBackupRuleTypeDef, total=False):
    ScheduleExpression: str
    StartWindowMinutes: int
    CompletionWindowMinutes: int
    Lifecycle: "LifecycleTypeDef"
    RecoveryPointTags: Dict[str, str]
    RuleId: str
    CopyActions: List["CopyActionTypeDef"]
    EnableContinuousBackup: bool


class _RequiredBackupSelectionTypeDef(TypedDict):
    SelectionName: str
    IamRoleArn: str


class BackupSelectionTypeDef(_RequiredBackupSelectionTypeDef, total=False):
    Resources: List[str]
    ListOfTags: List["ConditionTypeDef"]


class BackupSelectionsListMemberTypeDef(TypedDict, total=False):
    SelectionId: str
    SelectionName: str
    BackupPlanId: str
    CreationDate: datetime
    CreatorRequestId: str
    IamRoleArn: str


class BackupVaultListMemberTypeDef(TypedDict, total=False):
    BackupVaultName: str
    BackupVaultArn: str
    CreationDate: datetime
    EncryptionKeyArn: str
    CreatorRequestId: str
    NumberOfRecoveryPoints: int


class CalculatedLifecycleTypeDef(TypedDict, total=False):
    MoveToColdStorageAt: datetime
    DeleteAt: datetime


class ConditionTypeDef(TypedDict):
    ConditionType: Literal["STRINGEQUALS"]
    ConditionKey: str
    ConditionValue: str


class _RequiredCopyActionTypeDef(TypedDict):
    DestinationBackupVaultArn: str


class CopyActionTypeDef(_RequiredCopyActionTypeDef, total=False):
    Lifecycle: "LifecycleTypeDef"


class CopyJobTypeDef(TypedDict, total=False):
    AccountId: str
    CopyJobId: str
    SourceBackupVaultArn: str
    SourceRecoveryPointArn: str
    DestinationBackupVaultArn: str
    DestinationRecoveryPointArn: str
    ResourceArn: str
    CreationDate: datetime
    CompletionDate: datetime
    State: CopyJobState
    StatusMessage: str
    BackupSizeInBytes: int
    IamRoleArn: str
    CreatedBy: "RecoveryPointCreatorTypeDef"
    ResourceType: str


class CreateBackupPlanOutputTypeDef(TypedDict):
    BackupPlanId: str
    BackupPlanArn: str
    CreationDate: datetime
    VersionId: str
    AdvancedBackupSettings: List["AdvancedBackupSettingTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class CreateBackupSelectionOutputTypeDef(TypedDict):
    SelectionId: str
    BackupPlanId: str
    CreationDate: datetime
    ResponseMetadata: "ResponseMetadata"


class CreateBackupVaultOutputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultArn: str
    CreationDate: datetime
    ResponseMetadata: "ResponseMetadata"


class DeleteBackupPlanOutputTypeDef(TypedDict):
    BackupPlanId: str
    BackupPlanArn: str
    DeletionDate: datetime
    VersionId: str
    ResponseMetadata: "ResponseMetadata"


class DescribeBackupJobOutputTypeDef(TypedDict):
    AccountId: str
    BackupJobId: str
    BackupVaultName: str
    BackupVaultArn: str
    RecoveryPointArn: str
    ResourceArn: str
    CreationDate: datetime
    CompletionDate: datetime
    State: BackupJobState
    StatusMessage: str
    PercentDone: str
    BackupSizeInBytes: int
    IamRoleArn: str
    CreatedBy: "RecoveryPointCreatorTypeDef"
    ResourceType: str
    BytesTransferred: int
    ExpectedCompletionDate: datetime
    StartBy: datetime
    BackupOptions: Dict[str, str]
    BackupType: str
    ResponseMetadata: "ResponseMetadata"


class DescribeBackupVaultOutputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultArn: str
    EncryptionKeyArn: str
    CreationDate: datetime
    CreatorRequestId: str
    NumberOfRecoveryPoints: int
    ResponseMetadata: "ResponseMetadata"


class DescribeCopyJobOutputTypeDef(TypedDict):
    CopyJob: "CopyJobTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeGlobalSettingsOutputTypeDef(TypedDict):
    GlobalSettings: Dict[str, str]
    LastUpdateTime: datetime
    ResponseMetadata: "ResponseMetadata"


class DescribeProtectedResourceOutputTypeDef(TypedDict):
    ResourceArn: str
    ResourceType: str
    LastBackupTime: datetime
    ResponseMetadata: "ResponseMetadata"


class DescribeRecoveryPointOutputTypeDef(TypedDict):
    RecoveryPointArn: str
    BackupVaultName: str
    BackupVaultArn: str
    SourceBackupVaultArn: str
    ResourceArn: str
    ResourceType: str
    CreatedBy: "RecoveryPointCreatorTypeDef"
    IamRoleArn: str
    Status: RecoveryPointStatus
    CreationDate: datetime
    CompletionDate: datetime
    BackupSizeInBytes: int
    CalculatedLifecycle: "CalculatedLifecycleTypeDef"
    Lifecycle: "LifecycleTypeDef"
    EncryptionKeyArn: str
    IsEncrypted: bool
    StorageClass: StorageClass
    LastRestoreTime: datetime
    ResponseMetadata: "ResponseMetadata"


class DescribeRegionSettingsOutputTypeDef(TypedDict):
    ResourceTypeOptInPreference: Dict[str, bool]
    ResponseMetadata: "ResponseMetadata"


class DescribeRestoreJobOutputTypeDef(TypedDict):
    AccountId: str
    RestoreJobId: str
    RecoveryPointArn: str
    CreationDate: datetime
    CompletionDate: datetime
    Status: RestoreJobStatus
    StatusMessage: str
    PercentDone: str
    BackupSizeInBytes: int
    IamRoleArn: str
    ExpectedCompletionTimeMinutes: int
    CreatedResourceArn: str
    ResourceType: str
    ResponseMetadata: "ResponseMetadata"


class ExportBackupPlanTemplateOutputTypeDef(TypedDict):
    BackupPlanTemplateJson: str
    ResponseMetadata: "ResponseMetadata"


class GetBackupPlanFromJSONOutputTypeDef(TypedDict):
    BackupPlan: "BackupPlanTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetBackupPlanFromTemplateOutputTypeDef(TypedDict):
    BackupPlanDocument: "BackupPlanTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetBackupPlanOutputTypeDef(TypedDict):
    BackupPlan: "BackupPlanTypeDef"
    BackupPlanId: str
    BackupPlanArn: str
    VersionId: str
    CreatorRequestId: str
    CreationDate: datetime
    DeletionDate: datetime
    LastExecutionDate: datetime
    AdvancedBackupSettings: List["AdvancedBackupSettingTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetBackupSelectionOutputTypeDef(TypedDict):
    BackupSelection: "BackupSelectionTypeDef"
    SelectionId: str
    BackupPlanId: str
    CreationDate: datetime
    CreatorRequestId: str
    ResponseMetadata: "ResponseMetadata"


class GetBackupVaultAccessPolicyOutputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultArn: str
    Policy: str
    ResponseMetadata: "ResponseMetadata"


class GetBackupVaultNotificationsOutputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultArn: str
    SNSTopicArn: str
    BackupVaultEvents: List[BackupVaultEvent]
    ResponseMetadata: "ResponseMetadata"


class GetRecoveryPointRestoreMetadataOutputTypeDef(TypedDict):
    BackupVaultArn: str
    RecoveryPointArn: str
    RestoreMetadata: Dict[str, str]
    ResponseMetadata: "ResponseMetadata"


class GetSupportedResourceTypesOutputTypeDef(TypedDict):
    ResourceTypes: List[str]
    ResponseMetadata: "ResponseMetadata"


class LifecycleTypeDef(TypedDict, total=False):
    MoveToColdStorageAfterDays: int
    DeleteAfterDays: int


class ListBackupJobsOutputTypeDef(TypedDict):
    BackupJobs: List["BackupJobTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListBackupPlanTemplatesOutputTypeDef(TypedDict):
    NextToken: str
    BackupPlanTemplatesList: List["BackupPlanTemplatesListMemberTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListBackupPlanVersionsOutputTypeDef(TypedDict):
    NextToken: str
    BackupPlanVersionsList: List["BackupPlansListMemberTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListBackupPlansOutputTypeDef(TypedDict):
    NextToken: str
    BackupPlansList: List["BackupPlansListMemberTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListBackupSelectionsOutputTypeDef(TypedDict):
    NextToken: str
    BackupSelectionsList: List["BackupSelectionsListMemberTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListBackupVaultsOutputTypeDef(TypedDict):
    BackupVaultList: List["BackupVaultListMemberTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListCopyJobsOutputTypeDef(TypedDict):
    CopyJobs: List["CopyJobTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListProtectedResourcesOutputTypeDef(TypedDict):
    Results: List["ProtectedResourceTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListRecoveryPointsByBackupVaultOutputTypeDef(TypedDict):
    NextToken: str
    RecoveryPoints: List["RecoveryPointByBackupVaultTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListRecoveryPointsByResourceOutputTypeDef(TypedDict):
    NextToken: str
    RecoveryPoints: List["RecoveryPointByResourceTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListRestoreJobsOutputTypeDef(TypedDict):
    RestoreJobs: List["RestoreJobsListMemberTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsOutputTypeDef(TypedDict):
    NextToken: str
    Tags: Dict[str, str]
    ResponseMetadata: "ResponseMetadata"


class ProtectedResourceTypeDef(TypedDict, total=False):
    ResourceArn: str
    ResourceType: str
    LastBackupTime: datetime


class RecoveryPointByBackupVaultTypeDef(TypedDict, total=False):
    RecoveryPointArn: str
    BackupVaultName: str
    BackupVaultArn: str
    SourceBackupVaultArn: str
    ResourceArn: str
    ResourceType: str
    CreatedBy: "RecoveryPointCreatorTypeDef"
    IamRoleArn: str
    Status: RecoveryPointStatus
    CreationDate: datetime
    CompletionDate: datetime
    BackupSizeInBytes: int
    CalculatedLifecycle: "CalculatedLifecycleTypeDef"
    Lifecycle: "LifecycleTypeDef"
    EncryptionKeyArn: str
    IsEncrypted: bool
    LastRestoreTime: datetime


class RecoveryPointByResourceTypeDef(TypedDict, total=False):
    RecoveryPointArn: str
    CreationDate: datetime
    Status: RecoveryPointStatus
    EncryptionKeyArn: str
    BackupSizeBytes: int
    BackupVaultName: str


class RecoveryPointCreatorTypeDef(TypedDict, total=False):
    BackupPlanId: str
    BackupPlanArn: str
    BackupPlanVersion: str
    BackupRuleId: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RestoreJobsListMemberTypeDef(TypedDict, total=False):
    AccountId: str
    RestoreJobId: str
    RecoveryPointArn: str
    CreationDate: datetime
    CompletionDate: datetime
    Status: RestoreJobStatus
    StatusMessage: str
    PercentDone: str
    BackupSizeInBytes: int
    IamRoleArn: str
    ExpectedCompletionTimeMinutes: int
    CreatedResourceArn: str
    ResourceType: str


class StartBackupJobOutputTypeDef(TypedDict):
    BackupJobId: str
    RecoveryPointArn: str
    CreationDate: datetime
    ResponseMetadata: "ResponseMetadata"


class StartCopyJobOutputTypeDef(TypedDict):
    CopyJobId: str
    CreationDate: datetime
    ResponseMetadata: "ResponseMetadata"


class StartRestoreJobOutputTypeDef(TypedDict):
    RestoreJobId: str
    ResponseMetadata: "ResponseMetadata"


class UpdateBackupPlanOutputTypeDef(TypedDict):
    BackupPlanId: str
    BackupPlanArn: str
    CreationDate: datetime
    VersionId: str
    AdvancedBackupSettings: List["AdvancedBackupSettingTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class UpdateRecoveryPointLifecycleOutputTypeDef(TypedDict):
    BackupVaultArn: str
    RecoveryPointArn: str
    Lifecycle: "LifecycleTypeDef"
    CalculatedLifecycle: "CalculatedLifecycleTypeDef"
    ResponseMetadata: "ResponseMetadata"
