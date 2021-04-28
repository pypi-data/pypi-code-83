# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetOutputResult',
    'AwaitableGetOutputResult',
    'get_output',
]

@pulumi.output_type
class GetOutputResult:
    """
    An output object, containing all information associated with the named output. All outputs are contained under a streaming job.
    """
    def __init__(__self__, datasource=None, diagnostics=None, etag=None, id=None, name=None, serialization=None, size_window=None, time_window=None, type=None):
        if datasource and not isinstance(datasource, dict):
            raise TypeError("Expected argument 'datasource' to be a dict")
        pulumi.set(__self__, "datasource", datasource)
        if diagnostics and not isinstance(diagnostics, dict):
            raise TypeError("Expected argument 'diagnostics' to be a dict")
        pulumi.set(__self__, "diagnostics", diagnostics)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if serialization and not isinstance(serialization, dict):
            raise TypeError("Expected argument 'serialization' to be a dict")
        pulumi.set(__self__, "serialization", serialization)
        if size_window and not isinstance(size_window, float):
            raise TypeError("Expected argument 'size_window' to be a float")
        pulumi.set(__self__, "size_window", size_window)
        if time_window and not isinstance(time_window, str):
            raise TypeError("Expected argument 'time_window' to be a str")
        pulumi.set(__self__, "time_window", time_window)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def datasource(self) -> Optional[Any]:
        """
        Describes the data source that output will be written to. Required on PUT (CreateOrReplace) requests.
        """
        return pulumi.get(self, "datasource")

    @property
    @pulumi.getter
    def diagnostics(self) -> 'outputs.DiagnosticsResponse':
        """
        Describes conditions applicable to the Input, Output, or the job overall, that warrant customer attention.
        """
        return pulumi.get(self, "diagnostics")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        The current entity tag for the output. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def serialization(self) -> Optional[Any]:
        """
        Describes how data from an input is serialized or how data is serialized when written to an output. Required on PUT (CreateOrReplace) requests.
        """
        return pulumi.get(self, "serialization")

    @property
    @pulumi.getter(name="sizeWindow")
    def size_window(self) -> Optional[float]:
        return pulumi.get(self, "size_window")

    @property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> Optional[str]:
        return pulumi.get(self, "time_window")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetOutputResult(GetOutputResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOutputResult(
            datasource=self.datasource,
            diagnostics=self.diagnostics,
            etag=self.etag,
            id=self.id,
            name=self.name,
            serialization=self.serialization,
            size_window=self.size_window,
            time_window=self.time_window,
            type=self.type)


def get_output(job_name: Optional[str] = None,
               output_name: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOutputResult:
    """
    An output object, containing all information associated with the named output. All outputs are contained under a streaming job.


    :param str job_name: The name of the streaming job.
    :param str output_name: The name of the output.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['jobName'] = job_name
    __args__['outputName'] = output_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:streamanalytics/v20170401preview:getOutput', __args__, opts=opts, typ=GetOutputResult).value

    return AwaitableGetOutputResult(
        datasource=__ret__.datasource,
        diagnostics=__ret__.diagnostics,
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        serialization=__ret__.serialization,
        size_window=__ret__.size_window,
        time_window=__ret__.time_window,
        type=__ret__.type)
