"""
Type annotations for clouddirectory service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/type_defs.html)

Usage::

    ```python
    from mypy_boto3_clouddirectory.type_defs import ApplySchemaResponseTypeDef

    data: ApplySchemaResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_clouddirectory.literals import (
    BatchReadExceptionType,
    DirectoryState,
    FacetAttributeType,
    FacetStyle,
    ObjectType,
    RangeMode,
    RequiredAttributeBehavior,
    RuleType,
    UpdateActionType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplySchemaResponseTypeDef",
    "AttachObjectResponseTypeDef",
    "AttachToIndexResponseTypeDef",
    "AttachTypedLinkResponseTypeDef",
    "AttributeKeyAndValueTypeDef",
    "AttributeKeyTypeDef",
    "AttributeNameAndValueTypeDef",
    "BatchAddFacetToObjectTypeDef",
    "BatchAttachObjectResponseTypeDef",
    "BatchAttachObjectTypeDef",
    "BatchAttachPolicyTypeDef",
    "BatchAttachToIndexResponseTypeDef",
    "BatchAttachToIndexTypeDef",
    "BatchAttachTypedLinkResponseTypeDef",
    "BatchAttachTypedLinkTypeDef",
    "BatchCreateIndexResponseTypeDef",
    "BatchCreateIndexTypeDef",
    "BatchCreateObjectResponseTypeDef",
    "BatchCreateObjectTypeDef",
    "BatchDeleteObjectTypeDef",
    "BatchDetachFromIndexResponseTypeDef",
    "BatchDetachFromIndexTypeDef",
    "BatchDetachObjectResponseTypeDef",
    "BatchDetachObjectTypeDef",
    "BatchDetachPolicyTypeDef",
    "BatchDetachTypedLinkTypeDef",
    "BatchGetLinkAttributesResponseTypeDef",
    "BatchGetLinkAttributesTypeDef",
    "BatchGetObjectAttributesResponseTypeDef",
    "BatchGetObjectAttributesTypeDef",
    "BatchGetObjectInformationResponseTypeDef",
    "BatchGetObjectInformationTypeDef",
    "BatchListAttachedIndicesResponseTypeDef",
    "BatchListAttachedIndicesTypeDef",
    "BatchListIncomingTypedLinksResponseTypeDef",
    "BatchListIncomingTypedLinksTypeDef",
    "BatchListIndexResponseTypeDef",
    "BatchListIndexTypeDef",
    "BatchListObjectAttributesResponseTypeDef",
    "BatchListObjectAttributesTypeDef",
    "BatchListObjectChildrenResponseTypeDef",
    "BatchListObjectChildrenTypeDef",
    "BatchListObjectParentPathsResponseTypeDef",
    "BatchListObjectParentPathsTypeDef",
    "BatchListObjectParentsResponseTypeDef",
    "BatchListObjectParentsTypeDef",
    "BatchListObjectPoliciesResponseTypeDef",
    "BatchListObjectPoliciesTypeDef",
    "BatchListOutgoingTypedLinksResponseTypeDef",
    "BatchListOutgoingTypedLinksTypeDef",
    "BatchListPolicyAttachmentsResponseTypeDef",
    "BatchListPolicyAttachmentsTypeDef",
    "BatchLookupPolicyResponseTypeDef",
    "BatchLookupPolicyTypeDef",
    "BatchReadExceptionTypeDef",
    "BatchReadOperationResponseTypeDef",
    "BatchReadOperationTypeDef",
    "BatchReadResponseTypeDef",
    "BatchReadSuccessfulResponseTypeDef",
    "BatchRemoveFacetFromObjectTypeDef",
    "BatchUpdateLinkAttributesTypeDef",
    "BatchUpdateObjectAttributesResponseTypeDef",
    "BatchUpdateObjectAttributesTypeDef",
    "BatchWriteOperationResponseTypeDef",
    "BatchWriteOperationTypeDef",
    "BatchWriteResponseTypeDef",
    "CreateDirectoryResponseTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateObjectResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "DeleteDirectoryResponseTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DetachFromIndexResponseTypeDef",
    "DetachObjectResponseTypeDef",
    "DirectoryTypeDef",
    "DisableDirectoryResponseTypeDef",
    "EnableDirectoryResponseTypeDef",
    "FacetAttributeDefinitionTypeDef",
    "FacetAttributeReferenceTypeDef",
    "FacetAttributeTypeDef",
    "FacetAttributeUpdateTypeDef",
    "FacetTypeDef",
    "GetAppliedSchemaVersionResponseTypeDef",
    "GetDirectoryResponseTypeDef",
    "GetFacetResponseTypeDef",
    "GetLinkAttributesResponseTypeDef",
    "GetObjectAttributesResponseTypeDef",
    "GetObjectInformationResponseTypeDef",
    "GetSchemaAsJsonResponseTypeDef",
    "GetTypedLinkFacetInformationResponseTypeDef",
    "IndexAttachmentTypeDef",
    "LinkAttributeActionTypeDef",
    "LinkAttributeUpdateTypeDef",
    "ListAppliedSchemaArnsResponseTypeDef",
    "ListAttachedIndicesResponseTypeDef",
    "ListDevelopmentSchemaArnsResponseTypeDef",
    "ListDirectoriesResponseTypeDef",
    "ListFacetAttributesResponseTypeDef",
    "ListFacetNamesResponseTypeDef",
    "ListIncomingTypedLinksResponseTypeDef",
    "ListIndexResponseTypeDef",
    "ListManagedSchemaArnsResponseTypeDef",
    "ListObjectAttributesResponseTypeDef",
    "ListObjectChildrenResponseTypeDef",
    "ListObjectParentPathsResponseTypeDef",
    "ListObjectParentsResponseTypeDef",
    "ListObjectPoliciesResponseTypeDef",
    "ListOutgoingTypedLinksResponseTypeDef",
    "ListPolicyAttachmentsResponseTypeDef",
    "ListPublishedSchemaArnsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypedLinkFacetAttributesResponseTypeDef",
    "ListTypedLinkFacetNamesResponseTypeDef",
    "LookupPolicyResponseTypeDef",
    "ObjectAttributeActionTypeDef",
    "ObjectAttributeRangeTypeDef",
    "ObjectAttributeUpdateTypeDef",
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    "ObjectReferenceTypeDef",
    "PaginatorConfigTypeDef",
    "PathToObjectIdentifiersTypeDef",
    "PolicyAttachmentTypeDef",
    "PolicyToPathTypeDef",
    "PublishSchemaResponseTypeDef",
    "PutSchemaFromJsonResponseTypeDef",
    "RuleTypeDef",
    "SchemaFacetTypeDef",
    "TagTypeDef",
    "TypedAttributeValueRangeTypeDef",
    "TypedAttributeValueTypeDef",
    "TypedLinkAttributeDefinitionTypeDef",
    "TypedLinkAttributeRangeTypeDef",
    "TypedLinkFacetAttributeUpdateTypeDef",
    "TypedLinkFacetTypeDef",
    "TypedLinkSchemaAndFacetNameTypeDef",
    "TypedLinkSpecifierTypeDef",
    "UpdateObjectAttributesResponseTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpgradeAppliedSchemaResponseTypeDef",
    "UpgradePublishedSchemaResponseTypeDef",
)


class ApplySchemaResponseTypeDef(TypedDict, total=False):
    AppliedSchemaArn: str
    DirectoryArn: str


class AttachObjectResponseTypeDef(TypedDict, total=False):
    AttachedObjectIdentifier: str


class AttachToIndexResponseTypeDef(TypedDict, total=False):
    AttachedObjectIdentifier: str


class AttachTypedLinkResponseTypeDef(TypedDict, total=False):
    TypedLinkSpecifier: "TypedLinkSpecifierTypeDef"


class AttributeKeyAndValueTypeDef(TypedDict):
    Key: "AttributeKeyTypeDef"
    Value: "TypedAttributeValueTypeDef"


class AttributeKeyTypeDef(TypedDict):
    SchemaArn: str
    FacetName: str
    Name: str


class AttributeNameAndValueTypeDef(TypedDict):
    AttributeName: str
    Value: "TypedAttributeValueTypeDef"


class BatchAddFacetToObjectTypeDef(TypedDict):
    SchemaFacet: "SchemaFacetTypeDef"
    ObjectAttributeList: List["AttributeKeyAndValueTypeDef"]
    ObjectReference: "ObjectReferenceTypeDef"


class BatchAttachObjectResponseTypeDef(TypedDict, total=False):
    attachedObjectIdentifier: str


class BatchAttachObjectTypeDef(TypedDict):
    ParentReference: "ObjectReferenceTypeDef"
    ChildReference: "ObjectReferenceTypeDef"
    LinkName: str


class BatchAttachPolicyTypeDef(TypedDict):
    PolicyReference: "ObjectReferenceTypeDef"
    ObjectReference: "ObjectReferenceTypeDef"


class BatchAttachToIndexResponseTypeDef(TypedDict, total=False):
    AttachedObjectIdentifier: str


class BatchAttachToIndexTypeDef(TypedDict):
    IndexReference: "ObjectReferenceTypeDef"
    TargetReference: "ObjectReferenceTypeDef"


class BatchAttachTypedLinkResponseTypeDef(TypedDict, total=False):
    TypedLinkSpecifier: "TypedLinkSpecifierTypeDef"


class BatchAttachTypedLinkTypeDef(TypedDict):
    SourceObjectReference: "ObjectReferenceTypeDef"
    TargetObjectReference: "ObjectReferenceTypeDef"
    TypedLinkFacet: "TypedLinkSchemaAndFacetNameTypeDef"
    Attributes: List["AttributeNameAndValueTypeDef"]


class BatchCreateIndexResponseTypeDef(TypedDict, total=False):
    ObjectIdentifier: str


class _RequiredBatchCreateIndexTypeDef(TypedDict):
    OrderedIndexedAttributeList: List["AttributeKeyTypeDef"]
    IsUnique: bool


class BatchCreateIndexTypeDef(_RequiredBatchCreateIndexTypeDef, total=False):
    ParentReference: "ObjectReferenceTypeDef"
    LinkName: str
    BatchReferenceName: str


class BatchCreateObjectResponseTypeDef(TypedDict, total=False):
    ObjectIdentifier: str


class _RequiredBatchCreateObjectTypeDef(TypedDict):
    SchemaFacet: List["SchemaFacetTypeDef"]
    ObjectAttributeList: List["AttributeKeyAndValueTypeDef"]


class BatchCreateObjectTypeDef(_RequiredBatchCreateObjectTypeDef, total=False):
    ParentReference: "ObjectReferenceTypeDef"
    LinkName: str
    BatchReferenceName: str


class BatchDeleteObjectTypeDef(TypedDict):
    ObjectReference: "ObjectReferenceTypeDef"


class BatchDetachFromIndexResponseTypeDef(TypedDict, total=False):
    DetachedObjectIdentifier: str


class BatchDetachFromIndexTypeDef(TypedDict):
    IndexReference: "ObjectReferenceTypeDef"
    TargetReference: "ObjectReferenceTypeDef"


class BatchDetachObjectResponseTypeDef(TypedDict, total=False):
    detachedObjectIdentifier: str


class _RequiredBatchDetachObjectTypeDef(TypedDict):
    ParentReference: "ObjectReferenceTypeDef"
    LinkName: str


class BatchDetachObjectTypeDef(_RequiredBatchDetachObjectTypeDef, total=False):
    BatchReferenceName: str


class BatchDetachPolicyTypeDef(TypedDict):
    PolicyReference: "ObjectReferenceTypeDef"
    ObjectReference: "ObjectReferenceTypeDef"


class BatchDetachTypedLinkTypeDef(TypedDict):
    TypedLinkSpecifier: "TypedLinkSpecifierTypeDef"


class BatchGetLinkAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: List["AttributeKeyAndValueTypeDef"]


class BatchGetLinkAttributesTypeDef(TypedDict):
    TypedLinkSpecifier: "TypedLinkSpecifierTypeDef"
    AttributeNames: List[str]


class BatchGetObjectAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: List["AttributeKeyAndValueTypeDef"]


class BatchGetObjectAttributesTypeDef(TypedDict):
    ObjectReference: "ObjectReferenceTypeDef"
    SchemaFacet: "SchemaFacetTypeDef"
    AttributeNames: List[str]


class BatchGetObjectInformationResponseTypeDef(TypedDict, total=False):
    SchemaFacets: List["SchemaFacetTypeDef"]
    ObjectIdentifier: str


class BatchGetObjectInformationTypeDef(TypedDict):
    ObjectReference: "ObjectReferenceTypeDef"


class BatchListAttachedIndicesResponseTypeDef(TypedDict, total=False):
    IndexAttachments: List["IndexAttachmentTypeDef"]
    NextToken: str


class _RequiredBatchListAttachedIndicesTypeDef(TypedDict):
    TargetReference: "ObjectReferenceTypeDef"


class BatchListAttachedIndicesTypeDef(_RequiredBatchListAttachedIndicesTypeDef, total=False):
    NextToken: str
    MaxResults: int


class BatchListIncomingTypedLinksResponseTypeDef(TypedDict, total=False):
    LinkSpecifiers: List["TypedLinkSpecifierTypeDef"]
    NextToken: str


class _RequiredBatchListIncomingTypedLinksTypeDef(TypedDict):
    ObjectReference: "ObjectReferenceTypeDef"


class BatchListIncomingTypedLinksTypeDef(_RequiredBatchListIncomingTypedLinksTypeDef, total=False):
    FilterAttributeRanges: List["TypedLinkAttributeRangeTypeDef"]
    FilterTypedLink: "TypedLinkSchemaAndFacetNameTypeDef"
    NextToken: str
    MaxResults: int


class BatchListIndexResponseTypeDef(TypedDict, total=False):
    IndexAttachments: List["IndexAttachmentTypeDef"]
    NextToken: str


class _RequiredBatchListIndexTypeDef(TypedDict):
    IndexReference: "ObjectReferenceTypeDef"


class BatchListIndexTypeDef(_RequiredBatchListIndexTypeDef, total=False):
    RangesOnIndexedValues: List["ObjectAttributeRangeTypeDef"]
    MaxResults: int
    NextToken: str


class BatchListObjectAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: List["AttributeKeyAndValueTypeDef"]
    NextToken: str


class _RequiredBatchListObjectAttributesTypeDef(TypedDict):
    ObjectReference: "ObjectReferenceTypeDef"


class BatchListObjectAttributesTypeDef(_RequiredBatchListObjectAttributesTypeDef, total=False):
    NextToken: str
    MaxResults: int
    FacetFilter: "SchemaFacetTypeDef"


class BatchListObjectChildrenResponseTypeDef(TypedDict, total=False):
    Children: Dict[str, str]
    NextToken: str


class _RequiredBatchListObjectChildrenTypeDef(TypedDict):
    ObjectReference: "ObjectReferenceTypeDef"


class BatchListObjectChildrenTypeDef(_RequiredBatchListObjectChildrenTypeDef, total=False):
    NextToken: str
    MaxResults: int


class BatchListObjectParentPathsResponseTypeDef(TypedDict, total=False):
    PathToObjectIdentifiersList: List["PathToObjectIdentifiersTypeDef"]
    NextToken: str


class _RequiredBatchListObjectParentPathsTypeDef(TypedDict):
    ObjectReference: "ObjectReferenceTypeDef"


class BatchListObjectParentPathsTypeDef(_RequiredBatchListObjectParentPathsTypeDef, total=False):
    NextToken: str
    MaxResults: int


class BatchListObjectParentsResponseTypeDef(TypedDict, total=False):
    ParentLinks: List["ObjectIdentifierAndLinkNameTupleTypeDef"]
    NextToken: str


class _RequiredBatchListObjectParentsTypeDef(TypedDict):
    ObjectReference: "ObjectReferenceTypeDef"


class BatchListObjectParentsTypeDef(_RequiredBatchListObjectParentsTypeDef, total=False):
    NextToken: str
    MaxResults: int


class BatchListObjectPoliciesResponseTypeDef(TypedDict, total=False):
    AttachedPolicyIds: List[str]
    NextToken: str


class _RequiredBatchListObjectPoliciesTypeDef(TypedDict):
    ObjectReference: "ObjectReferenceTypeDef"


class BatchListObjectPoliciesTypeDef(_RequiredBatchListObjectPoliciesTypeDef, total=False):
    NextToken: str
    MaxResults: int


class BatchListOutgoingTypedLinksResponseTypeDef(TypedDict, total=False):
    TypedLinkSpecifiers: List["TypedLinkSpecifierTypeDef"]
    NextToken: str


class _RequiredBatchListOutgoingTypedLinksTypeDef(TypedDict):
    ObjectReference: "ObjectReferenceTypeDef"


class BatchListOutgoingTypedLinksTypeDef(_RequiredBatchListOutgoingTypedLinksTypeDef, total=False):
    FilterAttributeRanges: List["TypedLinkAttributeRangeTypeDef"]
    FilterTypedLink: "TypedLinkSchemaAndFacetNameTypeDef"
    NextToken: str
    MaxResults: int


class BatchListPolicyAttachmentsResponseTypeDef(TypedDict, total=False):
    ObjectIdentifiers: List[str]
    NextToken: str


class _RequiredBatchListPolicyAttachmentsTypeDef(TypedDict):
    PolicyReference: "ObjectReferenceTypeDef"


class BatchListPolicyAttachmentsTypeDef(_RequiredBatchListPolicyAttachmentsTypeDef, total=False):
    NextToken: str
    MaxResults: int


class BatchLookupPolicyResponseTypeDef(TypedDict, total=False):
    PolicyToPathList: List["PolicyToPathTypeDef"]
    NextToken: str


class _RequiredBatchLookupPolicyTypeDef(TypedDict):
    ObjectReference: "ObjectReferenceTypeDef"


class BatchLookupPolicyTypeDef(_RequiredBatchLookupPolicyTypeDef, total=False):
    NextToken: str
    MaxResults: int


BatchReadExceptionTypeDef = TypedDict(
    "BatchReadExceptionTypeDef", {"Type": BatchReadExceptionType, "Message": str}, total=False
)


class BatchReadOperationResponseTypeDef(TypedDict, total=False):
    SuccessfulResponse: "BatchReadSuccessfulResponseTypeDef"
    ExceptionResponse: "BatchReadExceptionTypeDef"


class BatchReadOperationTypeDef(TypedDict, total=False):
    ListObjectAttributes: "BatchListObjectAttributesTypeDef"
    ListObjectChildren: "BatchListObjectChildrenTypeDef"
    ListAttachedIndices: "BatchListAttachedIndicesTypeDef"
    ListObjectParentPaths: "BatchListObjectParentPathsTypeDef"
    GetObjectInformation: "BatchGetObjectInformationTypeDef"
    GetObjectAttributes: "BatchGetObjectAttributesTypeDef"
    ListObjectParents: "BatchListObjectParentsTypeDef"
    ListObjectPolicies: "BatchListObjectPoliciesTypeDef"
    ListPolicyAttachments: "BatchListPolicyAttachmentsTypeDef"
    LookupPolicy: "BatchLookupPolicyTypeDef"
    ListIndex: "BatchListIndexTypeDef"
    ListOutgoingTypedLinks: "BatchListOutgoingTypedLinksTypeDef"
    ListIncomingTypedLinks: "BatchListIncomingTypedLinksTypeDef"
    GetLinkAttributes: "BatchGetLinkAttributesTypeDef"


class BatchReadResponseTypeDef(TypedDict, total=False):
    Responses: List["BatchReadOperationResponseTypeDef"]


class BatchReadSuccessfulResponseTypeDef(TypedDict, total=False):
    ListObjectAttributes: "BatchListObjectAttributesResponseTypeDef"
    ListObjectChildren: "BatchListObjectChildrenResponseTypeDef"
    GetObjectInformation: "BatchGetObjectInformationResponseTypeDef"
    GetObjectAttributes: "BatchGetObjectAttributesResponseTypeDef"
    ListAttachedIndices: "BatchListAttachedIndicesResponseTypeDef"
    ListObjectParentPaths: "BatchListObjectParentPathsResponseTypeDef"
    ListObjectPolicies: "BatchListObjectPoliciesResponseTypeDef"
    ListPolicyAttachments: "BatchListPolicyAttachmentsResponseTypeDef"
    LookupPolicy: "BatchLookupPolicyResponseTypeDef"
    ListIndex: "BatchListIndexResponseTypeDef"
    ListOutgoingTypedLinks: "BatchListOutgoingTypedLinksResponseTypeDef"
    ListIncomingTypedLinks: "BatchListIncomingTypedLinksResponseTypeDef"
    GetLinkAttributes: "BatchGetLinkAttributesResponseTypeDef"
    ListObjectParents: "BatchListObjectParentsResponseTypeDef"


class BatchRemoveFacetFromObjectTypeDef(TypedDict):
    SchemaFacet: "SchemaFacetTypeDef"
    ObjectReference: "ObjectReferenceTypeDef"


class BatchUpdateLinkAttributesTypeDef(TypedDict):
    TypedLinkSpecifier: "TypedLinkSpecifierTypeDef"
    AttributeUpdates: List["LinkAttributeUpdateTypeDef"]


class BatchUpdateObjectAttributesResponseTypeDef(TypedDict, total=False):
    ObjectIdentifier: str


class BatchUpdateObjectAttributesTypeDef(TypedDict):
    ObjectReference: "ObjectReferenceTypeDef"
    AttributeUpdates: List["ObjectAttributeUpdateTypeDef"]


class BatchWriteOperationResponseTypeDef(TypedDict, total=False):
    CreateObject: "BatchCreateObjectResponseTypeDef"
    AttachObject: "BatchAttachObjectResponseTypeDef"
    DetachObject: "BatchDetachObjectResponseTypeDef"
    UpdateObjectAttributes: "BatchUpdateObjectAttributesResponseTypeDef"
    DeleteObject: Dict[str, Any]
    AddFacetToObject: Dict[str, Any]
    RemoveFacetFromObject: Dict[str, Any]
    AttachPolicy: Dict[str, Any]
    DetachPolicy: Dict[str, Any]
    CreateIndex: "BatchCreateIndexResponseTypeDef"
    AttachToIndex: "BatchAttachToIndexResponseTypeDef"
    DetachFromIndex: "BatchDetachFromIndexResponseTypeDef"
    AttachTypedLink: "BatchAttachTypedLinkResponseTypeDef"
    DetachTypedLink: Dict[str, Any]
    UpdateLinkAttributes: Dict[str, Any]


class BatchWriteOperationTypeDef(TypedDict, total=False):
    CreateObject: "BatchCreateObjectTypeDef"
    AttachObject: "BatchAttachObjectTypeDef"
    DetachObject: "BatchDetachObjectTypeDef"
    UpdateObjectAttributes: "BatchUpdateObjectAttributesTypeDef"
    DeleteObject: "BatchDeleteObjectTypeDef"
    AddFacetToObject: "BatchAddFacetToObjectTypeDef"
    RemoveFacetFromObject: "BatchRemoveFacetFromObjectTypeDef"
    AttachPolicy: "BatchAttachPolicyTypeDef"
    DetachPolicy: "BatchDetachPolicyTypeDef"
    CreateIndex: "BatchCreateIndexTypeDef"
    AttachToIndex: "BatchAttachToIndexTypeDef"
    DetachFromIndex: "BatchDetachFromIndexTypeDef"
    AttachTypedLink: "BatchAttachTypedLinkTypeDef"
    DetachTypedLink: "BatchDetachTypedLinkTypeDef"
    UpdateLinkAttributes: "BatchUpdateLinkAttributesTypeDef"


class BatchWriteResponseTypeDef(TypedDict, total=False):
    Responses: List["BatchWriteOperationResponseTypeDef"]


class CreateDirectoryResponseTypeDef(TypedDict):
    DirectoryArn: str
    Name: str
    ObjectIdentifier: str
    AppliedSchemaArn: str


class CreateIndexResponseTypeDef(TypedDict, total=False):
    ObjectIdentifier: str


class CreateObjectResponseTypeDef(TypedDict, total=False):
    ObjectIdentifier: str


class CreateSchemaResponseTypeDef(TypedDict, total=False):
    SchemaArn: str


class DeleteDirectoryResponseTypeDef(TypedDict):
    DirectoryArn: str


class DeleteSchemaResponseTypeDef(TypedDict, total=False):
    SchemaArn: str


class DetachFromIndexResponseTypeDef(TypedDict, total=False):
    DetachedObjectIdentifier: str


class DetachObjectResponseTypeDef(TypedDict, total=False):
    DetachedObjectIdentifier: str


class DirectoryTypeDef(TypedDict, total=False):
    Name: str
    DirectoryArn: str
    State: DirectoryState
    CreationDateTime: datetime


class DisableDirectoryResponseTypeDef(TypedDict):
    DirectoryArn: str


class EnableDirectoryResponseTypeDef(TypedDict):
    DirectoryArn: str


_RequiredFacetAttributeDefinitionTypeDef = TypedDict(
    "_RequiredFacetAttributeDefinitionTypeDef", {"Type": FacetAttributeType}
)
_OptionalFacetAttributeDefinitionTypeDef = TypedDict(
    "_OptionalFacetAttributeDefinitionTypeDef",
    {
        "DefaultValue": "TypedAttributeValueTypeDef",
        "IsImmutable": bool,
        "Rules": Dict[str, "RuleTypeDef"],
    },
    total=False,
)


class FacetAttributeDefinitionTypeDef(
    _RequiredFacetAttributeDefinitionTypeDef, _OptionalFacetAttributeDefinitionTypeDef
):
    pass


class FacetAttributeReferenceTypeDef(TypedDict):
    TargetFacetName: str
    TargetAttributeName: str


class _RequiredFacetAttributeTypeDef(TypedDict):
    Name: str


class FacetAttributeTypeDef(_RequiredFacetAttributeTypeDef, total=False):
    AttributeDefinition: "FacetAttributeDefinitionTypeDef"
    AttributeReference: "FacetAttributeReferenceTypeDef"
    RequiredBehavior: RequiredAttributeBehavior


class FacetAttributeUpdateTypeDef(TypedDict, total=False):
    Attribute: "FacetAttributeTypeDef"
    Action: UpdateActionType


class FacetTypeDef(TypedDict, total=False):
    Name: str
    ObjectType: ObjectType
    FacetStyle: FacetStyle


class GetAppliedSchemaVersionResponseTypeDef(TypedDict, total=False):
    AppliedSchemaArn: str


class GetDirectoryResponseTypeDef(TypedDict):
    Directory: "DirectoryTypeDef"


class GetFacetResponseTypeDef(TypedDict, total=False):
    Facet: "FacetTypeDef"


class GetLinkAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: List["AttributeKeyAndValueTypeDef"]


class GetObjectAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: List["AttributeKeyAndValueTypeDef"]


class GetObjectInformationResponseTypeDef(TypedDict, total=False):
    SchemaFacets: List["SchemaFacetTypeDef"]
    ObjectIdentifier: str


class GetSchemaAsJsonResponseTypeDef(TypedDict, total=False):
    Name: str
    Document: str


class GetTypedLinkFacetInformationResponseTypeDef(TypedDict, total=False):
    IdentityAttributeOrder: List[str]


class IndexAttachmentTypeDef(TypedDict, total=False):
    IndexedAttributes: List["AttributeKeyAndValueTypeDef"]
    ObjectIdentifier: str


class LinkAttributeActionTypeDef(TypedDict, total=False):
    AttributeActionType: UpdateActionType
    AttributeUpdateValue: "TypedAttributeValueTypeDef"


class LinkAttributeUpdateTypeDef(TypedDict, total=False):
    AttributeKey: "AttributeKeyTypeDef"
    AttributeAction: "LinkAttributeActionTypeDef"


class ListAppliedSchemaArnsResponseTypeDef(TypedDict, total=False):
    SchemaArns: List[str]
    NextToken: str


class ListAttachedIndicesResponseTypeDef(TypedDict, total=False):
    IndexAttachments: List["IndexAttachmentTypeDef"]
    NextToken: str


class ListDevelopmentSchemaArnsResponseTypeDef(TypedDict, total=False):
    SchemaArns: List[str]
    NextToken: str


class _RequiredListDirectoriesResponseTypeDef(TypedDict):
    Directories: List["DirectoryTypeDef"]


class ListDirectoriesResponseTypeDef(_RequiredListDirectoriesResponseTypeDef, total=False):
    NextToken: str


class ListFacetAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: List["FacetAttributeTypeDef"]
    NextToken: str


class ListFacetNamesResponseTypeDef(TypedDict, total=False):
    FacetNames: List[str]
    NextToken: str


class ListIncomingTypedLinksResponseTypeDef(TypedDict, total=False):
    LinkSpecifiers: List["TypedLinkSpecifierTypeDef"]
    NextToken: str


class ListIndexResponseTypeDef(TypedDict, total=False):
    IndexAttachments: List["IndexAttachmentTypeDef"]
    NextToken: str


class ListManagedSchemaArnsResponseTypeDef(TypedDict, total=False):
    SchemaArns: List[str]
    NextToken: str


class ListObjectAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: List["AttributeKeyAndValueTypeDef"]
    NextToken: str


class ListObjectChildrenResponseTypeDef(TypedDict, total=False):
    Children: Dict[str, str]
    NextToken: str


class ListObjectParentPathsResponseTypeDef(TypedDict, total=False):
    PathToObjectIdentifiersList: List["PathToObjectIdentifiersTypeDef"]
    NextToken: str


class ListObjectParentsResponseTypeDef(TypedDict, total=False):
    Parents: Dict[str, str]
    NextToken: str
    ParentLinks: List["ObjectIdentifierAndLinkNameTupleTypeDef"]


class ListObjectPoliciesResponseTypeDef(TypedDict, total=False):
    AttachedPolicyIds: List[str]
    NextToken: str


class ListOutgoingTypedLinksResponseTypeDef(TypedDict, total=False):
    TypedLinkSpecifiers: List["TypedLinkSpecifierTypeDef"]
    NextToken: str


class ListPolicyAttachmentsResponseTypeDef(TypedDict, total=False):
    ObjectIdentifiers: List[str]
    NextToken: str


class ListPublishedSchemaArnsResponseTypeDef(TypedDict, total=False):
    SchemaArns: List[str]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class ListTypedLinkFacetAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: List["TypedLinkAttributeDefinitionTypeDef"]
    NextToken: str


class ListTypedLinkFacetNamesResponseTypeDef(TypedDict, total=False):
    FacetNames: List[str]
    NextToken: str


class LookupPolicyResponseTypeDef(TypedDict, total=False):
    PolicyToPathList: List["PolicyToPathTypeDef"]
    NextToken: str


class ObjectAttributeActionTypeDef(TypedDict, total=False):
    ObjectAttributeActionType: UpdateActionType
    ObjectAttributeUpdateValue: "TypedAttributeValueTypeDef"


class ObjectAttributeRangeTypeDef(TypedDict, total=False):
    AttributeKey: "AttributeKeyTypeDef"
    Range: "TypedAttributeValueRangeTypeDef"


class ObjectAttributeUpdateTypeDef(TypedDict, total=False):
    ObjectAttributeKey: "AttributeKeyTypeDef"
    ObjectAttributeAction: "ObjectAttributeActionTypeDef"


class ObjectIdentifierAndLinkNameTupleTypeDef(TypedDict, total=False):
    ObjectIdentifier: str
    LinkName: str


class ObjectReferenceTypeDef(TypedDict, total=False):
    Selector: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PathToObjectIdentifiersTypeDef(TypedDict, total=False):
    Path: str
    ObjectIdentifiers: List[str]


class PolicyAttachmentTypeDef(TypedDict, total=False):
    PolicyId: str
    ObjectIdentifier: str
    PolicyType: str


class PolicyToPathTypeDef(TypedDict, total=False):
    Path: str
    Policies: List["PolicyAttachmentTypeDef"]


class PublishSchemaResponseTypeDef(TypedDict, total=False):
    PublishedSchemaArn: str


class PutSchemaFromJsonResponseTypeDef(TypedDict, total=False):
    Arn: str


RuleTypeDef = TypedDict(
    "RuleTypeDef", {"Type": RuleType, "Parameters": Dict[str, str]}, total=False
)


class SchemaFacetTypeDef(TypedDict, total=False):
    SchemaArn: str
    FacetName: str


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class _RequiredTypedAttributeValueRangeTypeDef(TypedDict):
    StartMode: RangeMode
    EndMode: RangeMode


class TypedAttributeValueRangeTypeDef(_RequiredTypedAttributeValueRangeTypeDef, total=False):
    StartValue: "TypedAttributeValueTypeDef"
    EndValue: "TypedAttributeValueTypeDef"


class TypedAttributeValueTypeDef(TypedDict, total=False):
    StringValue: str
    BinaryValue: Union[bytes, IO[bytes]]
    BooleanValue: bool
    NumberValue: str
    DatetimeValue: datetime


_RequiredTypedLinkAttributeDefinitionTypeDef = TypedDict(
    "_RequiredTypedLinkAttributeDefinitionTypeDef",
    {"Name": str, "Type": FacetAttributeType, "RequiredBehavior": RequiredAttributeBehavior},
)
_OptionalTypedLinkAttributeDefinitionTypeDef = TypedDict(
    "_OptionalTypedLinkAttributeDefinitionTypeDef",
    {
        "DefaultValue": "TypedAttributeValueTypeDef",
        "IsImmutable": bool,
        "Rules": Dict[str, "RuleTypeDef"],
    },
    total=False,
)


class TypedLinkAttributeDefinitionTypeDef(
    _RequiredTypedLinkAttributeDefinitionTypeDef, _OptionalTypedLinkAttributeDefinitionTypeDef
):
    pass


class _RequiredTypedLinkAttributeRangeTypeDef(TypedDict):
    Range: "TypedAttributeValueRangeTypeDef"


class TypedLinkAttributeRangeTypeDef(_RequiredTypedLinkAttributeRangeTypeDef, total=False):
    AttributeName: str


class TypedLinkFacetAttributeUpdateTypeDef(TypedDict):
    Attribute: "TypedLinkAttributeDefinitionTypeDef"
    Action: UpdateActionType


class TypedLinkFacetTypeDef(TypedDict):
    Name: str
    Attributes: List["TypedLinkAttributeDefinitionTypeDef"]
    IdentityAttributeOrder: List[str]


class TypedLinkSchemaAndFacetNameTypeDef(TypedDict):
    SchemaArn: str
    TypedLinkName: str


class TypedLinkSpecifierTypeDef(TypedDict):
    TypedLinkFacet: "TypedLinkSchemaAndFacetNameTypeDef"
    SourceObjectReference: "ObjectReferenceTypeDef"
    TargetObjectReference: "ObjectReferenceTypeDef"
    IdentityAttributeValues: List["AttributeNameAndValueTypeDef"]


class UpdateObjectAttributesResponseTypeDef(TypedDict, total=False):
    ObjectIdentifier: str


class UpdateSchemaResponseTypeDef(TypedDict, total=False):
    SchemaArn: str


class UpgradeAppliedSchemaResponseTypeDef(TypedDict, total=False):
    UpgradedSchemaArn: str
    DirectoryArn: str


class UpgradePublishedSchemaResponseTypeDef(TypedDict, total=False):
    UpgradedSchemaArn: str
