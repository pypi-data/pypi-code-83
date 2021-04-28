# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ListNotebookProxyCredentialsResult',
    'AwaitableListNotebookProxyCredentialsResult',
    'list_notebook_proxy_credentials',
]

@pulumi.output_type
class ListNotebookProxyCredentialsResult:
    """
    Credentials and other properties of NotebookProxy resource
    """
    def __init__(__self__, hostname=None, primary_access_key=None, resource_id=None, secondary_access_key=None):
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if primary_access_key and not isinstance(primary_access_key, str):
            raise TypeError("Expected argument 'primary_access_key' to be a str")
        pulumi.set(__self__, "primary_access_key", primary_access_key)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if secondary_access_key and not isinstance(secondary_access_key, str):
            raise TypeError("Expected argument 'secondary_access_key' to be a str")
        pulumi.set(__self__, "secondary_access_key", secondary_access_key)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        """
        Hostname for the Notebook Proxy resource
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="primaryAccessKey")
    def primary_access_key(self) -> Optional[str]:
        """
        The primary key of the NotebookProxy resource.
        """
        return pulumi.get(self, "primary_access_key")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        Notebook Proxy resource id
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="secondaryAccessKey")
    def secondary_access_key(self) -> Optional[str]:
        """
        The secondary key of the NotebookProxy resource.
        """
        return pulumi.get(self, "secondary_access_key")


class AwaitableListNotebookProxyCredentialsResult(ListNotebookProxyCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListNotebookProxyCredentialsResult(
            hostname=self.hostname,
            primary_access_key=self.primary_access_key,
            resource_id=self.resource_id,
            secondary_access_key=self.secondary_access_key)


def list_notebook_proxy_credentials(resource_group_name: Optional[str] = None,
                                    resource_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListNotebookProxyCredentialsResult:
    """
    Credentials and other properties of NotebookProxy resource


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:notebooks/v20191011preview:listNotebookProxyCredentials', __args__, opts=opts, typ=ListNotebookProxyCredentialsResult).value

    return AwaitableListNotebookProxyCredentialsResult(
        hostname=__ret__.hostname,
        primary_access_key=__ret__.primary_access_key,
        resource_id=__ret__.resource_id,
        secondary_access_key=__ret__.secondary_access_key)
