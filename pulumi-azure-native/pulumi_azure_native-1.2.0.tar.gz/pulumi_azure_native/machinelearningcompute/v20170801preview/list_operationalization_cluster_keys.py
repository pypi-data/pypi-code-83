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
    'ListOperationalizationClusterKeysResult',
    'AwaitableListOperationalizationClusterKeysResult',
    'list_operationalization_cluster_keys',
]

@pulumi.output_type
class ListOperationalizationClusterKeysResult:
    """
    Credentials to resources in the cluster.
    """
    def __init__(__self__, app_insights=None, container_registry=None, container_service=None, service_auth_configuration=None, ssl_configuration=None, storage_account=None):
        if app_insights and not isinstance(app_insights, dict):
            raise TypeError("Expected argument 'app_insights' to be a dict")
        pulumi.set(__self__, "app_insights", app_insights)
        if container_registry and not isinstance(container_registry, dict):
            raise TypeError("Expected argument 'container_registry' to be a dict")
        pulumi.set(__self__, "container_registry", container_registry)
        if container_service and not isinstance(container_service, dict):
            raise TypeError("Expected argument 'container_service' to be a dict")
        pulumi.set(__self__, "container_service", container_service)
        if service_auth_configuration and not isinstance(service_auth_configuration, dict):
            raise TypeError("Expected argument 'service_auth_configuration' to be a dict")
        pulumi.set(__self__, "service_auth_configuration", service_auth_configuration)
        if ssl_configuration and not isinstance(ssl_configuration, dict):
            raise TypeError("Expected argument 'ssl_configuration' to be a dict")
        pulumi.set(__self__, "ssl_configuration", ssl_configuration)
        if storage_account and not isinstance(storage_account, dict):
            raise TypeError("Expected argument 'storage_account' to be a dict")
        pulumi.set(__self__, "storage_account", storage_account)

    @property
    @pulumi.getter(name="appInsights")
    def app_insights(self) -> Optional['outputs.AppInsightsCredentialsResponse']:
        """
        Credentials for Azure AppInsights.
        """
        return pulumi.get(self, "app_insights")

    @property
    @pulumi.getter(name="containerRegistry")
    def container_registry(self) -> Optional['outputs.ContainerRegistryCredentialsResponse']:
        """
        Credentials for Azure Container Registry.
        """
        return pulumi.get(self, "container_registry")

    @property
    @pulumi.getter(name="containerService")
    def container_service(self) -> Optional['outputs.ContainerServiceCredentialsResponse']:
        """
        Credentials for Azure Container Service.
        """
        return pulumi.get(self, "container_service")

    @property
    @pulumi.getter(name="serviceAuthConfiguration")
    def service_auth_configuration(self) -> Optional['outputs.ServiceAuthConfigurationResponse']:
        """
        Global authorization keys for all user services deployed in cluster. These are used if the service does not have auth keys.
        """
        return pulumi.get(self, "service_auth_configuration")

    @property
    @pulumi.getter(name="sslConfiguration")
    def ssl_configuration(self) -> Optional['outputs.SslConfigurationResponse']:
        """
        The SSL configuration for the services.
        """
        return pulumi.get(self, "ssl_configuration")

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> Optional['outputs.StorageAccountCredentialsResponse']:
        """
        Credentials for the Storage Account.
        """
        return pulumi.get(self, "storage_account")


class AwaitableListOperationalizationClusterKeysResult(ListOperationalizationClusterKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListOperationalizationClusterKeysResult(
            app_insights=self.app_insights,
            container_registry=self.container_registry,
            container_service=self.container_service,
            service_auth_configuration=self.service_auth_configuration,
            ssl_configuration=self.ssl_configuration,
            storage_account=self.storage_account)


def list_operationalization_cluster_keys(cluster_name: Optional[str] = None,
                                         resource_group_name: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListOperationalizationClusterKeysResult:
    """
    Credentials to resources in the cluster.


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: Name of the resource group in which the cluster is located.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningcompute/v20170801preview:listOperationalizationClusterKeys', __args__, opts=opts, typ=ListOperationalizationClusterKeysResult).value

    return AwaitableListOperationalizationClusterKeysResult(
        app_insights=__ret__.app_insights,
        container_registry=__ret__.container_registry,
        container_service=__ret__.container_service,
        service_auth_configuration=__ret__.service_auth_configuration,
        ssl_configuration=__ret__.ssl_configuration,
        storage_account=__ret__.storage_account)
