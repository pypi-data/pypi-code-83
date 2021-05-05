"""
Type annotations for backup service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_backup import BackupClient

    client: BackupClient = boto3.client("backup")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_backup.literals import (
    BackupJobState,
    BackupVaultEvent,
    CopyJobState,
    RestoreJobStatus,
)
from mypy_boto3_backup.type_defs import (
    BackupPlanInputTypeDef,
    BackupSelectionTypeDef,
    CreateBackupPlanOutputTypeDef,
    CreateBackupSelectionOutputTypeDef,
    CreateBackupVaultOutputTypeDef,
    DeleteBackupPlanOutputTypeDef,
    DescribeBackupJobOutputTypeDef,
    DescribeBackupVaultOutputTypeDef,
    DescribeCopyJobOutputTypeDef,
    DescribeGlobalSettingsOutputTypeDef,
    DescribeProtectedResourceOutputTypeDef,
    DescribeRecoveryPointOutputTypeDef,
    DescribeRegionSettingsOutputTypeDef,
    DescribeRestoreJobOutputTypeDef,
    ExportBackupPlanTemplateOutputTypeDef,
    GetBackupPlanFromJSONOutputTypeDef,
    GetBackupPlanFromTemplateOutputTypeDef,
    GetBackupPlanOutputTypeDef,
    GetBackupSelectionOutputTypeDef,
    GetBackupVaultAccessPolicyOutputTypeDef,
    GetBackupVaultNotificationsOutputTypeDef,
    GetRecoveryPointRestoreMetadataOutputTypeDef,
    GetSupportedResourceTypesOutputTypeDef,
    LifecycleTypeDef,
    ListBackupJobsOutputTypeDef,
    ListBackupPlansOutputTypeDef,
    ListBackupPlanTemplatesOutputTypeDef,
    ListBackupPlanVersionsOutputTypeDef,
    ListBackupSelectionsOutputTypeDef,
    ListBackupVaultsOutputTypeDef,
    ListCopyJobsOutputTypeDef,
    ListProtectedResourcesOutputTypeDef,
    ListRecoveryPointsByBackupVaultOutputTypeDef,
    ListRecoveryPointsByResourceOutputTypeDef,
    ListRestoreJobsOutputTypeDef,
    ListTagsOutputTypeDef,
    StartBackupJobOutputTypeDef,
    StartCopyJobOutputTypeDef,
    StartRestoreJobOutputTypeDef,
    UpdateBackupPlanOutputTypeDef,
    UpdateRecoveryPointLifecycleOutputTypeDef,
)

__all__ = ("BackupClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DependencyFailureException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidResourceStateException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MissingParameterValueException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]


class BackupClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#can-paginate)
        """

    def create_backup_plan(
        self,
        BackupPlan: BackupPlanInputTypeDef,
        BackupPlanTags: Dict[str, str] = None,
        CreatorRequestId: str = None,
    ) -> CreateBackupPlanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.create_backup_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create-backup-plan)
        """

    def create_backup_selection(
        self,
        BackupPlanId: str,
        BackupSelection: "BackupSelectionTypeDef",
        CreatorRequestId: str = None,
    ) -> CreateBackupSelectionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.create_backup_selection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create-backup-selection)
        """

    def create_backup_vault(
        self,
        BackupVaultName: str,
        BackupVaultTags: Dict[str, str] = None,
        EncryptionKeyArn: str = None,
        CreatorRequestId: str = None,
    ) -> CreateBackupVaultOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.create_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create-backup-vault)
        """

    def delete_backup_plan(self, BackupPlanId: str) -> DeleteBackupPlanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.delete_backup_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete-backup-plan)
        """

    def delete_backup_selection(self, BackupPlanId: str, SelectionId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.delete_backup_selection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete-backup-selection)
        """

    def delete_backup_vault(self, BackupVaultName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.delete_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete-backup-vault)
        """

    def delete_backup_vault_access_policy(self, BackupVaultName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.delete_backup_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete-backup-vault-access-policy)
        """

    def delete_backup_vault_notifications(self, BackupVaultName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.delete_backup_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete-backup-vault-notifications)
        """

    def delete_recovery_point(self, BackupVaultName: str, RecoveryPointArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.delete_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete-recovery-point)
        """

    def describe_backup_job(self, BackupJobId: str) -> DescribeBackupJobOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.describe_backup_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe-backup-job)
        """

    def describe_backup_vault(self, BackupVaultName: str) -> DescribeBackupVaultOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.describe_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe-backup-vault)
        """

    def describe_copy_job(self, CopyJobId: str) -> DescribeCopyJobOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.describe_copy_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe-copy-job)
        """

    def describe_global_settings(self) -> DescribeGlobalSettingsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.describe_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe-global-settings)
        """

    def describe_protected_resource(
        self, ResourceArn: str
    ) -> DescribeProtectedResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.describe_protected_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe-protected-resource)
        """

    def describe_recovery_point(
        self, BackupVaultName: str, RecoveryPointArn: str
    ) -> DescribeRecoveryPointOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.describe_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe-recovery-point)
        """

    def describe_region_settings(self) -> DescribeRegionSettingsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.describe_region_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe-region-settings)
        """

    def describe_restore_job(self, RestoreJobId: str) -> DescribeRestoreJobOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.describe_restore_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe-restore-job)
        """

    def disassociate_recovery_point(self, BackupVaultName: str, RecoveryPointArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.disassociate_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#disassociate-recovery-point)
        """

    def export_backup_plan_template(
        self, BackupPlanId: str
    ) -> ExportBackupPlanTemplateOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.export_backup_plan_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#export-backup-plan-template)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#generate-presigned-url)
        """

    def get_backup_plan(
        self, BackupPlanId: str, VersionId: str = None
    ) -> GetBackupPlanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.get_backup_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get-backup-plan)
        """

    def get_backup_plan_from_json(
        self, BackupPlanTemplateJson: str
    ) -> GetBackupPlanFromJSONOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.get_backup_plan_from_json)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get-backup-plan-from-json)
        """

    def get_backup_plan_from_template(
        self, BackupPlanTemplateId: str
    ) -> GetBackupPlanFromTemplateOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.get_backup_plan_from_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get-backup-plan-from-template)
        """

    def get_backup_selection(
        self, BackupPlanId: str, SelectionId: str
    ) -> GetBackupSelectionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.get_backup_selection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get-backup-selection)
        """

    def get_backup_vault_access_policy(
        self, BackupVaultName: str
    ) -> GetBackupVaultAccessPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.get_backup_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get-backup-vault-access-policy)
        """

    def get_backup_vault_notifications(
        self, BackupVaultName: str
    ) -> GetBackupVaultNotificationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.get_backup_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get-backup-vault-notifications)
        """

    def get_recovery_point_restore_metadata(
        self, BackupVaultName: str, RecoveryPointArn: str
    ) -> GetRecoveryPointRestoreMetadataOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.get_recovery_point_restore_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get-recovery-point-restore-metadata)
        """

    def get_supported_resource_types(self) -> GetSupportedResourceTypesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.get_supported_resource_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get-supported-resource-types)
        """

    def list_backup_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        ByResourceArn: str = None,
        ByState: BackupJobState = None,
        ByBackupVaultName: str = None,
        ByCreatedBefore: datetime = None,
        ByCreatedAfter: datetime = None,
        ByResourceType: str = None,
        ByAccountId: str = None,
    ) -> ListBackupJobsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.list_backup_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list-backup-jobs)
        """

    def list_backup_plan_templates(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupPlanTemplatesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.list_backup_plan_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list-backup-plan-templates)
        """

    def list_backup_plan_versions(
        self, BackupPlanId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupPlanVersionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.list_backup_plan_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list-backup-plan-versions)
        """

    def list_backup_plans(
        self, NextToken: str = None, MaxResults: int = None, IncludeDeleted: bool = None
    ) -> ListBackupPlansOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.list_backup_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list-backup-plans)
        """

    def list_backup_selections(
        self, BackupPlanId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupSelectionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.list_backup_selections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list-backup-selections)
        """

    def list_backup_vaults(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupVaultsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.list_backup_vaults)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list-backup-vaults)
        """

    def list_copy_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        ByResourceArn: str = None,
        ByState: CopyJobState = None,
        ByCreatedBefore: datetime = None,
        ByCreatedAfter: datetime = None,
        ByResourceType: str = None,
        ByDestinationVaultArn: str = None,
        ByAccountId: str = None,
    ) -> ListCopyJobsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.list_copy_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list-copy-jobs)
        """

    def list_protected_resources(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListProtectedResourcesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.list_protected_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list-protected-resources)
        """

    def list_recovery_points_by_backup_vault(
        self,
        BackupVaultName: str,
        NextToken: str = None,
        MaxResults: int = None,
        ByResourceArn: str = None,
        ByResourceType: str = None,
        ByBackupPlanId: str = None,
        ByCreatedBefore: datetime = None,
        ByCreatedAfter: datetime = None,
    ) -> ListRecoveryPointsByBackupVaultOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.list_recovery_points_by_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list-recovery-points-by-backup-vault)
        """

    def list_recovery_points_by_resource(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRecoveryPointsByResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.list_recovery_points_by_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list-recovery-points-by-resource)
        """

    def list_restore_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        ByAccountId: str = None,
        ByCreatedBefore: datetime = None,
        ByCreatedAfter: datetime = None,
        ByStatus: RestoreJobStatus = None,
    ) -> ListRestoreJobsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.list_restore_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list-restore-jobs)
        """

    def list_tags(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list-tags)
        """

    def put_backup_vault_access_policy(self, BackupVaultName: str, Policy: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.put_backup_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#put-backup-vault-access-policy)
        """

    def put_backup_vault_notifications(
        self, BackupVaultName: str, SNSTopicArn: str, BackupVaultEvents: List[BackupVaultEvent]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.put_backup_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#put-backup-vault-notifications)
        """

    def start_backup_job(
        self,
        BackupVaultName: str,
        ResourceArn: str,
        IamRoleArn: str,
        IdempotencyToken: str = None,
        StartWindowMinutes: int = None,
        CompleteWindowMinutes: int = None,
        Lifecycle: "LifecycleTypeDef" = None,
        RecoveryPointTags: Dict[str, str] = None,
        BackupOptions: Dict[str, str] = None,
    ) -> StartBackupJobOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.start_backup_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#start-backup-job)
        """

    def start_copy_job(
        self,
        RecoveryPointArn: str,
        SourceBackupVaultName: str,
        DestinationBackupVaultArn: str,
        IamRoleArn: str,
        IdempotencyToken: str = None,
        Lifecycle: "LifecycleTypeDef" = None,
    ) -> StartCopyJobOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.start_copy_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#start-copy-job)
        """

    def start_restore_job(
        self,
        RecoveryPointArn: str,
        Metadata: Dict[str, str],
        IamRoleArn: str,
        IdempotencyToken: str = None,
        ResourceType: str = None,
    ) -> StartRestoreJobOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.start_restore_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#start-restore-job)
        """

    def stop_backup_job(self, BackupJobId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.stop_backup_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#stop-backup-job)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeyList: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#untag-resource)
        """

    def update_backup_plan(
        self, BackupPlanId: str, BackupPlan: BackupPlanInputTypeDef
    ) -> UpdateBackupPlanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.update_backup_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update-backup-plan)
        """

    def update_global_settings(self, GlobalSettings: Dict[str, str] = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.update_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update-global-settings)
        """

    def update_recovery_point_lifecycle(
        self, BackupVaultName: str, RecoveryPointArn: str, Lifecycle: "LifecycleTypeDef" = None
    ) -> UpdateRecoveryPointLifecycleOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.update_recovery_point_lifecycle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update-recovery-point-lifecycle)
        """

    def update_region_settings(self, ResourceTypeOptInPreference: Dict[str, bool] = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/backup.html#Backup.Client.update_region_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update-region-settings)
        """
