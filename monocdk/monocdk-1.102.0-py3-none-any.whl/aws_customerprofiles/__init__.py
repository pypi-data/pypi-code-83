'''
# AWS::CustomerProfiles Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
from aws_cdk import aws_customerprofiles as customerprofiles
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

from .. import (
    CfnResource as _CfnResource_e0a482dc,
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnDomain(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_customerprofiles.CfnDomain",
):
    '''A CloudFormation ``AWS::CustomerProfiles::Domain``.

    :cloudformationResource: AWS::CustomerProfiles::Domain
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        dead_letter_queue_url: typing.Optional[builtins.str] = None,
        default_encryption_key: typing.Optional[builtins.str] = None,
        default_expiration_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
    ) -> None:
        '''Create a new ``AWS::CustomerProfiles::Domain``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_name: ``AWS::CustomerProfiles::Domain.DomainName``.
        :param dead_letter_queue_url: ``AWS::CustomerProfiles::Domain.DeadLetterQueueUrl``.
        :param default_encryption_key: ``AWS::CustomerProfiles::Domain.DefaultEncryptionKey``.
        :param default_expiration_days: ``AWS::CustomerProfiles::Domain.DefaultExpirationDays``.
        :param tags: ``AWS::CustomerProfiles::Domain.Tags``.
        '''
        props = CfnDomainProps(
            domain_name=domain_name,
            dead_letter_queue_url=dead_letter_queue_url,
            default_encryption_key=default_encryption_key,
            default_expiration_days=default_expiration_days,
            tags=tags,
        )

        jsii.create(CfnDomain, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
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
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::CustomerProfiles::Domain.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::Domain.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-domainname
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deadLetterQueueUrl")
    def dead_letter_queue_url(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Domain.DeadLetterQueueUrl``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-deadletterqueueurl
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deadLetterQueueUrl"))

    @dead_letter_queue_url.setter
    def dead_letter_queue_url(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "deadLetterQueueUrl", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultEncryptionKey")
    def default_encryption_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Domain.DefaultEncryptionKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultencryptionkey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultEncryptionKey"))

    @default_encryption_key.setter
    def default_encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultEncryptionKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultExpirationDays")
    def default_expiration_days(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CustomerProfiles::Domain.DefaultExpirationDays``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultexpirationdays
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultExpirationDays"))

    @default_expiration_days.setter
    def default_expiration_days(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "defaultExpirationDays", value)


@jsii.data_type(
    jsii_type="monocdk.aws_customerprofiles.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "dead_letter_queue_url": "deadLetterQueueUrl",
        "default_encryption_key": "defaultEncryptionKey",
        "default_expiration_days": "defaultExpirationDays",
        "tags": "tags",
    },
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        dead_letter_queue_url: typing.Optional[builtins.str] = None,
        default_encryption_key: typing.Optional[builtins.str] = None,
        default_expiration_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CustomerProfiles::Domain``.

        :param domain_name: ``AWS::CustomerProfiles::Domain.DomainName``.
        :param dead_letter_queue_url: ``AWS::CustomerProfiles::Domain.DeadLetterQueueUrl``.
        :param default_encryption_key: ``AWS::CustomerProfiles::Domain.DefaultEncryptionKey``.
        :param default_expiration_days: ``AWS::CustomerProfiles::Domain.DefaultExpirationDays``.
        :param tags: ``AWS::CustomerProfiles::Domain.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
        }
        if dead_letter_queue_url is not None:
            self._values["dead_letter_queue_url"] = dead_letter_queue_url
        if default_encryption_key is not None:
            self._values["default_encryption_key"] = default_encryption_key
        if default_expiration_days is not None:
            self._values["default_expiration_days"] = default_expiration_days
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::Domain.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dead_letter_queue_url(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Domain.DeadLetterQueueUrl``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-deadletterqueueurl
        '''
        result = self._values.get("dead_letter_queue_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_encryption_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Domain.DefaultEncryptionKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultencryptionkey
        '''
        result = self._values.get("default_encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_expiration_days(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CustomerProfiles::Domain.DefaultExpirationDays``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultexpirationdays
        '''
        result = self._values.get("default_expiration_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::CustomerProfiles::Domain.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnIntegration(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_customerprofiles.CfnIntegration",
):
    '''A CloudFormation ``AWS::CustomerProfiles::Integration``.

    :cloudformationResource: AWS::CustomerProfiles::Integration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        object_type_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CustomerProfiles::Integration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_name: ``AWS::CustomerProfiles::Integration.DomainName``.
        :param object_type_name: ``AWS::CustomerProfiles::Integration.ObjectTypeName``.
        :param tags: ``AWS::CustomerProfiles::Integration.Tags``.
        :param uri: ``AWS::CustomerProfiles::Integration.Uri``.
        '''
        props = CfnIntegrationProps(
            domain_name=domain_name,
            object_type_name=object_type_name,
            tags=tags,
            uri=uri,
        )

        jsii.create(CfnIntegration, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
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
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::CustomerProfiles::Integration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::Integration.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-domainname
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="objectTypeName")
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Integration.ObjectTypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-objecttypename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeName"))

    @object_type_name.setter
    def object_type_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "objectTypeName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="uri")
    def uri(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Integration.Uri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-uri
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "uri", value)


@jsii.data_type(
    jsii_type="monocdk.aws_customerprofiles.CfnIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "object_type_name": "objectTypeName",
        "tags": "tags",
        "uri": "uri",
    },
)
class CfnIntegrationProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        object_type_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CustomerProfiles::Integration``.

        :param domain_name: ``AWS::CustomerProfiles::Integration.DomainName``.
        :param object_type_name: ``AWS::CustomerProfiles::Integration.ObjectTypeName``.
        :param tags: ``AWS::CustomerProfiles::Integration.Tags``.
        :param uri: ``AWS::CustomerProfiles::Integration.Uri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
        }
        if object_type_name is not None:
            self._values["object_type_name"] = object_type_name
        if tags is not None:
            self._values["tags"] = tags
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::Integration.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Integration.ObjectTypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-objecttypename
        '''
        result = self._values.get("object_type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::CustomerProfiles::Integration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::Integration.Uri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-uri
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnObjectType(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_customerprofiles.CfnObjectType",
):
    '''A CloudFormation ``AWS::CustomerProfiles::ObjectType``.

    :cloudformationResource: AWS::CustomerProfiles::ObjectType
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        allow_profile_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        expiration_days: typing.Optional[jsii.Number] = None,
        fields: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnObjectType.FieldMapProperty", _IResolvable_a771d0ef]]]] = None,
        keys: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnObjectType.KeyMapProperty", _IResolvable_a771d0ef]]]] = None,
        object_type_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CustomerProfiles::ObjectType``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_name: ``AWS::CustomerProfiles::ObjectType.DomainName``.
        :param allow_profile_creation: ``AWS::CustomerProfiles::ObjectType.AllowProfileCreation``.
        :param description: ``AWS::CustomerProfiles::ObjectType.Description``.
        :param encryption_key: ``AWS::CustomerProfiles::ObjectType.EncryptionKey``.
        :param expiration_days: ``AWS::CustomerProfiles::ObjectType.ExpirationDays``.
        :param fields: ``AWS::CustomerProfiles::ObjectType.Fields``.
        :param keys: ``AWS::CustomerProfiles::ObjectType.Keys``.
        :param object_type_name: ``AWS::CustomerProfiles::ObjectType.ObjectTypeName``.
        :param tags: ``AWS::CustomerProfiles::ObjectType.Tags``.
        :param template_id: ``AWS::CustomerProfiles::ObjectType.TemplateId``.
        '''
        props = CfnObjectTypeProps(
            domain_name=domain_name,
            allow_profile_creation=allow_profile_creation,
            description=description,
            encryption_key=encryption_key,
            expiration_days=expiration_days,
            fields=fields,
            keys=keys,
            object_type_name=object_type_name,
            tags=tags,
            template_id=template_id,
        )

        jsii.create(CfnObjectType, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
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
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::CustomerProfiles::ObjectType.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::ObjectType.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-domainname
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="allowProfileCreation")
    def allow_profile_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''``AWS::CustomerProfiles::ObjectType.AllowProfileCreation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-allowprofilecreation
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "allowProfileCreation"))

    @allow_profile_creation.setter
    def allow_profile_creation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "allowProfileCreation", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.EncryptionKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-encryptionkey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKey"))

    @encryption_key.setter
    def encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "encryptionKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="expirationDays")
    def expiration_days(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CustomerProfiles::ObjectType.ExpirationDays``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-expirationdays
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expirationDays"))

    @expiration_days.setter
    def expiration_days(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "expirationDays", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fields")
    def fields(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnObjectType.FieldMapProperty", _IResolvable_a771d0ef]]]]:
        '''``AWS::CustomerProfiles::ObjectType.Fields``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-fields
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnObjectType.FieldMapProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "fields"))

    @fields.setter
    def fields(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnObjectType.FieldMapProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "fields", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keys")
    def keys(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnObjectType.KeyMapProperty", _IResolvable_a771d0ef]]]]:
        '''``AWS::CustomerProfiles::ObjectType.Keys``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-keys
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnObjectType.KeyMapProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "keys"))

    @keys.setter
    def keys(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnObjectType.KeyMapProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "keys", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="objectTypeName")
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.ObjectTypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-objecttypename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeName"))

    @object_type_name.setter
    def object_type_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "objectTypeName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateId")
    def template_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.TemplateId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-templateid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateId"))

    @template_id.setter
    def template_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "templateId", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_customerprofiles.CfnObjectType.FieldMapProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "object_type_field": "objectTypeField"},
    )
    class FieldMapProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            object_type_field: typing.Optional[typing.Union["CfnObjectType.ObjectTypeFieldProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''
            :param name: ``CfnObjectType.FieldMapProperty.Name``.
            :param object_type_field: ``CfnObjectType.FieldMapProperty.ObjectTypeField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if object_type_field is not None:
                self._values["object_type_field"] = object_type_field

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnObjectType.FieldMapProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_type_field(
            self,
        ) -> typing.Optional[typing.Union["CfnObjectType.ObjectTypeFieldProperty", _IResolvable_a771d0ef]]:
            '''``CfnObjectType.FieldMapProperty.ObjectTypeField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-objecttypefield
            '''
            result = self._values.get("object_type_field")
            return typing.cast(typing.Optional[typing.Union["CfnObjectType.ObjectTypeFieldProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_customerprofiles.CfnObjectType.KeyMapProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "object_type_key_list": "objectTypeKeyList"},
    )
    class KeyMapProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            object_type_key_list: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnObjectType.ObjectTypeKeyProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            '''
            :param name: ``CfnObjectType.KeyMapProperty.Name``.
            :param object_type_key_list: ``CfnObjectType.KeyMapProperty.ObjectTypeKeyList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if object_type_key_list is not None:
                self._values["object_type_key_list"] = object_type_key_list

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnObjectType.KeyMapProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_type_key_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnObjectType.ObjectTypeKeyProperty", _IResolvable_a771d0ef]]]]:
            '''``CfnObjectType.KeyMapProperty.ObjectTypeKeyList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-objecttypekeylist
            '''
            result = self._values.get("object_type_key_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnObjectType.ObjectTypeKeyProperty", _IResolvable_a771d0ef]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_customerprofiles.CfnObjectType.ObjectTypeFieldProperty",
        jsii_struct_bases=[],
        name_mapping={
            "content_type": "contentType",
            "source": "source",
            "target": "target",
        },
    )
    class ObjectTypeFieldProperty:
        def __init__(
            self,
            *,
            content_type: typing.Optional[builtins.str] = None,
            source: typing.Optional[builtins.str] = None,
            target: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param content_type: ``CfnObjectType.ObjectTypeFieldProperty.ContentType``.
            :param source: ``CfnObjectType.ObjectTypeFieldProperty.Source``.
            :param target: ``CfnObjectType.ObjectTypeFieldProperty.Target``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if content_type is not None:
                self._values["content_type"] = content_type
            if source is not None:
                self._values["source"] = source
            if target is not None:
                self._values["target"] = target

        @builtins.property
        def content_type(self) -> typing.Optional[builtins.str]:
            '''``CfnObjectType.ObjectTypeFieldProperty.ContentType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-contenttype
            '''
            result = self._values.get("content_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''``CfnObjectType.ObjectTypeFieldProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target(self) -> typing.Optional[builtins.str]:
            '''``CfnObjectType.ObjectTypeFieldProperty.Target``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-target
            '''
            result = self._values.get("target")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectTypeFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_customerprofiles.CfnObjectType.ObjectTypeKeyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_names": "fieldNames",
            "standard_identifiers": "standardIdentifiers",
        },
    )
    class ObjectTypeKeyProperty:
        def __init__(
            self,
            *,
            field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            standard_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param field_names: ``CfnObjectType.ObjectTypeKeyProperty.FieldNames``.
            :param standard_identifiers: ``CfnObjectType.ObjectTypeKeyProperty.StandardIdentifiers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if field_names is not None:
                self._values["field_names"] = field_names
            if standard_identifiers is not None:
                self._values["standard_identifiers"] = standard_identifiers

        @builtins.property
        def field_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnObjectType.ObjectTypeKeyProperty.FieldNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-fieldnames
            '''
            result = self._values.get("field_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def standard_identifiers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnObjectType.ObjectTypeKeyProperty.StandardIdentifiers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-standardidentifiers
            '''
            result = self._values.get("standard_identifiers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectTypeKeyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_customerprofiles.CfnObjectTypeProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "allow_profile_creation": "allowProfileCreation",
        "description": "description",
        "encryption_key": "encryptionKey",
        "expiration_days": "expirationDays",
        "fields": "fields",
        "keys": "keys",
        "object_type_name": "objectTypeName",
        "tags": "tags",
        "template_id": "templateId",
    },
)
class CfnObjectTypeProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        allow_profile_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        expiration_days: typing.Optional[jsii.Number] = None,
        fields: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnObjectType.FieldMapProperty, _IResolvable_a771d0ef]]]] = None,
        keys: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnObjectType.KeyMapProperty, _IResolvable_a771d0ef]]]] = None,
        object_type_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CustomerProfiles::ObjectType``.

        :param domain_name: ``AWS::CustomerProfiles::ObjectType.DomainName``.
        :param allow_profile_creation: ``AWS::CustomerProfiles::ObjectType.AllowProfileCreation``.
        :param description: ``AWS::CustomerProfiles::ObjectType.Description``.
        :param encryption_key: ``AWS::CustomerProfiles::ObjectType.EncryptionKey``.
        :param expiration_days: ``AWS::CustomerProfiles::ObjectType.ExpirationDays``.
        :param fields: ``AWS::CustomerProfiles::ObjectType.Fields``.
        :param keys: ``AWS::CustomerProfiles::ObjectType.Keys``.
        :param object_type_name: ``AWS::CustomerProfiles::ObjectType.ObjectTypeName``.
        :param tags: ``AWS::CustomerProfiles::ObjectType.Tags``.
        :param template_id: ``AWS::CustomerProfiles::ObjectType.TemplateId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
        }
        if allow_profile_creation is not None:
            self._values["allow_profile_creation"] = allow_profile_creation
        if description is not None:
            self._values["description"] = description
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if expiration_days is not None:
            self._values["expiration_days"] = expiration_days
        if fields is not None:
            self._values["fields"] = fields
        if keys is not None:
            self._values["keys"] = keys
        if object_type_name is not None:
            self._values["object_type_name"] = object_type_name
        if tags is not None:
            self._values["tags"] = tags
        if template_id is not None:
            self._values["template_id"] = template_id

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''``AWS::CustomerProfiles::ObjectType.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_profile_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''``AWS::CustomerProfiles::ObjectType.AllowProfileCreation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-allowprofilecreation
        '''
        result = self._values.get("allow_profile_creation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.EncryptionKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-encryptionkey
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiration_days(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CustomerProfiles::ObjectType.ExpirationDays``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-expirationdays
        '''
        result = self._values.get("expiration_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fields(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnObjectType.FieldMapProperty, _IResolvable_a771d0ef]]]]:
        '''``AWS::CustomerProfiles::ObjectType.Fields``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-fields
        '''
        result = self._values.get("fields")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnObjectType.FieldMapProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def keys(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnObjectType.KeyMapProperty, _IResolvable_a771d0ef]]]]:
        '''``AWS::CustomerProfiles::ObjectType.Keys``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-keys
        '''
        result = self._values.get("keys")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnObjectType.KeyMapProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.ObjectTypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-objecttypename
        '''
        result = self._values.get("object_type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::CustomerProfiles::ObjectType.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CustomerProfiles::ObjectType.TemplateId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-templateid
        '''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnObjectTypeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDomain",
    "CfnDomainProps",
    "CfnIntegration",
    "CfnIntegrationProps",
    "CfnObjectType",
    "CfnObjectTypeProps",
]

publication.publish()
