# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ManagedZoneDnssecConfigArgs',
    'ManagedZoneDnssecConfigDefaultKeySpecArgs',
    'ManagedZoneForwardingConfigArgs',
    'ManagedZoneForwardingConfigTargetNameServerArgs',
    'ManagedZonePeeringConfigArgs',
    'ManagedZonePeeringConfigTargetNetworkArgs',
    'ManagedZonePrivateVisibilityConfigArgs',
    'ManagedZonePrivateVisibilityConfigNetworkArgs',
    'ManagedZoneServiceDirectoryConfigArgs',
    'ManagedZoneServiceDirectoryConfigNamespaceArgs',
    'PolicyAlternativeNameServerConfigArgs',
    'PolicyAlternativeNameServerConfigTargetNameServerArgs',
    'PolicyNetworkArgs',
]

@pulumi.input_type
class ManagedZoneDnssecConfigArgs:
    def __init__(__self__, *,
                 default_key_specs: Optional[pulumi.Input[Sequence[pulumi.Input['ManagedZoneDnssecConfigDefaultKeySpecArgs']]]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 non_existence: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['ManagedZoneDnssecConfigDefaultKeySpecArgs']]] default_key_specs: Specifies parameters that will be used for generating initial DnsKeys
               for this ManagedZone. If you provide a spec for keySigning or zoneSigning,
               you must also provide one for the other.
               default_key_specs can only be updated when the state is `off`.
               Structure is documented below.
        :param pulumi.Input[str] kind: Identifies what kind of resource this is
        :param pulumi.Input[str] non_existence: Specifies the mechanism used to provide authenticated denial-of-existence responses.
               non_existence can only be updated when the state is `off`.
               Possible values are `nsec` and `nsec3`.
        :param pulumi.Input[str] state: Specifies whether DNSSEC is enabled, and what mode it is in
               Possible values are `off`, `on`, and `transfer`.
        """
        if default_key_specs is not None:
            pulumi.set(__self__, "default_key_specs", default_key_specs)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if non_existence is not None:
            pulumi.set(__self__, "non_existence", non_existence)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="defaultKeySpecs")
    def default_key_specs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ManagedZoneDnssecConfigDefaultKeySpecArgs']]]]:
        """
        Specifies parameters that will be used for generating initial DnsKeys
        for this ManagedZone. If you provide a spec for keySigning or zoneSigning,
        you must also provide one for the other.
        default_key_specs can only be updated when the state is `off`.
        Structure is documented below.
        """
        return pulumi.get(self, "default_key_specs")

    @default_key_specs.setter
    def default_key_specs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ManagedZoneDnssecConfigDefaultKeySpecArgs']]]]):
        pulumi.set(self, "default_key_specs", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Identifies what kind of resource this is
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="nonExistence")
    def non_existence(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the mechanism used to provide authenticated denial-of-existence responses.
        non_existence can only be updated when the state is `off`.
        Possible values are `nsec` and `nsec3`.
        """
        return pulumi.get(self, "non_existence")

    @non_existence.setter
    def non_existence(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "non_existence", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether DNSSEC is enabled, and what mode it is in
        Possible values are `off`, `on`, and `transfer`.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class ManagedZoneDnssecConfigDefaultKeySpecArgs:
    def __init__(__self__, *,
                 algorithm: Optional[pulumi.Input[str]] = None,
                 key_length: Optional[pulumi.Input[int]] = None,
                 key_type: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] algorithm: String mnemonic specifying the DNSSEC algorithm of this key
               Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
        :param pulumi.Input[int] key_length: Length of the keys in bits
        :param pulumi.Input[str] key_type: Specifies whether this is a key signing key (KSK) or a zone
               signing key (ZSK). Key signing keys have the Secure Entry
               Point flag set and, when active, will only be used to sign
               resource record sets of type DNSKEY. Zone signing keys do
               not have the Secure Entry Point flag set and will be used
               to sign all other types of resource record sets.
               Possible values are `keySigning` and `zoneSigning`.
        :param pulumi.Input[str] kind: Identifies what kind of resource this is
        """
        if algorithm is not None:
            pulumi.set(__self__, "algorithm", algorithm)
        if key_length is not None:
            pulumi.set(__self__, "key_length", key_length)
        if key_type is not None:
            pulumi.set(__self__, "key_type", key_type)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)

    @property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input[str]]:
        """
        String mnemonic specifying the DNSSEC algorithm of this key
        Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
        """
        return pulumi.get(self, "algorithm")

    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "algorithm", value)

    @property
    @pulumi.getter(name="keyLength")
    def key_length(self) -> Optional[pulumi.Input[int]]:
        """
        Length of the keys in bits
        """
        return pulumi.get(self, "key_length")

    @key_length.setter
    def key_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "key_length", value)

    @property
    @pulumi.getter(name="keyType")
    def key_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether this is a key signing key (KSK) or a zone
        signing key (ZSK). Key signing keys have the Secure Entry
        Point flag set and, when active, will only be used to sign
        resource record sets of type DNSKEY. Zone signing keys do
        not have the Secure Entry Point flag set and will be used
        to sign all other types of resource record sets.
        Possible values are `keySigning` and `zoneSigning`.
        """
        return pulumi.get(self, "key_type")

    @key_type.setter
    def key_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_type", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Identifies what kind of resource this is
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)


@pulumi.input_type
class ManagedZoneForwardingConfigArgs:
    def __init__(__self__, *,
                 target_name_servers: pulumi.Input[Sequence[pulumi.Input['ManagedZoneForwardingConfigTargetNameServerArgs']]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input['ManagedZoneForwardingConfigTargetNameServerArgs']]] target_name_servers: List of target name servers to forward to. Cloud DNS will
               select the best available name server if more than
               one target is given.
               Structure is documented below.
        """
        pulumi.set(__self__, "target_name_servers", target_name_servers)

    @property
    @pulumi.getter(name="targetNameServers")
    def target_name_servers(self) -> pulumi.Input[Sequence[pulumi.Input['ManagedZoneForwardingConfigTargetNameServerArgs']]]:
        """
        List of target name servers to forward to. Cloud DNS will
        select the best available name server if more than
        one target is given.
        Structure is documented below.
        """
        return pulumi.get(self, "target_name_servers")

    @target_name_servers.setter
    def target_name_servers(self, value: pulumi.Input[Sequence[pulumi.Input['ManagedZoneForwardingConfigTargetNameServerArgs']]]):
        pulumi.set(self, "target_name_servers", value)


@pulumi.input_type
class ManagedZoneForwardingConfigTargetNameServerArgs:
    def __init__(__self__, *,
                 ipv4_address: pulumi.Input[str],
                 forwarding_path: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] ipv4_address: IPv4 address of a target name server.
        :param pulumi.Input[str] forwarding_path: Forwarding path for this TargetNameServer. If unset or `default` Cloud DNS will make forwarding
               decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go
               to the Internet. When set to `private`, Cloud DNS will always send queries through VPC for this target
               Possible values are `default` and `private`.
        """
        pulumi.set(__self__, "ipv4_address", ipv4_address)
        if forwarding_path is not None:
            pulumi.set(__self__, "forwarding_path", forwarding_path)

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> pulumi.Input[str]:
        """
        IPv4 address of a target name server.
        """
        return pulumi.get(self, "ipv4_address")

    @ipv4_address.setter
    def ipv4_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "ipv4_address", value)

    @property
    @pulumi.getter(name="forwardingPath")
    def forwarding_path(self) -> Optional[pulumi.Input[str]]:
        """
        Forwarding path for this TargetNameServer. If unset or `default` Cloud DNS will make forwarding
        decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go
        to the Internet. When set to `private`, Cloud DNS will always send queries through VPC for this target
        Possible values are `default` and `private`.
        """
        return pulumi.get(self, "forwarding_path")

    @forwarding_path.setter
    def forwarding_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "forwarding_path", value)


@pulumi.input_type
class ManagedZonePeeringConfigArgs:
    def __init__(__self__, *,
                 target_network: pulumi.Input['ManagedZonePeeringConfigTargetNetworkArgs']):
        """
        :param pulumi.Input['ManagedZonePeeringConfigTargetNetworkArgs'] target_network: The network with which to peer.
               Structure is documented below.
        """
        pulumi.set(__self__, "target_network", target_network)

    @property
    @pulumi.getter(name="targetNetwork")
    def target_network(self) -> pulumi.Input['ManagedZonePeeringConfigTargetNetworkArgs']:
        """
        The network with which to peer.
        Structure is documented below.
        """
        return pulumi.get(self, "target_network")

    @target_network.setter
    def target_network(self, value: pulumi.Input['ManagedZonePeeringConfigTargetNetworkArgs']):
        pulumi.set(self, "target_network", value)


@pulumi.input_type
class ManagedZonePeeringConfigTargetNetworkArgs:
    def __init__(__self__, *,
                 network_url: pulumi.Input[str]):
        """
        :param pulumi.Input[str] network_url: The id or fully qualified URL of the VPC network to forward queries to.
               This should be formatted like `projects/{project}/global/networks/{network}` or
               `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
        """
        pulumi.set(__self__, "network_url", network_url)

    @property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> pulumi.Input[str]:
        """
        The id or fully qualified URL of the VPC network to forward queries to.
        This should be formatted like `projects/{project}/global/networks/{network}` or
        `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
        """
        return pulumi.get(self, "network_url")

    @network_url.setter
    def network_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_url", value)


@pulumi.input_type
class ManagedZonePrivateVisibilityConfigArgs:
    def __init__(__self__, *,
                 networks: pulumi.Input[Sequence[pulumi.Input['ManagedZonePrivateVisibilityConfigNetworkArgs']]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input['ManagedZonePrivateVisibilityConfigNetworkArgs']]] networks: The list of VPC networks that can see this zone. Structure is documented below.
        """
        pulumi.set(__self__, "networks", networks)

    @property
    @pulumi.getter
    def networks(self) -> pulumi.Input[Sequence[pulumi.Input['ManagedZonePrivateVisibilityConfigNetworkArgs']]]:
        """
        The list of VPC networks that can see this zone. Structure is documented below.
        """
        return pulumi.get(self, "networks")

    @networks.setter
    def networks(self, value: pulumi.Input[Sequence[pulumi.Input['ManagedZonePrivateVisibilityConfigNetworkArgs']]]):
        pulumi.set(self, "networks", value)


@pulumi.input_type
class ManagedZonePrivateVisibilityConfigNetworkArgs:
    def __init__(__self__, *,
                 network_url: pulumi.Input[str]):
        """
        :param pulumi.Input[str] network_url: The id or fully qualified URL of the VPC network to forward queries to.
               This should be formatted like `projects/{project}/global/networks/{network}` or
               `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
        """
        pulumi.set(__self__, "network_url", network_url)

    @property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> pulumi.Input[str]:
        """
        The id or fully qualified URL of the VPC network to forward queries to.
        This should be formatted like `projects/{project}/global/networks/{network}` or
        `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
        """
        return pulumi.get(self, "network_url")

    @network_url.setter
    def network_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_url", value)


@pulumi.input_type
class ManagedZoneServiceDirectoryConfigArgs:
    def __init__(__self__, *,
                 namespace: pulumi.Input['ManagedZoneServiceDirectoryConfigNamespaceArgs']):
        """
        :param pulumi.Input['ManagedZoneServiceDirectoryConfigNamespaceArgs'] namespace: The namespace associated with the zone.
               Structure is documented below.
        """
        pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input['ManagedZoneServiceDirectoryConfigNamespaceArgs']:
        """
        The namespace associated with the zone.
        Structure is documented below.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input['ManagedZoneServiceDirectoryConfigNamespaceArgs']):
        pulumi.set(self, "namespace", value)


@pulumi.input_type
class ManagedZoneServiceDirectoryConfigNamespaceArgs:
    def __init__(__self__, *,
                 namespace_url: pulumi.Input[str]):
        """
        :param pulumi.Input[str] namespace_url: The fully qualified or partial URL of the service directory namespace that should be
               associated with the zone. This should be formatted like
               `https://servicedirectory.googleapis.com/v1/projects/{project}/locations/{location}/namespaces/{namespace_id}`
               or simply `projects/{project}/locations/{location}/namespaces/{namespace_id}`
               Ignored for `public` visibility zones.
        """
        pulumi.set(__self__, "namespace_url", namespace_url)

    @property
    @pulumi.getter(name="namespaceUrl")
    def namespace_url(self) -> pulumi.Input[str]:
        """
        The fully qualified or partial URL of the service directory namespace that should be
        associated with the zone. This should be formatted like
        `https://servicedirectory.googleapis.com/v1/projects/{project}/locations/{location}/namespaces/{namespace_id}`
        or simply `projects/{project}/locations/{location}/namespaces/{namespace_id}`
        Ignored for `public` visibility zones.
        """
        return pulumi.get(self, "namespace_url")

    @namespace_url.setter
    def namespace_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_url", value)


@pulumi.input_type
class PolicyAlternativeNameServerConfigArgs:
    def __init__(__self__, *,
                 target_name_servers: pulumi.Input[Sequence[pulumi.Input['PolicyAlternativeNameServerConfigTargetNameServerArgs']]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input['PolicyAlternativeNameServerConfigTargetNameServerArgs']]] target_name_servers: Sets an alternative name server for the associated networks. When specified,
               all DNS queries are forwarded to a name server that you choose. Names such as .internal
               are not available when an alternative name server is specified.
               Structure is documented below.
        """
        pulumi.set(__self__, "target_name_servers", target_name_servers)

    @property
    @pulumi.getter(name="targetNameServers")
    def target_name_servers(self) -> pulumi.Input[Sequence[pulumi.Input['PolicyAlternativeNameServerConfigTargetNameServerArgs']]]:
        """
        Sets an alternative name server for the associated networks. When specified,
        all DNS queries are forwarded to a name server that you choose. Names such as .internal
        are not available when an alternative name server is specified.
        Structure is documented below.
        """
        return pulumi.get(self, "target_name_servers")

    @target_name_servers.setter
    def target_name_servers(self, value: pulumi.Input[Sequence[pulumi.Input['PolicyAlternativeNameServerConfigTargetNameServerArgs']]]):
        pulumi.set(self, "target_name_servers", value)


@pulumi.input_type
class PolicyAlternativeNameServerConfigTargetNameServerArgs:
    def __init__(__self__, *,
                 ipv4_address: pulumi.Input[str],
                 forwarding_path: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] ipv4_address: IPv4 address to forward to.
        :param pulumi.Input[str] forwarding_path: Forwarding path for this TargetNameServer. If unset or `default` Cloud DNS will make forwarding
               decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go
               to the Internet. When set to `private`, Cloud DNS will always send queries through VPC for this target
               Possible values are `default` and `private`.
        """
        pulumi.set(__self__, "ipv4_address", ipv4_address)
        if forwarding_path is not None:
            pulumi.set(__self__, "forwarding_path", forwarding_path)

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> pulumi.Input[str]:
        """
        IPv4 address to forward to.
        """
        return pulumi.get(self, "ipv4_address")

    @ipv4_address.setter
    def ipv4_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "ipv4_address", value)

    @property
    @pulumi.getter(name="forwardingPath")
    def forwarding_path(self) -> Optional[pulumi.Input[str]]:
        """
        Forwarding path for this TargetNameServer. If unset or `default` Cloud DNS will make forwarding
        decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go
        to the Internet. When set to `private`, Cloud DNS will always send queries through VPC for this target
        Possible values are `default` and `private`.
        """
        return pulumi.get(self, "forwarding_path")

    @forwarding_path.setter
    def forwarding_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "forwarding_path", value)


@pulumi.input_type
class PolicyNetworkArgs:
    def __init__(__self__, *,
                 network_url: pulumi.Input[str]):
        """
        :param pulumi.Input[str] network_url: The id or fully qualified URL of the VPC network to forward queries to.
               This should be formatted like `projects/{project}/global/networks/{network}` or
               `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
        """
        pulumi.set(__self__, "network_url", network_url)

    @property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> pulumi.Input[str]:
        """
        The id or fully qualified URL of the VPC network to forward queries to.
        This should be formatted like `projects/{project}/global/networks/{network}` or
        `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
        """
        return pulumi.get(self, "network_url")

    @network_url.setter
    def network_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_url", value)


