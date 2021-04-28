# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'PrivateEndpointServiceConnectionStatus',
    'SkuName',
    'SkuTier',
]


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been approved, rejected or removed by the Relay Namespace owner.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class SkuName(str, Enum):
    """
    Name of this SKU.
    """
    STANDARD = "Standard"


class SkuTier(str, Enum):
    """
    The tier of this SKU.
    """
    STANDARD = "Standard"
