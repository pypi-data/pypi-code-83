'''
# AWS::GlobalAccelerator Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

## Introduction

AWS Global Accelerator (AGA) is a service that improves the availability and
performance of your applications with local or global users.

It intercepts your user's network connection at an edge location close to
them, and routes it to one of potentially multiple, redundant backends across
the more reliable and less congested AWS global network.

AGA can be used to route traffic to Application Load Balancers, Network Load
Balancers, EC2 Instances and Elastic IP Addresses.

For more information, see the [AWS Global
Accelerator Developer Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GlobalAccelerator.html).

## Example

Here's an example that sets up a Global Accelerator for two Application Load
Balancers in two different AWS Regions:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk import aws_globalaccelerator as globalaccelerator
from aws_cdk import aws_globalaccelerator_endpoints as ga_endpoints
from aws_cdk import aws_elasticloadbalancingv2 as elbv2


# Create an Accelerator
accelerator = globalaccelerator.Accelerator(stack, "Accelerator")

# Create a Listener
listener = accelerator.add_listener("Listener",
    port_ranges=[PortRange(from_port=80), PortRange(from_port=443)
    ]
)

# Import the Load Balancers
nlb1 = elbv2.NetworkLoadBalancer.from_network_load_balancer_attributes(stack, "NLB1",
    load_balancer_arn="arn:aws:elasticloadbalancing:us-west-2:111111111111:loadbalancer/app/my-load-balancer1/e16bef66805b"
)
nlb2 = elbv2.NetworkLoadBalancer.from_network_load_balancer_attributes(stack, "NLB2",
    load_balancer_arn="arn:aws:elasticloadbalancing:ap-south-1:111111111111:loadbalancer/app/my-load-balancer2/5513dc2ea8a1"
)

# Add one EndpointGroup for each Region we are targeting
listener.add_endpoint_group("Group1",
    endpoints=[ga_endpoints.NetworkLoadBalancerEndpoint(nlb1)]
)
listener.add_endpoint_group("Group2",
    # Imported load balancers automatically calculate their Region from the ARN.
    # If you are load balancing to other resources, you must also pass a `region`
    # parameter here.
    endpoints=[ga_endpoints.NetworkLoadBalancerEndpoint(nlb2)]
)
```

## Concepts

The **Accelerator** construct defines a Global Accelerator resource.

An Accelerator includes one or more **Listeners** that accepts inbound
connections on one or more ports.

Each Listener has one or more **Endpoint Groups**, representing multiple
geographically distributed copies of your application. There is one Endpoint
Group per Region, and user traffic is routed to the closest Region by default.

An Endpoint Group consists of one or more **Endpoints**, which is where the
user traffic coming in on the Listener is ultimately sent. The Endpoint port
used is the same as the traffic came in on at the Listener, unless overridden.

## Types of Endpoints

There are 4 types of Endpoints, and they can be found in the
`@aws-cdk/aws-globalaccelerator-endpoints` package:

* Application Load Balancers
* Network Load Balancers
* EC2 Instances
* Elastic IP Addresses

### Application Load Balancers

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
alb = elbv2.ApplicationLoadBalancer(...)

listener.add_endpoint_group("Group",
    endpoints=[
        ga_endpoints.ApplicationLoadBalancerEndpoint(alb,
            weight=128,
            preserve_client_ip=True
        )
    ]
)
```

### Network Load Balancers

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
nlb = elbv2.NetworkLoadBalancer(...)

listener.add_endpoint_group("Group",
    endpoints=[
        ga_endpoints.NetworkLoadBalancerEndpoint(nlb,
            weight=128
        )
    ]
)
```

### EC2 Instances

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
instance = ec2.instance(...)

listener.add_endpoint_group("Group",
    endpoints=[
        ga_endpoints.InstanceEndpoint(instance,
            weight=128,
            preserve_client_ip=True
        )
    ]
)
```

### Elastic IP Addresses

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
eip = ec2.CfnEIP(...)

listener.add_endpoint_group("Group",
    endpoints=[
        ga_endpoints.CfnEipEndpoint(eip,
            weight=128
        )
    ]
)
```

## Client IP Address Preservation and Security Groups

When using the `preserveClientIp` feature, AGA creates
**Elastic Network Interfaces** (ENIs) in your AWS account, that are
associated with a Security Group AGA creates for you. You can use the
security group created by AGA as a source group in other security groups
(such as those for EC2 instances or Elastic Load Balancers), if you want to
restrict incoming traffic to the AGA security group rules.

AGA creates a specific security group called `GlobalAccelerator` for each VPC
it has an ENI in (this behavior can not be changed). CloudFormation doesn't
support referencing the security group created by AGA, but this construct
library comes with a custom resource that enables you to reference the AGA
security group.

Call `endpointGroup.connectionsPeer()` to obtain a reference to the Security Group
which you can use in connection rules. You must pass a reference to the VPC in whose
context the security group will be looked up. Example:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# ...

# Non-open ALB
alb = elbv2.ApplicationLoadBalancer(stack, "ALB")

endpoint_group = listener.add_endpoint_group("Group",
    endpoints=[
        ga_endpoints.ApplicationLoadBalancerEndpoint(alb,
            preserve_client_ips=True
        )
    ]
)

# Remember that there is only one AGA security group per VPC.
aga_sg = endpoint_group.connections_peer("GlobalAcceleratorSG", vpc)

# Allow connections from the AGA to the ALB
alb.connections.allow_from(aga_sg, Port.tcp(443))
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_ec2 import IPeer as _IPeer_cf58db9a, IVpc as _IVpc_f30d5663


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.AcceleratorAttributes",
    jsii_struct_bases=[],
    name_mapping={"accelerator_arn": "acceleratorArn", "dns_name": "dnsName"},
)
class AcceleratorAttributes:
    def __init__(
        self,
        *,
        accelerator_arn: builtins.str,
        dns_name: builtins.str,
    ) -> None:
        '''(experimental) Attributes required to import an existing accelerator to the stack.

        :param accelerator_arn: (experimental) The ARN of the accelerator.
        :param dns_name: (experimental) The DNS name of the accelerator.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "accelerator_arn": accelerator_arn,
            "dns_name": dns_name,
        }

    @builtins.property
    def accelerator_arn(self) -> builtins.str:
        '''(experimental) The ARN of the accelerator.

        :stability: experimental
        '''
        result = self._values.get("accelerator_arn")
        assert result is not None, "Required property 'accelerator_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_name(self) -> builtins.str:
        '''(experimental) The DNS name of the accelerator.

        :stability: experimental
        '''
        result = self._values.get("dns_name")
        assert result is not None, "Required property 'dns_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcceleratorAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.AcceleratorProps",
    jsii_struct_bases=[],
    name_mapping={"accelerator_name": "acceleratorName", "enabled": "enabled"},
)
class AcceleratorProps:
    def __init__(
        self,
        *,
        accelerator_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Construct properties of the Accelerator.

        :param accelerator_name: (experimental) The name of the accelerator. Default: - resource ID
        :param enabled: (experimental) Indicates whether the accelerator is enabled. Default: true

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if accelerator_name is not None:
            self._values["accelerator_name"] = accelerator_name
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def accelerator_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the accelerator.

        :default: - resource ID

        :stability: experimental
        '''
        result = self._values.get("accelerator_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether the accelerator is enabled.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcceleratorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAccelerator(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnAccelerator",
):
    '''A CloudFormation ``AWS::GlobalAccelerator::Accelerator``.

    :cloudformationResource: AWS::GlobalAccelerator::Accelerator
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::GlobalAccelerator::Accelerator``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::GlobalAccelerator::Accelerator.Name``.
        :param enabled: ``AWS::GlobalAccelerator::Accelerator.Enabled``.
        :param ip_addresses: ``AWS::GlobalAccelerator::Accelerator.IpAddresses``.
        :param ip_address_type: ``AWS::GlobalAccelerator::Accelerator.IpAddressType``.
        :param tags: ``AWS::GlobalAccelerator::Accelerator.Tags``.
        '''
        props = CfnAcceleratorProps(
            name=name,
            enabled=enabled,
            ip_addresses=ip_addresses,
            ip_address_type=ip_address_type,
            tags=tags,
        )

        jsii.create(CfnAccelerator, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAcceleratorArn")
    def attr_accelerator_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AcceleratorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAcceleratorArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDnsName")
    def attr_dns_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: DnsName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDnsName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::GlobalAccelerator::Accelerator.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::GlobalAccelerator::Accelerator.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::GlobalAccelerator::Accelerator.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::GlobalAccelerator::Accelerator.IpAddresses``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-ipaddresses
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipAddresses"))

    @ip_addresses.setter
    def ip_addresses(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "ipAddresses", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ipAddressType")
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::GlobalAccelerator::Accelerator.IpAddressType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-ipaddresstype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressType"))

    @ip_address_type.setter
    def ip_address_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "ipAddressType", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnAcceleratorProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "enabled": "enabled",
        "ip_addresses": "ipAddresses",
        "ip_address_type": "ipAddressType",
        "tags": "tags",
    },
)
class CfnAcceleratorProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::GlobalAccelerator::Accelerator``.

        :param name: ``AWS::GlobalAccelerator::Accelerator.Name``.
        :param enabled: ``AWS::GlobalAccelerator::Accelerator.Enabled``.
        :param ip_addresses: ``AWS::GlobalAccelerator::Accelerator.IpAddresses``.
        :param ip_address_type: ``AWS::GlobalAccelerator::Accelerator.IpAddressType``.
        :param tags: ``AWS::GlobalAccelerator::Accelerator.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if ip_addresses is not None:
            self._values["ip_addresses"] = ip_addresses
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::GlobalAccelerator::Accelerator.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::GlobalAccelerator::Accelerator.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def ip_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::GlobalAccelerator::Accelerator.IpAddresses``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-ipaddresses
        '''
        result = self._values.get("ip_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::GlobalAccelerator::Accelerator.IpAddressType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-ipaddresstype
        '''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::GlobalAccelerator::Accelerator.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAcceleratorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEndpointGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnEndpointGroup",
):
    '''A CloudFormation ``AWS::GlobalAccelerator::EndpointGroup``.

    :cloudformationResource: AWS::GlobalAccelerator::EndpointGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        endpoint_group_region: builtins.str,
        listener_arn: builtins.str,
        endpoint_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnEndpointGroup.EndpointConfigurationProperty", _IResolvable_da3f097b]]]] = None,
        health_check_interval_seconds: typing.Optional[jsii.Number] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        health_check_port: typing.Optional[jsii.Number] = None,
        health_check_protocol: typing.Optional[builtins.str] = None,
        port_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnEndpointGroup.PortOverrideProperty", _IResolvable_da3f097b]]]] = None,
        threshold_count: typing.Optional[jsii.Number] = None,
        traffic_dial_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::GlobalAccelerator::EndpointGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param endpoint_group_region: ``AWS::GlobalAccelerator::EndpointGroup.EndpointGroupRegion``.
        :param listener_arn: ``AWS::GlobalAccelerator::EndpointGroup.ListenerArn``.
        :param endpoint_configurations: ``AWS::GlobalAccelerator::EndpointGroup.EndpointConfigurations``.
        :param health_check_interval_seconds: ``AWS::GlobalAccelerator::EndpointGroup.HealthCheckIntervalSeconds``.
        :param health_check_path: ``AWS::GlobalAccelerator::EndpointGroup.HealthCheckPath``.
        :param health_check_port: ``AWS::GlobalAccelerator::EndpointGroup.HealthCheckPort``.
        :param health_check_protocol: ``AWS::GlobalAccelerator::EndpointGroup.HealthCheckProtocol``.
        :param port_overrides: ``AWS::GlobalAccelerator::EndpointGroup.PortOverrides``.
        :param threshold_count: ``AWS::GlobalAccelerator::EndpointGroup.ThresholdCount``.
        :param traffic_dial_percentage: ``AWS::GlobalAccelerator::EndpointGroup.TrafficDialPercentage``.
        '''
        props = CfnEndpointGroupProps(
            endpoint_group_region=endpoint_group_region,
            listener_arn=listener_arn,
            endpoint_configurations=endpoint_configurations,
            health_check_interval_seconds=health_check_interval_seconds,
            health_check_path=health_check_path,
            health_check_port=health_check_port,
            health_check_protocol=health_check_protocol,
            port_overrides=port_overrides,
            threshold_count=threshold_count,
            traffic_dial_percentage=traffic_dial_percentage,
        )

        jsii.create(CfnEndpointGroup, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEndpointGroupArn")
    def attr_endpoint_group_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: EndpointGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointGroupRegion")
    def endpoint_group_region(self) -> builtins.str:
        '''``AWS::GlobalAccelerator::EndpointGroup.EndpointGroupRegion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-endpointgroupregion
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointGroupRegion"))

    @endpoint_group_region.setter
    def endpoint_group_region(self, value: builtins.str) -> None:
        jsii.set(self, "endpointGroupRegion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="listenerArn")
    def listener_arn(self) -> builtins.str:
        '''``AWS::GlobalAccelerator::EndpointGroup.ListenerArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-listenerarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "listenerArn"))

    @listener_arn.setter
    def listener_arn(self, value: builtins.str) -> None:
        jsii.set(self, "listenerArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointConfigurations")
    def endpoint_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnEndpointGroup.EndpointConfigurationProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::GlobalAccelerator::EndpointGroup.EndpointConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-endpointconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnEndpointGroup.EndpointConfigurationProperty", _IResolvable_da3f097b]]]], jsii.get(self, "endpointConfigurations"))

    @endpoint_configurations.setter
    def endpoint_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnEndpointGroup.EndpointConfigurationProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "endpointConfigurations", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckIntervalSeconds")
    def health_check_interval_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GlobalAccelerator::EndpointGroup.HealthCheckIntervalSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckintervalseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckIntervalSeconds"))

    @health_check_interval_seconds.setter
    def health_check_interval_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        jsii.set(self, "healthCheckIntervalSeconds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckPath")
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''``AWS::GlobalAccelerator::EndpointGroup.HealthCheckPath``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckpath
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckPath"))

    @health_check_path.setter
    def health_check_path(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "healthCheckPath", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckPort")
    def health_check_port(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GlobalAccelerator::EndpointGroup.HealthCheckPort``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckport
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckPort"))

    @health_check_port.setter
    def health_check_port(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "healthCheckPort", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckProtocol")
    def health_check_protocol(self) -> typing.Optional[builtins.str]:
        '''``AWS::GlobalAccelerator::EndpointGroup.HealthCheckProtocol``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckprotocol
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckProtocol"))

    @health_check_protocol.setter
    def health_check_protocol(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "healthCheckProtocol", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="portOverrides")
    def port_overrides(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnEndpointGroup.PortOverrideProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::GlobalAccelerator::EndpointGroup.PortOverrides``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-portoverrides
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnEndpointGroup.PortOverrideProperty", _IResolvable_da3f097b]]]], jsii.get(self, "portOverrides"))

    @port_overrides.setter
    def port_overrides(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnEndpointGroup.PortOverrideProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "portOverrides", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="thresholdCount")
    def threshold_count(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GlobalAccelerator::EndpointGroup.ThresholdCount``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-thresholdcount
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdCount"))

    @threshold_count.setter
    def threshold_count(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "thresholdCount", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trafficDialPercentage")
    def traffic_dial_percentage(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GlobalAccelerator::EndpointGroup.TrafficDialPercentage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-trafficdialpercentage
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "trafficDialPercentage"))

    @traffic_dial_percentage.setter
    def traffic_dial_percentage(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "trafficDialPercentage", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnEndpointGroup.EndpointConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_id": "endpointId",
            "client_ip_preservation_enabled": "clientIpPreservationEnabled",
            "weight": "weight",
        },
    )
    class EndpointConfigurationProperty:
        def __init__(
            self,
            *,
            endpoint_id: builtins.str,
            client_ip_preservation_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            weight: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param endpoint_id: ``CfnEndpointGroup.EndpointConfigurationProperty.EndpointId``.
            :param client_ip_preservation_enabled: ``CfnEndpointGroup.EndpointConfigurationProperty.ClientIPPreservationEnabled``.
            :param weight: ``CfnEndpointGroup.EndpointConfigurationProperty.Weight``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_id": endpoint_id,
            }
            if client_ip_preservation_enabled is not None:
                self._values["client_ip_preservation_enabled"] = client_ip_preservation_enabled
            if weight is not None:
                self._values["weight"] = weight

        @builtins.property
        def endpoint_id(self) -> builtins.str:
            '''``CfnEndpointGroup.EndpointConfigurationProperty.EndpointId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html#cfn-globalaccelerator-endpointgroup-endpointconfiguration-endpointid
            '''
            result = self._values.get("endpoint_id")
            assert result is not None, "Required property 'endpoint_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_ip_preservation_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnEndpointGroup.EndpointConfigurationProperty.ClientIPPreservationEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html#cfn-globalaccelerator-endpointgroup-endpointconfiguration-clientippreservationenabled
            '''
            result = self._values.get("client_ip_preservation_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def weight(self) -> typing.Optional[jsii.Number]:
            '''``CfnEndpointGroup.EndpointConfigurationProperty.Weight``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html#cfn-globalaccelerator-endpointgroup-endpointconfiguration-weight
            '''
            result = self._values.get("weight")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnEndpointGroup.PortOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_port": "endpointPort",
            "listener_port": "listenerPort",
        },
    )
    class PortOverrideProperty:
        def __init__(
            self,
            *,
            endpoint_port: jsii.Number,
            listener_port: jsii.Number,
        ) -> None:
            '''
            :param endpoint_port: ``CfnEndpointGroup.PortOverrideProperty.EndpointPort``.
            :param listener_port: ``CfnEndpointGroup.PortOverrideProperty.ListenerPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-portoverride.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_port": endpoint_port,
                "listener_port": listener_port,
            }

        @builtins.property
        def endpoint_port(self) -> jsii.Number:
            '''``CfnEndpointGroup.PortOverrideProperty.EndpointPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-portoverride.html#cfn-globalaccelerator-endpointgroup-portoverride-endpointport
            '''
            result = self._values.get("endpoint_port")
            assert result is not None, "Required property 'endpoint_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def listener_port(self) -> jsii.Number:
            '''``CfnEndpointGroup.PortOverrideProperty.ListenerPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-portoverride.html#cfn-globalaccelerator-endpointgroup-portoverride-listenerport
            '''
            result = self._values.get("listener_port")
            assert result is not None, "Required property 'listener_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnEndpointGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_group_region": "endpointGroupRegion",
        "listener_arn": "listenerArn",
        "endpoint_configurations": "endpointConfigurations",
        "health_check_interval_seconds": "healthCheckIntervalSeconds",
        "health_check_path": "healthCheckPath",
        "health_check_port": "healthCheckPort",
        "health_check_protocol": "healthCheckProtocol",
        "port_overrides": "portOverrides",
        "threshold_count": "thresholdCount",
        "traffic_dial_percentage": "trafficDialPercentage",
    },
)
class CfnEndpointGroupProps:
    def __init__(
        self,
        *,
        endpoint_group_region: builtins.str,
        listener_arn: builtins.str,
        endpoint_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnEndpointGroup.EndpointConfigurationProperty, _IResolvable_da3f097b]]]] = None,
        health_check_interval_seconds: typing.Optional[jsii.Number] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        health_check_port: typing.Optional[jsii.Number] = None,
        health_check_protocol: typing.Optional[builtins.str] = None,
        port_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnEndpointGroup.PortOverrideProperty, _IResolvable_da3f097b]]]] = None,
        threshold_count: typing.Optional[jsii.Number] = None,
        traffic_dial_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``AWS::GlobalAccelerator::EndpointGroup``.

        :param endpoint_group_region: ``AWS::GlobalAccelerator::EndpointGroup.EndpointGroupRegion``.
        :param listener_arn: ``AWS::GlobalAccelerator::EndpointGroup.ListenerArn``.
        :param endpoint_configurations: ``AWS::GlobalAccelerator::EndpointGroup.EndpointConfigurations``.
        :param health_check_interval_seconds: ``AWS::GlobalAccelerator::EndpointGroup.HealthCheckIntervalSeconds``.
        :param health_check_path: ``AWS::GlobalAccelerator::EndpointGroup.HealthCheckPath``.
        :param health_check_port: ``AWS::GlobalAccelerator::EndpointGroup.HealthCheckPort``.
        :param health_check_protocol: ``AWS::GlobalAccelerator::EndpointGroup.HealthCheckProtocol``.
        :param port_overrides: ``AWS::GlobalAccelerator::EndpointGroup.PortOverrides``.
        :param threshold_count: ``AWS::GlobalAccelerator::EndpointGroup.ThresholdCount``.
        :param traffic_dial_percentage: ``AWS::GlobalAccelerator::EndpointGroup.TrafficDialPercentage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_group_region": endpoint_group_region,
            "listener_arn": listener_arn,
        }
        if endpoint_configurations is not None:
            self._values["endpoint_configurations"] = endpoint_configurations
        if health_check_interval_seconds is not None:
            self._values["health_check_interval_seconds"] = health_check_interval_seconds
        if health_check_path is not None:
            self._values["health_check_path"] = health_check_path
        if health_check_port is not None:
            self._values["health_check_port"] = health_check_port
        if health_check_protocol is not None:
            self._values["health_check_protocol"] = health_check_protocol
        if port_overrides is not None:
            self._values["port_overrides"] = port_overrides
        if threshold_count is not None:
            self._values["threshold_count"] = threshold_count
        if traffic_dial_percentage is not None:
            self._values["traffic_dial_percentage"] = traffic_dial_percentage

    @builtins.property
    def endpoint_group_region(self) -> builtins.str:
        '''``AWS::GlobalAccelerator::EndpointGroup.EndpointGroupRegion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-endpointgroupregion
        '''
        result = self._values.get("endpoint_group_region")
        assert result is not None, "Required property 'endpoint_group_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def listener_arn(self) -> builtins.str:
        '''``AWS::GlobalAccelerator::EndpointGroup.ListenerArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-listenerarn
        '''
        result = self._values.get("listener_arn")
        assert result is not None, "Required property 'listener_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnEndpointGroup.EndpointConfigurationProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::GlobalAccelerator::EndpointGroup.EndpointConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-endpointconfigurations
        '''
        result = self._values.get("endpoint_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnEndpointGroup.EndpointConfigurationProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def health_check_interval_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GlobalAccelerator::EndpointGroup.HealthCheckIntervalSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckintervalseconds
        '''
        result = self._values.get("health_check_interval_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''``AWS::GlobalAccelerator::EndpointGroup.HealthCheckPath``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckpath
        '''
        result = self._values.get("health_check_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_port(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GlobalAccelerator::EndpointGroup.HealthCheckPort``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckport
        '''
        result = self._values.get("health_check_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_protocol(self) -> typing.Optional[builtins.str]:
        '''``AWS::GlobalAccelerator::EndpointGroup.HealthCheckProtocol``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckprotocol
        '''
        result = self._values.get("health_check_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_overrides(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnEndpointGroup.PortOverrideProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::GlobalAccelerator::EndpointGroup.PortOverrides``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-portoverrides
        '''
        result = self._values.get("port_overrides")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnEndpointGroup.PortOverrideProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def threshold_count(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GlobalAccelerator::EndpointGroup.ThresholdCount``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-thresholdcount
        '''
        result = self._values.get("threshold_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def traffic_dial_percentage(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GlobalAccelerator::EndpointGroup.TrafficDialPercentage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-trafficdialpercentage
        '''
        result = self._values.get("traffic_dial_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnListener(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnListener",
):
    '''A CloudFormation ``AWS::GlobalAccelerator::Listener``.

    :cloudformationResource: AWS::GlobalAccelerator::Listener
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        accelerator_arn: builtins.str,
        port_ranges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnListener.PortRangeProperty", _IResolvable_da3f097b]]],
        protocol: builtins.str,
        client_affinity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::GlobalAccelerator::Listener``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param accelerator_arn: ``AWS::GlobalAccelerator::Listener.AcceleratorArn``.
        :param port_ranges: ``AWS::GlobalAccelerator::Listener.PortRanges``.
        :param protocol: ``AWS::GlobalAccelerator::Listener.Protocol``.
        :param client_affinity: ``AWS::GlobalAccelerator::Listener.ClientAffinity``.
        '''
        props = CfnListenerProps(
            accelerator_arn=accelerator_arn,
            port_ranges=port_ranges,
            protocol=protocol,
            client_affinity=client_affinity,
        )

        jsii.create(CfnListener, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrListenerArn")
    def attr_listener_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ListenerArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrListenerArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="acceleratorArn")
    def accelerator_arn(self) -> builtins.str:
        '''``AWS::GlobalAccelerator::Listener.AcceleratorArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-acceleratorarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "acceleratorArn"))

    @accelerator_arn.setter
    def accelerator_arn(self, value: builtins.str) -> None:
        jsii.set(self, "acceleratorArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="portRanges")
    def port_ranges(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnListener.PortRangeProperty", _IResolvable_da3f097b]]]:
        '''``AWS::GlobalAccelerator::Listener.PortRanges``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-portranges
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnListener.PortRangeProperty", _IResolvable_da3f097b]]], jsii.get(self, "portRanges"))

    @port_ranges.setter
    def port_ranges(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnListener.PortRangeProperty", _IResolvable_da3f097b]]],
    ) -> None:
        jsii.set(self, "portRanges", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        '''``AWS::GlobalAccelerator::Listener.Protocol``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-protocol
        '''
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        jsii.set(self, "protocol", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clientAffinity")
    def client_affinity(self) -> typing.Optional[builtins.str]:
        '''``AWS::GlobalAccelerator::Listener.ClientAffinity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-clientaffinity
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientAffinity"))

    @client_affinity.setter
    def client_affinity(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "clientAffinity", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnListener.PortRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"from_port": "fromPort", "to_port": "toPort"},
    )
    class PortRangeProperty:
        def __init__(self, *, from_port: jsii.Number, to_port: jsii.Number) -> None:
            '''
            :param from_port: ``CfnListener.PortRangeProperty.FromPort``.
            :param to_port: ``CfnListener.PortRangeProperty.ToPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-listener-portrange.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "from_port": from_port,
                "to_port": to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            '''``CfnListener.PortRangeProperty.FromPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-listener-portrange.html#cfn-globalaccelerator-listener-portrange-fromport
            '''
            result = self._values.get("from_port")
            assert result is not None, "Required property 'from_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def to_port(self) -> jsii.Number:
            '''``CfnListener.PortRangeProperty.ToPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-listener-portrange.html#cfn-globalaccelerator-listener-portrange-toport
            '''
            result = self._values.get("to_port")
            assert result is not None, "Required property 'to_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnListenerProps",
    jsii_struct_bases=[],
    name_mapping={
        "accelerator_arn": "acceleratorArn",
        "port_ranges": "portRanges",
        "protocol": "protocol",
        "client_affinity": "clientAffinity",
    },
)
class CfnListenerProps:
    def __init__(
        self,
        *,
        accelerator_arn: builtins.str,
        port_ranges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnListener.PortRangeProperty, _IResolvable_da3f097b]]],
        protocol: builtins.str,
        client_affinity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::GlobalAccelerator::Listener``.

        :param accelerator_arn: ``AWS::GlobalAccelerator::Listener.AcceleratorArn``.
        :param port_ranges: ``AWS::GlobalAccelerator::Listener.PortRanges``.
        :param protocol: ``AWS::GlobalAccelerator::Listener.Protocol``.
        :param client_affinity: ``AWS::GlobalAccelerator::Listener.ClientAffinity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "accelerator_arn": accelerator_arn,
            "port_ranges": port_ranges,
            "protocol": protocol,
        }
        if client_affinity is not None:
            self._values["client_affinity"] = client_affinity

    @builtins.property
    def accelerator_arn(self) -> builtins.str:
        '''``AWS::GlobalAccelerator::Listener.AcceleratorArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-acceleratorarn
        '''
        result = self._values.get("accelerator_arn")
        assert result is not None, "Required property 'accelerator_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port_ranges(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnListener.PortRangeProperty, _IResolvable_da3f097b]]]:
        '''``AWS::GlobalAccelerator::Listener.PortRanges``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-portranges
        '''
        result = self._values.get("port_ranges")
        assert result is not None, "Required property 'port_ranges' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnListener.PortRangeProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''``AWS::GlobalAccelerator::Listener.Protocol``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-protocol
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_affinity(self) -> typing.Optional[builtins.str]:
        '''``AWS::GlobalAccelerator::Listener.ClientAffinity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-clientaffinity
        '''
        result = self._values.get("client_affinity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnListenerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_globalaccelerator.ClientAffinity")
class ClientAffinity(enum.Enum):
    '''(experimental) Client affinity gives you control over whether to always route each client to the same specific endpoint.

    :see: https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners.html#about-listeners-client-affinity
    :stability: experimental
    '''

    NONE = "NONE"
    '''(experimental) Route traffic based on the 5-tuple ``(source IP, source port, destination IP, destination port, protocol)``.

    :stability: experimental
    '''
    SOURCE_IP = "SOURCE_IP"
    '''(experimental) Route traffic based on the 2-tuple ``(source IP, destination IP)``.

    The result is that multiple connections from the same client will be routed the same.

    :stability: experimental
    '''


@jsii.enum(jsii_type="aws-cdk-lib.aws_globalaccelerator.ConnectionProtocol")
class ConnectionProtocol(enum.Enum):
    '''(experimental) The protocol for the connections from clients to the accelerator.

    :stability: experimental
    '''

    TCP = "TCP"
    '''(experimental) TCP.

    :stability: experimental
    '''
    UDP = "UDP"
    '''(experimental) UDP.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.EndpointGroupOptions",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_group_name": "endpointGroupName",
        "endpoints": "endpoints",
        "health_check_interval": "healthCheckInterval",
        "health_check_path": "healthCheckPath",
        "health_check_port": "healthCheckPort",
        "health_check_protocol": "healthCheckProtocol",
        "health_check_threshold": "healthCheckThreshold",
        "port_overrides": "portOverrides",
        "region": "region",
        "traffic_dial_percentage": "trafficDialPercentage",
    },
)
class EndpointGroupOptions:
    def __init__(
        self,
        *,
        endpoint_group_name: typing.Optional[builtins.str] = None,
        endpoints: typing.Optional[typing.Sequence["IEndpoint"]] = None,
        health_check_interval: typing.Optional[_Duration_4839e8c3] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        health_check_port: typing.Optional[jsii.Number] = None,
        health_check_protocol: typing.Optional["HealthCheckProtocol"] = None,
        health_check_threshold: typing.Optional[jsii.Number] = None,
        port_overrides: typing.Optional[typing.Sequence["PortOverride"]] = None,
        region: typing.Optional[builtins.str] = None,
        traffic_dial_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Basic options for creating a new EndpointGroup.

        :param endpoint_group_name: (experimental) Name of the endpoint group. Default: - logical ID of the resource
        :param endpoints: (experimental) Initial list of endpoints for this group. Default: - Group is initially empty
        :param health_check_interval: (experimental) The time between health checks for each endpoint. Must be either 10 or 30 seconds. Default: Duration.seconds(30)
        :param health_check_path: (experimental) The ping path for health checks (if the protocol is HTTP(S)). Default: '/'
        :param health_check_port: (experimental) The port used to perform health checks. Default: - The listener's port
        :param health_check_protocol: (experimental) The protocol used to perform health checks. Default: HealthCheckProtocol.TCP
        :param health_check_threshold: (experimental) The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. Default: 3
        :param port_overrides: (experimental) Override the destination ports used to route traffic to an endpoint. Unless overridden, the port used to hit the endpoint will be the same as the port that traffic arrives on at the listener. Default: - No overrides
        :param region: (experimental) The AWS Region where the endpoint group is located. Default: - region of the first endpoint in this group, or the stack region if that region can't be determined
        :param traffic_dial_percentage: (experimental) The percentage of traffic to send to this AWS Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing. Additional traffic is distributed to other endpoint groups for this listener. Default: 100

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if endpoint_group_name is not None:
            self._values["endpoint_group_name"] = endpoint_group_name
        if endpoints is not None:
            self._values["endpoints"] = endpoints
        if health_check_interval is not None:
            self._values["health_check_interval"] = health_check_interval
        if health_check_path is not None:
            self._values["health_check_path"] = health_check_path
        if health_check_port is not None:
            self._values["health_check_port"] = health_check_port
        if health_check_protocol is not None:
            self._values["health_check_protocol"] = health_check_protocol
        if health_check_threshold is not None:
            self._values["health_check_threshold"] = health_check_threshold
        if port_overrides is not None:
            self._values["port_overrides"] = port_overrides
        if region is not None:
            self._values["region"] = region
        if traffic_dial_percentage is not None:
            self._values["traffic_dial_percentage"] = traffic_dial_percentage

    @builtins.property
    def endpoint_group_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the endpoint group.

        :default: - logical ID of the resource

        :stability: experimental
        '''
        result = self._values.get("endpoint_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoints(self) -> typing.Optional[typing.List["IEndpoint"]]:
        '''(experimental) Initial list of endpoints for this group.

        :default: - Group is initially empty

        :stability: experimental
        '''
        result = self._values.get("endpoints")
        return typing.cast(typing.Optional[typing.List["IEndpoint"]], result)

    @builtins.property
    def health_check_interval(self) -> typing.Optional[_Duration_4839e8c3]:
        '''(experimental) The time between health checks for each endpoint.

        Must be either 10 or 30 seconds.

        :default: Duration.seconds(30)

        :stability: experimental
        '''
        result = self._values.get("health_check_interval")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''(experimental) The ping path for health checks (if the protocol is HTTP(S)).

        :default: '/'

        :stability: experimental
        '''
        result = self._values.get("health_check_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_port(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The port used to perform health checks.

        :default: - The listener's port

        :stability: experimental
        '''
        result = self._values.get("health_check_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_protocol(self) -> typing.Optional["HealthCheckProtocol"]:
        '''(experimental) The protocol used to perform health checks.

        :default: HealthCheckProtocol.TCP

        :stability: experimental
        '''
        result = self._values.get("health_check_protocol")
        return typing.cast(typing.Optional["HealthCheckProtocol"], result)

    @builtins.property
    def health_check_threshold(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy.

        :default: 3

        :stability: experimental
        '''
        result = self._values.get("health_check_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_overrides(self) -> typing.Optional[typing.List["PortOverride"]]:
        '''(experimental) Override the destination ports used to route traffic to an endpoint.

        Unless overridden, the port used to hit the endpoint will be the same as the port
        that traffic arrives on at the listener.

        :default: - No overrides

        :stability: experimental
        '''
        result = self._values.get("port_overrides")
        return typing.cast(typing.Optional[typing.List["PortOverride"]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) The AWS Region where the endpoint group is located.

        :default: - region of the first endpoint in this group, or the stack region if that region can't be determined

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def traffic_dial_percentage(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The percentage of traffic to send to this AWS Region.

        The percentage is applied to the traffic that would otherwise have been
        routed to the Region based on optimal routing. Additional traffic is
        distributed to other endpoint groups for this listener.

        :default: 100

        :stability: experimental
        '''
        result = self._values.get("traffic_dial_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointGroupOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.EndpointGroupProps",
    jsii_struct_bases=[EndpointGroupOptions],
    name_mapping={
        "endpoint_group_name": "endpointGroupName",
        "endpoints": "endpoints",
        "health_check_interval": "healthCheckInterval",
        "health_check_path": "healthCheckPath",
        "health_check_port": "healthCheckPort",
        "health_check_protocol": "healthCheckProtocol",
        "health_check_threshold": "healthCheckThreshold",
        "port_overrides": "portOverrides",
        "region": "region",
        "traffic_dial_percentage": "trafficDialPercentage",
        "listener": "listener",
    },
)
class EndpointGroupProps(EndpointGroupOptions):
    def __init__(
        self,
        *,
        endpoint_group_name: typing.Optional[builtins.str] = None,
        endpoints: typing.Optional[typing.Sequence["IEndpoint"]] = None,
        health_check_interval: typing.Optional[_Duration_4839e8c3] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        health_check_port: typing.Optional[jsii.Number] = None,
        health_check_protocol: typing.Optional["HealthCheckProtocol"] = None,
        health_check_threshold: typing.Optional[jsii.Number] = None,
        port_overrides: typing.Optional[typing.Sequence["PortOverride"]] = None,
        region: typing.Optional[builtins.str] = None,
        traffic_dial_percentage: typing.Optional[jsii.Number] = None,
        listener: "IListener",
    ) -> None:
        '''(experimental) Property of the EndpointGroup.

        :param endpoint_group_name: (experimental) Name of the endpoint group. Default: - logical ID of the resource
        :param endpoints: (experimental) Initial list of endpoints for this group. Default: - Group is initially empty
        :param health_check_interval: (experimental) The time between health checks for each endpoint. Must be either 10 or 30 seconds. Default: Duration.seconds(30)
        :param health_check_path: (experimental) The ping path for health checks (if the protocol is HTTP(S)). Default: '/'
        :param health_check_port: (experimental) The port used to perform health checks. Default: - The listener's port
        :param health_check_protocol: (experimental) The protocol used to perform health checks. Default: HealthCheckProtocol.TCP
        :param health_check_threshold: (experimental) The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. Default: 3
        :param port_overrides: (experimental) Override the destination ports used to route traffic to an endpoint. Unless overridden, the port used to hit the endpoint will be the same as the port that traffic arrives on at the listener. Default: - No overrides
        :param region: (experimental) The AWS Region where the endpoint group is located. Default: - region of the first endpoint in this group, or the stack region if that region can't be determined
        :param traffic_dial_percentage: (experimental) The percentage of traffic to send to this AWS Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing. Additional traffic is distributed to other endpoint groups for this listener. Default: 100
        :param listener: (experimental) The Amazon Resource Name (ARN) of the listener.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "listener": listener,
        }
        if endpoint_group_name is not None:
            self._values["endpoint_group_name"] = endpoint_group_name
        if endpoints is not None:
            self._values["endpoints"] = endpoints
        if health_check_interval is not None:
            self._values["health_check_interval"] = health_check_interval
        if health_check_path is not None:
            self._values["health_check_path"] = health_check_path
        if health_check_port is not None:
            self._values["health_check_port"] = health_check_port
        if health_check_protocol is not None:
            self._values["health_check_protocol"] = health_check_protocol
        if health_check_threshold is not None:
            self._values["health_check_threshold"] = health_check_threshold
        if port_overrides is not None:
            self._values["port_overrides"] = port_overrides
        if region is not None:
            self._values["region"] = region
        if traffic_dial_percentage is not None:
            self._values["traffic_dial_percentage"] = traffic_dial_percentage

    @builtins.property
    def endpoint_group_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the endpoint group.

        :default: - logical ID of the resource

        :stability: experimental
        '''
        result = self._values.get("endpoint_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoints(self) -> typing.Optional[typing.List["IEndpoint"]]:
        '''(experimental) Initial list of endpoints for this group.

        :default: - Group is initially empty

        :stability: experimental
        '''
        result = self._values.get("endpoints")
        return typing.cast(typing.Optional[typing.List["IEndpoint"]], result)

    @builtins.property
    def health_check_interval(self) -> typing.Optional[_Duration_4839e8c3]:
        '''(experimental) The time between health checks for each endpoint.

        Must be either 10 or 30 seconds.

        :default: Duration.seconds(30)

        :stability: experimental
        '''
        result = self._values.get("health_check_interval")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''(experimental) The ping path for health checks (if the protocol is HTTP(S)).

        :default: '/'

        :stability: experimental
        '''
        result = self._values.get("health_check_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_port(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The port used to perform health checks.

        :default: - The listener's port

        :stability: experimental
        '''
        result = self._values.get("health_check_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_protocol(self) -> typing.Optional["HealthCheckProtocol"]:
        '''(experimental) The protocol used to perform health checks.

        :default: HealthCheckProtocol.TCP

        :stability: experimental
        '''
        result = self._values.get("health_check_protocol")
        return typing.cast(typing.Optional["HealthCheckProtocol"], result)

    @builtins.property
    def health_check_threshold(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy.

        :default: 3

        :stability: experimental
        '''
        result = self._values.get("health_check_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_overrides(self) -> typing.Optional[typing.List["PortOverride"]]:
        '''(experimental) Override the destination ports used to route traffic to an endpoint.

        Unless overridden, the port used to hit the endpoint will be the same as the port
        that traffic arrives on at the listener.

        :default: - No overrides

        :stability: experimental
        '''
        result = self._values.get("port_overrides")
        return typing.cast(typing.Optional[typing.List["PortOverride"]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) The AWS Region where the endpoint group is located.

        :default: - region of the first endpoint in this group, or the stack region if that region can't be determined

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def traffic_dial_percentage(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The percentage of traffic to send to this AWS Region.

        The percentage is applied to the traffic that would otherwise have been
        routed to the Region based on optimal routing. Additional traffic is
        distributed to other endpoint groups for this listener.

        :default: 100

        :stability: experimental
        '''
        result = self._values.get("traffic_dial_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def listener(self) -> "IListener":
        '''(experimental) The Amazon Resource Name (ARN) of the listener.

        :stability: experimental
        '''
        result = self._values.get("listener")
        assert result is not None, "Required property 'listener' is missing"
        return typing.cast("IListener", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_globalaccelerator.HealthCheckProtocol")
class HealthCheckProtocol(enum.Enum):
    '''(experimental) The protocol for the connections from clients to the accelerator.

    :stability: experimental
    '''

    TCP = "TCP"
    '''(experimental) TCP.

    :stability: experimental
    '''
    HTTP = "HTTP"
    '''(experimental) HTTP.

    :stability: experimental
    '''
    HTTPS = "HTTPS"
    '''(experimental) HTTPS.

    :stability: experimental
    '''


@jsii.interface(jsii_type="aws-cdk-lib.aws_globalaccelerator.IAccelerator")
class IAccelerator(_IResource_c80c4260, typing_extensions.Protocol):
    '''(experimental) The interface of the Accelerator.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IAcceleratorProxy"]:
        return _IAcceleratorProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="acceleratorArn")
    def accelerator_arn(self) -> builtins.str:
        '''(experimental) The ARN of the accelerator.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        '''(experimental) The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IP addresses.

        :stability: experimental
        :attribute: true
        '''
        ...


class _IAcceleratorProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''(experimental) The interface of the Accelerator.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_globalaccelerator.IAccelerator"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="acceleratorArn")
    def accelerator_arn(self) -> builtins.str:
        '''(experimental) The ARN of the accelerator.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "acceleratorArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        '''(experimental) The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IP addresses.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))


@jsii.interface(jsii_type="aws-cdk-lib.aws_globalaccelerator.IEndpoint")
class IEndpoint(typing_extensions.Protocol):
    '''(experimental) An endpoint for the endpoint group.

    Implementations of ``IEndpoint`` can be found in the ``aws-globalaccelerator-endpoints`` package.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IEndpointProxy"]:
        return _IEndpointProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) The region where the endpoint is located.

        If the region cannot be determined, ``undefined`` is returned

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="renderEndpointConfiguration")
    def render_endpoint_configuration(self) -> typing.Any:
        '''(experimental) Render the endpoint to an endpoint configuration.

        :stability: experimental
        '''
        ...


class _IEndpointProxy:
    '''(experimental) An endpoint for the endpoint group.

    Implementations of ``IEndpoint`` can be found in the ``aws-globalaccelerator-endpoints`` package.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_globalaccelerator.IEndpoint"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) The region where the endpoint is located.

        If the region cannot be determined, ``undefined`` is returned

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))

    @jsii.member(jsii_name="renderEndpointConfiguration")
    def render_endpoint_configuration(self) -> typing.Any:
        '''(experimental) Render the endpoint to an endpoint configuration.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "renderEndpointConfiguration", []))


@jsii.interface(jsii_type="aws-cdk-lib.aws_globalaccelerator.IEndpointGroup")
class IEndpointGroup(_IResource_c80c4260, typing_extensions.Protocol):
    '''(experimental) The interface of the EndpointGroup.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IEndpointGroupProxy"]:
        return _IEndpointGroupProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointGroupArn")
    def endpoint_group_arn(self) -> builtins.str:
        '''(experimental) EndpointGroup ARN.

        :stability: experimental
        :attribute: true
        '''
        ...


class _IEndpointGroupProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''(experimental) The interface of the EndpointGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_globalaccelerator.IEndpointGroup"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointGroupArn")
    def endpoint_group_arn(self) -> builtins.str:
        '''(experimental) EndpointGroup ARN.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointGroupArn"))


@jsii.interface(jsii_type="aws-cdk-lib.aws_globalaccelerator.IListener")
class IListener(_IResource_c80c4260, typing_extensions.Protocol):
    '''(experimental) Interface of the Listener.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IListenerProxy"]:
        return _IListenerProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="listenerArn")
    def listener_arn(self) -> builtins.str:
        '''(experimental) The ARN of the listener.

        :stability: experimental
        :attribute: true
        '''
        ...


class _IListenerProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''(experimental) Interface of the Listener.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_globalaccelerator.IListener"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="listenerArn")
    def listener_arn(self) -> builtins.str:
        '''(experimental) The ARN of the listener.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "listenerArn"))


@jsii.implements(IListener)
class Listener(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.Listener",
):
    '''(experimental) The construct for the Listener.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        accelerator: IAccelerator,
        port_ranges: typing.Sequence["PortRange"],
        client_affinity: typing.Optional[ClientAffinity] = None,
        listener_name: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[ConnectionProtocol] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param accelerator: (experimental) The accelerator for this listener.
        :param port_ranges: (experimental) The list of port ranges for the connections from clients to the accelerator.
        :param client_affinity: (experimental) Client affinity to direct all requests from a user to the same endpoint. If you have stateful applications, client affinity lets you direct all requests from a user to the same endpoint. By default, each connection from each client is routed to seperate endpoints. Set client affinity to SOURCE_IP to route all connections from a single client to the same endpoint. Default: ClientAffinity.NONE
        :param listener_name: (experimental) Name of the listener. Default: - logical ID of the resource
        :param protocol: (experimental) The protocol for the connections from clients to the accelerator. Default: ConnectionProtocol.TCP

        :stability: experimental
        '''
        props = ListenerProps(
            accelerator=accelerator,
            port_ranges=port_ranges,
            client_affinity=client_affinity,
            listener_name=listener_name,
            protocol=protocol,
        )

        jsii.create(Listener, self, [scope, id, props])

    @jsii.member(jsii_name="fromListenerArn") # type: ignore[misc]
    @builtins.classmethod
    def from_listener_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        listener_arn: builtins.str,
    ) -> IListener:
        '''(experimental) import from ARN.

        :param scope: -
        :param id: -
        :param listener_arn: -

        :stability: experimental
        '''
        return typing.cast(IListener, jsii.sinvoke(cls, "fromListenerArn", [scope, id, listener_arn]))

    @jsii.member(jsii_name="addEndpointGroup")
    def add_endpoint_group(
        self,
        id: builtins.str,
        *,
        endpoint_group_name: typing.Optional[builtins.str] = None,
        endpoints: typing.Optional[typing.Sequence[IEndpoint]] = None,
        health_check_interval: typing.Optional[_Duration_4839e8c3] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        health_check_port: typing.Optional[jsii.Number] = None,
        health_check_protocol: typing.Optional[HealthCheckProtocol] = None,
        health_check_threshold: typing.Optional[jsii.Number] = None,
        port_overrides: typing.Optional[typing.Sequence["PortOverride"]] = None,
        region: typing.Optional[builtins.str] = None,
        traffic_dial_percentage: typing.Optional[jsii.Number] = None,
    ) -> "EndpointGroup":
        '''(experimental) Add a new endpoint group to this listener.

        :param id: -
        :param endpoint_group_name: (experimental) Name of the endpoint group. Default: - logical ID of the resource
        :param endpoints: (experimental) Initial list of endpoints for this group. Default: - Group is initially empty
        :param health_check_interval: (experimental) The time between health checks for each endpoint. Must be either 10 or 30 seconds. Default: Duration.seconds(30)
        :param health_check_path: (experimental) The ping path for health checks (if the protocol is HTTP(S)). Default: '/'
        :param health_check_port: (experimental) The port used to perform health checks. Default: - The listener's port
        :param health_check_protocol: (experimental) The protocol used to perform health checks. Default: HealthCheckProtocol.TCP
        :param health_check_threshold: (experimental) The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. Default: 3
        :param port_overrides: (experimental) Override the destination ports used to route traffic to an endpoint. Unless overridden, the port used to hit the endpoint will be the same as the port that traffic arrives on at the listener. Default: - No overrides
        :param region: (experimental) The AWS Region where the endpoint group is located. Default: - region of the first endpoint in this group, or the stack region if that region can't be determined
        :param traffic_dial_percentage: (experimental) The percentage of traffic to send to this AWS Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing. Additional traffic is distributed to other endpoint groups for this listener. Default: 100

        :stability: experimental
        '''
        options = EndpointGroupOptions(
            endpoint_group_name=endpoint_group_name,
            endpoints=endpoints,
            health_check_interval=health_check_interval,
            health_check_path=health_check_path,
            health_check_port=health_check_port,
            health_check_protocol=health_check_protocol,
            health_check_threshold=health_check_threshold,
            port_overrides=port_overrides,
            region=region,
            traffic_dial_percentage=traffic_dial_percentage,
        )

        return typing.cast("EndpointGroup", jsii.invoke(self, "addEndpointGroup", [id, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="listenerArn")
    def listener_arn(self) -> builtins.str:
        '''(experimental) The ARN of the listener.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "listenerArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="listenerName")
    def listener_name(self) -> builtins.str:
        '''(experimental) The name of the listener.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "listenerName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.ListenerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "port_ranges": "portRanges",
        "client_affinity": "clientAffinity",
        "listener_name": "listenerName",
        "protocol": "protocol",
    },
)
class ListenerOptions:
    def __init__(
        self,
        *,
        port_ranges: typing.Sequence["PortRange"],
        client_affinity: typing.Optional[ClientAffinity] = None,
        listener_name: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[ConnectionProtocol] = None,
    ) -> None:
        '''(experimental) Construct options for Listener.

        :param port_ranges: (experimental) The list of port ranges for the connections from clients to the accelerator.
        :param client_affinity: (experimental) Client affinity to direct all requests from a user to the same endpoint. If you have stateful applications, client affinity lets you direct all requests from a user to the same endpoint. By default, each connection from each client is routed to seperate endpoints. Set client affinity to SOURCE_IP to route all connections from a single client to the same endpoint. Default: ClientAffinity.NONE
        :param listener_name: (experimental) Name of the listener. Default: - logical ID of the resource
        :param protocol: (experimental) The protocol for the connections from clients to the accelerator. Default: ConnectionProtocol.TCP

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "port_ranges": port_ranges,
        }
        if client_affinity is not None:
            self._values["client_affinity"] = client_affinity
        if listener_name is not None:
            self._values["listener_name"] = listener_name
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def port_ranges(self) -> typing.List["PortRange"]:
        '''(experimental) The list of port ranges for the connections from clients to the accelerator.

        :stability: experimental
        '''
        result = self._values.get("port_ranges")
        assert result is not None, "Required property 'port_ranges' is missing"
        return typing.cast(typing.List["PortRange"], result)

    @builtins.property
    def client_affinity(self) -> typing.Optional[ClientAffinity]:
        '''(experimental) Client affinity to direct all requests from a user to the same endpoint.

        If you have stateful applications, client affinity lets you direct all
        requests from a user to the same endpoint.

        By default, each connection from each client is routed to seperate
        endpoints. Set client affinity to SOURCE_IP to route all connections from
        a single client to the same endpoint.

        :default: ClientAffinity.NONE

        :stability: experimental
        '''
        result = self._values.get("client_affinity")
        return typing.cast(typing.Optional[ClientAffinity], result)

    @builtins.property
    def listener_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the listener.

        :default: - logical ID of the resource

        :stability: experimental
        '''
        result = self._values.get("listener_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[ConnectionProtocol]:
        '''(experimental) The protocol for the connections from clients to the accelerator.

        :default: ConnectionProtocol.TCP

        :stability: experimental
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[ConnectionProtocol], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListenerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.ListenerProps",
    jsii_struct_bases=[ListenerOptions],
    name_mapping={
        "port_ranges": "portRanges",
        "client_affinity": "clientAffinity",
        "listener_name": "listenerName",
        "protocol": "protocol",
        "accelerator": "accelerator",
    },
)
class ListenerProps(ListenerOptions):
    def __init__(
        self,
        *,
        port_ranges: typing.Sequence["PortRange"],
        client_affinity: typing.Optional[ClientAffinity] = None,
        listener_name: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[ConnectionProtocol] = None,
        accelerator: IAccelerator,
    ) -> None:
        '''(experimental) Construct properties for Listener.

        :param port_ranges: (experimental) The list of port ranges for the connections from clients to the accelerator.
        :param client_affinity: (experimental) Client affinity to direct all requests from a user to the same endpoint. If you have stateful applications, client affinity lets you direct all requests from a user to the same endpoint. By default, each connection from each client is routed to seperate endpoints. Set client affinity to SOURCE_IP to route all connections from a single client to the same endpoint. Default: ClientAffinity.NONE
        :param listener_name: (experimental) Name of the listener. Default: - logical ID of the resource
        :param protocol: (experimental) The protocol for the connections from clients to the accelerator. Default: ConnectionProtocol.TCP
        :param accelerator: (experimental) The accelerator for this listener.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "port_ranges": port_ranges,
            "accelerator": accelerator,
        }
        if client_affinity is not None:
            self._values["client_affinity"] = client_affinity
        if listener_name is not None:
            self._values["listener_name"] = listener_name
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def port_ranges(self) -> typing.List["PortRange"]:
        '''(experimental) The list of port ranges for the connections from clients to the accelerator.

        :stability: experimental
        '''
        result = self._values.get("port_ranges")
        assert result is not None, "Required property 'port_ranges' is missing"
        return typing.cast(typing.List["PortRange"], result)

    @builtins.property
    def client_affinity(self) -> typing.Optional[ClientAffinity]:
        '''(experimental) Client affinity to direct all requests from a user to the same endpoint.

        If you have stateful applications, client affinity lets you direct all
        requests from a user to the same endpoint.

        By default, each connection from each client is routed to seperate
        endpoints. Set client affinity to SOURCE_IP to route all connections from
        a single client to the same endpoint.

        :default: ClientAffinity.NONE

        :stability: experimental
        '''
        result = self._values.get("client_affinity")
        return typing.cast(typing.Optional[ClientAffinity], result)

    @builtins.property
    def listener_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the listener.

        :default: - logical ID of the resource

        :stability: experimental
        '''
        result = self._values.get("listener_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[ConnectionProtocol]:
        '''(experimental) The protocol for the connections from clients to the accelerator.

        :default: ConnectionProtocol.TCP

        :stability: experimental
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[ConnectionProtocol], result)

    @builtins.property
    def accelerator(self) -> IAccelerator:
        '''(experimental) The accelerator for this listener.

        :stability: experimental
        '''
        result = self._values.get("accelerator")
        assert result is not None, "Required property 'accelerator' is missing"
        return typing.cast(IAccelerator, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListenerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.PortOverride",
    jsii_struct_bases=[],
    name_mapping={"endpoint_port": "endpointPort", "listener_port": "listenerPort"},
)
class PortOverride:
    def __init__(
        self,
        *,
        endpoint_port: jsii.Number,
        listener_port: jsii.Number,
    ) -> None:
        '''(experimental) Override specific listener ports used to route traffic to endpoints that are part of an endpoint group.

        :param endpoint_port: (experimental) The endpoint port that you want a listener port to be mapped to. This is the port on the endpoint, such as the Application Load Balancer or Amazon EC2 instance.
        :param listener_port: (experimental) The listener port that you want to map to a specific endpoint port. This is the port that user traffic arrives to the Global Accelerator on.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_port": endpoint_port,
            "listener_port": listener_port,
        }

    @builtins.property
    def endpoint_port(self) -> jsii.Number:
        '''(experimental) The endpoint port that you want a listener port to be mapped to.

        This is the port on the endpoint, such as the Application Load Balancer or Amazon EC2 instance.

        :stability: experimental
        '''
        result = self._values.get("endpoint_port")
        assert result is not None, "Required property 'endpoint_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def listener_port(self) -> jsii.Number:
        '''(experimental) The listener port that you want to map to a specific endpoint port.

        This is the port that user traffic arrives to the Global Accelerator on.

        :stability: experimental
        '''
        result = self._values.get("listener_port")
        assert result is not None, "Required property 'listener_port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PortOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.PortRange",
    jsii_struct_bases=[],
    name_mapping={"from_port": "fromPort", "to_port": "toPort"},
)
class PortRange:
    def __init__(
        self,
        *,
        from_port: jsii.Number,
        to_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) The list of port ranges for the connections from clients to the accelerator.

        :param from_port: (experimental) The first port in the range of ports, inclusive.
        :param to_port: (experimental) The last port in the range of ports, inclusive. Default: - same as ``fromPort``

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "from_port": from_port,
        }
        if to_port is not None:
            self._values["to_port"] = to_port

    @builtins.property
    def from_port(self) -> jsii.Number:
        '''(experimental) The first port in the range of ports, inclusive.

        :stability: experimental
        '''
        result = self._values.get("from_port")
        assert result is not None, "Required property 'from_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def to_port(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The last port in the range of ports, inclusive.

        :default: - same as ``fromPort``

        :stability: experimental
        '''
        result = self._values.get("to_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PortRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IEndpoint)
class RawEndpoint(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.RawEndpoint",
):
    '''(experimental) Untyped endpoint implementation.

    Prefer using the classes in the ``aws-globalaccelerator-endpoints`` package instead,
    as they accept typed constructs. You can use this class if you want to use an
    endpoint type that does not have an appropriate class in that package yet.

    :stability: experimental
    '''

    def __init__(
        self,
        *,
        endpoint_id: builtins.str,
        preserve_client_ip: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param endpoint_id: (experimental) Identifier of the endpoint. Load balancer ARN, instance ID or EIP allocation ID.
        :param preserve_client_ip: (experimental) Forward the client IP address. GlobalAccelerator will create Network Interfaces in your VPC in order to preserve the client IP address. Only applies to Application Load Balancers and EC2 instances. Client IP address preservation is supported only in specific AWS Regions. See the GlobalAccelerator Developer Guide for a list. Default: true if possible and available
        :param region: (experimental) The region where this endpoint is located. Default: - Unknown what region this endpoint is located
        :param weight: (experimental) Endpoint weight across all endpoints in the group. Must be a value between 0 and 255. Default: 128

        :stability: experimental
        '''
        props = RawEndpointProps(
            endpoint_id=endpoint_id,
            preserve_client_ip=preserve_client_ip,
            region=region,
            weight=weight,
        )

        jsii.create(RawEndpoint, self, [props])

    @jsii.member(jsii_name="renderEndpointConfiguration")
    def render_endpoint_configuration(self) -> typing.Any:
        '''(experimental) Render the endpoint to an endpoint configuration.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "renderEndpointConfiguration", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) The region where the endpoint is located.

        If the region cannot be determined, ``undefined`` is returned

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.RawEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_id": "endpointId",
        "preserve_client_ip": "preserveClientIp",
        "region": "region",
        "weight": "weight",
    },
)
class RawEndpointProps:
    def __init__(
        self,
        *,
        endpoint_id: builtins.str,
        preserve_client_ip: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Properties for RawEndpoint.

        :param endpoint_id: (experimental) Identifier of the endpoint. Load balancer ARN, instance ID or EIP allocation ID.
        :param preserve_client_ip: (experimental) Forward the client IP address. GlobalAccelerator will create Network Interfaces in your VPC in order to preserve the client IP address. Only applies to Application Load Balancers and EC2 instances. Client IP address preservation is supported only in specific AWS Regions. See the GlobalAccelerator Developer Guide for a list. Default: true if possible and available
        :param region: (experimental) The region where this endpoint is located. Default: - Unknown what region this endpoint is located
        :param weight: (experimental) Endpoint weight across all endpoints in the group. Must be a value between 0 and 255. Default: 128

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_id": endpoint_id,
        }
        if preserve_client_ip is not None:
            self._values["preserve_client_ip"] = preserve_client_ip
        if region is not None:
            self._values["region"] = region
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def endpoint_id(self) -> builtins.str:
        '''(experimental) Identifier of the endpoint.

        Load balancer ARN, instance ID or EIP allocation ID.

        :stability: experimental
        '''
        result = self._values.get("endpoint_id")
        assert result is not None, "Required property 'endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def preserve_client_ip(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Forward the client IP address.

        GlobalAccelerator will create Network Interfaces in your VPC in order
        to preserve the client IP address.

        Only applies to Application Load Balancers and EC2 instances.

        Client IP address preservation is supported only in specific AWS Regions.
        See the GlobalAccelerator Developer Guide for a list.

        :default: true if possible and available

        :stability: experimental
        '''
        result = self._values.get("preserve_client_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) The region where this endpoint is located.

        :default: - Unknown what region this endpoint is located

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Endpoint weight across all endpoints in the group.

        Must be a value between 0 and 255.

        :default: 128

        :stability: experimental
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RawEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IAccelerator)
class Accelerator(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.Accelerator",
):
    '''(experimental) The Accelerator construct.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        accelerator_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param accelerator_name: (experimental) The name of the accelerator. Default: - resource ID
        :param enabled: (experimental) Indicates whether the accelerator is enabled. Default: true

        :stability: experimental
        '''
        props = AcceleratorProps(accelerator_name=accelerator_name, enabled=enabled)

        jsii.create(Accelerator, self, [scope, id, props])

    @jsii.member(jsii_name="fromAcceleratorAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_accelerator_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        accelerator_arn: builtins.str,
        dns_name: builtins.str,
    ) -> IAccelerator:
        '''(experimental) import from attributes.

        :param scope: -
        :param id: -
        :param accelerator_arn: (experimental) The ARN of the accelerator.
        :param dns_name: (experimental) The DNS name of the accelerator.

        :stability: experimental
        '''
        attrs = AcceleratorAttributes(
            accelerator_arn=accelerator_arn, dns_name=dns_name
        )

        return typing.cast(IAccelerator, jsii.sinvoke(cls, "fromAcceleratorAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addListener")
    def add_listener(
        self,
        id: builtins.str,
        *,
        port_ranges: typing.Sequence[PortRange],
        client_affinity: typing.Optional[ClientAffinity] = None,
        listener_name: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[ConnectionProtocol] = None,
    ) -> Listener:
        '''(experimental) Add a listener to the accelerator.

        :param id: -
        :param port_ranges: (experimental) The list of port ranges for the connections from clients to the accelerator.
        :param client_affinity: (experimental) Client affinity to direct all requests from a user to the same endpoint. If you have stateful applications, client affinity lets you direct all requests from a user to the same endpoint. By default, each connection from each client is routed to seperate endpoints. Set client affinity to SOURCE_IP to route all connections from a single client to the same endpoint. Default: ClientAffinity.NONE
        :param listener_name: (experimental) Name of the listener. Default: - logical ID of the resource
        :param protocol: (experimental) The protocol for the connections from clients to the accelerator. Default: ConnectionProtocol.TCP

        :stability: experimental
        '''
        options = ListenerOptions(
            port_ranges=port_ranges,
            client_affinity=client_affinity,
            listener_name=listener_name,
            protocol=protocol,
        )

        return typing.cast(Listener, jsii.invoke(self, "addListener", [id, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="acceleratorArn")
    def accelerator_arn(self) -> builtins.str:
        '''(experimental) The ARN of the accelerator.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "acceleratorArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        '''(experimental) The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IP addresses.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))


@jsii.implements(IEndpointGroup)
class EndpointGroup(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.EndpointGroup",
):
    '''(experimental) EndpointGroup construct.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        listener: IListener,
        endpoint_group_name: typing.Optional[builtins.str] = None,
        endpoints: typing.Optional[typing.Sequence[IEndpoint]] = None,
        health_check_interval: typing.Optional[_Duration_4839e8c3] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        health_check_port: typing.Optional[jsii.Number] = None,
        health_check_protocol: typing.Optional[HealthCheckProtocol] = None,
        health_check_threshold: typing.Optional[jsii.Number] = None,
        port_overrides: typing.Optional[typing.Sequence[PortOverride]] = None,
        region: typing.Optional[builtins.str] = None,
        traffic_dial_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param listener: (experimental) The Amazon Resource Name (ARN) of the listener.
        :param endpoint_group_name: (experimental) Name of the endpoint group. Default: - logical ID of the resource
        :param endpoints: (experimental) Initial list of endpoints for this group. Default: - Group is initially empty
        :param health_check_interval: (experimental) The time between health checks for each endpoint. Must be either 10 or 30 seconds. Default: Duration.seconds(30)
        :param health_check_path: (experimental) The ping path for health checks (if the protocol is HTTP(S)). Default: '/'
        :param health_check_port: (experimental) The port used to perform health checks. Default: - The listener's port
        :param health_check_protocol: (experimental) The protocol used to perform health checks. Default: HealthCheckProtocol.TCP
        :param health_check_threshold: (experimental) The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. Default: 3
        :param port_overrides: (experimental) Override the destination ports used to route traffic to an endpoint. Unless overridden, the port used to hit the endpoint will be the same as the port that traffic arrives on at the listener. Default: - No overrides
        :param region: (experimental) The AWS Region where the endpoint group is located. Default: - region of the first endpoint in this group, or the stack region if that region can't be determined
        :param traffic_dial_percentage: (experimental) The percentage of traffic to send to this AWS Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing. Additional traffic is distributed to other endpoint groups for this listener. Default: 100

        :stability: experimental
        '''
        props = EndpointGroupProps(
            listener=listener,
            endpoint_group_name=endpoint_group_name,
            endpoints=endpoints,
            health_check_interval=health_check_interval,
            health_check_path=health_check_path,
            health_check_port=health_check_port,
            health_check_protocol=health_check_protocol,
            health_check_threshold=health_check_threshold,
            port_overrides=port_overrides,
            region=region,
            traffic_dial_percentage=traffic_dial_percentage,
        )

        jsii.create(EndpointGroup, self, [scope, id, props])

    @jsii.member(jsii_name="fromEndpointGroupArn") # type: ignore[misc]
    @builtins.classmethod
    def from_endpoint_group_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        endpoint_group_arn: builtins.str,
    ) -> IEndpointGroup:
        '''(experimental) import from ARN.

        :param scope: -
        :param id: -
        :param endpoint_group_arn: -

        :stability: experimental
        '''
        return typing.cast(IEndpointGroup, jsii.sinvoke(cls, "fromEndpointGroupArn", [scope, id, endpoint_group_arn]))

    @jsii.member(jsii_name="addEndpoint")
    def add_endpoint(self, endpoint: IEndpoint) -> None:
        '''(experimental) Add an endpoint.

        :param endpoint: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addEndpoint", [endpoint]))

    @jsii.member(jsii_name="connectionsPeer")
    def connections_peer(
        self,
        id: builtins.str,
        vpc: _IVpc_f30d5663,
    ) -> _IPeer_cf58db9a:
        '''(experimental) Return an object that represents the Accelerator's Security Group.

        Uses a Custom Resource to look up the Security Group that Accelerator
        creates at deploy time. Requires your VPC ID to perform the lookup.

        The Security Group will only be created if you enable **Client IP
        Preservation** on any of the endpoints.

        You cannot manipulate the rules inside this security group, but you can
        use this security group as a Peer in Connections rules on other
        constructs.

        :param id: -
        :param vpc: -

        :stability: experimental
        '''
        return typing.cast(_IPeer_cf58db9a, jsii.invoke(self, "connectionsPeer", [id, vpc]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointGroupArn")
    def endpoint_group_arn(self) -> builtins.str:
        '''(experimental) EndpointGroup ARN.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointGroupName")
    def endpoint_group_name(self) -> builtins.str:
        '''(experimental) The name of the endpoint group.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointGroupName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpoints")
    def _endpoints(self) -> typing.List[IEndpoint]:
        '''(experimental) The array of the endpoints in this endpoint group.

        :stability: experimental
        '''
        return typing.cast(typing.List[IEndpoint], jsii.get(self, "endpoints"))


__all__ = [
    "Accelerator",
    "AcceleratorAttributes",
    "AcceleratorProps",
    "CfnAccelerator",
    "CfnAcceleratorProps",
    "CfnEndpointGroup",
    "CfnEndpointGroupProps",
    "CfnListener",
    "CfnListenerProps",
    "ClientAffinity",
    "ConnectionProtocol",
    "EndpointGroup",
    "EndpointGroupOptions",
    "EndpointGroupProps",
    "HealthCheckProtocol",
    "IAccelerator",
    "IEndpoint",
    "IEndpointGroup",
    "IListener",
    "Listener",
    "ListenerOptions",
    "ListenerProps",
    "PortOverride",
    "PortRange",
    "RawEndpoint",
    "RawEndpointProps",
]

publication.publish()
