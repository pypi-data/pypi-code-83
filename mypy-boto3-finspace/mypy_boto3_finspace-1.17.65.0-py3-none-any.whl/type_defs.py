"""
Type annotations for finspace service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/type_defs.html)

Usage::

    ```python
    from mypy_boto3_finspace.type_defs import CreateEnvironmentResponseTypeDef

    data: CreateEnvironmentResponseTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_finspace.literals import EnvironmentStatus, FederationMode

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEnvironmentResponseTypeDef",
    "EnvironmentTypeDef",
    "FederationParametersTypeDef",
    "GetEnvironmentResponseTypeDef",
    "ListEnvironmentsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateEnvironmentResponseTypeDef",
)


class CreateEnvironmentResponseTypeDef(TypedDict, total=False):
    environmentId: str
    environmentArn: str
    environmentUrl: str


class EnvironmentTypeDef(TypedDict, total=False):
    name: str
    environmentId: str
    awsAccountId: str
    status: EnvironmentStatus
    environmentUrl: str
    description: str
    environmentArn: str
    sageMakerStudioDomainUrl: str
    kmsKeyId: str
    dedicatedServiceAccountId: str
    federationMode: FederationMode
    federationParameters: "FederationParametersTypeDef"


class FederationParametersTypeDef(TypedDict, total=False):
    samlMetadataDocument: str
    samlMetadataURL: str
    applicationCallBackURL: str
    federationURN: str
    federationProviderName: str
    attributeMap: Dict[str, str]


class GetEnvironmentResponseTypeDef(TypedDict, total=False):
    environment: "EnvironmentTypeDef"


class ListEnvironmentsResponseTypeDef(TypedDict, total=False):
    environments: List["EnvironmentTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class UpdateEnvironmentResponseTypeDef(TypedDict, total=False):
    environment: "EnvironmentTypeDef"
