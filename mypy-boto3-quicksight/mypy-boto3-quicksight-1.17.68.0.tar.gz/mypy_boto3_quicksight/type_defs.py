"""
Type annotations for quicksight service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/type_defs.html)

Usage::

    ```python
    from mypy_boto3_quicksight.type_defs import AccountCustomizationTypeDef

    data: AccountCustomizationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_quicksight.literals import (
    AnalysisErrorType,
    AssignmentStatus,
    ColumnDataType,
    DashboardBehavior,
    DashboardErrorType,
    DashboardUIState,
    DataSetImportMode,
    DataSourceErrorInfoType,
    DataSourceType,
    Edition,
    FileFormat,
    GeoSpatialDataRole,
    IdentityType,
    IngestionErrorType,
    IngestionRequestSource,
    IngestionRequestType,
    IngestionStatus,
    InputColumnDataType,
    JoinType,
    NamespaceErrorType,
    NamespaceStatus,
    ResourceStatus,
    RowLevelPermissionPolicy,
    TemplateErrorType,
    TextQualifier,
    ThemeType,
    UserRole,
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
    "AccountCustomizationTypeDef",
    "AccountSettingsTypeDef",
    "ActiveIAMPolicyAssignmentTypeDef",
    "AdHocFilteringOptionTypeDef",
    "AmazonElasticsearchParametersTypeDef",
    "AnalysisErrorTypeDef",
    "AnalysisSearchFilterTypeDef",
    "AnalysisSourceEntityTypeDef",
    "AnalysisSourceTemplateTypeDef",
    "AnalysisSummaryTypeDef",
    "AnalysisTypeDef",
    "AthenaParametersTypeDef",
    "AuroraParametersTypeDef",
    "AuroraPostgreSqlParametersTypeDef",
    "AwsIotAnalyticsParametersTypeDef",
    "BorderStyleTypeDef",
    "CalculatedColumnTypeDef",
    "CancelIngestionResponseTypeDef",
    "CastColumnTypeOperationTypeDef",
    "ColumnDescriptionTypeDef",
    "ColumnGroupColumnSchemaTypeDef",
    "ColumnGroupSchemaTypeDef",
    "ColumnGroupTypeDef",
    "ColumnLevelPermissionRuleTypeDef",
    "ColumnSchemaTypeDef",
    "ColumnTagTypeDef",
    "CreateAccountCustomizationResponseTypeDef",
    "CreateAnalysisResponseTypeDef",
    "CreateColumnsOperationTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateDataSetResponseTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateGroupMembershipResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateIAMPolicyAssignmentResponseTypeDef",
    "CreateIngestionResponseTypeDef",
    "CreateNamespaceResponseTypeDef",
    "CreateTemplateAliasResponseTypeDef",
    "CreateTemplateResponseTypeDef",
    "CreateThemeAliasResponseTypeDef",
    "CreateThemeResponseTypeDef",
    "CredentialPairTypeDef",
    "CustomSqlTypeDef",
    "DashboardErrorTypeDef",
    "DashboardPublishOptionsTypeDef",
    "DashboardSearchFilterTypeDef",
    "DashboardSourceEntityTypeDef",
    "DashboardSourceTemplateTypeDef",
    "DashboardSummaryTypeDef",
    "DashboardTypeDef",
    "DashboardVersionSummaryTypeDef",
    "DashboardVersionTypeDef",
    "DataColorPaletteTypeDef",
    "DataSetConfigurationTypeDef",
    "DataSetReferenceTypeDef",
    "DataSetSchemaTypeDef",
    "DataSetSummaryTypeDef",
    "DataSetTypeDef",
    "DataSourceCredentialsTypeDef",
    "DataSourceErrorInfoTypeDef",
    "DataSourceParametersTypeDef",
    "DataSourceTypeDef",
    "DateTimeParameterTypeDef",
    "DecimalParameterTypeDef",
    "DeleteAccountCustomizationResponseTypeDef",
    "DeleteAnalysisResponseTypeDef",
    "DeleteDashboardResponseTypeDef",
    "DeleteDataSetResponseTypeDef",
    "DeleteDataSourceResponseTypeDef",
    "DeleteGroupMembershipResponseTypeDef",
    "DeleteGroupResponseTypeDef",
    "DeleteIAMPolicyAssignmentResponseTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteTemplateAliasResponseTypeDef",
    "DeleteTemplateResponseTypeDef",
    "DeleteThemeAliasResponseTypeDef",
    "DeleteThemeResponseTypeDef",
    "DeleteUserByPrincipalIdResponseTypeDef",
    "DeleteUserResponseTypeDef",
    "DescribeAccountCustomizationResponseTypeDef",
    "DescribeAccountSettingsResponseTypeDef",
    "DescribeAnalysisPermissionsResponseTypeDef",
    "DescribeAnalysisResponseTypeDef",
    "DescribeDashboardPermissionsResponseTypeDef",
    "DescribeDashboardResponseTypeDef",
    "DescribeDataSetPermissionsResponseTypeDef",
    "DescribeDataSetResponseTypeDef",
    "DescribeDataSourcePermissionsResponseTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeIAMPolicyAssignmentResponseTypeDef",
    "DescribeIngestionResponseTypeDef",
    "DescribeNamespaceResponseTypeDef",
    "DescribeTemplateAliasResponseTypeDef",
    "DescribeTemplatePermissionsResponseTypeDef",
    "DescribeTemplateResponseTypeDef",
    "DescribeThemeAliasResponseTypeDef",
    "DescribeThemePermissionsResponseTypeDef",
    "DescribeThemeResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "ErrorInfoTypeDef",
    "ExportToCSVOptionTypeDef",
    "FieldFolderTypeDef",
    "FilterOperationTypeDef",
    "GeoSpatialColumnGroupTypeDef",
    "GetDashboardEmbedUrlResponseTypeDef",
    "GetSessionEmbedUrlResponseTypeDef",
    "GroupMemberTypeDef",
    "GroupTypeDef",
    "GutterStyleTypeDef",
    "IAMPolicyAssignmentSummaryTypeDef",
    "IAMPolicyAssignmentTypeDef",
    "IngestionTypeDef",
    "InputColumnTypeDef",
    "IntegerParameterTypeDef",
    "JiraParametersTypeDef",
    "JoinInstructionTypeDef",
    "JoinKeyPropertiesTypeDef",
    "ListAnalysesResponseTypeDef",
    "ListDashboardVersionsResponseTypeDef",
    "ListDashboardsResponseTypeDef",
    "ListDataSetsResponseTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListGroupMembershipsResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListIAMPolicyAssignmentsForUserResponseTypeDef",
    "ListIAMPolicyAssignmentsResponseTypeDef",
    "ListIngestionsResponseTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplateAliasesResponseTypeDef",
    "ListTemplateVersionsResponseTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListThemeAliasesResponseTypeDef",
    "ListThemeVersionsResponseTypeDef",
    "ListThemesResponseTypeDef",
    "ListUserGroupsResponseTypeDef",
    "ListUsersResponseTypeDef",
    "LogicalTableSourceTypeDef",
    "LogicalTableTypeDef",
    "ManifestFileLocationTypeDef",
    "MarginStyleTypeDef",
    "MariaDbParametersTypeDef",
    "MySqlParametersTypeDef",
    "NamespaceErrorTypeDef",
    "NamespaceInfoV2TypeDef",
    "OracleParametersTypeDef",
    "OutputColumnTypeDef",
    "PaginatorConfigTypeDef",
    "ParametersTypeDef",
    "PhysicalTableTypeDef",
    "PostgreSqlParametersTypeDef",
    "PrestoParametersTypeDef",
    "ProjectOperationTypeDef",
    "QueueInfoTypeDef",
    "RdsParametersTypeDef",
    "RedshiftParametersTypeDef",
    "RegisterUserResponseTypeDef",
    "RelationalTableTypeDef",
    "RenameColumnOperationTypeDef",
    "ResourcePermissionTypeDef",
    "RestoreAnalysisResponseTypeDef",
    "RowInfoTypeDef",
    "RowLevelPermissionDataSetTypeDef",
    "S3ParametersTypeDef",
    "S3SourceTypeDef",
    "SearchAnalysesResponseTypeDef",
    "SearchDashboardsResponseTypeDef",
    "ServiceNowParametersTypeDef",
    "SheetControlsOptionTypeDef",
    "SheetStyleTypeDef",
    "SheetTypeDef",
    "SnowflakeParametersTypeDef",
    "SparkParametersTypeDef",
    "SqlServerParametersTypeDef",
    "SslPropertiesTypeDef",
    "StringParameterTypeDef",
    "TagColumnOperationTypeDef",
    "TagResourceResponseTypeDef",
    "TagTypeDef",
    "TemplateAliasTypeDef",
    "TemplateErrorTypeDef",
    "TemplateSourceAnalysisTypeDef",
    "TemplateSourceEntityTypeDef",
    "TemplateSourceTemplateTypeDef",
    "TemplateSummaryTypeDef",
    "TemplateTypeDef",
    "TemplateVersionSummaryTypeDef",
    "TemplateVersionTypeDef",
    "TeradataParametersTypeDef",
    "ThemeAliasTypeDef",
    "ThemeConfigurationTypeDef",
    "ThemeErrorTypeDef",
    "ThemeSummaryTypeDef",
    "ThemeTypeDef",
    "ThemeVersionSummaryTypeDef",
    "ThemeVersionTypeDef",
    "TileLayoutStyleTypeDef",
    "TileStyleTypeDef",
    "TransformOperationTypeDef",
    "TwitterParametersTypeDef",
    "UIColorPaletteTypeDef",
    "UntagResourceResponseTypeDef",
    "UpdateAccountCustomizationResponseTypeDef",
    "UpdateAccountSettingsResponseTypeDef",
    "UpdateAnalysisPermissionsResponseTypeDef",
    "UpdateAnalysisResponseTypeDef",
    "UpdateDashboardPermissionsResponseTypeDef",
    "UpdateDashboardPublishedVersionResponseTypeDef",
    "UpdateDashboardResponseTypeDef",
    "UpdateDataSetPermissionsResponseTypeDef",
    "UpdateDataSetResponseTypeDef",
    "UpdateDataSourcePermissionsResponseTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateGroupResponseTypeDef",
    "UpdateIAMPolicyAssignmentResponseTypeDef",
    "UpdateTemplateAliasResponseTypeDef",
    "UpdateTemplatePermissionsResponseTypeDef",
    "UpdateTemplateResponseTypeDef",
    "UpdateThemeAliasResponseTypeDef",
    "UpdateThemePermissionsResponseTypeDef",
    "UpdateThemeResponseTypeDef",
    "UpdateUserResponseTypeDef",
    "UploadSettingsTypeDef",
    "UserTypeDef",
    "VpcConnectionPropertiesTypeDef",
)


class AccountCustomizationTypeDef(TypedDict, total=False):
    DefaultTheme: str


class AccountSettingsTypeDef(TypedDict, total=False):
    AccountName: str
    Edition: Edition
    DefaultNamespace: str
    NotificationEmail: str


class ActiveIAMPolicyAssignmentTypeDef(TypedDict, total=False):
    AssignmentName: str
    PolicyArn: str


class AdHocFilteringOptionTypeDef(TypedDict, total=False):
    AvailabilityStatus: DashboardBehavior


class AmazonElasticsearchParametersTypeDef(TypedDict):
    Domain: str


AnalysisErrorTypeDef = TypedDict(
    "AnalysisErrorTypeDef", {"Type": AnalysisErrorType, "Message": str}, total=False
)


class AnalysisSearchFilterTypeDef(TypedDict, total=False):
    Operator: Literal["StringEquals"]
    Name: Literal["QUICKSIGHT_USER"]
    Value: str


class AnalysisSourceEntityTypeDef(TypedDict, total=False):
    SourceTemplate: "AnalysisSourceTemplateTypeDef"


class AnalysisSourceTemplateTypeDef(TypedDict):
    DataSetReferences: List["DataSetReferenceTypeDef"]
    Arn: str


class AnalysisSummaryTypeDef(TypedDict, total=False):
    Arn: str
    AnalysisId: str
    Name: str
    Status: ResourceStatus
    CreatedTime: datetime
    LastUpdatedTime: datetime


class AnalysisTypeDef(TypedDict, total=False):
    AnalysisId: str
    Arn: str
    Name: str
    Status: ResourceStatus
    Errors: List["AnalysisErrorTypeDef"]
    DataSetArns: List[str]
    ThemeArn: str
    CreatedTime: datetime
    LastUpdatedTime: datetime
    Sheets: List["SheetTypeDef"]


class AthenaParametersTypeDef(TypedDict, total=False):
    WorkGroup: str


class AuroraParametersTypeDef(TypedDict):
    Host: str
    Port: int
    Database: str


class AuroraPostgreSqlParametersTypeDef(TypedDict):
    Host: str
    Port: int
    Database: str


class AwsIotAnalyticsParametersTypeDef(TypedDict):
    DataSetName: str


class BorderStyleTypeDef(TypedDict, total=False):
    Show: bool


class CalculatedColumnTypeDef(TypedDict):
    ColumnName: str
    ColumnId: str
    Expression: str


class CancelIngestionResponseTypeDef(TypedDict, total=False):
    Arn: str
    IngestionId: str
    RequestId: str
    Status: int


class _RequiredCastColumnTypeOperationTypeDef(TypedDict):
    ColumnName: str
    NewColumnType: ColumnDataType


class CastColumnTypeOperationTypeDef(_RequiredCastColumnTypeOperationTypeDef, total=False):
    Format: str


ColumnDescriptionTypeDef = TypedDict("ColumnDescriptionTypeDef", {"Text": str}, total=False)


class ColumnGroupColumnSchemaTypeDef(TypedDict, total=False):
    Name: str


class ColumnGroupSchemaTypeDef(TypedDict, total=False):
    Name: str
    ColumnGroupColumnSchemaList: List["ColumnGroupColumnSchemaTypeDef"]


class ColumnGroupTypeDef(TypedDict, total=False):
    GeoSpatialColumnGroup: "GeoSpatialColumnGroupTypeDef"


class ColumnLevelPermissionRuleTypeDef(TypedDict, total=False):
    Principals: List[str]
    ColumnNames: List[str]


class ColumnSchemaTypeDef(TypedDict, total=False):
    Name: str
    DataType: str
    GeographicRole: str


class ColumnTagTypeDef(TypedDict, total=False):
    ColumnGeographicRole: GeoSpatialDataRole
    ColumnDescription: "ColumnDescriptionTypeDef"


class CreateAccountCustomizationResponseTypeDef(TypedDict, total=False):
    Arn: str
    AwsAccountId: str
    Namespace: str
    AccountCustomization: "AccountCustomizationTypeDef"
    RequestId: str
    Status: int


class CreateAnalysisResponseTypeDef(TypedDict, total=False):
    Arn: str
    AnalysisId: str
    CreationStatus: ResourceStatus
    Status: int
    RequestId: str


class CreateColumnsOperationTypeDef(TypedDict):
    Columns: List["CalculatedColumnTypeDef"]


class CreateDashboardResponseTypeDef(TypedDict, total=False):
    Arn: str
    VersionArn: str
    DashboardId: str
    CreationStatus: ResourceStatus
    Status: int
    RequestId: str


class CreateDataSetResponseTypeDef(TypedDict, total=False):
    Arn: str
    DataSetId: str
    IngestionArn: str
    IngestionId: str
    RequestId: str
    Status: int


class CreateDataSourceResponseTypeDef(TypedDict, total=False):
    Arn: str
    DataSourceId: str
    CreationStatus: ResourceStatus
    RequestId: str
    Status: int


class CreateGroupMembershipResponseTypeDef(TypedDict, total=False):
    GroupMember: "GroupMemberTypeDef"
    RequestId: str
    Status: int


class CreateGroupResponseTypeDef(TypedDict, total=False):
    Group: "GroupTypeDef"
    RequestId: str
    Status: int


class CreateIAMPolicyAssignmentResponseTypeDef(TypedDict, total=False):
    AssignmentName: str
    AssignmentId: str
    AssignmentStatus: AssignmentStatus
    PolicyArn: str
    Identities: Dict[str, List[str]]
    RequestId: str
    Status: int


class CreateIngestionResponseTypeDef(TypedDict, total=False):
    Arn: str
    IngestionId: str
    IngestionStatus: IngestionStatus
    RequestId: str
    Status: int


class CreateNamespaceResponseTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    CapacityRegion: str
    CreationStatus: NamespaceStatus
    IdentityStore: Literal["QUICKSIGHT"]
    RequestId: str
    Status: int


class CreateTemplateAliasResponseTypeDef(TypedDict, total=False):
    TemplateAlias: "TemplateAliasTypeDef"
    Status: int
    RequestId: str


class CreateTemplateResponseTypeDef(TypedDict, total=False):
    Arn: str
    VersionArn: str
    TemplateId: str
    CreationStatus: ResourceStatus
    Status: int
    RequestId: str


class CreateThemeAliasResponseTypeDef(TypedDict, total=False):
    ThemeAlias: "ThemeAliasTypeDef"
    Status: int
    RequestId: str


class CreateThemeResponseTypeDef(TypedDict, total=False):
    Arn: str
    VersionArn: str
    ThemeId: str
    CreationStatus: ResourceStatus
    Status: int
    RequestId: str


class _RequiredCredentialPairTypeDef(TypedDict):
    Username: str
    Password: str


class CredentialPairTypeDef(_RequiredCredentialPairTypeDef, total=False):
    AlternateDataSourceParameters: List["DataSourceParametersTypeDef"]


class _RequiredCustomSqlTypeDef(TypedDict):
    DataSourceArn: str
    Name: str
    SqlQuery: str


class CustomSqlTypeDef(_RequiredCustomSqlTypeDef, total=False):
    Columns: List["InputColumnTypeDef"]


DashboardErrorTypeDef = TypedDict(
    "DashboardErrorTypeDef", {"Type": DashboardErrorType, "Message": str}, total=False
)


class DashboardPublishOptionsTypeDef(TypedDict, total=False):
    AdHocFilteringOption: "AdHocFilteringOptionTypeDef"
    ExportToCSVOption: "ExportToCSVOptionTypeDef"
    SheetControlsOption: "SheetControlsOptionTypeDef"


class _RequiredDashboardSearchFilterTypeDef(TypedDict):
    Operator: Literal["StringEquals"]


class DashboardSearchFilterTypeDef(_RequiredDashboardSearchFilterTypeDef, total=False):
    Name: Literal["QUICKSIGHT_USER"]
    Value: str


class DashboardSourceEntityTypeDef(TypedDict, total=False):
    SourceTemplate: "DashboardSourceTemplateTypeDef"


class DashboardSourceTemplateTypeDef(TypedDict):
    DataSetReferences: List["DataSetReferenceTypeDef"]
    Arn: str


class DashboardSummaryTypeDef(TypedDict, total=False):
    Arn: str
    DashboardId: str
    Name: str
    CreatedTime: datetime
    LastUpdatedTime: datetime
    PublishedVersionNumber: int
    LastPublishedTime: datetime


class DashboardTypeDef(TypedDict, total=False):
    DashboardId: str
    Arn: str
    Name: str
    Version: "DashboardVersionTypeDef"
    CreatedTime: datetime
    LastPublishedTime: datetime
    LastUpdatedTime: datetime


class DashboardVersionSummaryTypeDef(TypedDict, total=False):
    Arn: str
    CreatedTime: datetime
    VersionNumber: int
    Status: ResourceStatus
    SourceEntityArn: str
    Description: str


class DashboardVersionTypeDef(TypedDict, total=False):
    CreatedTime: datetime
    Errors: List["DashboardErrorTypeDef"]
    VersionNumber: int
    Status: ResourceStatus
    Arn: str
    SourceEntityArn: str
    DataSetArns: List[str]
    Description: str
    ThemeArn: str
    Sheets: List["SheetTypeDef"]


class DataColorPaletteTypeDef(TypedDict, total=False):
    Colors: List[str]
    MinMaxGradient: List[str]
    EmptyFillColor: str


class DataSetConfigurationTypeDef(TypedDict, total=False):
    Placeholder: str
    DataSetSchema: "DataSetSchemaTypeDef"
    ColumnGroupSchemaList: List["ColumnGroupSchemaTypeDef"]


class DataSetReferenceTypeDef(TypedDict):
    DataSetPlaceholder: str
    DataSetArn: str


class DataSetSchemaTypeDef(TypedDict, total=False):
    ColumnSchemaList: List["ColumnSchemaTypeDef"]


class DataSetSummaryTypeDef(TypedDict, total=False):
    Arn: str
    DataSetId: str
    Name: str
    CreatedTime: datetime
    LastUpdatedTime: datetime
    ImportMode: DataSetImportMode
    RowLevelPermissionDataSet: "RowLevelPermissionDataSetTypeDef"
    ColumnLevelPermissionRulesApplied: bool


class DataSetTypeDef(TypedDict, total=False):
    Arn: str
    DataSetId: str
    Name: str
    CreatedTime: datetime
    LastUpdatedTime: datetime
    PhysicalTableMap: Dict[str, "PhysicalTableTypeDef"]
    LogicalTableMap: Dict[str, "LogicalTableTypeDef"]
    OutputColumns: List["OutputColumnTypeDef"]
    ImportMode: DataSetImportMode
    ConsumedSpiceCapacityInBytes: int
    ColumnGroups: List["ColumnGroupTypeDef"]
    FieldFolders: Dict[str, "FieldFolderTypeDef"]
    RowLevelPermissionDataSet: "RowLevelPermissionDataSetTypeDef"
    ColumnLevelPermissionRules: List["ColumnLevelPermissionRuleTypeDef"]


class DataSourceCredentialsTypeDef(TypedDict, total=False):
    CredentialPair: "CredentialPairTypeDef"
    CopySourceArn: str


DataSourceErrorInfoTypeDef = TypedDict(
    "DataSourceErrorInfoTypeDef", {"Type": DataSourceErrorInfoType, "Message": str}, total=False
)


class DataSourceParametersTypeDef(TypedDict, total=False):
    AmazonElasticsearchParameters: "AmazonElasticsearchParametersTypeDef"
    AthenaParameters: "AthenaParametersTypeDef"
    AuroraParameters: "AuroraParametersTypeDef"
    AuroraPostgreSqlParameters: "AuroraPostgreSqlParametersTypeDef"
    AwsIotAnalyticsParameters: "AwsIotAnalyticsParametersTypeDef"
    JiraParameters: "JiraParametersTypeDef"
    MariaDbParameters: "MariaDbParametersTypeDef"
    MySqlParameters: "MySqlParametersTypeDef"
    OracleParameters: "OracleParametersTypeDef"
    PostgreSqlParameters: "PostgreSqlParametersTypeDef"
    PrestoParameters: "PrestoParametersTypeDef"
    RdsParameters: "RdsParametersTypeDef"
    RedshiftParameters: "RedshiftParametersTypeDef"
    S3Parameters: "S3ParametersTypeDef"
    ServiceNowParameters: "ServiceNowParametersTypeDef"
    SnowflakeParameters: "SnowflakeParametersTypeDef"
    SparkParameters: "SparkParametersTypeDef"
    SqlServerParameters: "SqlServerParametersTypeDef"
    TeradataParameters: "TeradataParametersTypeDef"
    TwitterParameters: "TwitterParametersTypeDef"


DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "Name": str,
        "Type": DataSourceType,
        "Status": ResourceStatus,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "DataSourceParameters": "DataSourceParametersTypeDef",
        "AlternateDataSourceParameters": List["DataSourceParametersTypeDef"],
        "VpcConnectionProperties": "VpcConnectionPropertiesTypeDef",
        "SslProperties": "SslPropertiesTypeDef",
        "ErrorInfo": "DataSourceErrorInfoTypeDef",
    },
    total=False,
)


class DateTimeParameterTypeDef(TypedDict):
    Name: str
    Values: List[datetime]


class DecimalParameterTypeDef(TypedDict):
    Name: str
    Values: List[float]


class DeleteAccountCustomizationResponseTypeDef(TypedDict, total=False):
    RequestId: str
    Status: int


class DeleteAnalysisResponseTypeDef(TypedDict, total=False):
    Status: int
    Arn: str
    AnalysisId: str
    DeletionTime: datetime
    RequestId: str


class DeleteDashboardResponseTypeDef(TypedDict, total=False):
    Status: int
    Arn: str
    DashboardId: str
    RequestId: str


class DeleteDataSetResponseTypeDef(TypedDict, total=False):
    Arn: str
    DataSetId: str
    RequestId: str
    Status: int


class DeleteDataSourceResponseTypeDef(TypedDict, total=False):
    Arn: str
    DataSourceId: str
    RequestId: str
    Status: int


class DeleteGroupMembershipResponseTypeDef(TypedDict, total=False):
    RequestId: str
    Status: int


class DeleteGroupResponseTypeDef(TypedDict, total=False):
    RequestId: str
    Status: int


class DeleteIAMPolicyAssignmentResponseTypeDef(TypedDict, total=False):
    AssignmentName: str
    RequestId: str
    Status: int


class DeleteNamespaceResponseTypeDef(TypedDict, total=False):
    RequestId: str
    Status: int


class DeleteTemplateAliasResponseTypeDef(TypedDict, total=False):
    Status: int
    TemplateId: str
    AliasName: str
    Arn: str
    RequestId: str


class DeleteTemplateResponseTypeDef(TypedDict, total=False):
    RequestId: str
    Arn: str
    TemplateId: str
    Status: int


class DeleteThemeAliasResponseTypeDef(TypedDict, total=False):
    AliasName: str
    Arn: str
    RequestId: str
    Status: int
    ThemeId: str


class DeleteThemeResponseTypeDef(TypedDict, total=False):
    Arn: str
    RequestId: str
    Status: int
    ThemeId: str


class DeleteUserByPrincipalIdResponseTypeDef(TypedDict, total=False):
    RequestId: str
    Status: int


class DeleteUserResponseTypeDef(TypedDict, total=False):
    RequestId: str
    Status: int


class DescribeAccountCustomizationResponseTypeDef(TypedDict, total=False):
    Arn: str
    AwsAccountId: str
    Namespace: str
    AccountCustomization: "AccountCustomizationTypeDef"
    RequestId: str
    Status: int


class DescribeAccountSettingsResponseTypeDef(TypedDict, total=False):
    AccountSettings: "AccountSettingsTypeDef"
    RequestId: str
    Status: int


class DescribeAnalysisPermissionsResponseTypeDef(TypedDict, total=False):
    AnalysisId: str
    AnalysisArn: str
    Permissions: List["ResourcePermissionTypeDef"]
    Status: int
    RequestId: str


class DescribeAnalysisResponseTypeDef(TypedDict, total=False):
    Analysis: "AnalysisTypeDef"
    Status: int
    RequestId: str


class DescribeDashboardPermissionsResponseTypeDef(TypedDict, total=False):
    DashboardId: str
    DashboardArn: str
    Permissions: List["ResourcePermissionTypeDef"]
    Status: int
    RequestId: str


class DescribeDashboardResponseTypeDef(TypedDict, total=False):
    Dashboard: "DashboardTypeDef"
    Status: int
    RequestId: str


class DescribeDataSetPermissionsResponseTypeDef(TypedDict, total=False):
    DataSetArn: str
    DataSetId: str
    Permissions: List["ResourcePermissionTypeDef"]
    RequestId: str
    Status: int


class DescribeDataSetResponseTypeDef(TypedDict, total=False):
    DataSet: "DataSetTypeDef"
    RequestId: str
    Status: int


class DescribeDataSourcePermissionsResponseTypeDef(TypedDict, total=False):
    DataSourceArn: str
    DataSourceId: str
    Permissions: List["ResourcePermissionTypeDef"]
    RequestId: str
    Status: int


class DescribeDataSourceResponseTypeDef(TypedDict, total=False):
    DataSource: "DataSourceTypeDef"
    RequestId: str
    Status: int


class DescribeGroupResponseTypeDef(TypedDict, total=False):
    Group: "GroupTypeDef"
    RequestId: str
    Status: int


class DescribeIAMPolicyAssignmentResponseTypeDef(TypedDict, total=False):
    IAMPolicyAssignment: "IAMPolicyAssignmentTypeDef"
    RequestId: str
    Status: int


class DescribeIngestionResponseTypeDef(TypedDict, total=False):
    Ingestion: "IngestionTypeDef"
    RequestId: str
    Status: int


class DescribeNamespaceResponseTypeDef(TypedDict, total=False):
    Namespace: "NamespaceInfoV2TypeDef"
    RequestId: str
    Status: int


class DescribeTemplateAliasResponseTypeDef(TypedDict, total=False):
    TemplateAlias: "TemplateAliasTypeDef"
    Status: int
    RequestId: str


class DescribeTemplatePermissionsResponseTypeDef(TypedDict, total=False):
    TemplateId: str
    TemplateArn: str
    Permissions: List["ResourcePermissionTypeDef"]
    RequestId: str
    Status: int


class DescribeTemplateResponseTypeDef(TypedDict, total=False):
    Template: "TemplateTypeDef"
    Status: int
    RequestId: str


class DescribeThemeAliasResponseTypeDef(TypedDict, total=False):
    ThemeAlias: "ThemeAliasTypeDef"
    Status: int
    RequestId: str


class DescribeThemePermissionsResponseTypeDef(TypedDict, total=False):
    ThemeId: str
    ThemeArn: str
    Permissions: List["ResourcePermissionTypeDef"]
    RequestId: str
    Status: int


class DescribeThemeResponseTypeDef(TypedDict, total=False):
    Theme: "ThemeTypeDef"
    Status: int
    RequestId: str


class DescribeUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"
    RequestId: str
    Status: int


ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef", {"Type": IngestionErrorType, "Message": str}, total=False
)


class ExportToCSVOptionTypeDef(TypedDict, total=False):
    AvailabilityStatus: DashboardBehavior


class FieldFolderTypeDef(TypedDict, total=False):
    description: str
    columns: List[str]


class FilterOperationTypeDef(TypedDict):
    ConditionExpression: str


class GeoSpatialColumnGroupTypeDef(TypedDict):
    Name: str
    CountryCode: Literal["US"]
    Columns: List[str]


class GetDashboardEmbedUrlResponseTypeDef(TypedDict, total=False):
    EmbedUrl: str
    Status: int
    RequestId: str


class GetSessionEmbedUrlResponseTypeDef(TypedDict, total=False):
    EmbedUrl: str
    Status: int
    RequestId: str


class GroupMemberTypeDef(TypedDict, total=False):
    Arn: str
    MemberName: str


class GroupTypeDef(TypedDict, total=False):
    Arn: str
    GroupName: str
    Description: str
    PrincipalId: str


class GutterStyleTypeDef(TypedDict, total=False):
    Show: bool


class IAMPolicyAssignmentSummaryTypeDef(TypedDict, total=False):
    AssignmentName: str
    AssignmentStatus: AssignmentStatus


class IAMPolicyAssignmentTypeDef(TypedDict, total=False):
    AwsAccountId: str
    AssignmentId: str
    AssignmentName: str
    PolicyArn: str
    Identities: Dict[str, List[str]]
    AssignmentStatus: AssignmentStatus


class _RequiredIngestionTypeDef(TypedDict):
    Arn: str
    IngestionStatus: IngestionStatus
    CreatedTime: datetime


class IngestionTypeDef(_RequiredIngestionTypeDef, total=False):
    IngestionId: str
    ErrorInfo: "ErrorInfoTypeDef"
    RowInfo: "RowInfoTypeDef"
    QueueInfo: "QueueInfoTypeDef"
    IngestionTimeInSeconds: int
    IngestionSizeInBytes: int
    RequestSource: IngestionRequestSource
    RequestType: IngestionRequestType


InputColumnTypeDef = TypedDict("InputColumnTypeDef", {"Name": str, "Type": InputColumnDataType})


class IntegerParameterTypeDef(TypedDict):
    Name: str
    Values: List[int]


class JiraParametersTypeDef(TypedDict):
    SiteBaseUrl: str


_RequiredJoinInstructionTypeDef = TypedDict(
    "_RequiredJoinInstructionTypeDef",
    {"LeftOperand": str, "RightOperand": str, "Type": JoinType, "OnClause": str},
)
_OptionalJoinInstructionTypeDef = TypedDict(
    "_OptionalJoinInstructionTypeDef",
    {
        "LeftJoinKeyProperties": "JoinKeyPropertiesTypeDef",
        "RightJoinKeyProperties": "JoinKeyPropertiesTypeDef",
    },
    total=False,
)


class JoinInstructionTypeDef(_RequiredJoinInstructionTypeDef, _OptionalJoinInstructionTypeDef):
    pass


class JoinKeyPropertiesTypeDef(TypedDict, total=False):
    UniqueKey: bool


class ListAnalysesResponseTypeDef(TypedDict, total=False):
    AnalysisSummaryList: List["AnalysisSummaryTypeDef"]
    NextToken: str
    Status: int
    RequestId: str


class ListDashboardVersionsResponseTypeDef(TypedDict, total=False):
    DashboardVersionSummaryList: List["DashboardVersionSummaryTypeDef"]
    NextToken: str
    Status: int
    RequestId: str


class ListDashboardsResponseTypeDef(TypedDict, total=False):
    DashboardSummaryList: List["DashboardSummaryTypeDef"]
    NextToken: str
    Status: int
    RequestId: str


class ListDataSetsResponseTypeDef(TypedDict, total=False):
    DataSetSummaries: List["DataSetSummaryTypeDef"]
    NextToken: str
    RequestId: str
    Status: int


class ListDataSourcesResponseTypeDef(TypedDict, total=False):
    DataSources: List["DataSourceTypeDef"]
    NextToken: str
    RequestId: str
    Status: int


class ListGroupMembershipsResponseTypeDef(TypedDict, total=False):
    GroupMemberList: List["GroupMemberTypeDef"]
    NextToken: str
    RequestId: str
    Status: int


class ListGroupsResponseTypeDef(TypedDict, total=False):
    GroupList: List["GroupTypeDef"]
    NextToken: str
    RequestId: str
    Status: int


class ListIAMPolicyAssignmentsForUserResponseTypeDef(TypedDict, total=False):
    ActiveAssignments: List["ActiveIAMPolicyAssignmentTypeDef"]
    RequestId: str
    NextToken: str
    Status: int


class ListIAMPolicyAssignmentsResponseTypeDef(TypedDict, total=False):
    IAMPolicyAssignments: List["IAMPolicyAssignmentSummaryTypeDef"]
    NextToken: str
    RequestId: str
    Status: int


class ListIngestionsResponseTypeDef(TypedDict, total=False):
    Ingestions: List["IngestionTypeDef"]
    NextToken: str
    RequestId: str
    Status: int


class ListNamespacesResponseTypeDef(TypedDict, total=False):
    Namespaces: List["NamespaceInfoV2TypeDef"]
    NextToken: str
    RequestId: str
    Status: int


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    RequestId: str
    Status: int


class ListTemplateAliasesResponseTypeDef(TypedDict, total=False):
    TemplateAliasList: List["TemplateAliasTypeDef"]
    Status: int
    RequestId: str
    NextToken: str


class ListTemplateVersionsResponseTypeDef(TypedDict, total=False):
    TemplateVersionSummaryList: List["TemplateVersionSummaryTypeDef"]
    NextToken: str
    Status: int
    RequestId: str


class ListTemplatesResponseTypeDef(TypedDict, total=False):
    TemplateSummaryList: List["TemplateSummaryTypeDef"]
    NextToken: str
    Status: int
    RequestId: str


class ListThemeAliasesResponseTypeDef(TypedDict, total=False):
    ThemeAliasList: List["ThemeAliasTypeDef"]
    Status: int
    RequestId: str
    NextToken: str


class ListThemeVersionsResponseTypeDef(TypedDict, total=False):
    ThemeVersionSummaryList: List["ThemeVersionSummaryTypeDef"]
    NextToken: str
    Status: int
    RequestId: str


class ListThemesResponseTypeDef(TypedDict, total=False):
    ThemeSummaryList: List["ThemeSummaryTypeDef"]
    NextToken: str
    Status: int
    RequestId: str


class ListUserGroupsResponseTypeDef(TypedDict, total=False):
    GroupList: List["GroupTypeDef"]
    NextToken: str
    RequestId: str
    Status: int


class ListUsersResponseTypeDef(TypedDict, total=False):
    UserList: List["UserTypeDef"]
    NextToken: str
    RequestId: str
    Status: int


class LogicalTableSourceTypeDef(TypedDict, total=False):
    JoinInstruction: "JoinInstructionTypeDef"
    PhysicalTableId: str


class _RequiredLogicalTableTypeDef(TypedDict):
    Alias: str
    Source: "LogicalTableSourceTypeDef"


class LogicalTableTypeDef(_RequiredLogicalTableTypeDef, total=False):
    DataTransforms: List["TransformOperationTypeDef"]


class ManifestFileLocationTypeDef(TypedDict):
    Bucket: str
    Key: str


class MarginStyleTypeDef(TypedDict, total=False):
    Show: bool


class MariaDbParametersTypeDef(TypedDict):
    Host: str
    Port: int
    Database: str


class MySqlParametersTypeDef(TypedDict):
    Host: str
    Port: int
    Database: str


NamespaceErrorTypeDef = TypedDict(
    "NamespaceErrorTypeDef", {"Type": NamespaceErrorType, "Message": str}, total=False
)


class NamespaceInfoV2TypeDef(TypedDict, total=False):
    Name: str
    Arn: str
    CapacityRegion: str
    CreationStatus: NamespaceStatus
    IdentityStore: Literal["QUICKSIGHT"]
    NamespaceError: "NamespaceErrorTypeDef"


class OracleParametersTypeDef(TypedDict):
    Host: str
    Port: int
    Database: str


OutputColumnTypeDef = TypedDict(
    "OutputColumnTypeDef", {"Name": str, "Description": str, "Type": ColumnDataType}, total=False
)


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParametersTypeDef(TypedDict, total=False):
    StringParameters: List["StringParameterTypeDef"]
    IntegerParameters: List["IntegerParameterTypeDef"]
    DecimalParameters: List["DecimalParameterTypeDef"]
    DateTimeParameters: List["DateTimeParameterTypeDef"]


class PhysicalTableTypeDef(TypedDict, total=False):
    RelationalTable: "RelationalTableTypeDef"
    CustomSql: "CustomSqlTypeDef"
    S3Source: "S3SourceTypeDef"


class PostgreSqlParametersTypeDef(TypedDict):
    Host: str
    Port: int
    Database: str


class PrestoParametersTypeDef(TypedDict):
    Host: str
    Port: int
    Catalog: str


class ProjectOperationTypeDef(TypedDict):
    ProjectedColumns: List[str]


class QueueInfoTypeDef(TypedDict):
    WaitingOnIngestion: str
    QueuedIngestion: str


class RdsParametersTypeDef(TypedDict):
    InstanceId: str
    Database: str


class _RequiredRedshiftParametersTypeDef(TypedDict):
    Database: str


class RedshiftParametersTypeDef(_RequiredRedshiftParametersTypeDef, total=False):
    Host: str
    Port: int
    ClusterId: str


class RegisterUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"
    UserInvitationUrl: str
    RequestId: str
    Status: int


class _RequiredRelationalTableTypeDef(TypedDict):
    DataSourceArn: str
    Name: str
    InputColumns: List["InputColumnTypeDef"]


class RelationalTableTypeDef(_RequiredRelationalTableTypeDef, total=False):
    Catalog: str
    Schema: str


class RenameColumnOperationTypeDef(TypedDict):
    ColumnName: str
    NewColumnName: str


class ResourcePermissionTypeDef(TypedDict):
    Principal: str
    Actions: List[str]


class RestoreAnalysisResponseTypeDef(TypedDict, total=False):
    Status: int
    Arn: str
    AnalysisId: str
    RequestId: str


class RowInfoTypeDef(TypedDict, total=False):
    RowsIngested: int
    RowsDropped: int


class _RequiredRowLevelPermissionDataSetTypeDef(TypedDict):
    Arn: str
    PermissionPolicy: RowLevelPermissionPolicy


class RowLevelPermissionDataSetTypeDef(_RequiredRowLevelPermissionDataSetTypeDef, total=False):
    Namespace: str


class S3ParametersTypeDef(TypedDict):
    ManifestFileLocation: "ManifestFileLocationTypeDef"


class _RequiredS3SourceTypeDef(TypedDict):
    DataSourceArn: str
    InputColumns: List["InputColumnTypeDef"]


class S3SourceTypeDef(_RequiredS3SourceTypeDef, total=False):
    UploadSettings: "UploadSettingsTypeDef"


class SearchAnalysesResponseTypeDef(TypedDict, total=False):
    AnalysisSummaryList: List["AnalysisSummaryTypeDef"]
    NextToken: str
    Status: int
    RequestId: str


class SearchDashboardsResponseTypeDef(TypedDict, total=False):
    DashboardSummaryList: List["DashboardSummaryTypeDef"]
    NextToken: str
    Status: int
    RequestId: str


class ServiceNowParametersTypeDef(TypedDict):
    SiteBaseUrl: str


class SheetControlsOptionTypeDef(TypedDict, total=False):
    VisibilityState: DashboardUIState


class SheetStyleTypeDef(TypedDict, total=False):
    Tile: "TileStyleTypeDef"
    TileLayout: "TileLayoutStyleTypeDef"


class SheetTypeDef(TypedDict, total=False):
    SheetId: str
    Name: str


class SnowflakeParametersTypeDef(TypedDict):
    Host: str
    Database: str
    Warehouse: str


class SparkParametersTypeDef(TypedDict):
    Host: str
    Port: int


class SqlServerParametersTypeDef(TypedDict):
    Host: str
    Port: int
    Database: str


class SslPropertiesTypeDef(TypedDict, total=False):
    DisableSsl: bool


class StringParameterTypeDef(TypedDict):
    Name: str
    Values: List[str]


class TagColumnOperationTypeDef(TypedDict):
    ColumnName: str
    Tags: List["ColumnTagTypeDef"]


class TagResourceResponseTypeDef(TypedDict, total=False):
    RequestId: str
    Status: int


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TemplateAliasTypeDef(TypedDict, total=False):
    AliasName: str
    Arn: str
    TemplateVersionNumber: int


TemplateErrorTypeDef = TypedDict(
    "TemplateErrorTypeDef", {"Type": TemplateErrorType, "Message": str}, total=False
)


class TemplateSourceAnalysisTypeDef(TypedDict):
    Arn: str
    DataSetReferences: List["DataSetReferenceTypeDef"]


class TemplateSourceEntityTypeDef(TypedDict, total=False):
    SourceAnalysis: "TemplateSourceAnalysisTypeDef"
    SourceTemplate: "TemplateSourceTemplateTypeDef"


class TemplateSourceTemplateTypeDef(TypedDict):
    Arn: str


class TemplateSummaryTypeDef(TypedDict, total=False):
    Arn: str
    TemplateId: str
    Name: str
    LatestVersionNumber: int
    CreatedTime: datetime
    LastUpdatedTime: datetime


class TemplateTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    Version: "TemplateVersionTypeDef"
    TemplateId: str
    LastUpdatedTime: datetime
    CreatedTime: datetime


class TemplateVersionSummaryTypeDef(TypedDict, total=False):
    Arn: str
    VersionNumber: int
    CreatedTime: datetime
    Status: ResourceStatus
    Description: str


class TemplateVersionTypeDef(TypedDict, total=False):
    CreatedTime: datetime
    Errors: List["TemplateErrorTypeDef"]
    VersionNumber: int
    Status: ResourceStatus
    DataSetConfigurations: List["DataSetConfigurationTypeDef"]
    Description: str
    SourceEntityArn: str
    ThemeArn: str
    Sheets: List["SheetTypeDef"]


class TeradataParametersTypeDef(TypedDict):
    Host: str
    Port: int
    Database: str


class ThemeAliasTypeDef(TypedDict, total=False):
    Arn: str
    AliasName: str
    ThemeVersionNumber: int


class ThemeConfigurationTypeDef(TypedDict, total=False):
    DataColorPalette: "DataColorPaletteTypeDef"
    UIColorPalette: "UIColorPaletteTypeDef"
    Sheet: "SheetStyleTypeDef"


ThemeErrorTypeDef = TypedDict(
    "ThemeErrorTypeDef", {"Type": Literal["INTERNAL_FAILURE"], "Message": str}, total=False
)


class ThemeSummaryTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    ThemeId: str
    LatestVersionNumber: int
    CreatedTime: datetime
    LastUpdatedTime: datetime


ThemeTypeDef = TypedDict(
    "ThemeTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ThemeId": str,
        "Version": "ThemeVersionTypeDef",
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Type": ThemeType,
    },
    total=False,
)


class ThemeVersionSummaryTypeDef(TypedDict, total=False):
    VersionNumber: int
    Arn: str
    Description: str
    CreatedTime: datetime
    Status: ResourceStatus


class ThemeVersionTypeDef(TypedDict, total=False):
    VersionNumber: int
    Arn: str
    Description: str
    BaseThemeId: str
    CreatedTime: datetime
    Configuration: "ThemeConfigurationTypeDef"
    Errors: List["ThemeErrorTypeDef"]
    Status: ResourceStatus


class TileLayoutStyleTypeDef(TypedDict, total=False):
    Gutter: "GutterStyleTypeDef"
    Margin: "MarginStyleTypeDef"


class TileStyleTypeDef(TypedDict, total=False):
    Border: "BorderStyleTypeDef"


class TransformOperationTypeDef(TypedDict, total=False):
    ProjectOperation: "ProjectOperationTypeDef"
    FilterOperation: "FilterOperationTypeDef"
    CreateColumnsOperation: "CreateColumnsOperationTypeDef"
    RenameColumnOperation: "RenameColumnOperationTypeDef"
    CastColumnTypeOperation: "CastColumnTypeOperationTypeDef"
    TagColumnOperation: "TagColumnOperationTypeDef"


class TwitterParametersTypeDef(TypedDict):
    Query: str
    MaxRows: int


UIColorPaletteTypeDef = TypedDict(
    "UIColorPaletteTypeDef",
    {
        "PrimaryForeground": str,
        "PrimaryBackground": str,
        "SecondaryForeground": str,
        "SecondaryBackground": str,
        "Accent": str,
        "AccentForeground": str,
        "Danger": str,
        "DangerForeground": str,
        "Warning": str,
        "WarningForeground": str,
        "Success": str,
        "SuccessForeground": str,
        "Dimension": str,
        "DimensionForeground": str,
        "Measure": str,
        "MeasureForeground": str,
    },
    total=False,
)


class UntagResourceResponseTypeDef(TypedDict, total=False):
    RequestId: str
    Status: int


class UpdateAccountCustomizationResponseTypeDef(TypedDict, total=False):
    Arn: str
    AwsAccountId: str
    Namespace: str
    AccountCustomization: "AccountCustomizationTypeDef"
    RequestId: str
    Status: int


class UpdateAccountSettingsResponseTypeDef(TypedDict, total=False):
    RequestId: str
    Status: int


class UpdateAnalysisPermissionsResponseTypeDef(TypedDict, total=False):
    AnalysisArn: str
    AnalysisId: str
    Permissions: List["ResourcePermissionTypeDef"]
    RequestId: str
    Status: int


class UpdateAnalysisResponseTypeDef(TypedDict, total=False):
    Arn: str
    AnalysisId: str
    UpdateStatus: ResourceStatus
    Status: int
    RequestId: str


class UpdateDashboardPermissionsResponseTypeDef(TypedDict, total=False):
    DashboardArn: str
    DashboardId: str
    Permissions: List["ResourcePermissionTypeDef"]
    RequestId: str
    Status: int


class UpdateDashboardPublishedVersionResponseTypeDef(TypedDict, total=False):
    DashboardId: str
    DashboardArn: str
    Status: int
    RequestId: str


class UpdateDashboardResponseTypeDef(TypedDict, total=False):
    Arn: str
    VersionArn: str
    DashboardId: str
    CreationStatus: ResourceStatus
    Status: int
    RequestId: str


class UpdateDataSetPermissionsResponseTypeDef(TypedDict, total=False):
    DataSetArn: str
    DataSetId: str
    RequestId: str
    Status: int


class UpdateDataSetResponseTypeDef(TypedDict, total=False):
    Arn: str
    DataSetId: str
    IngestionArn: str
    IngestionId: str
    RequestId: str
    Status: int


class UpdateDataSourcePermissionsResponseTypeDef(TypedDict, total=False):
    DataSourceArn: str
    DataSourceId: str
    RequestId: str
    Status: int


class UpdateDataSourceResponseTypeDef(TypedDict, total=False):
    Arn: str
    DataSourceId: str
    UpdateStatus: ResourceStatus
    RequestId: str
    Status: int


class UpdateGroupResponseTypeDef(TypedDict, total=False):
    Group: "GroupTypeDef"
    RequestId: str
    Status: int


class UpdateIAMPolicyAssignmentResponseTypeDef(TypedDict, total=False):
    AssignmentName: str
    AssignmentId: str
    PolicyArn: str
    Identities: Dict[str, List[str]]
    AssignmentStatus: AssignmentStatus
    RequestId: str
    Status: int


class UpdateTemplateAliasResponseTypeDef(TypedDict, total=False):
    TemplateAlias: "TemplateAliasTypeDef"
    Status: int
    RequestId: str


class UpdateTemplatePermissionsResponseTypeDef(TypedDict, total=False):
    TemplateId: str
    TemplateArn: str
    Permissions: List["ResourcePermissionTypeDef"]
    RequestId: str
    Status: int


class UpdateTemplateResponseTypeDef(TypedDict, total=False):
    TemplateId: str
    Arn: str
    VersionArn: str
    CreationStatus: ResourceStatus
    Status: int
    RequestId: str


class UpdateThemeAliasResponseTypeDef(TypedDict, total=False):
    ThemeAlias: "ThemeAliasTypeDef"
    Status: int
    RequestId: str


class UpdateThemePermissionsResponseTypeDef(TypedDict, total=False):
    ThemeId: str
    ThemeArn: str
    Permissions: List["ResourcePermissionTypeDef"]
    RequestId: str
    Status: int


class UpdateThemeResponseTypeDef(TypedDict, total=False):
    ThemeId: str
    Arn: str
    VersionArn: str
    CreationStatus: ResourceStatus
    Status: int
    RequestId: str


class UpdateUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"
    RequestId: str
    Status: int


class UploadSettingsTypeDef(TypedDict, total=False):
    Format: FileFormat
    StartFromRow: int
    ContainsHeader: bool
    TextQualifier: TextQualifier
    Delimiter: str


class UserTypeDef(TypedDict, total=False):
    Arn: str
    UserName: str
    Email: str
    Role: UserRole
    IdentityType: IdentityType
    Active: bool
    PrincipalId: str
    CustomPermissionsName: str


class VpcConnectionPropertiesTypeDef(TypedDict):
    VpcConnectionArn: str
