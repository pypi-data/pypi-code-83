"""
Type annotations for customer-profiles service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/type_defs.html)

Usage::

    ```python
    from mypy_boto3_customer_profiles.type_defs import AddProfileKeyResponseTypeDef

    data: AddProfileKeyResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_customer_profiles.literals import (
    DataPullMode,
    FieldContentType,
    Gender,
    MarketoConnectorOperator,
    OperatorPropertiesKeys,
    PartyType,
    S3ConnectorOperator,
    SalesforceConnectorOperator,
    ServiceNowConnectorOperator,
    SourceConnectorType,
    StandardIdentifier,
    TaskType,
    TriggerType,
    ZendeskConnectorOperator,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddProfileKeyResponseTypeDef",
    "AddressTypeDef",
    "ConnectorOperatorTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateProfileResponseTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteIntegrationResponseTypeDef",
    "DeleteProfileKeyResponseTypeDef",
    "DeleteProfileObjectResponseTypeDef",
    "DeleteProfileObjectTypeResponseTypeDef",
    "DeleteProfileResponseTypeDef",
    "DomainStatsTypeDef",
    "FieldSourceProfileIdsTypeDef",
    "FlowDefinitionTypeDef",
    "GetDomainResponseTypeDef",
    "GetIntegrationResponseTypeDef",
    "GetMatchesResponseTypeDef",
    "GetProfileObjectTypeResponseTypeDef",
    "GetProfileObjectTypeTemplateResponseTypeDef",
    "IncrementalPullConfigTypeDef",
    "ListAccountIntegrationsResponseTypeDef",
    "ListDomainItemTypeDef",
    "ListDomainsResponseTypeDef",
    "ListIntegrationItemTypeDef",
    "ListIntegrationsResponseTypeDef",
    "ListProfileObjectTypeItemTypeDef",
    "ListProfileObjectTypeTemplateItemTypeDef",
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    "ListProfileObjectTypesResponseTypeDef",
    "ListProfileObjectsItemTypeDef",
    "ListProfileObjectsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "MatchItemTypeDef",
    "MatchingRequestTypeDef",
    "MatchingResponseTypeDef",
    "MergeProfilesResponseTypeDef",
    "ObjectTypeFieldTypeDef",
    "ObjectTypeKeyTypeDef",
    "ProfileTypeDef",
    "PutIntegrationResponseTypeDef",
    "PutProfileObjectResponseTypeDef",
    "PutProfileObjectTypeResponseTypeDef",
    "S3SourcePropertiesTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "SearchProfilesResponseTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "SourceFlowConfigTypeDef",
    "TaskTypeDef",
    "TriggerConfigTypeDef",
    "TriggerPropertiesTypeDef",
    "UpdateAddressTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateProfileResponseTypeDef",
    "ZendeskSourcePropertiesTypeDef",
)


class AddProfileKeyResponseTypeDef(TypedDict, total=False):
    KeyName: str
    Values: List[str]


class AddressTypeDef(TypedDict, total=False):
    Address1: str
    Address2: str
    Address3: str
    Address4: str
    City: str
    County: str
    State: str
    Province: str
    Country: str
    PostalCode: str


class ConnectorOperatorTypeDef(TypedDict, total=False):
    Marketo: MarketoConnectorOperator
    S3: S3ConnectorOperator
    Salesforce: SalesforceConnectorOperator
    ServiceNow: ServiceNowConnectorOperator
    Zendesk: ZendeskConnectorOperator


class _RequiredCreateDomainResponseTypeDef(TypedDict):
    DomainName: str
    DefaultExpirationDays: int
    CreatedAt: datetime
    LastUpdatedAt: datetime


class CreateDomainResponseTypeDef(_RequiredCreateDomainResponseTypeDef, total=False):
    DefaultEncryptionKey: str
    DeadLetterQueueUrl: str
    Matching: "MatchingResponseTypeDef"
    Tags: Dict[str, str]


class CreateProfileResponseTypeDef(TypedDict):
    ProfileId: str


class DeleteDomainResponseTypeDef(TypedDict):
    Message: str


class DeleteIntegrationResponseTypeDef(TypedDict):
    Message: str


class DeleteProfileKeyResponseTypeDef(TypedDict, total=False):
    Message: str


class DeleteProfileObjectResponseTypeDef(TypedDict, total=False):
    Message: str


class DeleteProfileObjectTypeResponseTypeDef(TypedDict):
    Message: str


class DeleteProfileResponseTypeDef(TypedDict, total=False):
    Message: str


class DomainStatsTypeDef(TypedDict, total=False):
    ProfileCount: int
    MeteringProfileCount: int
    ObjectCount: int
    TotalSize: int


class FieldSourceProfileIdsTypeDef(TypedDict, total=False):
    AccountNumber: str
    AdditionalInformation: str
    PartyType: str
    BusinessName: str
    FirstName: str
    MiddleName: str
    LastName: str
    BirthDate: str
    Gender: str
    PhoneNumber: str
    MobilePhoneNumber: str
    HomePhoneNumber: str
    BusinessPhoneNumber: str
    EmailAddress: str
    PersonalEmailAddress: str
    BusinessEmailAddress: str
    Address: str
    ShippingAddress: str
    MailingAddress: str
    BillingAddress: str
    Attributes: Dict[str, str]


class _RequiredFlowDefinitionTypeDef(TypedDict):
    FlowName: str
    KmsArn: str
    SourceFlowConfig: "SourceFlowConfigTypeDef"
    Tasks: List["TaskTypeDef"]
    TriggerConfig: "TriggerConfigTypeDef"


class FlowDefinitionTypeDef(_RequiredFlowDefinitionTypeDef, total=False):
    Description: str


class _RequiredGetDomainResponseTypeDef(TypedDict):
    DomainName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime


class GetDomainResponseTypeDef(_RequiredGetDomainResponseTypeDef, total=False):
    DefaultExpirationDays: int
    DefaultEncryptionKey: str
    DeadLetterQueueUrl: str
    Stats: "DomainStatsTypeDef"
    Matching: "MatchingResponseTypeDef"
    Tags: Dict[str, str]


class _RequiredGetIntegrationResponseTypeDef(TypedDict):
    DomainName: str
    Uri: str
    ObjectTypeName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime


class GetIntegrationResponseTypeDef(_RequiredGetIntegrationResponseTypeDef, total=False):
    Tags: Dict[str, str]


class GetMatchesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    MatchGenerationDate: datetime
    PotentialMatches: int
    Matches: List["MatchItemTypeDef"]


class _RequiredGetProfileObjectTypeResponseTypeDef(TypedDict):
    ObjectTypeName: str
    Description: str


class GetProfileObjectTypeResponseTypeDef(
    _RequiredGetProfileObjectTypeResponseTypeDef, total=False
):
    TemplateId: str
    ExpirationDays: int
    EncryptionKey: str
    AllowProfileCreation: bool
    Fields: Dict[str, "ObjectTypeFieldTypeDef"]
    Keys: Dict[str, List["ObjectTypeKeyTypeDef"]]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]


class GetProfileObjectTypeTemplateResponseTypeDef(TypedDict, total=False):
    TemplateId: str
    SourceName: str
    SourceObject: str
    AllowProfileCreation: bool
    Fields: Dict[str, "ObjectTypeFieldTypeDef"]
    Keys: Dict[str, List["ObjectTypeKeyTypeDef"]]


class IncrementalPullConfigTypeDef(TypedDict, total=False):
    DatetimeTypeFieldName: str


class ListAccountIntegrationsResponseTypeDef(TypedDict, total=False):
    Items: List["ListIntegrationItemTypeDef"]
    NextToken: str


class _RequiredListDomainItemTypeDef(TypedDict):
    DomainName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime


class ListDomainItemTypeDef(_RequiredListDomainItemTypeDef, total=False):
    Tags: Dict[str, str]


class ListDomainsResponseTypeDef(TypedDict, total=False):
    Items: List["ListDomainItemTypeDef"]
    NextToken: str


class _RequiredListIntegrationItemTypeDef(TypedDict):
    DomainName: str
    Uri: str
    ObjectTypeName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime


class ListIntegrationItemTypeDef(_RequiredListIntegrationItemTypeDef, total=False):
    Tags: Dict[str, str]


class ListIntegrationsResponseTypeDef(TypedDict, total=False):
    Items: List["ListIntegrationItemTypeDef"]
    NextToken: str


class _RequiredListProfileObjectTypeItemTypeDef(TypedDict):
    ObjectTypeName: str
    Description: str


class ListProfileObjectTypeItemTypeDef(_RequiredListProfileObjectTypeItemTypeDef, total=False):
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]


class ListProfileObjectTypeTemplateItemTypeDef(TypedDict, total=False):
    TemplateId: str
    SourceName: str
    SourceObject: str


class ListProfileObjectTypeTemplatesResponseTypeDef(TypedDict, total=False):
    Items: List["ListProfileObjectTypeTemplateItemTypeDef"]
    NextToken: str


class ListProfileObjectTypesResponseTypeDef(TypedDict, total=False):
    Items: List["ListProfileObjectTypeItemTypeDef"]
    NextToken: str


class ListProfileObjectsItemTypeDef(TypedDict, total=False):
    ObjectTypeName: str
    ProfileObjectUniqueKey: str
    Object: str


class ListProfileObjectsResponseTypeDef(TypedDict, total=False):
    Items: List["ListProfileObjectsItemTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class MarketoSourcePropertiesTypeDef(TypedDict):
    Object: str


class MatchItemTypeDef(TypedDict, total=False):
    MatchId: str
    ProfileIds: List[str]


class MatchingRequestTypeDef(TypedDict):
    Enabled: bool


class MatchingResponseTypeDef(TypedDict, total=False):
    Enabled: bool


class MergeProfilesResponseTypeDef(TypedDict, total=False):
    Message: str


class ObjectTypeFieldTypeDef(TypedDict, total=False):
    Source: str
    Target: str
    ContentType: FieldContentType


class ObjectTypeKeyTypeDef(TypedDict, total=False):
    StandardIdentifiers: List[StandardIdentifier]
    FieldNames: List[str]


class ProfileTypeDef(TypedDict, total=False):
    ProfileId: str
    AccountNumber: str
    AdditionalInformation: str
    PartyType: PartyType
    BusinessName: str
    FirstName: str
    MiddleName: str
    LastName: str
    BirthDate: str
    Gender: Gender
    PhoneNumber: str
    MobilePhoneNumber: str
    HomePhoneNumber: str
    BusinessPhoneNumber: str
    EmailAddress: str
    PersonalEmailAddress: str
    BusinessEmailAddress: str
    Address: "AddressTypeDef"
    ShippingAddress: "AddressTypeDef"
    MailingAddress: "AddressTypeDef"
    BillingAddress: "AddressTypeDef"
    Attributes: Dict[str, str]


class _RequiredPutIntegrationResponseTypeDef(TypedDict):
    DomainName: str
    Uri: str
    ObjectTypeName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime


class PutIntegrationResponseTypeDef(_RequiredPutIntegrationResponseTypeDef, total=False):
    Tags: Dict[str, str]


class PutProfileObjectResponseTypeDef(TypedDict, total=False):
    ProfileObjectUniqueKey: str


class _RequiredPutProfileObjectTypeResponseTypeDef(TypedDict):
    ObjectTypeName: str
    Description: str


class PutProfileObjectTypeResponseTypeDef(
    _RequiredPutProfileObjectTypeResponseTypeDef, total=False
):
    TemplateId: str
    ExpirationDays: int
    EncryptionKey: str
    AllowProfileCreation: bool
    Fields: Dict[str, "ObjectTypeFieldTypeDef"]
    Keys: Dict[str, List["ObjectTypeKeyTypeDef"]]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]


class _RequiredS3SourcePropertiesTypeDef(TypedDict):
    BucketName: str


class S3SourcePropertiesTypeDef(_RequiredS3SourcePropertiesTypeDef, total=False):
    BucketPrefix: str


class _RequiredSalesforceSourcePropertiesTypeDef(TypedDict):
    Object: str


class SalesforceSourcePropertiesTypeDef(_RequiredSalesforceSourcePropertiesTypeDef, total=False):
    EnableDynamicFieldUpdate: bool
    IncludeDeletedRecords: bool


class _RequiredScheduledTriggerPropertiesTypeDef(TypedDict):
    ScheduleExpression: str


class ScheduledTriggerPropertiesTypeDef(_RequiredScheduledTriggerPropertiesTypeDef, total=False):
    DataPullMode: DataPullMode
    ScheduleStartTime: datetime
    ScheduleEndTime: datetime
    Timezone: str
    ScheduleOffset: int
    FirstExecutionFrom: datetime


class SearchProfilesResponseTypeDef(TypedDict, total=False):
    Items: List["ProfileTypeDef"]
    NextToken: str


class ServiceNowSourcePropertiesTypeDef(TypedDict):
    Object: str


class SourceConnectorPropertiesTypeDef(TypedDict, total=False):
    Marketo: "MarketoSourcePropertiesTypeDef"
    S3: "S3SourcePropertiesTypeDef"
    Salesforce: "SalesforceSourcePropertiesTypeDef"
    ServiceNow: "ServiceNowSourcePropertiesTypeDef"
    Zendesk: "ZendeskSourcePropertiesTypeDef"


class _RequiredSourceFlowConfigTypeDef(TypedDict):
    ConnectorType: SourceConnectorType
    SourceConnectorProperties: "SourceConnectorPropertiesTypeDef"


class SourceFlowConfigTypeDef(_RequiredSourceFlowConfigTypeDef, total=False):
    ConnectorProfileName: str
    IncrementalPullConfig: "IncrementalPullConfigTypeDef"


class _RequiredTaskTypeDef(TypedDict):
    SourceFields: List[str]
    TaskType: TaskType


class TaskTypeDef(_RequiredTaskTypeDef, total=False):
    ConnectorOperator: "ConnectorOperatorTypeDef"
    DestinationField: str
    TaskProperties: Dict[OperatorPropertiesKeys, str]


class _RequiredTriggerConfigTypeDef(TypedDict):
    TriggerType: TriggerType


class TriggerConfigTypeDef(_RequiredTriggerConfigTypeDef, total=False):
    TriggerProperties: "TriggerPropertiesTypeDef"


class TriggerPropertiesTypeDef(TypedDict, total=False):
    Scheduled: "ScheduledTriggerPropertiesTypeDef"


class UpdateAddressTypeDef(TypedDict, total=False):
    Address1: str
    Address2: str
    Address3: str
    Address4: str
    City: str
    County: str
    State: str
    Province: str
    Country: str
    PostalCode: str


class _RequiredUpdateDomainResponseTypeDef(TypedDict):
    DomainName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime


class UpdateDomainResponseTypeDef(_RequiredUpdateDomainResponseTypeDef, total=False):
    DefaultExpirationDays: int
    DefaultEncryptionKey: str
    DeadLetterQueueUrl: str
    Matching: "MatchingResponseTypeDef"
    Tags: Dict[str, str]


class UpdateProfileResponseTypeDef(TypedDict):
    ProfileId: str


class ZendeskSourcePropertiesTypeDef(TypedDict):
    Object: str
