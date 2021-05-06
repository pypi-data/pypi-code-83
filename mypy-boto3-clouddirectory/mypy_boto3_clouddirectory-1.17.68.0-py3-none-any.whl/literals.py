"""
Type annotations for clouddirectory service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/literals.html)

Usage::

    ```python
    from mypy_boto3_clouddirectory.literals import BatchReadExceptionType

    data: BatchReadExceptionType = "AccessDeniedException"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BatchReadExceptionType",
    "ConsistencyLevel",
    "DirectoryState",
    "FacetAttributeType",
    "FacetStyle",
    "ListAppliedSchemaArnsPaginatorName",
    "ListAttachedIndicesPaginatorName",
    "ListDevelopmentSchemaArnsPaginatorName",
    "ListDirectoriesPaginatorName",
    "ListFacetAttributesPaginatorName",
    "ListFacetNamesPaginatorName",
    "ListIncomingTypedLinksPaginatorName",
    "ListIndexPaginatorName",
    "ListManagedSchemaArnsPaginatorName",
    "ListObjectAttributesPaginatorName",
    "ListObjectParentPathsPaginatorName",
    "ListObjectPoliciesPaginatorName",
    "ListOutgoingTypedLinksPaginatorName",
    "ListPolicyAttachmentsPaginatorName",
    "ListPublishedSchemaArnsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListTypedLinkFacetAttributesPaginatorName",
    "ListTypedLinkFacetNamesPaginatorName",
    "LookupPolicyPaginatorName",
    "ObjectType",
    "RangeMode",
    "RequiredAttributeBehavior",
    "RuleType",
    "UpdateActionType",
)


BatchReadExceptionType = Literal[
    "AccessDeniedException",
    "CannotListParentOfRootException",
    "DirectoryNotEnabledException",
    "FacetValidationException",
    "InternalServiceException",
    "InvalidArnException",
    "InvalidNextTokenException",
    "LimitExceededException",
    "NotIndexException",
    "NotNodeException",
    "NotPolicyException",
    "ResourceNotFoundException",
    "ValidationException",
]
ConsistencyLevel = Literal["EVENTUAL", "SERIALIZABLE"]
DirectoryState = Literal["DELETED", "DISABLED", "ENABLED"]
FacetAttributeType = Literal["BINARY", "BOOLEAN", "DATETIME", "NUMBER", "STRING", "VARIANT"]
FacetStyle = Literal["DYNAMIC", "STATIC"]
ListAppliedSchemaArnsPaginatorName = Literal["list_applied_schema_arns"]
ListAttachedIndicesPaginatorName = Literal["list_attached_indices"]
ListDevelopmentSchemaArnsPaginatorName = Literal["list_development_schema_arns"]
ListDirectoriesPaginatorName = Literal["list_directories"]
ListFacetAttributesPaginatorName = Literal["list_facet_attributes"]
ListFacetNamesPaginatorName = Literal["list_facet_names"]
ListIncomingTypedLinksPaginatorName = Literal["list_incoming_typed_links"]
ListIndexPaginatorName = Literal["list_index"]
ListManagedSchemaArnsPaginatorName = Literal["list_managed_schema_arns"]
ListObjectAttributesPaginatorName = Literal["list_object_attributes"]
ListObjectParentPathsPaginatorName = Literal["list_object_parent_paths"]
ListObjectPoliciesPaginatorName = Literal["list_object_policies"]
ListOutgoingTypedLinksPaginatorName = Literal["list_outgoing_typed_links"]
ListPolicyAttachmentsPaginatorName = Literal["list_policy_attachments"]
ListPublishedSchemaArnsPaginatorName = Literal["list_published_schema_arns"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTypedLinkFacetAttributesPaginatorName = Literal["list_typed_link_facet_attributes"]
ListTypedLinkFacetNamesPaginatorName = Literal["list_typed_link_facet_names"]
LookupPolicyPaginatorName = Literal["lookup_policy"]
ObjectType = Literal["INDEX", "LEAF_NODE", "NODE", "POLICY"]
RangeMode = Literal["EXCLUSIVE", "FIRST", "INCLUSIVE", "LAST", "LAST_BEFORE_MISSING_VALUES"]
RequiredAttributeBehavior = Literal["NOT_REQUIRED", "REQUIRED_ALWAYS"]
RuleType = Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"]
UpdateActionType = Literal["CREATE_OR_UPDATE", "DELETE"]
