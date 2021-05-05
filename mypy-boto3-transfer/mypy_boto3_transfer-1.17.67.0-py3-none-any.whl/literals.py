"""
Type annotations for transfer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/literals.html)

Usage::

    ```python
    from mypy_boto3_transfer.literals import Domain

    data: Domain = "EFS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "Domain",
    "EndpointType",
    "HomeDirectoryType",
    "IdentityProviderType",
    "ListServersPaginatorName",
    "ProtocolType",
    "State",
)


Domain = Literal["EFS", "S3"]
EndpointType = Literal["PUBLIC", "VPC", "VPC_ENDPOINT"]
HomeDirectoryType = Literal["LOGICAL", "PATH"]
IdentityProviderType = Literal["API_GATEWAY", "SERVICE_MANAGED"]
ListServersPaginatorName = Literal["list_servers"]
ProtocolType = Literal["FTP", "FTPS", "SFTP"]
State = Literal["OFFLINE", "ONLINE", "STARTING", "START_FAILED", "STOPPING", "STOP_FAILED"]
