"""
Type annotations for kendra service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kendra.type_defs import AccessControlListConfigurationTypeDef

    data: AccessControlListConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_kendra.literals import (
    ConfluenceAttachmentFieldName,
    ConfluenceBlogFieldName,
    ConfluencePageFieldName,
    ConfluenceSpaceFieldName,
    ConfluenceVersion,
    ContentType,
    DatabaseEngineType,
    DataSourceStatus,
    DataSourceSyncJobStatus,
    DataSourceType,
    DocumentAttributeValueType,
    ErrorCode,
    FaqFileFormat,
    FaqStatus,
    HighlightType,
    IndexEdition,
    IndexStatus,
    KeyLocation,
    Order,
    PrincipalType,
    QueryIdentifiersEnclosingOption,
    QueryResultType,
    ReadAccessType,
    RelevanceType,
    SalesforceChatterFeedIncludeFilterType,
    SalesforceKnowledgeArticleState,
    SalesforceStandardObjectName,
    ScoreConfidence,
    ServiceNowAuthenticationType,
    ServiceNowBuildVersionType,
    SortOrder,
    ThesaurusStatus,
    UserContextPolicy,
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
    "AccessControlListConfigurationTypeDef",
    "AclConfigurationTypeDef",
    "AdditionalResultAttributeTypeDef",
    "AdditionalResultAttributeValueTypeDef",
    "AttributeFilterTypeDef",
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    "BatchDeleteDocumentResponseTypeDef",
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    "BatchPutDocumentResponseTypeDef",
    "CapacityUnitsConfigurationTypeDef",
    "ClickFeedbackTypeDef",
    "ColumnConfigurationTypeDef",
    "ConfluenceAttachmentConfigurationTypeDef",
    "ConfluenceAttachmentToIndexFieldMappingTypeDef",
    "ConfluenceBlogConfigurationTypeDef",
    "ConfluenceBlogToIndexFieldMappingTypeDef",
    "ConfluenceConfigurationTypeDef",
    "ConfluencePageConfigurationTypeDef",
    "ConfluencePageToIndexFieldMappingTypeDef",
    "ConfluenceSpaceConfigurationTypeDef",
    "ConfluenceSpaceToIndexFieldMappingTypeDef",
    "ConnectionConfigurationTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateFaqResponseTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateThesaurusResponseTypeDef",
    "DataSourceConfigurationTypeDef",
    "DataSourceSummaryTypeDef",
    "DataSourceSyncJobMetricTargetTypeDef",
    "DataSourceSyncJobMetricsTypeDef",
    "DataSourceSyncJobTypeDef",
    "DataSourceToIndexFieldMappingTypeDef",
    "DataSourceVpcConfigurationTypeDef",
    "DatabaseConfigurationTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "DescribeFaqResponseTypeDef",
    "DescribeIndexResponseTypeDef",
    "DescribeThesaurusResponseTypeDef",
    "DocumentAttributeTypeDef",
    "DocumentAttributeValueCountPairTypeDef",
    "DocumentAttributeValueTypeDef",
    "DocumentMetadataConfigurationTypeDef",
    "DocumentRelevanceConfigurationTypeDef",
    "DocumentTypeDef",
    "DocumentsMetadataConfigurationTypeDef",
    "FacetResultTypeDef",
    "FacetTypeDef",
    "FaqStatisticsTypeDef",
    "FaqSummaryTypeDef",
    "GoogleDriveConfigurationTypeDef",
    "HighlightTypeDef",
    "IndexConfigurationSummaryTypeDef",
    "IndexStatisticsTypeDef",
    "JsonTokenTypeConfigurationTypeDef",
    "JwtTokenTypeConfigurationTypeDef",
    "ListDataSourceSyncJobsResponseTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListFaqsResponseTypeDef",
    "ListIndicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListThesauriResponseTypeDef",
    "OneDriveConfigurationTypeDef",
    "OneDriveUsersTypeDef",
    "PrincipalTypeDef",
    "QueryResultItemTypeDef",
    "QueryResultTypeDef",
    "RelevanceFeedbackTypeDef",
    "RelevanceTypeDef",
    "S3DataSourceConfigurationTypeDef",
    "S3PathTypeDef",
    "SalesforceChatterFeedConfigurationTypeDef",
    "SalesforceConfigurationTypeDef",
    "SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceKnowledgeArticleConfigurationTypeDef",
    "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    "SalesforceStandardObjectConfigurationTypeDef",
    "ScoreAttributesTypeDef",
    "SearchTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServiceNowConfigurationTypeDef",
    "ServiceNowKnowledgeArticleConfigurationTypeDef",
    "ServiceNowServiceCatalogConfigurationTypeDef",
    "SharePointConfigurationTypeDef",
    "SortingConfigurationTypeDef",
    "SqlConfigurationTypeDef",
    "StartDataSourceSyncJobResponseTypeDef",
    "TagTypeDef",
    "TextDocumentStatisticsTypeDef",
    "TextWithHighlightsTypeDef",
    "ThesaurusSummaryTypeDef",
    "TimeRangeTypeDef",
    "UserContextTypeDef",
    "UserTokenConfigurationTypeDef",
)


class AccessControlListConfigurationTypeDef(TypedDict, total=False):
    KeyPath: str


class AclConfigurationTypeDef(TypedDict):
    AllowedGroupsColumnName: str


class AdditionalResultAttributeTypeDef(TypedDict):
    Key: str
    ValueType: Literal["TEXT_WITH_HIGHLIGHTS_VALUE"]
    Value: "AdditionalResultAttributeValueTypeDef"


class AdditionalResultAttributeValueTypeDef(TypedDict, total=False):
    TextWithHighlightsValue: "TextWithHighlightsTypeDef"


class AttributeFilterTypeDef(TypedDict, total=False):
    AndAllFilters: List[Dict[str, Any]]
    OrAllFilters: List[Dict[str, Any]]
    NotFilter: Dict[str, Any]
    EqualsTo: "DocumentAttributeTypeDef"
    ContainsAll: "DocumentAttributeTypeDef"
    ContainsAny: "DocumentAttributeTypeDef"
    GreaterThan: "DocumentAttributeTypeDef"
    GreaterThanOrEquals: "DocumentAttributeTypeDef"
    LessThan: "DocumentAttributeTypeDef"
    LessThanOrEquals: "DocumentAttributeTypeDef"


class BatchDeleteDocumentResponseFailedDocumentTypeDef(TypedDict, total=False):
    Id: str
    ErrorCode: ErrorCode
    ErrorMessage: str


class BatchDeleteDocumentResponseTypeDef(TypedDict, total=False):
    FailedDocuments: List["BatchDeleteDocumentResponseFailedDocumentTypeDef"]


class BatchPutDocumentResponseFailedDocumentTypeDef(TypedDict, total=False):
    Id: str
    ErrorCode: ErrorCode
    ErrorMessage: str


class BatchPutDocumentResponseTypeDef(TypedDict, total=False):
    FailedDocuments: List["BatchPutDocumentResponseFailedDocumentTypeDef"]


class CapacityUnitsConfigurationTypeDef(TypedDict):
    StorageCapacityUnits: int
    QueryCapacityUnits: int


class ClickFeedbackTypeDef(TypedDict):
    ResultId: str
    ClickTime: datetime


class _RequiredColumnConfigurationTypeDef(TypedDict):
    DocumentIdColumnName: str
    DocumentDataColumnName: str
    ChangeDetectingColumns: List[str]


class ColumnConfigurationTypeDef(_RequiredColumnConfigurationTypeDef, total=False):
    DocumentTitleColumnName: str
    FieldMappings: List["DataSourceToIndexFieldMappingTypeDef"]


class ConfluenceAttachmentConfigurationTypeDef(TypedDict, total=False):
    CrawlAttachments: bool
    AttachmentFieldMappings: List["ConfluenceAttachmentToIndexFieldMappingTypeDef"]


class ConfluenceAttachmentToIndexFieldMappingTypeDef(TypedDict, total=False):
    DataSourceFieldName: ConfluenceAttachmentFieldName
    DateFieldFormat: str
    IndexFieldName: str


class ConfluenceBlogConfigurationTypeDef(TypedDict, total=False):
    BlogFieldMappings: List["ConfluenceBlogToIndexFieldMappingTypeDef"]


class ConfluenceBlogToIndexFieldMappingTypeDef(TypedDict, total=False):
    DataSourceFieldName: ConfluenceBlogFieldName
    DateFieldFormat: str
    IndexFieldName: str


class _RequiredConfluenceConfigurationTypeDef(TypedDict):
    ServerUrl: str
    SecretArn: str
    Version: ConfluenceVersion


class ConfluenceConfigurationTypeDef(_RequiredConfluenceConfigurationTypeDef, total=False):
    SpaceConfiguration: "ConfluenceSpaceConfigurationTypeDef"
    PageConfiguration: "ConfluencePageConfigurationTypeDef"
    BlogConfiguration: "ConfluenceBlogConfigurationTypeDef"
    AttachmentConfiguration: "ConfluenceAttachmentConfigurationTypeDef"
    VpcConfiguration: "DataSourceVpcConfigurationTypeDef"
    InclusionPatterns: List[str]
    ExclusionPatterns: List[str]


class ConfluencePageConfigurationTypeDef(TypedDict, total=False):
    PageFieldMappings: List["ConfluencePageToIndexFieldMappingTypeDef"]


class ConfluencePageToIndexFieldMappingTypeDef(TypedDict, total=False):
    DataSourceFieldName: ConfluencePageFieldName
    DateFieldFormat: str
    IndexFieldName: str


class ConfluenceSpaceConfigurationTypeDef(TypedDict, total=False):
    CrawlPersonalSpaces: bool
    CrawlArchivedSpaces: bool
    IncludeSpaces: List[str]
    ExcludeSpaces: List[str]
    SpaceFieldMappings: List["ConfluenceSpaceToIndexFieldMappingTypeDef"]


class ConfluenceSpaceToIndexFieldMappingTypeDef(TypedDict, total=False):
    DataSourceFieldName: ConfluenceSpaceFieldName
    DateFieldFormat: str
    IndexFieldName: str


class ConnectionConfigurationTypeDef(TypedDict):
    DatabaseHost: str
    DatabasePort: int
    DatabaseName: str
    TableName: str
    SecretArn: str


class CreateDataSourceResponseTypeDef(TypedDict):
    Id: str


class CreateFaqResponseTypeDef(TypedDict, total=False):
    Id: str


class CreateIndexResponseTypeDef(TypedDict, total=False):
    Id: str


class CreateThesaurusResponseTypeDef(TypedDict, total=False):
    Id: str


class DataSourceConfigurationTypeDef(TypedDict, total=False):
    S3Configuration: "S3DataSourceConfigurationTypeDef"
    SharePointConfiguration: "SharePointConfigurationTypeDef"
    DatabaseConfiguration: "DatabaseConfigurationTypeDef"
    SalesforceConfiguration: "SalesforceConfigurationTypeDef"
    OneDriveConfiguration: "OneDriveConfigurationTypeDef"
    ServiceNowConfiguration: "ServiceNowConfigurationTypeDef"
    ConfluenceConfiguration: "ConfluenceConfigurationTypeDef"
    GoogleDriveConfiguration: "GoogleDriveConfigurationTypeDef"


DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Type": DataSourceType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": DataSourceStatus,
    },
    total=False,
)


class DataSourceSyncJobMetricTargetTypeDef(TypedDict):
    DataSourceId: str
    DataSourceSyncJobId: str


class DataSourceSyncJobMetricsTypeDef(TypedDict, total=False):
    DocumentsAdded: str
    DocumentsModified: str
    DocumentsDeleted: str
    DocumentsFailed: str
    DocumentsScanned: str


class DataSourceSyncJobTypeDef(TypedDict, total=False):
    ExecutionId: str
    StartTime: datetime
    EndTime: datetime
    Status: DataSourceSyncJobStatus
    ErrorMessage: str
    ErrorCode: ErrorCode
    DataSourceErrorCode: str
    Metrics: "DataSourceSyncJobMetricsTypeDef"


class _RequiredDataSourceToIndexFieldMappingTypeDef(TypedDict):
    DataSourceFieldName: str
    IndexFieldName: str


class DataSourceToIndexFieldMappingTypeDef(
    _RequiredDataSourceToIndexFieldMappingTypeDef, total=False
):
    DateFieldFormat: str


class DataSourceVpcConfigurationTypeDef(TypedDict):
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class _RequiredDatabaseConfigurationTypeDef(TypedDict):
    DatabaseEngineType: DatabaseEngineType
    ConnectionConfiguration: "ConnectionConfigurationTypeDef"
    ColumnConfiguration: "ColumnConfigurationTypeDef"


class DatabaseConfigurationTypeDef(_RequiredDatabaseConfigurationTypeDef, total=False):
    VpcConfiguration: "DataSourceVpcConfigurationTypeDef"
    AclConfiguration: "AclConfigurationTypeDef"
    SqlConfiguration: "SqlConfigurationTypeDef"


DescribeDataSourceResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Type": DataSourceType,
        "Configuration": "DataSourceConfigurationTypeDef",
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Description": str,
        "Status": DataSourceStatus,
        "Schedule": str,
        "RoleArn": str,
        "ErrorMessage": str,
    },
    total=False,
)


class DescribeFaqResponseTypeDef(TypedDict, total=False):
    Id: str
    IndexId: str
    Name: str
    Description: str
    CreatedAt: datetime
    UpdatedAt: datetime
    S3Path: "S3PathTypeDef"
    Status: FaqStatus
    RoleArn: str
    ErrorMessage: str
    FileFormat: FaqFileFormat


class DescribeIndexResponseTypeDef(TypedDict, total=False):
    Name: str
    Id: str
    Edition: IndexEdition
    RoleArn: str
    ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef"
    Status: IndexStatus
    Description: str
    CreatedAt: datetime
    UpdatedAt: datetime
    DocumentMetadataConfigurations: List["DocumentMetadataConfigurationTypeDef"]
    IndexStatistics: "IndexStatisticsTypeDef"
    ErrorMessage: str
    CapacityUnits: "CapacityUnitsConfigurationTypeDef"
    UserTokenConfigurations: List["UserTokenConfigurationTypeDef"]
    UserContextPolicy: UserContextPolicy


class DescribeThesaurusResponseTypeDef(TypedDict, total=False):
    Id: str
    IndexId: str
    Name: str
    Description: str
    Status: ThesaurusStatus
    ErrorMessage: str
    CreatedAt: datetime
    UpdatedAt: datetime
    RoleArn: str
    SourceS3Path: "S3PathTypeDef"
    FileSizeBytes: int
    TermCount: int
    SynonymRuleCount: int


class DocumentAttributeTypeDef(TypedDict):
    Key: str
    Value: "DocumentAttributeValueTypeDef"


class DocumentAttributeValueCountPairTypeDef(TypedDict, total=False):
    DocumentAttributeValue: "DocumentAttributeValueTypeDef"
    Count: int


class DocumentAttributeValueTypeDef(TypedDict, total=False):
    StringValue: str
    StringListValue: List[str]
    LongValue: int
    DateValue: datetime


_RequiredDocumentMetadataConfigurationTypeDef = TypedDict(
    "_RequiredDocumentMetadataConfigurationTypeDef",
    {"Name": str, "Type": DocumentAttributeValueType},
)
_OptionalDocumentMetadataConfigurationTypeDef = TypedDict(
    "_OptionalDocumentMetadataConfigurationTypeDef",
    {"Relevance": "RelevanceTypeDef", "Search": "SearchTypeDef"},
    total=False,
)


class DocumentMetadataConfigurationTypeDef(
    _RequiredDocumentMetadataConfigurationTypeDef, _OptionalDocumentMetadataConfigurationTypeDef
):
    pass


class DocumentRelevanceConfigurationTypeDef(TypedDict):
    Name: str
    Relevance: "RelevanceTypeDef"


class _RequiredDocumentTypeDef(TypedDict):
    Id: str


class DocumentTypeDef(_RequiredDocumentTypeDef, total=False):
    Title: str
    Blob: Union[bytes, IO[bytes]]
    S3Path: "S3PathTypeDef"
    Attributes: List["DocumentAttributeTypeDef"]
    AccessControlList: List["PrincipalTypeDef"]
    ContentType: ContentType


class DocumentsMetadataConfigurationTypeDef(TypedDict, total=False):
    S3Prefix: str


class FacetResultTypeDef(TypedDict, total=False):
    DocumentAttributeKey: str
    DocumentAttributeValueType: DocumentAttributeValueType
    DocumentAttributeValueCountPairs: List["DocumentAttributeValueCountPairTypeDef"]


class FacetTypeDef(TypedDict, total=False):
    DocumentAttributeKey: str


class FaqStatisticsTypeDef(TypedDict):
    IndexedQuestionAnswersCount: int


class FaqSummaryTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Status: FaqStatus
    CreatedAt: datetime
    UpdatedAt: datetime
    FileFormat: FaqFileFormat


class _RequiredGoogleDriveConfigurationTypeDef(TypedDict):
    SecretArn: str


class GoogleDriveConfigurationTypeDef(_RequiredGoogleDriveConfigurationTypeDef, total=False):
    InclusionPatterns: List[str]
    ExclusionPatterns: List[str]
    FieldMappings: List["DataSourceToIndexFieldMappingTypeDef"]
    ExcludeMimeTypes: List[str]
    ExcludeUserAccounts: List[str]
    ExcludeSharedDrives: List[str]


_RequiredHighlightTypeDef = TypedDict(
    "_RequiredHighlightTypeDef", {"BeginOffset": int, "EndOffset": int}
)
_OptionalHighlightTypeDef = TypedDict(
    "_OptionalHighlightTypeDef", {"TopAnswer": bool, "Type": HighlightType}, total=False
)


class HighlightTypeDef(_RequiredHighlightTypeDef, _OptionalHighlightTypeDef):
    pass


class _RequiredIndexConfigurationSummaryTypeDef(TypedDict):
    CreatedAt: datetime
    UpdatedAt: datetime
    Status: IndexStatus


class IndexConfigurationSummaryTypeDef(_RequiredIndexConfigurationSummaryTypeDef, total=False):
    Name: str
    Id: str
    Edition: IndexEdition


class IndexStatisticsTypeDef(TypedDict):
    FaqStatistics: "FaqStatisticsTypeDef"
    TextDocumentStatistics: "TextDocumentStatisticsTypeDef"


class JsonTokenTypeConfigurationTypeDef(TypedDict):
    UserNameAttributeField: str
    GroupAttributeField: str


class _RequiredJwtTokenTypeConfigurationTypeDef(TypedDict):
    KeyLocation: KeyLocation


class JwtTokenTypeConfigurationTypeDef(_RequiredJwtTokenTypeConfigurationTypeDef, total=False):
    URL: str
    SecretManagerArn: str
    UserNameAttributeField: str
    GroupAttributeField: str
    Issuer: str
    ClaimRegex: str


class ListDataSourceSyncJobsResponseTypeDef(TypedDict, total=False):
    History: List["DataSourceSyncJobTypeDef"]
    NextToken: str


class ListDataSourcesResponseTypeDef(TypedDict, total=False):
    SummaryItems: List["DataSourceSummaryTypeDef"]
    NextToken: str


class ListFaqsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    FaqSummaryItems: List["FaqSummaryTypeDef"]


class ListIndicesResponseTypeDef(TypedDict, total=False):
    IndexConfigurationSummaryItems: List["IndexConfigurationSummaryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class ListThesauriResponseTypeDef(TypedDict, total=False):
    NextToken: str
    ThesaurusSummaryItems: List["ThesaurusSummaryTypeDef"]


class _RequiredOneDriveConfigurationTypeDef(TypedDict):
    TenantDomain: str
    SecretArn: str
    OneDriveUsers: "OneDriveUsersTypeDef"


class OneDriveConfigurationTypeDef(_RequiredOneDriveConfigurationTypeDef, total=False):
    InclusionPatterns: List[str]
    ExclusionPatterns: List[str]
    FieldMappings: List["DataSourceToIndexFieldMappingTypeDef"]
    DisableLocalGroups: bool


class OneDriveUsersTypeDef(TypedDict, total=False):
    OneDriveUserList: List[str]
    OneDriveUserS3Path: "S3PathTypeDef"


PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef", {"Name": str, "Type": PrincipalType, "Access": ReadAccessType}
)

QueryResultItemTypeDef = TypedDict(
    "QueryResultItemTypeDef",
    {
        "Id": str,
        "Type": QueryResultType,
        "AdditionalAttributes": List["AdditionalResultAttributeTypeDef"],
        "DocumentId": str,
        "DocumentTitle": "TextWithHighlightsTypeDef",
        "DocumentExcerpt": "TextWithHighlightsTypeDef",
        "DocumentURI": str,
        "DocumentAttributes": List["DocumentAttributeTypeDef"],
        "ScoreAttributes": "ScoreAttributesTypeDef",
        "FeedbackToken": str,
    },
    total=False,
)


class QueryResultTypeDef(TypedDict, total=False):
    QueryId: str
    ResultItems: List["QueryResultItemTypeDef"]
    FacetResults: List["FacetResultTypeDef"]
    TotalNumberOfResults: int


class RelevanceFeedbackTypeDef(TypedDict):
    ResultId: str
    RelevanceValue: RelevanceType


class RelevanceTypeDef(TypedDict, total=False):
    Freshness: bool
    Importance: int
    Duration: str
    RankOrder: Order
    ValueImportanceMap: Dict[str, int]


class _RequiredS3DataSourceConfigurationTypeDef(TypedDict):
    BucketName: str


class S3DataSourceConfigurationTypeDef(_RequiredS3DataSourceConfigurationTypeDef, total=False):
    InclusionPrefixes: List[str]
    InclusionPatterns: List[str]
    ExclusionPatterns: List[str]
    DocumentsMetadataConfiguration: "DocumentsMetadataConfigurationTypeDef"
    AccessControlListConfiguration: "AccessControlListConfigurationTypeDef"


class S3PathTypeDef(TypedDict):
    Bucket: str
    Key: str


class _RequiredSalesforceChatterFeedConfigurationTypeDef(TypedDict):
    DocumentDataFieldName: str


class SalesforceChatterFeedConfigurationTypeDef(
    _RequiredSalesforceChatterFeedConfigurationTypeDef, total=False
):
    DocumentTitleFieldName: str
    FieldMappings: List["DataSourceToIndexFieldMappingTypeDef"]
    IncludeFilterTypes: List[SalesforceChatterFeedIncludeFilterType]


class _RequiredSalesforceConfigurationTypeDef(TypedDict):
    ServerUrl: str
    SecretArn: str


class SalesforceConfigurationTypeDef(_RequiredSalesforceConfigurationTypeDef, total=False):
    StandardObjectConfigurations: List["SalesforceStandardObjectConfigurationTypeDef"]
    KnowledgeArticleConfiguration: "SalesforceKnowledgeArticleConfigurationTypeDef"
    ChatterFeedConfiguration: "SalesforceChatterFeedConfigurationTypeDef"
    CrawlAttachments: bool
    StandardObjectAttachmentConfiguration: "SalesforceStandardObjectAttachmentConfigurationTypeDef"
    IncludeAttachmentFilePatterns: List[str]
    ExcludeAttachmentFilePatterns: List[str]


class _RequiredSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef(TypedDict):
    Name: str
    DocumentDataFieldName: str


class SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef(
    _RequiredSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef, total=False
):
    DocumentTitleFieldName: str
    FieldMappings: List["DataSourceToIndexFieldMappingTypeDef"]


class _RequiredSalesforceKnowledgeArticleConfigurationTypeDef(TypedDict):
    IncludedStates: List[SalesforceKnowledgeArticleState]


class SalesforceKnowledgeArticleConfigurationTypeDef(
    _RequiredSalesforceKnowledgeArticleConfigurationTypeDef, total=False
):
    StandardKnowledgeArticleTypeConfiguration: "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef"
    CustomKnowledgeArticleTypeConfigurations: List[
        "SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef"
    ]


class _RequiredSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef(TypedDict):
    DocumentDataFieldName: str


class SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef(
    _RequiredSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef, total=False
):
    DocumentTitleFieldName: str
    FieldMappings: List["DataSourceToIndexFieldMappingTypeDef"]


class SalesforceStandardObjectAttachmentConfigurationTypeDef(TypedDict, total=False):
    DocumentTitleFieldName: str
    FieldMappings: List["DataSourceToIndexFieldMappingTypeDef"]


class _RequiredSalesforceStandardObjectConfigurationTypeDef(TypedDict):
    Name: SalesforceStandardObjectName
    DocumentDataFieldName: str


class SalesforceStandardObjectConfigurationTypeDef(
    _RequiredSalesforceStandardObjectConfigurationTypeDef, total=False
):
    DocumentTitleFieldName: str
    FieldMappings: List["DataSourceToIndexFieldMappingTypeDef"]


class ScoreAttributesTypeDef(TypedDict, total=False):
    ScoreConfidence: ScoreConfidence


class SearchTypeDef(TypedDict, total=False):
    Facetable: bool
    Searchable: bool
    Displayable: bool
    Sortable: bool


class ServerSideEncryptionConfigurationTypeDef(TypedDict, total=False):
    KmsKeyId: str


class _RequiredServiceNowConfigurationTypeDef(TypedDict):
    HostUrl: str
    SecretArn: str
    ServiceNowBuildVersion: ServiceNowBuildVersionType


class ServiceNowConfigurationTypeDef(_RequiredServiceNowConfigurationTypeDef, total=False):
    KnowledgeArticleConfiguration: "ServiceNowKnowledgeArticleConfigurationTypeDef"
    ServiceCatalogConfiguration: "ServiceNowServiceCatalogConfigurationTypeDef"
    AuthenticationType: ServiceNowAuthenticationType


class _RequiredServiceNowKnowledgeArticleConfigurationTypeDef(TypedDict):
    DocumentDataFieldName: str


class ServiceNowKnowledgeArticleConfigurationTypeDef(
    _RequiredServiceNowKnowledgeArticleConfigurationTypeDef, total=False
):
    CrawlAttachments: bool
    IncludeAttachmentFilePatterns: List[str]
    ExcludeAttachmentFilePatterns: List[str]
    DocumentTitleFieldName: str
    FieldMappings: List["DataSourceToIndexFieldMappingTypeDef"]
    FilterQuery: str


class _RequiredServiceNowServiceCatalogConfigurationTypeDef(TypedDict):
    DocumentDataFieldName: str


class ServiceNowServiceCatalogConfigurationTypeDef(
    _RequiredServiceNowServiceCatalogConfigurationTypeDef, total=False
):
    CrawlAttachments: bool
    IncludeAttachmentFilePatterns: List[str]
    ExcludeAttachmentFilePatterns: List[str]
    DocumentTitleFieldName: str
    FieldMappings: List["DataSourceToIndexFieldMappingTypeDef"]


class _RequiredSharePointConfigurationTypeDef(TypedDict):
    SharePointVersion: Literal["SHAREPOINT_ONLINE"]
    Urls: List[str]
    SecretArn: str


class SharePointConfigurationTypeDef(_RequiredSharePointConfigurationTypeDef, total=False):
    CrawlAttachments: bool
    UseChangeLog: bool
    InclusionPatterns: List[str]
    ExclusionPatterns: List[str]
    VpcConfiguration: "DataSourceVpcConfigurationTypeDef"
    FieldMappings: List["DataSourceToIndexFieldMappingTypeDef"]
    DocumentTitleFieldName: str
    DisableLocalGroups: bool


class SortingConfigurationTypeDef(TypedDict):
    DocumentAttributeKey: str
    SortOrder: SortOrder


class SqlConfigurationTypeDef(TypedDict, total=False):
    QueryIdentifiersEnclosingOption: QueryIdentifiersEnclosingOption


class StartDataSourceSyncJobResponseTypeDef(TypedDict, total=False):
    ExecutionId: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TextDocumentStatisticsTypeDef(TypedDict):
    IndexedTextDocumentsCount: int
    IndexedTextBytes: int


TextWithHighlightsTypeDef = TypedDict(
    "TextWithHighlightsTypeDef", {"Text": str, "Highlights": List["HighlightTypeDef"]}, total=False
)


class ThesaurusSummaryTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Status: ThesaurusStatus
    CreatedAt: datetime
    UpdatedAt: datetime


class TimeRangeTypeDef(TypedDict, total=False):
    StartTime: datetime
    EndTime: datetime


class UserContextTypeDef(TypedDict, total=False):
    Token: str


class UserTokenConfigurationTypeDef(TypedDict, total=False):
    JwtTokenTypeConfiguration: "JwtTokenTypeConfigurationTypeDef"
    JsonTokenTypeConfiguration: "JsonTokenTypeConfigurationTypeDef"
