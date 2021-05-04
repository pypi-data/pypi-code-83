"""
Type annotations for appintegrations service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appintegrations.type_defs import CreateEventIntegrationResponseTypeDef

    data: CreateEventIntegrationResponseTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEventIntegrationResponseTypeDef",
    "EventFilterTypeDef",
    "EventIntegrationAssociationTypeDef",
    "EventIntegrationTypeDef",
    "GetEventIntegrationResponseTypeDef",
    "ListEventIntegrationAssociationsResponseTypeDef",
    "ListEventIntegrationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
)


class CreateEventIntegrationResponseTypeDef(TypedDict, total=False):
    EventIntegrationArn: str


class EventFilterTypeDef(TypedDict):
    Source: str


class EventIntegrationAssociationTypeDef(TypedDict, total=False):
    EventIntegrationAssociationArn: str
    EventIntegrationAssociationId: str
    EventIntegrationName: str
    ClientId: str
    EventBridgeRuleName: str
    ClientAssociationMetadata: Dict[str, str]


class EventIntegrationTypeDef(TypedDict, total=False):
    EventIntegrationArn: str
    Name: str
    Description: str
    EventFilter: "EventFilterTypeDef"
    EventBridgeBus: str
    Tags: Dict[str, str]


class GetEventIntegrationResponseTypeDef(TypedDict, total=False):
    Name: str
    Description: str
    EventIntegrationArn: str
    EventBridgeBus: str
    EventFilter: "EventFilterTypeDef"
    Tags: Dict[str, str]


class ListEventIntegrationAssociationsResponseTypeDef(TypedDict, total=False):
    EventIntegrationAssociations: List["EventIntegrationAssociationTypeDef"]
    NextToken: str


class ListEventIntegrationsResponseTypeDef(TypedDict, total=False):
    EventIntegrations: List["EventIntegrationTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]
