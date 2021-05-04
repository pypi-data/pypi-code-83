"""
Type annotations for transfer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_transfer.type_defs import CreateServerResponseTypeDef

    data: CreateServerResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_transfer.literals import (
    Domain,
    EndpointType,
    HomeDirectoryType,
    IdentityProviderType,
    ProtocolType,
    State,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateServerResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DescribeSecurityPolicyResponseTypeDef",
    "DescribeServerResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "DescribedSecurityPolicyTypeDef",
    "DescribedServerTypeDef",
    "DescribedUserTypeDef",
    "EndpointDetailsTypeDef",
    "HomeDirectoryMapEntryTypeDef",
    "IdentityProviderDetailsTypeDef",
    "ImportSshPublicKeyResponseTypeDef",
    "ListSecurityPoliciesResponseTypeDef",
    "ListServersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersResponseTypeDef",
    "ListedServerTypeDef",
    "ListedUserTypeDef",
    "PaginatorConfigTypeDef",
    "PosixProfileTypeDef",
    "SshPublicKeyTypeDef",
    "TagTypeDef",
    "TestIdentityProviderResponseTypeDef",
    "UpdateServerResponseTypeDef",
    "UpdateUserResponseTypeDef",
)


class CreateServerResponseTypeDef(TypedDict):
    ServerId: str


class CreateUserResponseTypeDef(TypedDict):
    ServerId: str
    UserName: str


class DescribeSecurityPolicyResponseTypeDef(TypedDict):
    SecurityPolicy: "DescribedSecurityPolicyTypeDef"


class DescribeServerResponseTypeDef(TypedDict):
    Server: "DescribedServerTypeDef"


class DescribeUserResponseTypeDef(TypedDict):
    ServerId: str
    User: "DescribedUserTypeDef"


class _RequiredDescribedSecurityPolicyTypeDef(TypedDict):
    SecurityPolicyName: str


class DescribedSecurityPolicyTypeDef(_RequiredDescribedSecurityPolicyTypeDef, total=False):
    Fips: bool
    SshCiphers: List[str]
    SshKexs: List[str]
    SshMacs: List[str]
    TlsCiphers: List[str]


class _RequiredDescribedServerTypeDef(TypedDict):
    Arn: str


class DescribedServerTypeDef(_RequiredDescribedServerTypeDef, total=False):
    Certificate: str
    Domain: Domain
    EndpointDetails: "EndpointDetailsTypeDef"
    EndpointType: EndpointType
    HostKeyFingerprint: str
    IdentityProviderDetails: "IdentityProviderDetailsTypeDef"
    IdentityProviderType: IdentityProviderType
    LoggingRole: str
    Protocols: List[ProtocolType]
    SecurityPolicyName: str
    ServerId: str
    State: State
    Tags: List["TagTypeDef"]
    UserCount: int


class _RequiredDescribedUserTypeDef(TypedDict):
    Arn: str


class DescribedUserTypeDef(_RequiredDescribedUserTypeDef, total=False):
    HomeDirectory: str
    HomeDirectoryMappings: List["HomeDirectoryMapEntryTypeDef"]
    HomeDirectoryType: HomeDirectoryType
    Policy: str
    PosixProfile: "PosixProfileTypeDef"
    Role: str
    SshPublicKeys: List["SshPublicKeyTypeDef"]
    Tags: List["TagTypeDef"]
    UserName: str


class EndpointDetailsTypeDef(TypedDict, total=False):
    AddressAllocationIds: List[str]
    SubnetIds: List[str]
    VpcEndpointId: str
    VpcId: str
    SecurityGroupIds: List[str]


class HomeDirectoryMapEntryTypeDef(TypedDict):
    Entry: str
    Target: str


class IdentityProviderDetailsTypeDef(TypedDict, total=False):
    Url: str
    InvocationRole: str


class ImportSshPublicKeyResponseTypeDef(TypedDict):
    ServerId: str
    SshPublicKeyId: str
    UserName: str


class _RequiredListSecurityPoliciesResponseTypeDef(TypedDict):
    SecurityPolicyNames: List[str]


class ListSecurityPoliciesResponseTypeDef(
    _RequiredListSecurityPoliciesResponseTypeDef, total=False
):
    NextToken: str


class _RequiredListServersResponseTypeDef(TypedDict):
    Servers: List["ListedServerTypeDef"]


class ListServersResponseTypeDef(_RequiredListServersResponseTypeDef, total=False):
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Arn: str
    NextToken: str
    Tags: List["TagTypeDef"]


class _RequiredListUsersResponseTypeDef(TypedDict):
    ServerId: str
    Users: List["ListedUserTypeDef"]


class ListUsersResponseTypeDef(_RequiredListUsersResponseTypeDef, total=False):
    NextToken: str


class _RequiredListedServerTypeDef(TypedDict):
    Arn: str


class ListedServerTypeDef(_RequiredListedServerTypeDef, total=False):
    Domain: Domain
    IdentityProviderType: IdentityProviderType
    EndpointType: EndpointType
    LoggingRole: str
    ServerId: str
    State: State
    UserCount: int


class _RequiredListedUserTypeDef(TypedDict):
    Arn: str


class ListedUserTypeDef(_RequiredListedUserTypeDef, total=False):
    HomeDirectory: str
    HomeDirectoryType: HomeDirectoryType
    Role: str
    SshPublicKeyCount: int
    UserName: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredPosixProfileTypeDef(TypedDict):
    Uid: int
    Gid: int


class PosixProfileTypeDef(_RequiredPosixProfileTypeDef, total=False):
    SecondaryGids: List[int]


class SshPublicKeyTypeDef(TypedDict):
    DateImported: datetime
    SshPublicKeyBody: str
    SshPublicKeyId: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class _RequiredTestIdentityProviderResponseTypeDef(TypedDict):
    StatusCode: int
    Url: str


class TestIdentityProviderResponseTypeDef(
    _RequiredTestIdentityProviderResponseTypeDef, total=False
):
    Response: str
    Message: str


class UpdateServerResponseTypeDef(TypedDict):
    ServerId: str


class UpdateUserResponseTypeDef(TypedDict):
    ServerId: str
    UserName: str
