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
    'GetVideoResult',
    'AwaitableGetVideoResult',
    'get_video',
]

@pulumi.output_type
class GetVideoResult:
    """
    The representation of a single video in a Video Analyzer account.
    """
    def __init__(__self__, description=None, flags=None, id=None, media_info=None, name=None, streaming=None, system_data=None, title=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if flags and not isinstance(flags, dict):
            raise TypeError("Expected argument 'flags' to be a dict")
        pulumi.set(__self__, "flags", flags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if media_info and not isinstance(media_info, dict):
            raise TypeError("Expected argument 'media_info' to be a dict")
        pulumi.set(__self__, "media_info", media_info)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if streaming and not isinstance(streaming, dict):
            raise TypeError("Expected argument 'streaming' to be a dict")
        pulumi.set(__self__, "streaming", streaming)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Optional video description provided by the user. Value can be up to 2048 characters long.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def flags(self) -> 'outputs.VideoFlagsResponse':
        """
        Video flags contain information about the available video actions and its dynamic properties based on the current video state.
        """
        return pulumi.get(self, "flags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="mediaInfo")
    def media_info(self) -> 'outputs.VideoMediaInfoResponse':
        """
        Contains information about the video and audio content.
        """
        return pulumi.get(self, "media_info")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def streaming(self) -> 'outputs.VideoStreamingResponse':
        """
        Video streaming holds information about video streaming URLs.
        """
        return pulumi.get(self, "streaming")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def title(self) -> Optional[str]:
        """
        Optional video title provided by the user. Value can be up to 256 characters long.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetVideoResult(GetVideoResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVideoResult(
            description=self.description,
            flags=self.flags,
            id=self.id,
            media_info=self.media_info,
            name=self.name,
            streaming=self.streaming,
            system_data=self.system_data,
            title=self.title,
            type=self.type)


def get_video(account_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              video_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVideoResult:
    """
    The representation of a single video in a Video Analyzer account.


    :param str account_name: The Azure Video Analyzer account name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str video_name: The name of the video to retrieve.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['videoName'] = video_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:videoanalyzer/v20210501preview:getVideo', __args__, opts=opts, typ=GetVideoResult).value

    return AwaitableGetVideoResult(
        description=__ret__.description,
        flags=__ret__.flags,
        id=__ret__.id,
        media_info=__ret__.media_info,
        name=__ret__.name,
        streaming=__ret__.streaming,
        system_data=__ret__.system_data,
        title=__ret__.title,
        type=__ret__.type)
