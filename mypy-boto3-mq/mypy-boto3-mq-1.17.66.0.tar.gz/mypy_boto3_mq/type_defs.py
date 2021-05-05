"""
Type annotations for mq service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mq.type_defs import AvailabilityZoneTypeDef

    data: AvailabilityZoneTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_mq.literals import (
    AuthenticationStrategy,
    BrokerState,
    BrokerStorageType,
    ChangeType,
    DayOfWeek,
    DeploymentMode,
    EngineType,
    SanitizationWarningReason,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AvailabilityZoneTypeDef",
    "BrokerEngineTypeTypeDef",
    "BrokerInstanceOptionTypeDef",
    "BrokerInstanceTypeDef",
    "BrokerSummaryTypeDef",
    "ConfigurationIdTypeDef",
    "ConfigurationRevisionTypeDef",
    "ConfigurationTypeDef",
    "ConfigurationsTypeDef",
    "CreateBrokerResponseTypeDef",
    "CreateConfigurationResponseTypeDef",
    "DeleteBrokerResponseTypeDef",
    "DescribeBrokerEngineTypesResponseTypeDef",
    "DescribeBrokerInstanceOptionsResponseTypeDef",
    "DescribeBrokerResponseTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "EncryptionOptionsTypeDef",
    "EngineVersionTypeDef",
    "LdapServerMetadataInputTypeDef",
    "LdapServerMetadataOutputTypeDef",
    "ListBrokersResponseTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListTagsResponseTypeDef",
    "ListUsersResponseTypeDef",
    "LogsSummaryTypeDef",
    "LogsTypeDef",
    "PaginatorConfigTypeDef",
    "PendingLogsTypeDef",
    "ResponseMetadata",
    "SanitizationWarningTypeDef",
    "UpdateBrokerResponseTypeDef",
    "UpdateConfigurationResponseTypeDef",
    "UserPendingChangesTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "WeeklyStartTimeTypeDef",
)


class AvailabilityZoneTypeDef(TypedDict, total=False):
    Name: str


class BrokerEngineTypeTypeDef(TypedDict, total=False):
    EngineType: EngineType
    EngineVersions: List["EngineVersionTypeDef"]


class BrokerInstanceOptionTypeDef(TypedDict, total=False):
    AvailabilityZones: List["AvailabilityZoneTypeDef"]
    EngineType: EngineType
    HostInstanceType: str
    StorageType: BrokerStorageType
    SupportedDeploymentModes: List[DeploymentMode]
    SupportedEngineVersions: List[str]


class BrokerInstanceTypeDef(TypedDict, total=False):
    ConsoleURL: str
    Endpoints: List[str]
    IpAddress: str


class BrokerSummaryTypeDef(TypedDict, total=False):
    BrokerArn: str
    BrokerId: str
    BrokerName: str
    BrokerState: BrokerState
    Created: datetime
    DeploymentMode: DeploymentMode
    EngineType: EngineType
    HostInstanceType: str


class ConfigurationIdTypeDef(TypedDict, total=False):
    Id: str
    Revision: int


class ConfigurationRevisionTypeDef(TypedDict, total=False):
    Created: datetime
    Description: str
    Revision: int


class ConfigurationTypeDef(TypedDict, total=False):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategy
    Created: datetime
    Description: str
    EngineType: EngineType
    EngineVersion: str
    Id: str
    LatestRevision: "ConfigurationRevisionTypeDef"
    Name: str
    Tags: Dict[str, str]


class ConfigurationsTypeDef(TypedDict, total=False):
    Current: "ConfigurationIdTypeDef"
    History: List["ConfigurationIdTypeDef"]
    Pending: "ConfigurationIdTypeDef"


class CreateBrokerResponseTypeDef(TypedDict, total=False):
    BrokerArn: str
    BrokerId: str


class CreateConfigurationResponseTypeDef(TypedDict, total=False):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategy
    Created: datetime
    Id: str
    LatestRevision: "ConfigurationRevisionTypeDef"
    Name: str


class DeleteBrokerResponseTypeDef(TypedDict, total=False):
    BrokerId: str


class DescribeBrokerEngineTypesResponseTypeDef(TypedDict, total=False):
    BrokerEngineTypes: List["BrokerEngineTypeTypeDef"]
    MaxResults: int
    NextToken: str


class DescribeBrokerInstanceOptionsResponseTypeDef(TypedDict, total=False):
    BrokerInstanceOptions: List["BrokerInstanceOptionTypeDef"]
    MaxResults: int
    NextToken: str


class DescribeBrokerResponseTypeDef(TypedDict, total=False):
    AuthenticationStrategy: AuthenticationStrategy
    AutoMinorVersionUpgrade: bool
    BrokerArn: str
    BrokerId: str
    BrokerInstances: List["BrokerInstanceTypeDef"]
    BrokerName: str
    BrokerState: BrokerState
    Configurations: "ConfigurationsTypeDef"
    Created: datetime
    DeploymentMode: DeploymentMode
    EncryptionOptions: "EncryptionOptionsTypeDef"
    EngineType: EngineType
    EngineVersion: str
    HostInstanceType: str
    LdapServerMetadata: "LdapServerMetadataOutputTypeDef"
    Logs: "LogsSummaryTypeDef"
    MaintenanceWindowStartTime: "WeeklyStartTimeTypeDef"
    PendingAuthenticationStrategy: AuthenticationStrategy
    PendingEngineVersion: str
    PendingHostInstanceType: str
    PendingLdapServerMetadata: "LdapServerMetadataOutputTypeDef"
    PendingSecurityGroups: List[str]
    PubliclyAccessible: bool
    SecurityGroups: List[str]
    StorageType: BrokerStorageType
    SubnetIds: List[str]
    Tags: Dict[str, str]
    Users: List["UserSummaryTypeDef"]


class DescribeConfigurationResponseTypeDef(TypedDict, total=False):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategy
    Created: datetime
    Description: str
    EngineType: EngineType
    EngineVersion: str
    Id: str
    LatestRevision: "ConfigurationRevisionTypeDef"
    Name: str
    Tags: Dict[str, str]


class DescribeConfigurationRevisionResponseTypeDef(TypedDict, total=False):
    ConfigurationId: str
    Created: datetime
    Data: str
    Description: str


class DescribeUserResponseTypeDef(TypedDict, total=False):
    BrokerId: str
    ConsoleAccess: bool
    Groups: List[str]
    Pending: "UserPendingChangesTypeDef"
    Username: str


class _RequiredEncryptionOptionsTypeDef(TypedDict):
    UseAwsOwnedKey: bool


class EncryptionOptionsTypeDef(_RequiredEncryptionOptionsTypeDef, total=False):
    KmsKeyId: str


class EngineVersionTypeDef(TypedDict, total=False):
    Name: str


class LdapServerMetadataInputTypeDef(TypedDict, total=False):
    Hosts: List[str]
    RoleBase: str
    RoleName: str
    RoleSearchMatching: str
    RoleSearchSubtree: bool
    ServiceAccountPassword: str
    ServiceAccountUsername: str
    UserBase: str
    UserRoleName: str
    UserSearchMatching: str
    UserSearchSubtree: bool


class LdapServerMetadataOutputTypeDef(TypedDict):
    Hosts: List[str]
    RoleBase: str
    RoleName: str
    RoleSearchMatching: str
    RoleSearchSubtree: bool
    ServiceAccountUsername: str
    UserBase: str
    UserRoleName: str
    UserSearchMatching: str
    UserSearchSubtree: bool
    ResponseMetadata: "ResponseMetadata"


class ListBrokersResponseTypeDef(TypedDict, total=False):
    BrokerSummaries: List["BrokerSummaryTypeDef"]
    NextToken: str


class ListConfigurationRevisionsResponseTypeDef(TypedDict, total=False):
    ConfigurationId: str
    MaxResults: int
    NextToken: str
    Revisions: List["ConfigurationRevisionTypeDef"]


class ListConfigurationsResponseTypeDef(TypedDict, total=False):
    Configurations: List["ConfigurationTypeDef"]
    MaxResults: int
    NextToken: str


class ListTagsResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class ListUsersResponseTypeDef(TypedDict, total=False):
    BrokerId: str
    MaxResults: int
    NextToken: str
    Users: List["UserSummaryTypeDef"]


class LogsSummaryTypeDef(TypedDict, total=False):
    Audit: bool
    AuditLogGroup: str
    General: bool
    GeneralLogGroup: str
    Pending: "PendingLogsTypeDef"


class LogsTypeDef(TypedDict, total=False):
    Audit: bool
    General: bool


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PendingLogsTypeDef(TypedDict, total=False):
    Audit: bool
    General: bool


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class SanitizationWarningTypeDef(TypedDict, total=False):
    AttributeName: str
    ElementName: str
    Reason: SanitizationWarningReason


class UpdateBrokerResponseTypeDef(TypedDict, total=False):
    AuthenticationStrategy: AuthenticationStrategy
    AutoMinorVersionUpgrade: bool
    BrokerId: str
    Configuration: "ConfigurationIdTypeDef"
    EngineVersion: str
    HostInstanceType: str
    LdapServerMetadata: "LdapServerMetadataOutputTypeDef"
    Logs: "LogsTypeDef"
    SecurityGroups: List[str]


class UpdateConfigurationResponseTypeDef(TypedDict, total=False):
    Arn: str
    Created: datetime
    Id: str
    LatestRevision: "ConfigurationRevisionTypeDef"
    Name: str
    Warnings: List["SanitizationWarningTypeDef"]


class UserPendingChangesTypeDef(TypedDict, total=False):
    ConsoleAccess: bool
    Groups: List[str]
    PendingChange: ChangeType


class UserSummaryTypeDef(TypedDict, total=False):
    PendingChange: ChangeType
    Username: str


class UserTypeDef(TypedDict, total=False):
    ConsoleAccess: bool
    Groups: List[str]
    Password: str
    Username: str


class WeeklyStartTimeTypeDef(TypedDict, total=False):
    DayOfWeek: DayOfWeek
    TimeOfDay: str
    TimeZone: str
