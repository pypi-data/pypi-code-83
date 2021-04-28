'''
# AWS Systems Manager Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Installation

Install the module:

```console
$ npm i @aws-cdk/aws-ssm
```

Import it into your code:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk import aws_ssm as ssm
```

## Using existing SSM Parameters in your CDK app

You can reference existing SSM Parameter Store values that you want to use in
your CDK app by using `ssm.ParameterStoreString`:

[using SSM parameter](test/integ.parameter-store-string.lit.ts)

## Creating new SSM Parameters in your CDK app

You can create either `ssm.StringParameter` or `ssm.StringListParameter`s in
a CDK app. These are public (not secret) values. Parameters of type
*SecretString* cannot be created directly from a CDK application; if you want
to provision secrets automatically, use Secrets Manager Secrets (see the
`@aws-cdk/aws-secretsmanager` package).

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
ssm.StringParameter(stack, "Parameter",
    allowed_pattern=".*",
    description="The value Foo",
    parameter_name="FooParameter",
    string_value="Foo",
    tier=ssm.ParameterTier.ADVANCED
)
```

[creating SSM parameters](test/integ.parameter.lit.ts)

When specifying an `allowedPattern`, the values provided as string literals
are validated against the pattern and an exception is raised if a value
provided does not comply.
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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_iam import Grant as _Grant_a7ae64f8, IGrantable as _IGrantable_71c4f5de
from ..aws_kms import IKey as _IKey_5f11635f


@jsii.implements(_IInspectable_c2943556)
class CfnAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation",
):
    '''A CloudFormation ``AWS::SSM::Association``.

    :cloudformationResource: AWS::SSM::Association
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        apply_only_at_cron_interval: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        association_name: typing.Optional[builtins.str] = None,
        automation_target_parameter_name: typing.Optional[builtins.str] = None,
        compliance_severity: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        output_location: typing.Optional[typing.Union["CfnAssociation.InstanceAssociationOutputLocationProperty", _IResolvable_da3f097b]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Sequence[builtins.str]]]] = None,
        schedule_expression: typing.Optional[builtins.str] = None,
        sync_compliance: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnAssociation.TargetProperty", _IResolvable_da3f097b]]]] = None,
        wait_for_success_timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::Association``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::SSM::Association.Name``.
        :param apply_only_at_cron_interval: ``AWS::SSM::Association.ApplyOnlyAtCronInterval``.
        :param association_name: ``AWS::SSM::Association.AssociationName``.
        :param automation_target_parameter_name: ``AWS::SSM::Association.AutomationTargetParameterName``.
        :param compliance_severity: ``AWS::SSM::Association.ComplianceSeverity``.
        :param document_version: ``AWS::SSM::Association.DocumentVersion``.
        :param instance_id: ``AWS::SSM::Association.InstanceId``.
        :param max_concurrency: ``AWS::SSM::Association.MaxConcurrency``.
        :param max_errors: ``AWS::SSM::Association.MaxErrors``.
        :param output_location: ``AWS::SSM::Association.OutputLocation``.
        :param parameters: ``AWS::SSM::Association.Parameters``.
        :param schedule_expression: ``AWS::SSM::Association.ScheduleExpression``.
        :param sync_compliance: ``AWS::SSM::Association.SyncCompliance``.
        :param targets: ``AWS::SSM::Association.Targets``.
        :param wait_for_success_timeout_seconds: ``AWS::SSM::Association.WaitForSuccessTimeoutSeconds``.
        '''
        props = CfnAssociationProps(
            name=name,
            apply_only_at_cron_interval=apply_only_at_cron_interval,
            association_name=association_name,
            automation_target_parameter_name=automation_target_parameter_name,
            compliance_severity=compliance_severity,
            document_version=document_version,
            instance_id=instance_id,
            max_concurrency=max_concurrency,
            max_errors=max_errors,
            output_location=output_location,
            parameters=parameters,
            schedule_expression=schedule_expression,
            sync_compliance=sync_compliance,
            targets=targets,
            wait_for_success_timeout_seconds=wait_for_success_timeout_seconds,
        )

        jsii.create(CfnAssociation, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrAssociationId")
    def attr_association_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssociationId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::SSM::Association.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applyOnlyAtCronInterval")
    def apply_only_at_cron_interval(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::SSM::Association.ApplyOnlyAtCronInterval``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-applyonlyatcroninterval
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "applyOnlyAtCronInterval"))

    @apply_only_at_cron_interval.setter
    def apply_only_at_cron_interval(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "applyOnlyAtCronInterval", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="associationName")
    def association_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.AssociationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-associationname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associationName"))

    @association_name.setter
    def association_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "associationName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="automationTargetParameterName")
    def automation_target_parameter_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.AutomationTargetParameterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-automationtargetparametername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "automationTargetParameterName"))

    @automation_target_parameter_name.setter
    def automation_target_parameter_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "automationTargetParameterName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="complianceSeverity")
    def compliance_severity(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.ComplianceSeverity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-complianceseverity
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "complianceSeverity"))

    @compliance_severity.setter
    def compliance_severity(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "complianceSeverity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="documentVersion")
    def document_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.DocumentVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-documentversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentVersion"))

    @document_version.setter
    def document_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "documentVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.InstanceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-instanceid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.MaxConcurrency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-maxconcurrency
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "maxConcurrency", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxErrors")
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.MaxErrors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-maxerrors
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxErrors"))

    @max_errors.setter
    def max_errors(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "maxErrors", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outputLocation")
    def output_location(
        self,
    ) -> typing.Optional[typing.Union["CfnAssociation.InstanceAssociationOutputLocationProperty", _IResolvable_da3f097b]]:
        '''``AWS::SSM::Association.OutputLocation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-outputlocation
        '''
        return typing.cast(typing.Optional[typing.Union["CfnAssociation.InstanceAssociationOutputLocationProperty", _IResolvable_da3f097b]], jsii.get(self, "outputLocation"))

    @output_location.setter
    def output_location(
        self,
        value: typing.Optional[typing.Union["CfnAssociation.InstanceAssociationOutputLocationProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "outputLocation", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.List[builtins.str]]]]:
        '''``AWS::SSM::Association.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-parameters
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.List[builtins.str]]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.List[builtins.str]]]],
    ) -> None:
        jsii.set(self, "parameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.ScheduleExpression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-scheduleexpression
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleExpression"))

    @schedule_expression.setter
    def schedule_expression(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "scheduleExpression", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="syncCompliance")
    def sync_compliance(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.SyncCompliance``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-synccompliance
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncCompliance"))

    @sync_compliance.setter
    def sync_compliance(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "syncCompliance", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnAssociation.TargetProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::SSM::Association.Targets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-targets
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnAssociation.TargetProperty", _IResolvable_da3f097b]]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnAssociation.TargetProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "targets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="waitForSuccessTimeoutSeconds")
    def wait_for_success_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::SSM::Association.WaitForSuccessTimeoutSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-waitforsuccesstimeoutseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitForSuccessTimeoutSeconds"))

    @wait_for_success_timeout_seconds.setter
    def wait_for_success_timeout_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        jsii.set(self, "waitForSuccessTimeoutSeconds", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation.InstanceAssociationOutputLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_location": "s3Location"},
    )
    class InstanceAssociationOutputLocationProperty:
        def __init__(
            self,
            *,
            s3_location: typing.Optional[typing.Union["CfnAssociation.S3OutputLocationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param s3_location: ``CfnAssociation.InstanceAssociationOutputLocationProperty.S3Location``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_location is not None:
                self._values["s3_location"] = s3_location

        @builtins.property
        def s3_location(
            self,
        ) -> typing.Optional[typing.Union["CfnAssociation.S3OutputLocationProperty", _IResolvable_da3f097b]]:
            '''``CfnAssociation.InstanceAssociationOutputLocationProperty.S3Location``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html#cfn-ssm-association-instanceassociationoutputlocation-s3location
            '''
            result = self._values.get("s3_location")
            return typing.cast(typing.Optional[typing.Union["CfnAssociation.S3OutputLocationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceAssociationOutputLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation.ParameterValuesProperty",
        jsii_struct_bases=[],
        name_mapping={"parameter_values": "parameterValues"},
    )
    class ParameterValuesProperty:
        def __init__(
            self,
            *,
            parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param parameter_values: ``CfnAssociation.ParameterValuesProperty.ParameterValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-parametervalues.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if parameter_values is not None:
                self._values["parameter_values"] = parameter_values

        @builtins.property
        def parameter_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnAssociation.ParameterValuesProperty.ParameterValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-parametervalues.html#cfn-ssm-association-parametervalues-parametervalues
            '''
            result = self._values.get("parameter_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterValuesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation.S3OutputLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "output_s3_bucket_name": "outputS3BucketName",
            "output_s3_key_prefix": "outputS3KeyPrefix",
            "output_s3_region": "outputS3Region",
        },
    )
    class S3OutputLocationProperty:
        def __init__(
            self,
            *,
            output_s3_bucket_name: typing.Optional[builtins.str] = None,
            output_s3_key_prefix: typing.Optional[builtins.str] = None,
            output_s3_region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param output_s3_bucket_name: ``CfnAssociation.S3OutputLocationProperty.OutputS3BucketName``.
            :param output_s3_key_prefix: ``CfnAssociation.S3OutputLocationProperty.OutputS3KeyPrefix``.
            :param output_s3_region: ``CfnAssociation.S3OutputLocationProperty.OutputS3Region``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if output_s3_bucket_name is not None:
                self._values["output_s3_bucket_name"] = output_s3_bucket_name
            if output_s3_key_prefix is not None:
                self._values["output_s3_key_prefix"] = output_s3_key_prefix
            if output_s3_region is not None:
                self._values["output_s3_region"] = output_s3_region

        @builtins.property
        def output_s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''``CfnAssociation.S3OutputLocationProperty.OutputS3BucketName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3bucketname
            '''
            result = self._values.get("output_s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnAssociation.S3OutputLocationProperty.OutputS3KeyPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3keyprefix
            '''
            result = self._values.get("output_s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_s3_region(self) -> typing.Optional[builtins.str]:
            '''``CfnAssociation.S3OutputLocationProperty.OutputS3Region``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3region
            '''
            result = self._values.get("output_s3_region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation.TargetProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class TargetProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param key: ``CfnAssociation.TargetProperty.Key``.
            :param values: ``CfnAssociation.TargetProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "values": values,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnAssociation.TargetProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html#cfn-ssm-association-target-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''``CfnAssociation.TargetProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html#cfn-ssm-association-target-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "apply_only_at_cron_interval": "applyOnlyAtCronInterval",
        "association_name": "associationName",
        "automation_target_parameter_name": "automationTargetParameterName",
        "compliance_severity": "complianceSeverity",
        "document_version": "documentVersion",
        "instance_id": "instanceId",
        "max_concurrency": "maxConcurrency",
        "max_errors": "maxErrors",
        "output_location": "outputLocation",
        "parameters": "parameters",
        "schedule_expression": "scheduleExpression",
        "sync_compliance": "syncCompliance",
        "targets": "targets",
        "wait_for_success_timeout_seconds": "waitForSuccessTimeoutSeconds",
    },
)
class CfnAssociationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        apply_only_at_cron_interval: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        association_name: typing.Optional[builtins.str] = None,
        automation_target_parameter_name: typing.Optional[builtins.str] = None,
        compliance_severity: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        output_location: typing.Optional[typing.Union[CfnAssociation.InstanceAssociationOutputLocationProperty, _IResolvable_da3f097b]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Sequence[builtins.str]]]] = None,
        schedule_expression: typing.Optional[builtins.str] = None,
        sync_compliance: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnAssociation.TargetProperty, _IResolvable_da3f097b]]]] = None,
        wait_for_success_timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SSM::Association``.

        :param name: ``AWS::SSM::Association.Name``.
        :param apply_only_at_cron_interval: ``AWS::SSM::Association.ApplyOnlyAtCronInterval``.
        :param association_name: ``AWS::SSM::Association.AssociationName``.
        :param automation_target_parameter_name: ``AWS::SSM::Association.AutomationTargetParameterName``.
        :param compliance_severity: ``AWS::SSM::Association.ComplianceSeverity``.
        :param document_version: ``AWS::SSM::Association.DocumentVersion``.
        :param instance_id: ``AWS::SSM::Association.InstanceId``.
        :param max_concurrency: ``AWS::SSM::Association.MaxConcurrency``.
        :param max_errors: ``AWS::SSM::Association.MaxErrors``.
        :param output_location: ``AWS::SSM::Association.OutputLocation``.
        :param parameters: ``AWS::SSM::Association.Parameters``.
        :param schedule_expression: ``AWS::SSM::Association.ScheduleExpression``.
        :param sync_compliance: ``AWS::SSM::Association.SyncCompliance``.
        :param targets: ``AWS::SSM::Association.Targets``.
        :param wait_for_success_timeout_seconds: ``AWS::SSM::Association.WaitForSuccessTimeoutSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if apply_only_at_cron_interval is not None:
            self._values["apply_only_at_cron_interval"] = apply_only_at_cron_interval
        if association_name is not None:
            self._values["association_name"] = association_name
        if automation_target_parameter_name is not None:
            self._values["automation_target_parameter_name"] = automation_target_parameter_name
        if compliance_severity is not None:
            self._values["compliance_severity"] = compliance_severity
        if document_version is not None:
            self._values["document_version"] = document_version
        if instance_id is not None:
            self._values["instance_id"] = instance_id
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_errors is not None:
            self._values["max_errors"] = max_errors
        if output_location is not None:
            self._values["output_location"] = output_location
        if parameters is not None:
            self._values["parameters"] = parameters
        if schedule_expression is not None:
            self._values["schedule_expression"] = schedule_expression
        if sync_compliance is not None:
            self._values["sync_compliance"] = sync_compliance
        if targets is not None:
            self._values["targets"] = targets
        if wait_for_success_timeout_seconds is not None:
            self._values["wait_for_success_timeout_seconds"] = wait_for_success_timeout_seconds

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::SSM::Association.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def apply_only_at_cron_interval(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::SSM::Association.ApplyOnlyAtCronInterval``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-applyonlyatcroninterval
        '''
        result = self._values.get("apply_only_at_cron_interval")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def association_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.AssociationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-associationname
        '''
        result = self._values.get("association_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automation_target_parameter_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.AutomationTargetParameterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-automationtargetparametername
        '''
        result = self._values.get("automation_target_parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compliance_severity(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.ComplianceSeverity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-complianceseverity
        '''
        result = self._values.get("compliance_severity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.DocumentVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-documentversion
        '''
        result = self._values.get("document_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.InstanceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-instanceid
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.MaxConcurrency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-maxconcurrency
        '''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.MaxErrors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-maxerrors
        '''
        result = self._values.get("max_errors")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_location(
        self,
    ) -> typing.Optional[typing.Union[CfnAssociation.InstanceAssociationOutputLocationProperty, _IResolvable_da3f097b]]:
        '''``AWS::SSM::Association.OutputLocation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-outputlocation
        '''
        result = self._values.get("output_location")
        return typing.cast(typing.Optional[typing.Union[CfnAssociation.InstanceAssociationOutputLocationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.List[builtins.str]]]]:
        '''``AWS::SSM::Association.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.List[builtins.str]]]], result)

    @builtins.property
    def schedule_expression(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.ScheduleExpression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-scheduleexpression
        '''
        result = self._values.get("schedule_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sync_compliance(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Association.SyncCompliance``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-synccompliance
        '''
        result = self._values.get("sync_compliance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnAssociation.TargetProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::SSM::Association.Targets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-targets
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnAssociation.TargetProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def wait_for_success_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::SSM::Association.WaitForSuccessTimeoutSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-waitforsuccesstimeoutseconds
        '''
        result = self._values.get("wait_for_success_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDocument(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnDocument",
):
    '''A CloudFormation ``AWS::SSM::Document``.

    :cloudformationResource: AWS::SSM::Document
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        content: typing.Any,
        document_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::Document``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param content: ``AWS::SSM::Document.Content``.
        :param document_type: ``AWS::SSM::Document.DocumentType``.
        :param name: ``AWS::SSM::Document.Name``.
        :param tags: ``AWS::SSM::Document.Tags``.
        '''
        props = CfnDocumentProps(
            content=content, document_type=document_type, name=name, tags=tags
        )

        jsii.create(CfnDocument, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::SSM::Document.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="content")
    def content(self) -> typing.Any:
        '''``AWS::SSM::Document.Content``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-content
        '''
        return typing.cast(typing.Any, jsii.get(self, "content"))

    @content.setter
    def content(self, value: typing.Any) -> None:
        jsii.set(self, "content", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="documentType")
    def document_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Document.DocumentType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-documenttype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentType"))

    @document_type.setter
    def document_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "documentType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Document.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnDocumentProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "document_type": "documentType",
        "name": "name",
        "tags": "tags",
    },
)
class CfnDocumentProps:
    def __init__(
        self,
        *,
        content: typing.Any,
        document_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SSM::Document``.

        :param content: ``AWS::SSM::Document.Content``.
        :param document_type: ``AWS::SSM::Document.DocumentType``.
        :param name: ``AWS::SSM::Document.Name``.
        :param tags: ``AWS::SSM::Document.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
        }
        if document_type is not None:
            self._values["document_type"] = document_type
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def content(self) -> typing.Any:
        '''``AWS::SSM::Document.Content``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def document_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Document.DocumentType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-documenttype
        '''
        result = self._values.get("document_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Document.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::SSM::Document.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMaintenanceWindow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindow",
):
    '''A CloudFormation ``AWS::SSM::MaintenanceWindow``.

    :cloudformationResource: AWS::SSM::MaintenanceWindow
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        allow_unassociated_targets: typing.Union[builtins.bool, _IResolvable_da3f097b],
        cutoff: jsii.Number,
        duration: jsii.Number,
        name: builtins.str,
        schedule: builtins.str,
        description: typing.Optional[builtins.str] = None,
        end_date: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        schedule_timezone: typing.Optional[builtins.str] = None,
        start_date: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::MaintenanceWindow``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param allow_unassociated_targets: ``AWS::SSM::MaintenanceWindow.AllowUnassociatedTargets``.
        :param cutoff: ``AWS::SSM::MaintenanceWindow.Cutoff``.
        :param duration: ``AWS::SSM::MaintenanceWindow.Duration``.
        :param name: ``AWS::SSM::MaintenanceWindow.Name``.
        :param schedule: ``AWS::SSM::MaintenanceWindow.Schedule``.
        :param description: ``AWS::SSM::MaintenanceWindow.Description``.
        :param end_date: ``AWS::SSM::MaintenanceWindow.EndDate``.
        :param schedule_offset: ``AWS::SSM::MaintenanceWindow.ScheduleOffset``.
        :param schedule_timezone: ``AWS::SSM::MaintenanceWindow.ScheduleTimezone``.
        :param start_date: ``AWS::SSM::MaintenanceWindow.StartDate``.
        :param tags: ``AWS::SSM::MaintenanceWindow.Tags``.
        '''
        props = CfnMaintenanceWindowProps(
            allow_unassociated_targets=allow_unassociated_targets,
            cutoff=cutoff,
            duration=duration,
            name=name,
            schedule=schedule,
            description=description,
            end_date=end_date,
            schedule_offset=schedule_offset,
            schedule_timezone=schedule_timezone,
            start_date=start_date,
            tags=tags,
        )

        jsii.create(CfnMaintenanceWindow, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::SSM::MaintenanceWindow.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="allowUnassociatedTargets")
    def allow_unassociated_targets(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''``AWS::SSM::MaintenanceWindow.AllowUnassociatedTargets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-allowunassociatedtargets
        '''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "allowUnassociatedTargets"))

    @allow_unassociated_targets.setter
    def allow_unassociated_targets(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        jsii.set(self, "allowUnassociatedTargets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cutoff")
    def cutoff(self) -> jsii.Number:
        '''``AWS::SSM::MaintenanceWindow.Cutoff``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-cutoff
        '''
        return typing.cast(jsii.Number, jsii.get(self, "cutoff"))

    @cutoff.setter
    def cutoff(self, value: jsii.Number) -> None:
        jsii.set(self, "cutoff", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        '''``AWS::SSM::MaintenanceWindow.Duration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-duration
        '''
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        jsii.set(self, "duration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindow.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindow.Schedule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-schedule
        '''
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        jsii.set(self, "schedule", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindow.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endDate")
    def end_date(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindow.EndDate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-enddate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endDate"))

    @end_date.setter
    def end_date(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endDate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scheduleOffset")
    def schedule_offset(self) -> typing.Optional[jsii.Number]:
        '''``AWS::SSM::MaintenanceWindow.ScheduleOffset``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduleoffset
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scheduleOffset"))

    @schedule_offset.setter
    def schedule_offset(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "scheduleOffset", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scheduleTimezone")
    def schedule_timezone(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindow.ScheduleTimezone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduletimezone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleTimezone"))

    @schedule_timezone.setter
    def schedule_timezone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "scheduleTimezone", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="startDate")
    def start_date(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindow.StartDate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-startdate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startDate"))

    @start_date.setter
    def start_date(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "startDate", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowProps",
    jsii_struct_bases=[],
    name_mapping={
        "allow_unassociated_targets": "allowUnassociatedTargets",
        "cutoff": "cutoff",
        "duration": "duration",
        "name": "name",
        "schedule": "schedule",
        "description": "description",
        "end_date": "endDate",
        "schedule_offset": "scheduleOffset",
        "schedule_timezone": "scheduleTimezone",
        "start_date": "startDate",
        "tags": "tags",
    },
)
class CfnMaintenanceWindowProps:
    def __init__(
        self,
        *,
        allow_unassociated_targets: typing.Union[builtins.bool, _IResolvable_da3f097b],
        cutoff: jsii.Number,
        duration: jsii.Number,
        name: builtins.str,
        schedule: builtins.str,
        description: typing.Optional[builtins.str] = None,
        end_date: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        schedule_timezone: typing.Optional[builtins.str] = None,
        start_date: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SSM::MaintenanceWindow``.

        :param allow_unassociated_targets: ``AWS::SSM::MaintenanceWindow.AllowUnassociatedTargets``.
        :param cutoff: ``AWS::SSM::MaintenanceWindow.Cutoff``.
        :param duration: ``AWS::SSM::MaintenanceWindow.Duration``.
        :param name: ``AWS::SSM::MaintenanceWindow.Name``.
        :param schedule: ``AWS::SSM::MaintenanceWindow.Schedule``.
        :param description: ``AWS::SSM::MaintenanceWindow.Description``.
        :param end_date: ``AWS::SSM::MaintenanceWindow.EndDate``.
        :param schedule_offset: ``AWS::SSM::MaintenanceWindow.ScheduleOffset``.
        :param schedule_timezone: ``AWS::SSM::MaintenanceWindow.ScheduleTimezone``.
        :param start_date: ``AWS::SSM::MaintenanceWindow.StartDate``.
        :param tags: ``AWS::SSM::MaintenanceWindow.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "allow_unassociated_targets": allow_unassociated_targets,
            "cutoff": cutoff,
            "duration": duration,
            "name": name,
            "schedule": schedule,
        }
        if description is not None:
            self._values["description"] = description
        if end_date is not None:
            self._values["end_date"] = end_date
        if schedule_offset is not None:
            self._values["schedule_offset"] = schedule_offset
        if schedule_timezone is not None:
            self._values["schedule_timezone"] = schedule_timezone
        if start_date is not None:
            self._values["start_date"] = start_date
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def allow_unassociated_targets(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''``AWS::SSM::MaintenanceWindow.AllowUnassociatedTargets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-allowunassociatedtargets
        '''
        result = self._values.get("allow_unassociated_targets")
        assert result is not None, "Required property 'allow_unassociated_targets' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def cutoff(self) -> jsii.Number:
        '''``AWS::SSM::MaintenanceWindow.Cutoff``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-cutoff
        '''
        result = self._values.get("cutoff")
        assert result is not None, "Required property 'cutoff' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def duration(self) -> jsii.Number:
        '''``AWS::SSM::MaintenanceWindow.Duration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-duration
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindow.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindow.Schedule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-schedule
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindow.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def end_date(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindow.EndDate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-enddate
        '''
        result = self._values.get("end_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_offset(self) -> typing.Optional[jsii.Number]:
        '''``AWS::SSM::MaintenanceWindow.ScheduleOffset``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduleoffset
        '''
        result = self._values.get("schedule_offset")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def schedule_timezone(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindow.ScheduleTimezone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduletimezone
        '''
        result = self._values.get("schedule_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_date(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindow.StartDate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-startdate
        '''
        result = self._values.get("start_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::SSM::MaintenanceWindow.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMaintenanceWindowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMaintenanceWindowTarget(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTarget",
):
    '''A CloudFormation ``AWS::SSM::MaintenanceWindowTarget``.

    :cloudformationResource: AWS::SSM::MaintenanceWindowTarget
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        resource_type: builtins.str,
        targets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnMaintenanceWindowTarget.TargetsProperty", _IResolvable_da3f097b]]],
        window_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        owner_information: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::MaintenanceWindowTarget``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_type: ``AWS::SSM::MaintenanceWindowTarget.ResourceType``.
        :param targets: ``AWS::SSM::MaintenanceWindowTarget.Targets``.
        :param window_id: ``AWS::SSM::MaintenanceWindowTarget.WindowId``.
        :param description: ``AWS::SSM::MaintenanceWindowTarget.Description``.
        :param name: ``AWS::SSM::MaintenanceWindowTarget.Name``.
        :param owner_information: ``AWS::SSM::MaintenanceWindowTarget.OwnerInformation``.
        '''
        props = CfnMaintenanceWindowTargetProps(
            resource_type=resource_type,
            targets=targets,
            window_id=window_id,
            description=description,
            name=name,
            owner_information=owner_information,
        )

        jsii.create(CfnMaintenanceWindowTarget, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindowTarget.ResourceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-resourcetype
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        jsii.set(self, "resourceType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMaintenanceWindowTarget.TargetsProperty", _IResolvable_da3f097b]]]:
        '''``AWS::SSM::MaintenanceWindowTarget.Targets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-targets
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMaintenanceWindowTarget.TargetsProperty", _IResolvable_da3f097b]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMaintenanceWindowTarget.TargetsProperty", _IResolvable_da3f097b]]],
    ) -> None:
        jsii.set(self, "targets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="windowId")
    def window_id(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindowTarget.WindowId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-windowid
        '''
        return typing.cast(builtins.str, jsii.get(self, "windowId"))

    @window_id.setter
    def window_id(self, value: builtins.str) -> None:
        jsii.set(self, "windowId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTarget.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTarget.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ownerInformation")
    def owner_information(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTarget.OwnerInformation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-ownerinformation
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInformation"))

    @owner_information.setter
    def owner_information(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "ownerInformation", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTarget.TargetsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class TargetsProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param key: ``CfnMaintenanceWindowTarget.TargetsProperty.Key``.
            :param values: ``CfnMaintenanceWindowTarget.TargetsProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "values": values,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnMaintenanceWindowTarget.TargetsProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html#cfn-ssm-maintenancewindowtarget-targets-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''``CfnMaintenanceWindowTarget.TargetsProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html#cfn-ssm-maintenancewindowtarget-targets-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_type": "resourceType",
        "targets": "targets",
        "window_id": "windowId",
        "description": "description",
        "name": "name",
        "owner_information": "ownerInformation",
    },
)
class CfnMaintenanceWindowTargetProps:
    def __init__(
        self,
        *,
        resource_type: builtins.str,
        targets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnMaintenanceWindowTarget.TargetsProperty, _IResolvable_da3f097b]]],
        window_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        owner_information: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SSM::MaintenanceWindowTarget``.

        :param resource_type: ``AWS::SSM::MaintenanceWindowTarget.ResourceType``.
        :param targets: ``AWS::SSM::MaintenanceWindowTarget.Targets``.
        :param window_id: ``AWS::SSM::MaintenanceWindowTarget.WindowId``.
        :param description: ``AWS::SSM::MaintenanceWindowTarget.Description``.
        :param name: ``AWS::SSM::MaintenanceWindowTarget.Name``.
        :param owner_information: ``AWS::SSM::MaintenanceWindowTarget.OwnerInformation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resource_type": resource_type,
            "targets": targets,
            "window_id": window_id,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if owner_information is not None:
            self._values["owner_information"] = owner_information

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindowTarget.ResourceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-resourcetype
        '''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnMaintenanceWindowTarget.TargetsProperty, _IResolvable_da3f097b]]]:
        '''``AWS::SSM::MaintenanceWindowTarget.Targets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-targets
        '''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnMaintenanceWindowTarget.TargetsProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def window_id(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindowTarget.WindowId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-windowid
        '''
        result = self._values.get("window_id")
        assert result is not None, "Required property 'window_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTarget.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTarget.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner_information(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTarget.OwnerInformation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-ownerinformation
        '''
        result = self._values.get("owner_information")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMaintenanceWindowTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMaintenanceWindowTask(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask",
):
    '''A CloudFormation ``AWS::SSM::MaintenanceWindowTask``.

    :cloudformationResource: AWS::SSM::MaintenanceWindowTask
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        priority: jsii.Number,
        task_arn: builtins.str,
        task_type: builtins.str,
        window_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        logging_info: typing.Optional[typing.Union["CfnMaintenanceWindowTask.LoggingInfoProperty", _IResolvable_da3f097b]] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnMaintenanceWindowTask.TargetProperty", _IResolvable_da3f097b]]]] = None,
        task_invocation_parameters: typing.Optional[typing.Union["CfnMaintenanceWindowTask.TaskInvocationParametersProperty", _IResolvable_da3f097b]] = None,
        task_parameters: typing.Any = None,
    ) -> None:
        '''Create a new ``AWS::SSM::MaintenanceWindowTask``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param priority: ``AWS::SSM::MaintenanceWindowTask.Priority``.
        :param task_arn: ``AWS::SSM::MaintenanceWindowTask.TaskArn``.
        :param task_type: ``AWS::SSM::MaintenanceWindowTask.TaskType``.
        :param window_id: ``AWS::SSM::MaintenanceWindowTask.WindowId``.
        :param description: ``AWS::SSM::MaintenanceWindowTask.Description``.
        :param logging_info: ``AWS::SSM::MaintenanceWindowTask.LoggingInfo``.
        :param max_concurrency: ``AWS::SSM::MaintenanceWindowTask.MaxConcurrency``.
        :param max_errors: ``AWS::SSM::MaintenanceWindowTask.MaxErrors``.
        :param name: ``AWS::SSM::MaintenanceWindowTask.Name``.
        :param service_role_arn: ``AWS::SSM::MaintenanceWindowTask.ServiceRoleArn``.
        :param targets: ``AWS::SSM::MaintenanceWindowTask.Targets``.
        :param task_invocation_parameters: ``AWS::SSM::MaintenanceWindowTask.TaskInvocationParameters``.
        :param task_parameters: ``AWS::SSM::MaintenanceWindowTask.TaskParameters``.
        '''
        props = CfnMaintenanceWindowTaskProps(
            priority=priority,
            task_arn=task_arn,
            task_type=task_type,
            window_id=window_id,
            description=description,
            logging_info=logging_info,
            max_concurrency=max_concurrency,
            max_errors=max_errors,
            name=name,
            service_role_arn=service_role_arn,
            targets=targets,
            task_invocation_parameters=task_invocation_parameters,
            task_parameters=task_parameters,
        )

        jsii.create(CfnMaintenanceWindowTask, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        '''``AWS::SSM::MaintenanceWindowTask.Priority``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-priority
        '''
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        jsii.set(self, "priority", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="taskArn")
    def task_arn(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindowTask.TaskArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "taskArn"))

    @task_arn.setter
    def task_arn(self, value: builtins.str) -> None:
        jsii.set(self, "taskArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="taskParameters")
    def task_parameters(self) -> typing.Any:
        '''``AWS::SSM::MaintenanceWindowTask.TaskParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskparameters
        '''
        return typing.cast(typing.Any, jsii.get(self, "taskParameters"))

    @task_parameters.setter
    def task_parameters(self, value: typing.Any) -> None:
        jsii.set(self, "taskParameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindowTask.TaskType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-tasktype
        '''
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        jsii.set(self, "taskType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="windowId")
    def window_id(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindowTask.WindowId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-windowid
        '''
        return typing.cast(builtins.str, jsii.get(self, "windowId"))

    @window_id.setter
    def window_id(self, value: builtins.str) -> None:
        jsii.set(self, "windowId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTask.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loggingInfo")
    def logging_info(
        self,
    ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.LoggingInfoProperty", _IResolvable_da3f097b]]:
        '''``AWS::SSM::MaintenanceWindowTask.LoggingInfo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-logginginfo
        '''
        return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.LoggingInfoProperty", _IResolvable_da3f097b]], jsii.get(self, "loggingInfo"))

    @logging_info.setter
    def logging_info(
        self,
        value: typing.Optional[typing.Union["CfnMaintenanceWindowTask.LoggingInfoProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "loggingInfo", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTask.MaxConcurrency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxconcurrency
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "maxConcurrency", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxErrors")
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTask.MaxErrors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxerrors
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxErrors"))

    @max_errors.setter
    def max_errors(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "maxErrors", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTask.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTask.ServiceRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-servicerolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMaintenanceWindowTask.TargetProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::SSM::MaintenanceWindowTask.Targets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-targets
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMaintenanceWindowTask.TargetProperty", _IResolvable_da3f097b]]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMaintenanceWindowTask.TargetProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "targets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="taskInvocationParameters")
    def task_invocation_parameters(
        self,
    ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.TaskInvocationParametersProperty", _IResolvable_da3f097b]]:
        '''``AWS::SSM::MaintenanceWindowTask.TaskInvocationParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters
        '''
        return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.TaskInvocationParametersProperty", _IResolvable_da3f097b]], jsii.get(self, "taskInvocationParameters"))

    @task_invocation_parameters.setter
    def task_invocation_parameters(
        self,
        value: typing.Optional[typing.Union["CfnMaintenanceWindowTask.TaskInvocationParametersProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "taskInvocationParameters", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.LoggingInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region": "region",
            "s3_bucket": "s3Bucket",
            "s3_prefix": "s3Prefix",
        },
    )
    class LoggingInfoProperty:
        def __init__(
            self,
            *,
            region: builtins.str,
            s3_bucket: builtins.str,
            s3_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param region: ``CfnMaintenanceWindowTask.LoggingInfoProperty.Region``.
            :param s3_bucket: ``CfnMaintenanceWindowTask.LoggingInfoProperty.S3Bucket``.
            :param s3_prefix: ``CfnMaintenanceWindowTask.LoggingInfoProperty.S3Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "region": region,
                "s3_bucket": s3_bucket,
            }
            if s3_prefix is not None:
                self._values["s3_prefix"] = s3_prefix

        @builtins.property
        def region(self) -> builtins.str:
            '''``CfnMaintenanceWindowTask.LoggingInfoProperty.Region``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''``CfnMaintenanceWindowTask.LoggingInfoProperty.S3Bucket``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.LoggingInfoProperty.S3Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-s3prefix
            '''
            result = self._values.get("s3_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_version": "documentVersion",
            "parameters": "parameters",
        },
    )
    class MaintenanceWindowAutomationParametersProperty:
        def __init__(
            self,
            *,
            document_version: typing.Optional[builtins.str] = None,
            parameters: typing.Any = None,
        ) -> None:
            '''
            :param document_version: ``CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty.DocumentVersion``.
            :param parameters: ``CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if document_version is not None:
                self._values["document_version"] = document_version
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def document_version(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty.DocumentVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowautomationparameters-documentversion
            '''
            result = self._values.get("document_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowautomationparameters-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowAutomationParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_context": "clientContext",
            "payload": "payload",
            "qualifier": "qualifier",
        },
    )
    class MaintenanceWindowLambdaParametersProperty:
        def __init__(
            self,
            *,
            client_context: typing.Optional[builtins.str] = None,
            payload: typing.Optional[builtins.str] = None,
            qualifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param client_context: ``CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty.ClientContext``.
            :param payload: ``CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty.Payload``.
            :param qualifier: ``CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty.Qualifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if client_context is not None:
                self._values["client_context"] = client_context
            if payload is not None:
                self._values["payload"] = payload
            if qualifier is not None:
                self._values["qualifier"] = qualifier

        @builtins.property
        def client_context(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty.ClientContext``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-clientcontext
            '''
            result = self._values.get("client_context")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def payload(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def qualifier(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty.Qualifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-qualifier
            '''
            result = self._values.get("qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowLambdaParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comment": "comment",
            "document_hash": "documentHash",
            "document_hash_type": "documentHashType",
            "notification_config": "notificationConfig",
            "output_s3_bucket_name": "outputS3BucketName",
            "output_s3_key_prefix": "outputS3KeyPrefix",
            "parameters": "parameters",
            "service_role_arn": "serviceRoleArn",
            "timeout_seconds": "timeoutSeconds",
        },
    )
    class MaintenanceWindowRunCommandParametersProperty:
        def __init__(
            self,
            *,
            comment: typing.Optional[builtins.str] = None,
            document_hash: typing.Optional[builtins.str] = None,
            document_hash_type: typing.Optional[builtins.str] = None,
            notification_config: typing.Optional[typing.Union["CfnMaintenanceWindowTask.NotificationConfigProperty", _IResolvable_da3f097b]] = None,
            output_s3_bucket_name: typing.Optional[builtins.str] = None,
            output_s3_key_prefix: typing.Optional[builtins.str] = None,
            parameters: typing.Any = None,
            service_role_arn: typing.Optional[builtins.str] = None,
            timeout_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param comment: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.Comment``.
            :param document_hash: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.DocumentHash``.
            :param document_hash_type: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.DocumentHashType``.
            :param notification_config: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.NotificationConfig``.
            :param output_s3_bucket_name: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.OutputS3BucketName``.
            :param output_s3_key_prefix: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.OutputS3KeyPrefix``.
            :param parameters: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.Parameters``.
            :param service_role_arn: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.ServiceRoleArn``.
            :param timeout_seconds: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.TimeoutSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if comment is not None:
                self._values["comment"] = comment
            if document_hash is not None:
                self._values["document_hash"] = document_hash
            if document_hash_type is not None:
                self._values["document_hash_type"] = document_hash_type
            if notification_config is not None:
                self._values["notification_config"] = notification_config
            if output_s3_bucket_name is not None:
                self._values["output_s3_bucket_name"] = output_s3_bucket_name
            if output_s3_key_prefix is not None:
                self._values["output_s3_key_prefix"] = output_s3_key_prefix
            if parameters is not None:
                self._values["parameters"] = parameters
            if service_role_arn is not None:
                self._values["service_role_arn"] = service_role_arn
            if timeout_seconds is not None:
                self._values["timeout_seconds"] = timeout_seconds

        @builtins.property
        def comment(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.Comment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-comment
            '''
            result = self._values.get("comment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_hash(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.DocumentHash``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documenthash
            '''
            result = self._values.get("document_hash")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_hash_type(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.DocumentHashType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documenthashtype
            '''
            result = self._values.get("document_hash_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def notification_config(
            self,
        ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.NotificationConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.NotificationConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-notificationconfig
            '''
            result = self._values.get("notification_config")
            return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.NotificationConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def output_s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.OutputS3BucketName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-outputs3bucketname
            '''
            result = self._values.get("output_s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.OutputS3KeyPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-outputs3keyprefix
            '''
            result = self._values.get("output_s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def service_role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.ServiceRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-servicerolearn
            '''
            result = self._values.get("service_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.TimeoutSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-timeoutseconds
            '''
            result = self._values.get("timeout_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowRunCommandParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"input": "input", "name": "name"},
    )
    class MaintenanceWindowStepFunctionsParametersProperty:
        def __init__(
            self,
            *,
            input: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param input: ``CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty.Input``.
            :param name: ``CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if input is not None:
                self._values["input"] = input
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def input(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty.Input``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowStepFunctionsParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.NotificationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "notification_arn": "notificationArn",
            "notification_events": "notificationEvents",
            "notification_type": "notificationType",
        },
    )
    class NotificationConfigProperty:
        def __init__(
            self,
            *,
            notification_arn: builtins.str,
            notification_events: typing.Optional[typing.Sequence[builtins.str]] = None,
            notification_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param notification_arn: ``CfnMaintenanceWindowTask.NotificationConfigProperty.NotificationArn``.
            :param notification_events: ``CfnMaintenanceWindowTask.NotificationConfigProperty.NotificationEvents``.
            :param notification_type: ``CfnMaintenanceWindowTask.NotificationConfigProperty.NotificationType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "notification_arn": notification_arn,
            }
            if notification_events is not None:
                self._values["notification_events"] = notification_events
            if notification_type is not None:
                self._values["notification_type"] = notification_type

        @builtins.property
        def notification_arn(self) -> builtins.str:
            '''``CfnMaintenanceWindowTask.NotificationConfigProperty.NotificationArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationarn
            '''
            result = self._values.get("notification_arn")
            assert result is not None, "Required property 'notification_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def notification_events(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnMaintenanceWindowTask.NotificationConfigProperty.NotificationEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationevents
            '''
            result = self._values.get("notification_events")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def notification_type(self) -> typing.Optional[builtins.str]:
            '''``CfnMaintenanceWindowTask.NotificationConfigProperty.NotificationType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationtype
            '''
            result = self._values.get("notification_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.TargetProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class TargetProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param key: ``CfnMaintenanceWindowTask.TargetProperty.Key``.
            :param values: ``CfnMaintenanceWindowTask.TargetProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "values": values,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnMaintenanceWindowTask.TargetProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html#cfn-ssm-maintenancewindowtask-target-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''``CfnMaintenanceWindowTask.TargetProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html#cfn-ssm-maintenancewindowtask-target-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.TaskInvocationParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maintenance_window_automation_parameters": "maintenanceWindowAutomationParameters",
            "maintenance_window_lambda_parameters": "maintenanceWindowLambdaParameters",
            "maintenance_window_run_command_parameters": "maintenanceWindowRunCommandParameters",
            "maintenance_window_step_functions_parameters": "maintenanceWindowStepFunctionsParameters",
        },
    )
    class TaskInvocationParametersProperty:
        def __init__(
            self,
            *,
            maintenance_window_automation_parameters: typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty", _IResolvable_da3f097b]] = None,
            maintenance_window_lambda_parameters: typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty", _IResolvable_da3f097b]] = None,
            maintenance_window_run_command_parameters: typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty", _IResolvable_da3f097b]] = None,
            maintenance_window_step_functions_parameters: typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param maintenance_window_automation_parameters: ``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowAutomationParameters``.
            :param maintenance_window_lambda_parameters: ``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowLambdaParameters``.
            :param maintenance_window_run_command_parameters: ``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowRunCommandParameters``.
            :param maintenance_window_step_functions_parameters: ``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowStepFunctionsParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if maintenance_window_automation_parameters is not None:
                self._values["maintenance_window_automation_parameters"] = maintenance_window_automation_parameters
            if maintenance_window_lambda_parameters is not None:
                self._values["maintenance_window_lambda_parameters"] = maintenance_window_lambda_parameters
            if maintenance_window_run_command_parameters is not None:
                self._values["maintenance_window_run_command_parameters"] = maintenance_window_run_command_parameters
            if maintenance_window_step_functions_parameters is not None:
                self._values["maintenance_window_step_functions_parameters"] = maintenance_window_step_functions_parameters

        @builtins.property
        def maintenance_window_automation_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty", _IResolvable_da3f097b]]:
            '''``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowAutomationParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowautomationparameters
            '''
            result = self._values.get("maintenance_window_automation_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def maintenance_window_lambda_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty", _IResolvable_da3f097b]]:
            '''``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowLambdaParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowlambdaparameters
            '''
            result = self._values.get("maintenance_window_lambda_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def maintenance_window_run_command_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty", _IResolvable_da3f097b]]:
            '''``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowRunCommandParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowruncommandparameters
            '''
            result = self._values.get("maintenance_window_run_command_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def maintenance_window_step_functions_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty", _IResolvable_da3f097b]]:
            '''``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowStepFunctionsParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowstepfunctionsparameters
            '''
            result = self._values.get("maintenance_window_step_functions_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskInvocationParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "priority": "priority",
        "task_arn": "taskArn",
        "task_type": "taskType",
        "window_id": "windowId",
        "description": "description",
        "logging_info": "loggingInfo",
        "max_concurrency": "maxConcurrency",
        "max_errors": "maxErrors",
        "name": "name",
        "service_role_arn": "serviceRoleArn",
        "targets": "targets",
        "task_invocation_parameters": "taskInvocationParameters",
        "task_parameters": "taskParameters",
    },
)
class CfnMaintenanceWindowTaskProps:
    def __init__(
        self,
        *,
        priority: jsii.Number,
        task_arn: builtins.str,
        task_type: builtins.str,
        window_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        logging_info: typing.Optional[typing.Union[CfnMaintenanceWindowTask.LoggingInfoProperty, _IResolvable_da3f097b]] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnMaintenanceWindowTask.TargetProperty, _IResolvable_da3f097b]]]] = None,
        task_invocation_parameters: typing.Optional[typing.Union[CfnMaintenanceWindowTask.TaskInvocationParametersProperty, _IResolvable_da3f097b]] = None,
        task_parameters: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``AWS::SSM::MaintenanceWindowTask``.

        :param priority: ``AWS::SSM::MaintenanceWindowTask.Priority``.
        :param task_arn: ``AWS::SSM::MaintenanceWindowTask.TaskArn``.
        :param task_type: ``AWS::SSM::MaintenanceWindowTask.TaskType``.
        :param window_id: ``AWS::SSM::MaintenanceWindowTask.WindowId``.
        :param description: ``AWS::SSM::MaintenanceWindowTask.Description``.
        :param logging_info: ``AWS::SSM::MaintenanceWindowTask.LoggingInfo``.
        :param max_concurrency: ``AWS::SSM::MaintenanceWindowTask.MaxConcurrency``.
        :param max_errors: ``AWS::SSM::MaintenanceWindowTask.MaxErrors``.
        :param name: ``AWS::SSM::MaintenanceWindowTask.Name``.
        :param service_role_arn: ``AWS::SSM::MaintenanceWindowTask.ServiceRoleArn``.
        :param targets: ``AWS::SSM::MaintenanceWindowTask.Targets``.
        :param task_invocation_parameters: ``AWS::SSM::MaintenanceWindowTask.TaskInvocationParameters``.
        :param task_parameters: ``AWS::SSM::MaintenanceWindowTask.TaskParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "priority": priority,
            "task_arn": task_arn,
            "task_type": task_type,
            "window_id": window_id,
        }
        if description is not None:
            self._values["description"] = description
        if logging_info is not None:
            self._values["logging_info"] = logging_info
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_errors is not None:
            self._values["max_errors"] = max_errors
        if name is not None:
            self._values["name"] = name
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn
        if targets is not None:
            self._values["targets"] = targets
        if task_invocation_parameters is not None:
            self._values["task_invocation_parameters"] = task_invocation_parameters
        if task_parameters is not None:
            self._values["task_parameters"] = task_parameters

    @builtins.property
    def priority(self) -> jsii.Number:
        '''``AWS::SSM::MaintenanceWindowTask.Priority``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-priority
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def task_arn(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindowTask.TaskArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskarn
        '''
        result = self._values.get("task_arn")
        assert result is not None, "Required property 'task_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_type(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindowTask.TaskType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-tasktype
        '''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def window_id(self) -> builtins.str:
        '''``AWS::SSM::MaintenanceWindowTask.WindowId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-windowid
        '''
        result = self._values.get("window_id")
        assert result is not None, "Required property 'window_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTask.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_info(
        self,
    ) -> typing.Optional[typing.Union[CfnMaintenanceWindowTask.LoggingInfoProperty, _IResolvable_da3f097b]]:
        '''``AWS::SSM::MaintenanceWindowTask.LoggingInfo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-logginginfo
        '''
        result = self._values.get("logging_info")
        return typing.cast(typing.Optional[typing.Union[CfnMaintenanceWindowTask.LoggingInfoProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTask.MaxConcurrency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxconcurrency
        '''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTask.MaxErrors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxerrors
        '''
        result = self._values.get("max_errors")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTask.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::MaintenanceWindowTask.ServiceRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-servicerolearn
        '''
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnMaintenanceWindowTask.TargetProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::SSM::MaintenanceWindowTask.Targets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-targets
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnMaintenanceWindowTask.TargetProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def task_invocation_parameters(
        self,
    ) -> typing.Optional[typing.Union[CfnMaintenanceWindowTask.TaskInvocationParametersProperty, _IResolvable_da3f097b]]:
        '''``AWS::SSM::MaintenanceWindowTask.TaskInvocationParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters
        '''
        result = self._values.get("task_invocation_parameters")
        return typing.cast(typing.Optional[typing.Union[CfnMaintenanceWindowTask.TaskInvocationParametersProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def task_parameters(self) -> typing.Any:
        '''``AWS::SSM::MaintenanceWindowTask.TaskParameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskparameters
        '''
        result = self._values.get("task_parameters")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMaintenanceWindowTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnParameter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnParameter",
):
    '''A CloudFormation ``AWS::SSM::Parameter``.

    :cloudformationResource: AWS::SSM::Parameter
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        type: builtins.str,
        value: builtins.str,
        allowed_pattern: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        policies: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        tier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::Parameter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param type: ``AWS::SSM::Parameter.Type``.
        :param value: ``AWS::SSM::Parameter.Value``.
        :param allowed_pattern: ``AWS::SSM::Parameter.AllowedPattern``.
        :param data_type: ``AWS::SSM::Parameter.DataType``.
        :param description: ``AWS::SSM::Parameter.Description``.
        :param name: ``AWS::SSM::Parameter.Name``.
        :param policies: ``AWS::SSM::Parameter.Policies``.
        :param tags: ``AWS::SSM::Parameter.Tags``.
        :param tier: ``AWS::SSM::Parameter.Tier``.
        '''
        props = CfnParameterProps(
            type=type,
            value=value,
            allowed_pattern=allowed_pattern,
            data_type=data_type,
            description=description,
            name=name,
            policies=policies,
            tags=tags,
            tier=tier,
        )

        jsii.create(CfnParameter, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrValue")
    def attr_value(self) -> builtins.str:
        '''
        :cloudformationAttribute: Value
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::SSM::Parameter.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''``AWS::SSM::Parameter.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''``AWS::SSM::Parameter.Value``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-value
        '''
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        jsii.set(self, "value", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="allowedPattern")
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Parameter.AllowedPattern``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-allowedpattern
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedPattern"))

    @allowed_pattern.setter
    def allowed_pattern(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "allowedPattern", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Parameter.DataType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-datatype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dataType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Parameter.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Parameter.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Parameter.Policies``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-policies
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "policies", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tier")
    def tier(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Parameter.Tier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tier", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnParameterProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "value": "value",
        "allowed_pattern": "allowedPattern",
        "data_type": "dataType",
        "description": "description",
        "name": "name",
        "policies": "policies",
        "tags": "tags",
        "tier": "tier",
    },
)
class CfnParameterProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        value: builtins.str,
        allowed_pattern: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        policies: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        tier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SSM::Parameter``.

        :param type: ``AWS::SSM::Parameter.Type``.
        :param value: ``AWS::SSM::Parameter.Value``.
        :param allowed_pattern: ``AWS::SSM::Parameter.AllowedPattern``.
        :param data_type: ``AWS::SSM::Parameter.DataType``.
        :param description: ``AWS::SSM::Parameter.Description``.
        :param name: ``AWS::SSM::Parameter.Name``.
        :param policies: ``AWS::SSM::Parameter.Policies``.
        :param tags: ``AWS::SSM::Parameter.Tags``.
        :param tier: ``AWS::SSM::Parameter.Tier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
            "value": value,
        }
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if data_type is not None:
            self._values["data_type"] = data_type
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if policies is not None:
            self._values["policies"] = policies
        if tags is not None:
            self._values["tags"] = tags
        if tier is not None:
            self._values["tier"] = tier

    @builtins.property
    def type(self) -> builtins.str:
        '''``AWS::SSM::Parameter.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''``AWS::SSM::Parameter.Value``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-value
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Parameter.AllowedPattern``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-allowedpattern
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Parameter.DataType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-datatype
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Parameter.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Parameter.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Parameter.Policies``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-policies
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''``AWS::SSM::Parameter.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tier(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::Parameter.Tier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tier
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnParameterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPatchBaseline(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline",
):
    '''A CloudFormation ``AWS::SSM::PatchBaseline``.

    :cloudformationResource: AWS::SSM::PatchBaseline
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        approval_rules: typing.Optional[typing.Union["CfnPatchBaseline.RuleGroupProperty", _IResolvable_da3f097b]] = None,
        approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        approved_patches_compliance_level: typing.Optional[builtins.str] = None,
        approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        global_filters: typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]] = None,
        operating_system: typing.Optional[builtins.str] = None,
        patch_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches_action: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnPatchBaseline.PatchSourceProperty", _IResolvable_da3f097b]]]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::PatchBaseline``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::SSM::PatchBaseline.Name``.
        :param approval_rules: ``AWS::SSM::PatchBaseline.ApprovalRules``.
        :param approved_patches: ``AWS::SSM::PatchBaseline.ApprovedPatches``.
        :param approved_patches_compliance_level: ``AWS::SSM::PatchBaseline.ApprovedPatchesComplianceLevel``.
        :param approved_patches_enable_non_security: ``AWS::SSM::PatchBaseline.ApprovedPatchesEnableNonSecurity``.
        :param description: ``AWS::SSM::PatchBaseline.Description``.
        :param global_filters: ``AWS::SSM::PatchBaseline.GlobalFilters``.
        :param operating_system: ``AWS::SSM::PatchBaseline.OperatingSystem``.
        :param patch_groups: ``AWS::SSM::PatchBaseline.PatchGroups``.
        :param rejected_patches: ``AWS::SSM::PatchBaseline.RejectedPatches``.
        :param rejected_patches_action: ``AWS::SSM::PatchBaseline.RejectedPatchesAction``.
        :param sources: ``AWS::SSM::PatchBaseline.Sources``.
        :param tags: ``AWS::SSM::PatchBaseline.Tags``.
        '''
        props = CfnPatchBaselineProps(
            name=name,
            approval_rules=approval_rules,
            approved_patches=approved_patches,
            approved_patches_compliance_level=approved_patches_compliance_level,
            approved_patches_enable_non_security=approved_patches_enable_non_security,
            description=description,
            global_filters=global_filters,
            operating_system=operating_system,
            patch_groups=patch_groups,
            rejected_patches=rejected_patches,
            rejected_patches_action=rejected_patches_action,
            sources=sources,
            tags=tags,
        )

        jsii.create(CfnPatchBaseline, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::SSM::PatchBaseline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::SSM::PatchBaseline.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="approvalRules")
    def approval_rules(
        self,
    ) -> typing.Optional[typing.Union["CfnPatchBaseline.RuleGroupProperty", _IResolvable_da3f097b]]:
        '''``AWS::SSM::PatchBaseline.ApprovalRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvalrules
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPatchBaseline.RuleGroupProperty", _IResolvable_da3f097b]], jsii.get(self, "approvalRules"))

    @approval_rules.setter
    def approval_rules(
        self,
        value: typing.Optional[typing.Union["CfnPatchBaseline.RuleGroupProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "approvalRules", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="approvedPatches")
    def approved_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SSM::PatchBaseline.ApprovedPatches``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatches
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "approvedPatches"))

    @approved_patches.setter
    def approved_patches(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "approvedPatches", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::PatchBaseline.ApprovedPatchesComplianceLevel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchescompliancelevel
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "approvedPatchesComplianceLevel"))

    @approved_patches_compliance_level.setter
    def approved_patches_compliance_level(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "approvedPatchesComplianceLevel", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::SSM::PatchBaseline.ApprovedPatchesEnableNonSecurity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchesenablenonsecurity
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "approvedPatchesEnableNonSecurity"))

    @approved_patches_enable_non_security.setter
    def approved_patches_enable_non_security(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "approvedPatchesEnableNonSecurity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::PatchBaseline.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalFilters")
    def global_filters(
        self,
    ) -> typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]]:
        '''``AWS::SSM::PatchBaseline.GlobalFilters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-globalfilters
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]], jsii.get(self, "globalFilters"))

    @global_filters.setter
    def global_filters(
        self,
        value: typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "globalFilters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::PatchBaseline.OperatingSystem``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-operatingsystem
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatingSystem"))

    @operating_system.setter
    def operating_system(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "operatingSystem", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="patchGroups")
    def patch_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SSM::PatchBaseline.PatchGroups``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-patchgroups
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "patchGroups"))

    @patch_groups.setter
    def patch_groups(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "patchGroups", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rejectedPatches")
    def rejected_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SSM::PatchBaseline.RejectedPatches``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatches
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rejectedPatches"))

    @rejected_patches.setter
    def rejected_patches(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "rejectedPatches", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rejectedPatchesAction")
    def rejected_patches_action(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::PatchBaseline.RejectedPatchesAction``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatchesaction
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rejectedPatchesAction"))

    @rejected_patches_action.setter
    def rejected_patches_action(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "rejectedPatchesAction", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.PatchSourceProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::SSM::PatchBaseline.Sources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-sources
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.PatchSourceProperty", _IResolvable_da3f097b]]]], jsii.get(self, "sources"))

    @sources.setter
    def sources(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.PatchSourceProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "sources", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.PatchFilterGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"patch_filters": "patchFilters"},
    )
    class PatchFilterGroupProperty:
        def __init__(
            self,
            *,
            patch_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnPatchBaseline.PatchFilterProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param patch_filters: ``CfnPatchBaseline.PatchFilterGroupProperty.PatchFilters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if patch_filters is not None:
                self._values["patch_filters"] = patch_filters

        @builtins.property
        def patch_filters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.PatchFilterProperty", _IResolvable_da3f097b]]]]:
            '''``CfnPatchBaseline.PatchFilterGroupProperty.PatchFilters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html#cfn-ssm-patchbaseline-patchfiltergroup-patchfilters
            '''
            result = self._values.get("patch_filters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.PatchFilterProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PatchFilterGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.PatchFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class PatchFilterProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param key: ``CfnPatchBaseline.PatchFilterProperty.Key``.
            :param values: ``CfnPatchBaseline.PatchFilterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnPatchBaseline.PatchFilterProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html#cfn-ssm-patchbaseline-patchfilter-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPatchBaseline.PatchFilterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html#cfn-ssm-patchbaseline-patchfilter-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PatchFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.PatchSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration": "configuration",
            "name": "name",
            "products": "products",
        },
    )
    class PatchSourceProperty:
        def __init__(
            self,
            *,
            configuration: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            products: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param configuration: ``CfnPatchBaseline.PatchSourceProperty.Configuration``.
            :param name: ``CfnPatchBaseline.PatchSourceProperty.Name``.
            :param products: ``CfnPatchBaseline.PatchSourceProperty.Products``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if configuration is not None:
                self._values["configuration"] = configuration
            if name is not None:
                self._values["name"] = name
            if products is not None:
                self._values["products"] = products

        @builtins.property
        def configuration(self) -> typing.Optional[builtins.str]:
            '''``CfnPatchBaseline.PatchSourceProperty.Configuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-configuration
            '''
            result = self._values.get("configuration")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPatchBaseline.PatchSourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def products(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPatchBaseline.PatchSourceProperty.Products``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-products
            '''
            result = self._values.get("products")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PatchSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.RuleGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"patch_rules": "patchRules"},
    )
    class RuleGroupProperty:
        def __init__(
            self,
            *,
            patch_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnPatchBaseline.RuleProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param patch_rules: ``CfnPatchBaseline.RuleGroupProperty.PatchRules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if patch_rules is not None:
                self._values["patch_rules"] = patch_rules

        @builtins.property
        def patch_rules(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.RuleProperty", _IResolvable_da3f097b]]]]:
            '''``CfnPatchBaseline.RuleGroupProperty.PatchRules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html#cfn-ssm-patchbaseline-rulegroup-patchrules
            '''
            result = self._values.get("patch_rules")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.RuleProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "approve_after_days": "approveAfterDays",
            "approve_until_date": "approveUntilDate",
            "compliance_level": "complianceLevel",
            "enable_non_security": "enableNonSecurity",
            "patch_filter_group": "patchFilterGroup",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            approve_after_days: typing.Optional[jsii.Number] = None,
            approve_until_date: typing.Optional[builtins.str] = None,
            compliance_level: typing.Optional[builtins.str] = None,
            enable_non_security: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            patch_filter_group: typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param approve_after_days: ``CfnPatchBaseline.RuleProperty.ApproveAfterDays``.
            :param approve_until_date: ``CfnPatchBaseline.RuleProperty.ApproveUntilDate``.
            :param compliance_level: ``CfnPatchBaseline.RuleProperty.ComplianceLevel``.
            :param enable_non_security: ``CfnPatchBaseline.RuleProperty.EnableNonSecurity``.
            :param patch_filter_group: ``CfnPatchBaseline.RuleProperty.PatchFilterGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if approve_after_days is not None:
                self._values["approve_after_days"] = approve_after_days
            if approve_until_date is not None:
                self._values["approve_until_date"] = approve_until_date
            if compliance_level is not None:
                self._values["compliance_level"] = compliance_level
            if enable_non_security is not None:
                self._values["enable_non_security"] = enable_non_security
            if patch_filter_group is not None:
                self._values["patch_filter_group"] = patch_filter_group

        @builtins.property
        def approve_after_days(self) -> typing.Optional[jsii.Number]:
            '''``CfnPatchBaseline.RuleProperty.ApproveAfterDays``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-approveafterdays
            '''
            result = self._values.get("approve_after_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def approve_until_date(self) -> typing.Optional[builtins.str]:
            '''``CfnPatchBaseline.RuleProperty.ApproveUntilDate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-approveuntildate
            '''
            result = self._values.get("approve_until_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def compliance_level(self) -> typing.Optional[builtins.str]:
            '''``CfnPatchBaseline.RuleProperty.ComplianceLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-compliancelevel
            '''
            result = self._values.get("compliance_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_non_security(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnPatchBaseline.RuleProperty.EnableNonSecurity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-enablenonsecurity
            '''
            result = self._values.get("enable_non_security")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def patch_filter_group(
            self,
        ) -> typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]]:
            '''``CfnPatchBaseline.RuleProperty.PatchFilterGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-patchfiltergroup
            '''
            result = self._values.get("patch_filter_group")
            return typing.cast(typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaselineProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "approval_rules": "approvalRules",
        "approved_patches": "approvedPatches",
        "approved_patches_compliance_level": "approvedPatchesComplianceLevel",
        "approved_patches_enable_non_security": "approvedPatchesEnableNonSecurity",
        "description": "description",
        "global_filters": "globalFilters",
        "operating_system": "operatingSystem",
        "patch_groups": "patchGroups",
        "rejected_patches": "rejectedPatches",
        "rejected_patches_action": "rejectedPatchesAction",
        "sources": "sources",
        "tags": "tags",
    },
)
class CfnPatchBaselineProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        approval_rules: typing.Optional[typing.Union[CfnPatchBaseline.RuleGroupProperty, _IResolvable_da3f097b]] = None,
        approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        approved_patches_compliance_level: typing.Optional[builtins.str] = None,
        approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        global_filters: typing.Optional[typing.Union[CfnPatchBaseline.PatchFilterGroupProperty, _IResolvable_da3f097b]] = None,
        operating_system: typing.Optional[builtins.str] = None,
        patch_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches_action: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnPatchBaseline.PatchSourceProperty, _IResolvable_da3f097b]]]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SSM::PatchBaseline``.

        :param name: ``AWS::SSM::PatchBaseline.Name``.
        :param approval_rules: ``AWS::SSM::PatchBaseline.ApprovalRules``.
        :param approved_patches: ``AWS::SSM::PatchBaseline.ApprovedPatches``.
        :param approved_patches_compliance_level: ``AWS::SSM::PatchBaseline.ApprovedPatchesComplianceLevel``.
        :param approved_patches_enable_non_security: ``AWS::SSM::PatchBaseline.ApprovedPatchesEnableNonSecurity``.
        :param description: ``AWS::SSM::PatchBaseline.Description``.
        :param global_filters: ``AWS::SSM::PatchBaseline.GlobalFilters``.
        :param operating_system: ``AWS::SSM::PatchBaseline.OperatingSystem``.
        :param patch_groups: ``AWS::SSM::PatchBaseline.PatchGroups``.
        :param rejected_patches: ``AWS::SSM::PatchBaseline.RejectedPatches``.
        :param rejected_patches_action: ``AWS::SSM::PatchBaseline.RejectedPatchesAction``.
        :param sources: ``AWS::SSM::PatchBaseline.Sources``.
        :param tags: ``AWS::SSM::PatchBaseline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if approval_rules is not None:
            self._values["approval_rules"] = approval_rules
        if approved_patches is not None:
            self._values["approved_patches"] = approved_patches
        if approved_patches_compliance_level is not None:
            self._values["approved_patches_compliance_level"] = approved_patches_compliance_level
        if approved_patches_enable_non_security is not None:
            self._values["approved_patches_enable_non_security"] = approved_patches_enable_non_security
        if description is not None:
            self._values["description"] = description
        if global_filters is not None:
            self._values["global_filters"] = global_filters
        if operating_system is not None:
            self._values["operating_system"] = operating_system
        if patch_groups is not None:
            self._values["patch_groups"] = patch_groups
        if rejected_patches is not None:
            self._values["rejected_patches"] = rejected_patches
        if rejected_patches_action is not None:
            self._values["rejected_patches_action"] = rejected_patches_action
        if sources is not None:
            self._values["sources"] = sources
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::SSM::PatchBaseline.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def approval_rules(
        self,
    ) -> typing.Optional[typing.Union[CfnPatchBaseline.RuleGroupProperty, _IResolvable_da3f097b]]:
        '''``AWS::SSM::PatchBaseline.ApprovalRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvalrules
        '''
        result = self._values.get("approval_rules")
        return typing.cast(typing.Optional[typing.Union[CfnPatchBaseline.RuleGroupProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def approved_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SSM::PatchBaseline.ApprovedPatches``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatches
        '''
        result = self._values.get("approved_patches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def approved_patches_compliance_level(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::PatchBaseline.ApprovedPatchesComplianceLevel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchescompliancelevel
        '''
        result = self._values.get("approved_patches_compliance_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def approved_patches_enable_non_security(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::SSM::PatchBaseline.ApprovedPatchesEnableNonSecurity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchesenablenonsecurity
        '''
        result = self._values.get("approved_patches_enable_non_security")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::PatchBaseline.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_filters(
        self,
    ) -> typing.Optional[typing.Union[CfnPatchBaseline.PatchFilterGroupProperty, _IResolvable_da3f097b]]:
        '''``AWS::SSM::PatchBaseline.GlobalFilters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-globalfilters
        '''
        result = self._values.get("global_filters")
        return typing.cast(typing.Optional[typing.Union[CfnPatchBaseline.PatchFilterGroupProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::PatchBaseline.OperatingSystem``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-operatingsystem
        '''
        result = self._values.get("operating_system")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def patch_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SSM::PatchBaseline.PatchGroups``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-patchgroups
        '''
        result = self._values.get("patch_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rejected_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SSM::PatchBaseline.RejectedPatches``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatches
        '''
        result = self._values.get("rejected_patches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rejected_patches_action(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::PatchBaseline.RejectedPatchesAction``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatchesaction
        '''
        result = self._values.get("rejected_patches_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnPatchBaseline.PatchSourceProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::SSM::PatchBaseline.Sources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-sources
        '''
        result = self._values.get("sources")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnPatchBaseline.PatchSourceProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::SSM::PatchBaseline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPatchBaselineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourceDataSync(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSync",
):
    '''A CloudFormation ``AWS::SSM::ResourceDataSync``.

    :cloudformationResource: AWS::SSM::ResourceDataSync
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        sync_name: builtins.str,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        bucket_region: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        s3_destination: typing.Optional[typing.Union["CfnResourceDataSync.S3DestinationProperty", _IResolvable_da3f097b]] = None,
        sync_format: typing.Optional[builtins.str] = None,
        sync_source: typing.Optional[typing.Union["CfnResourceDataSync.SyncSourceProperty", _IResolvable_da3f097b]] = None,
        sync_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::ResourceDataSync``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param sync_name: ``AWS::SSM::ResourceDataSync.SyncName``.
        :param bucket_name: ``AWS::SSM::ResourceDataSync.BucketName``.
        :param bucket_prefix: ``AWS::SSM::ResourceDataSync.BucketPrefix``.
        :param bucket_region: ``AWS::SSM::ResourceDataSync.BucketRegion``.
        :param kms_key_arn: ``AWS::SSM::ResourceDataSync.KMSKeyArn``.
        :param s3_destination: ``AWS::SSM::ResourceDataSync.S3Destination``.
        :param sync_format: ``AWS::SSM::ResourceDataSync.SyncFormat``.
        :param sync_source: ``AWS::SSM::ResourceDataSync.SyncSource``.
        :param sync_type: ``AWS::SSM::ResourceDataSync.SyncType``.
        '''
        props = CfnResourceDataSyncProps(
            sync_name=sync_name,
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            bucket_region=bucket_region,
            kms_key_arn=kms_key_arn,
            s3_destination=s3_destination,
            sync_format=sync_format,
            sync_source=sync_source,
            sync_type=sync_type,
        )

        jsii.create(CfnResourceDataSync, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrSyncName")
    def attr_sync_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: SyncName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSyncName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="syncName")
    def sync_name(self) -> builtins.str:
        '''``AWS::SSM::ResourceDataSync.SyncName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncname
        '''
        return typing.cast(builtins.str, jsii.get(self, "syncName"))

    @sync_name.setter
    def sync_name(self, value: builtins.str) -> None:
        jsii.set(self, "syncName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::ResourceDataSync.BucketName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "bucketName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::ResourceDataSync.BucketPrefix``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketprefix
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "bucketPrefix", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bucketRegion")
    def bucket_region(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::ResourceDataSync.BucketRegion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketregion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketRegion"))

    @bucket_region.setter
    def bucket_region(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "bucketRegion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::ResourceDataSync.KMSKeyArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-kmskeyarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="s3Destination")
    def s3_destination(
        self,
    ) -> typing.Optional[typing.Union["CfnResourceDataSync.S3DestinationProperty", _IResolvable_da3f097b]]:
        '''``AWS::SSM::ResourceDataSync.S3Destination``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-s3destination
        '''
        return typing.cast(typing.Optional[typing.Union["CfnResourceDataSync.S3DestinationProperty", _IResolvable_da3f097b]], jsii.get(self, "s3Destination"))

    @s3_destination.setter
    def s3_destination(
        self,
        value: typing.Optional[typing.Union["CfnResourceDataSync.S3DestinationProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "s3Destination", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="syncFormat")
    def sync_format(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::ResourceDataSync.SyncFormat``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncformat
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncFormat"))

    @sync_format.setter
    def sync_format(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "syncFormat", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="syncSource")
    def sync_source(
        self,
    ) -> typing.Optional[typing.Union["CfnResourceDataSync.SyncSourceProperty", _IResolvable_da3f097b]]:
        '''``AWS::SSM::ResourceDataSync.SyncSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncsource
        '''
        return typing.cast(typing.Optional[typing.Union["CfnResourceDataSync.SyncSourceProperty", _IResolvable_da3f097b]], jsii.get(self, "syncSource"))

    @sync_source.setter
    def sync_source(
        self,
        value: typing.Optional[typing.Union["CfnResourceDataSync.SyncSourceProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "syncSource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="syncType")
    def sync_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::ResourceDataSync.SyncType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-synctype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncType"))

    @sync_type.setter
    def sync_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "syncType", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSync.AwsOrganizationsSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "organization_source_type": "organizationSourceType",
            "organizational_units": "organizationalUnits",
        },
    )
    class AwsOrganizationsSourceProperty:
        def __init__(
            self,
            *,
            organization_source_type: builtins.str,
            organizational_units: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param organization_source_type: ``CfnResourceDataSync.AwsOrganizationsSourceProperty.OrganizationSourceType``.
            :param organizational_units: ``CfnResourceDataSync.AwsOrganizationsSourceProperty.OrganizationalUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "organization_source_type": organization_source_type,
            }
            if organizational_units is not None:
                self._values["organizational_units"] = organizational_units

        @builtins.property
        def organization_source_type(self) -> builtins.str:
            '''``CfnResourceDataSync.AwsOrganizationsSourceProperty.OrganizationSourceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html#cfn-ssm-resourcedatasync-awsorganizationssource-organizationsourcetype
            '''
            result = self._values.get("organization_source_type")
            assert result is not None, "Required property 'organization_source_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def organizational_units(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnResourceDataSync.AwsOrganizationsSourceProperty.OrganizationalUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html#cfn-ssm-resourcedatasync-awsorganizationssource-organizationalunits
            '''
            result = self._values.get("organizational_units")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsOrganizationsSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSync.S3DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "bucket_region": "bucketRegion",
            "sync_format": "syncFormat",
            "bucket_prefix": "bucketPrefix",
            "kms_key_arn": "kmsKeyArn",
        },
    )
    class S3DestinationProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            bucket_region: builtins.str,
            sync_format: builtins.str,
            bucket_prefix: typing.Optional[builtins.str] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bucket_name: ``CfnResourceDataSync.S3DestinationProperty.BucketName``.
            :param bucket_region: ``CfnResourceDataSync.S3DestinationProperty.BucketRegion``.
            :param sync_format: ``CfnResourceDataSync.S3DestinationProperty.SyncFormat``.
            :param bucket_prefix: ``CfnResourceDataSync.S3DestinationProperty.BucketPrefix``.
            :param kms_key_arn: ``CfnResourceDataSync.S3DestinationProperty.KMSKeyArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket_name": bucket_name,
                "bucket_region": bucket_region,
                "sync_format": sync_format,
            }
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''``CfnResourceDataSync.S3DestinationProperty.BucketName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_region(self) -> builtins.str:
            '''``CfnResourceDataSync.S3DestinationProperty.BucketRegion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-bucketregion
            '''
            result = self._values.get("bucket_region")
            assert result is not None, "Required property 'bucket_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sync_format(self) -> builtins.str:
            '''``CfnResourceDataSync.S3DestinationProperty.SyncFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-syncformat
            '''
            result = self._values.get("sync_format")
            assert result is not None, "Required property 'sync_format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceDataSync.S3DestinationProperty.BucketPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceDataSync.S3DestinationProperty.KMSKeyArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSync.SyncSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_regions": "sourceRegions",
            "source_type": "sourceType",
            "aws_organizations_source": "awsOrganizationsSource",
            "include_future_regions": "includeFutureRegions",
        },
    )
    class SyncSourceProperty:
        def __init__(
            self,
            *,
            source_regions: typing.Sequence[builtins.str],
            source_type: builtins.str,
            aws_organizations_source: typing.Optional[typing.Union["CfnResourceDataSync.AwsOrganizationsSourceProperty", _IResolvable_da3f097b]] = None,
            include_future_regions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param source_regions: ``CfnResourceDataSync.SyncSourceProperty.SourceRegions``.
            :param source_type: ``CfnResourceDataSync.SyncSourceProperty.SourceType``.
            :param aws_organizations_source: ``CfnResourceDataSync.SyncSourceProperty.AwsOrganizationsSource``.
            :param include_future_regions: ``CfnResourceDataSync.SyncSourceProperty.IncludeFutureRegions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "source_regions": source_regions,
                "source_type": source_type,
            }
            if aws_organizations_source is not None:
                self._values["aws_organizations_source"] = aws_organizations_source
            if include_future_regions is not None:
                self._values["include_future_regions"] = include_future_regions

        @builtins.property
        def source_regions(self) -> typing.List[builtins.str]:
            '''``CfnResourceDataSync.SyncSourceProperty.SourceRegions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-sourceregions
            '''
            result = self._values.get("source_regions")
            assert result is not None, "Required property 'source_regions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def source_type(self) -> builtins.str:
            '''``CfnResourceDataSync.SyncSourceProperty.SourceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-sourcetype
            '''
            result = self._values.get("source_type")
            assert result is not None, "Required property 'source_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_organizations_source(
            self,
        ) -> typing.Optional[typing.Union["CfnResourceDataSync.AwsOrganizationsSourceProperty", _IResolvable_da3f097b]]:
            '''``CfnResourceDataSync.SyncSourceProperty.AwsOrganizationsSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-awsorganizationssource
            '''
            result = self._values.get("aws_organizations_source")
            return typing.cast(typing.Optional[typing.Union["CfnResourceDataSync.AwsOrganizationsSourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def include_future_regions(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnResourceDataSync.SyncSourceProperty.IncludeFutureRegions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-includefutureregions
            '''
            result = self._values.get("include_future_regions")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SyncSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSyncProps",
    jsii_struct_bases=[],
    name_mapping={
        "sync_name": "syncName",
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "bucket_region": "bucketRegion",
        "kms_key_arn": "kmsKeyArn",
        "s3_destination": "s3Destination",
        "sync_format": "syncFormat",
        "sync_source": "syncSource",
        "sync_type": "syncType",
    },
)
class CfnResourceDataSyncProps:
    def __init__(
        self,
        *,
        sync_name: builtins.str,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        bucket_region: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        s3_destination: typing.Optional[typing.Union[CfnResourceDataSync.S3DestinationProperty, _IResolvable_da3f097b]] = None,
        sync_format: typing.Optional[builtins.str] = None,
        sync_source: typing.Optional[typing.Union[CfnResourceDataSync.SyncSourceProperty, _IResolvable_da3f097b]] = None,
        sync_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SSM::ResourceDataSync``.

        :param sync_name: ``AWS::SSM::ResourceDataSync.SyncName``.
        :param bucket_name: ``AWS::SSM::ResourceDataSync.BucketName``.
        :param bucket_prefix: ``AWS::SSM::ResourceDataSync.BucketPrefix``.
        :param bucket_region: ``AWS::SSM::ResourceDataSync.BucketRegion``.
        :param kms_key_arn: ``AWS::SSM::ResourceDataSync.KMSKeyArn``.
        :param s3_destination: ``AWS::SSM::ResourceDataSync.S3Destination``.
        :param sync_format: ``AWS::SSM::ResourceDataSync.SyncFormat``.
        :param sync_source: ``AWS::SSM::ResourceDataSync.SyncSource``.
        :param sync_type: ``AWS::SSM::ResourceDataSync.SyncType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "sync_name": sync_name,
        }
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if bucket_region is not None:
            self._values["bucket_region"] = bucket_region
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if s3_destination is not None:
            self._values["s3_destination"] = s3_destination
        if sync_format is not None:
            self._values["sync_format"] = sync_format
        if sync_source is not None:
            self._values["sync_source"] = sync_source
        if sync_type is not None:
            self._values["sync_type"] = sync_type

    @builtins.property
    def sync_name(self) -> builtins.str:
        '''``AWS::SSM::ResourceDataSync.SyncName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncname
        '''
        result = self._values.get("sync_name")
        assert result is not None, "Required property 'sync_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::ResourceDataSync.BucketName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketname
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::ResourceDataSync.BucketPrefix``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketprefix
        '''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_region(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::ResourceDataSync.BucketRegion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketregion
        '''
        result = self._values.get("bucket_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::ResourceDataSync.KMSKeyArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_destination(
        self,
    ) -> typing.Optional[typing.Union[CfnResourceDataSync.S3DestinationProperty, _IResolvable_da3f097b]]:
        '''``AWS::SSM::ResourceDataSync.S3Destination``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-s3destination
        '''
        result = self._values.get("s3_destination")
        return typing.cast(typing.Optional[typing.Union[CfnResourceDataSync.S3DestinationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def sync_format(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::ResourceDataSync.SyncFormat``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncformat
        '''
        result = self._values.get("sync_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sync_source(
        self,
    ) -> typing.Optional[typing.Union[CfnResourceDataSync.SyncSourceProperty, _IResolvable_da3f097b]]:
        '''``AWS::SSM::ResourceDataSync.SyncSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncsource
        '''
        result = self._values.get("sync_source")
        return typing.cast(typing.Optional[typing.Union[CfnResourceDataSync.SyncSourceProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def sync_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSM::ResourceDataSync.SyncType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-synctype
        '''
        result = self._values.get("sync_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceDataSyncProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CommonStringParameterAttributes",
    jsii_struct_bases=[],
    name_mapping={"parameter_name": "parameterName", "simple_name": "simpleName"},
)
class CommonStringParameterAttributes:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Common attributes for string parameters.

        :param parameter_name: (experimental) The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: (experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "parameter_name": parameter_name,
        }
        if simple_name is not None:
            self._values["simple_name"] = simple_name

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''(experimental) The name of the parameter store value.

        This value can be a token or a concrete string. If it is a concrete string
        and includes "/" it must also be prefixed with a "/" (fully-qualified).

        :stability: experimental
        '''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators).

        This is only required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``

        :stability: experimental
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonStringParameterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_ssm.IParameter")
class IParameter(_IResource_c80c4260, typing_extensions.Protocol):
    '''(experimental) An SSM Parameter reference.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IParameterProxy"]:
        return _IParameterProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> builtins.str:
        '''(experimental) The ARN of the SSM Parameter resource.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        '''(experimental) The name of the SSM Parameter resource.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''(experimental) The type of the SSM Parameter resource.

        :stability: experimental
        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(experimental) Grants read (DescribeParameter, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: the role to be granted read-only access to the parameter.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(experimental) Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: the role to be granted write access to the parameter.

        :stability: experimental
        '''
        ...


class _IParameterProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''(experimental) An SSM Parameter reference.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ssm.IParameter"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> builtins.str:
        '''(experimental) The ARN of the SSM Parameter resource.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        '''(experimental) The name of the SSM Parameter resource.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''(experimental) The type of the SSM Parameter resource.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterType"))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(experimental) Grants read (DescribeParameter, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: the role to be granted read-only access to the parameter.

        :stability: experimental
        '''
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(experimental) Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: the role to be granted write access to the parameter.

        :stability: experimental
        '''
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))


@jsii.interface(jsii_type="aws-cdk-lib.aws_ssm.IStringListParameter")
class IStringListParameter(IParameter, typing_extensions.Protocol):
    '''(experimental) A StringList SSM Parameter.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IStringListParameterProxy"]:
        return _IStringListParameterProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        '''(experimental) The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value. Values in the array
        cannot contain commas (``,``).

        :stability: experimental
        :attribute: Value
        '''
        ...


class _IStringListParameterProxy(
    jsii.proxy_for(IParameter) # type: ignore[misc]
):
    '''(experimental) A StringList SSM Parameter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ssm.IStringListParameter"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        '''(experimental) The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value. Values in the array
        cannot contain commas (``,``).

        :stability: experimental
        :attribute: Value
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))


@jsii.interface(jsii_type="aws-cdk-lib.aws_ssm.IStringParameter")
class IStringParameter(IParameter, typing_extensions.Protocol):
    '''(experimental) A String SSM Parameter.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IStringParameterProxy"]:
        return _IStringParameterProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        '''(experimental) The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value.

        :stability: experimental
        :attribute: Value
        '''
        ...


class _IStringParameterProxy(
    jsii.proxy_for(IParameter) # type: ignore[misc]
):
    '''(experimental) A String SSM Parameter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ssm.IStringParameter"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        '''(experimental) The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value.

        :stability: experimental
        :attribute: Value
        '''
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.ParameterOptions",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_pattern": "allowedPattern",
        "description": "description",
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "tier": "tier",
    },
)
class ParameterOptions:
    def __init__(
        self,
        *,
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional["ParameterTier"] = None,
    ) -> None:
        '''(experimental) Properties needed to create a new SSM Parameter.

        :param allowed_pattern: (experimental) A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: - no validation is performed
        :param description: (experimental) Information about the parameter that you want to add to the system. Default: - none
        :param parameter_name: (experimental) The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: (experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: (experimental) The tier of the string parameter. Default: - undefined

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if description is not None:
            self._values["description"] = description
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if tier is not None:
            self._values["tier"] = tier

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''(experimental) A regular expression used to validate the parameter value.

        For example, for String types with values restricted to
        numbers, you can specify the following: ``^\\d+$``

        :default: - no validation is performed

        :stability: experimental
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Information about the parameter that you want to add to the system.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the parameter.

        :default: - a name will be generated by CloudFormation

        :stability: experimental
        '''
        result = self._values.get("parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators).

        This is only required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``

        :stability: experimental
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tier(self) -> typing.Optional["ParameterTier"]:
        '''(experimental) The tier of the string parameter.

        :default: - undefined

        :stability: experimental
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional["ParameterTier"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParameterOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ssm.ParameterTier")
class ParameterTier(enum.Enum):
    '''(experimental) SSM parameter tier.

    :stability: experimental
    '''

    ADVANCED = "ADVANCED"
    '''(experimental) String.

    :stability: experimental
    '''
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    '''(experimental) String.

    :stability: experimental
    '''
    STANDARD = "STANDARD"
    '''(experimental) String.

    :stability: experimental
    '''


@jsii.enum(jsii_type="aws-cdk-lib.aws_ssm.ParameterType")
class ParameterType(enum.Enum):
    '''(experimental) SSM parameter type.

    :stability: experimental
    '''

    STRING = "STRING"
    '''(experimental) String.

    :stability: experimental
    '''
    SECURE_STRING = "SECURE_STRING"
    '''(experimental) Secure String Parameter Store uses an AWS Key Management Service (KMS) customer master key (CMK) to encrypt the parameter value.

    :stability: experimental
    '''
    STRING_LIST = "STRING_LIST"
    '''(experimental) String List.

    :stability: experimental
    '''
    AWS_EC2_IMAGE_ID = "AWS_EC2_IMAGE_ID"
    '''(experimental) An Amazon EC2 image ID, such as ami-0ff8a91507f77f867.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.SecureStringParameterAttributes",
    jsii_struct_bases=[CommonStringParameterAttributes],
    name_mapping={
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "version": "version",
        "encryption_key": "encryptionKey",
    },
)
class SecureStringParameterAttributes(CommonStringParameterAttributes):
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
        version: jsii.Number,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
    ) -> None:
        '''(experimental) Attributes for secure string parameters.

        :param parameter_name: (experimental) The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: (experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param version: (experimental) The version number of the value you wish to retrieve. This is required for secure strings.
        :param encryption_key: (experimental) The encryption key that is used to encrypt this parameter. Default: - default master key

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "parameter_name": parameter_name,
            "version": version,
        }
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''(experimental) The name of the parameter store value.

        This value can be a token or a concrete string. If it is a concrete string
        and includes "/" it must also be prefixed with a "/" (fully-qualified).

        :stability: experimental
        '''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators).

        This is only required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``

        :stability: experimental
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def version(self) -> jsii.Number:
        '''(experimental) The version number of the value you wish to retrieve.

        This is required for secure strings.

        :stability: experimental
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''(experimental) The encryption key that is used to encrypt this parameter.

        :default: - default master key

        :stability: experimental
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecureStringParameterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IStringListParameter, IParameter)
class StringListParameter(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.StringListParameter",
):
    '''(experimental) Creates a new StringList SSM Parameter.

    :stability: experimental
    :resource: AWS::SSM::Parameter
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        string_list_value: typing.Sequence[builtins.str],
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional[ParameterTier] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param string_list_value: (experimental) The values of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        :param allowed_pattern: (experimental) A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: - no validation is performed
        :param description: (experimental) Information about the parameter that you want to add to the system. Default: - none
        :param parameter_name: (experimental) The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: (experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: (experimental) The tier of the string parameter. Default: - undefined

        :stability: experimental
        '''
        props = StringListParameterProps(
            string_list_value=string_list_value,
            allowed_pattern=allowed_pattern,
            description=description,
            parameter_name=parameter_name,
            simple_name=simple_name,
            tier=tier,
        )

        jsii.create(StringListParameter, self, [scope, id, props])

    @jsii.member(jsii_name="fromStringListParameterName") # type: ignore[misc]
    @builtins.classmethod
    def from_string_list_parameter_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        string_list_parameter_name: builtins.str,
    ) -> IStringListParameter:
        '''(experimental) Imports an external parameter of type string list.

        Returns a token and should not be parsed.

        :param scope: -
        :param id: -
        :param string_list_parameter_name: -

        :stability: experimental
        '''
        return typing.cast(IStringListParameter, jsii.sinvoke(cls, "fromStringListParameterName", [scope, id, string_list_parameter_name]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(experimental) Grants read (DescribeParameter, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: -

        :stability: experimental
        '''
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(experimental) Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: -

        :stability: experimental
        '''
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> builtins.str:
        '''(experimental) The ARN of the SSM Parameter resource.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        '''(experimental) The name of the SSM Parameter resource.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''(experimental) The type of the SSM Parameter resource.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        '''(experimental) The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value. Values in the array
        cannot contain commas (``,``).

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''(experimental) The encryption key that is used to encrypt this parameter.

        - @default - default master key

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "encryptionKey"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.StringListParameterProps",
    jsii_struct_bases=[ParameterOptions],
    name_mapping={
        "allowed_pattern": "allowedPattern",
        "description": "description",
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "tier": "tier",
        "string_list_value": "stringListValue",
    },
)
class StringListParameterProps(ParameterOptions):
    def __init__(
        self,
        *,
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional[ParameterTier] = None,
        string_list_value: typing.Sequence[builtins.str],
    ) -> None:
        '''(experimental) Properties needed to create a StringList SSM Parameter.

        :param allowed_pattern: (experimental) A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: - no validation is performed
        :param description: (experimental) Information about the parameter that you want to add to the system. Default: - none
        :param parameter_name: (experimental) The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: (experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: (experimental) The tier of the string parameter. Default: - undefined
        :param string_list_value: (experimental) The values of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "string_list_value": string_list_value,
        }
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if description is not None:
            self._values["description"] = description
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if tier is not None:
            self._values["tier"] = tier

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''(experimental) A regular expression used to validate the parameter value.

        For example, for String types with values restricted to
        numbers, you can specify the following: ``^\\d+$``

        :default: - no validation is performed

        :stability: experimental
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Information about the parameter that you want to add to the system.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the parameter.

        :default: - a name will be generated by CloudFormation

        :stability: experimental
        '''
        result = self._values.get("parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators).

        This is only required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``

        :stability: experimental
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tier(self) -> typing.Optional[ParameterTier]:
        '''(experimental) The tier of the string parameter.

        :default: - undefined

        :stability: experimental
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[ParameterTier], result)

    @builtins.property
    def string_list_value(self) -> typing.List[builtins.str]:
        '''(experimental) The values of the parameter.

        It may not reference another parameter and ``{{}}`` cannot be used in the value.

        :stability: experimental
        '''
        result = self._values.get("string_list_value")
        assert result is not None, "Required property 'string_list_value' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StringListParameterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IStringParameter, IParameter)
class StringParameter(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.StringParameter",
):
    '''(experimental) Creates a new String SSM Parameter.

    :stability: experimental
    :resource: AWS::SSM::Parameter
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        string_value: builtins.str,
        type: typing.Optional[ParameterType] = None,
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional[ParameterTier] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param string_value: (experimental) The value of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        :param type: (experimental) The type of the string parameter. Default: ParameterType.STRING
        :param allowed_pattern: (experimental) A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: - no validation is performed
        :param description: (experimental) Information about the parameter that you want to add to the system. Default: - none
        :param parameter_name: (experimental) The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: (experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: (experimental) The tier of the string parameter. Default: - undefined

        :stability: experimental
        '''
        props = StringParameterProps(
            string_value=string_value,
            type=type,
            allowed_pattern=allowed_pattern,
            description=description,
            parameter_name=parameter_name,
            simple_name=simple_name,
            tier=tier,
        )

        jsii.create(StringParameter, self, [scope, id, props])

    @jsii.member(jsii_name="fromSecureStringParameterAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_secure_string_parameter_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        version: jsii.Number,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
    ) -> IStringParameter:
        '''(experimental) Imports a secure string parameter from the SSM parameter store.

        :param scope: -
        :param id: -
        :param version: (experimental) The version number of the value you wish to retrieve. This is required for secure strings.
        :param encryption_key: (experimental) The encryption key that is used to encrypt this parameter. Default: - default master key
        :param parameter_name: (experimental) The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: (experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``

        :stability: experimental
        '''
        attrs = SecureStringParameterAttributes(
            version=version,
            encryption_key=encryption_key,
            parameter_name=parameter_name,
            simple_name=simple_name,
        )

        return typing.cast(IStringParameter, jsii.sinvoke(cls, "fromSecureStringParameterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromStringParameterAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_string_parameter_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        type: typing.Optional[ParameterType] = None,
        version: typing.Optional[jsii.Number] = None,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
    ) -> IStringParameter:
        '''(experimental) Imports an external string parameter with name and optional version.

        :param scope: -
        :param id: -
        :param type: (experimental) The type of the string parameter. Default: ParameterType.STRING
        :param version: (experimental) The version number of the value you wish to retrieve. Default: - The latest version will be retrieved.
        :param parameter_name: (experimental) The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: (experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``

        :stability: experimental
        '''
        attrs = StringParameterAttributes(
            type=type,
            version=version,
            parameter_name=parameter_name,
            simple_name=simple_name,
        )

        return typing.cast(IStringParameter, jsii.sinvoke(cls, "fromStringParameterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromStringParameterName") # type: ignore[misc]
    @builtins.classmethod
    def from_string_parameter_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        string_parameter_name: builtins.str,
    ) -> IStringParameter:
        '''(experimental) Imports an external string parameter by name.

        :param scope: -
        :param id: -
        :param string_parameter_name: -

        :stability: experimental
        '''
        return typing.cast(IStringParameter, jsii.sinvoke(cls, "fromStringParameterName", [scope, id, string_parameter_name]))

    @jsii.member(jsii_name="valueForSecureStringParameter") # type: ignore[misc]
    @builtins.classmethod
    def value_for_secure_string_parameter(
        cls,
        scope: constructs.Construct,
        parameter_name: builtins.str,
        version: jsii.Number,
    ) -> builtins.str:
        '''(experimental) Returns a token that will resolve (during deployment).

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param version: The parameter version (required for secure strings).

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueForSecureStringParameter", [scope, parameter_name, version]))

    @jsii.member(jsii_name="valueForStringParameter") # type: ignore[misc]
    @builtins.classmethod
    def value_for_string_parameter(
        cls,
        scope: constructs.Construct,
        parameter_name: builtins.str,
        version: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''(experimental) Returns a token that will resolve (during deployment) to the string value of an SSM string parameter.

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param version: The parameter version (recommended in order to ensure that the value won't change during deployment).

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueForStringParameter", [scope, parameter_name, version]))

    @jsii.member(jsii_name="valueForTypedStringParameter") # type: ignore[misc]
    @builtins.classmethod
    def value_for_typed_string_parameter(
        cls,
        scope: constructs.Construct,
        parameter_name: builtins.str,
        type: typing.Optional[ParameterType] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''(experimental) Returns a token that will resolve (during deployment) to the string value of an SSM string parameter.

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param type: The type of the SSM parameter.
        :param version: The parameter version (recommended in order to ensure that the value won't change during deployment).

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueForTypedStringParameter", [scope, parameter_name, type, version]))

    @jsii.member(jsii_name="valueFromLookup") # type: ignore[misc]
    @builtins.classmethod
    def value_from_lookup(
        cls,
        scope: constructs.Construct,
        parameter_name: builtins.str,
    ) -> builtins.str:
        '''(experimental) Reads the value of an SSM parameter during synthesis through an environmental context provider.

        Requires that the stack this scope is defined in will have explicit
        account/region information. Otherwise, it will fail during synthesis.

        :param scope: -
        :param parameter_name: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueFromLookup", [scope, parameter_name]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(experimental) Grants read (DescribeParameter, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: -

        :stability: experimental
        '''
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''(experimental) Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: -

        :stability: experimental
        '''
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> builtins.str:
        '''(experimental) The ARN of the SSM Parameter resource.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        '''(experimental) The name of the SSM Parameter resource.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''(experimental) The type of the SSM Parameter resource.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        '''(experimental) The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''(experimental) The encryption key that is used to encrypt this parameter.

        - @default - default master key

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "encryptionKey"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.StringParameterAttributes",
    jsii_struct_bases=[CommonStringParameterAttributes],
    name_mapping={
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "type": "type",
        "version": "version",
    },
)
class StringParameterAttributes(CommonStringParameterAttributes):
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
        type: typing.Optional[ParameterType] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Attributes for parameters of various types of string.

        :param parameter_name: (experimental) The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: (experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param type: (experimental) The type of the string parameter. Default: ParameterType.STRING
        :param version: (experimental) The version number of the value you wish to retrieve. Default: - The latest version will be retrieved.

        :see: ParameterType
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "parameter_name": parameter_name,
        }
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if type is not None:
            self._values["type"] = type
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''(experimental) The name of the parameter store value.

        This value can be a token or a concrete string. If it is a concrete string
        and includes "/" it must also be prefixed with a "/" (fully-qualified).

        :stability: experimental
        '''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators).

        This is only required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``

        :stability: experimental
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def type(self) -> typing.Optional[ParameterType]:
        '''(experimental) The type of the string parameter.

        :default: ParameterType.STRING

        :stability: experimental
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[ParameterType], result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The version number of the value you wish to retrieve.

        :default: - The latest version will be retrieved.

        :stability: experimental
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StringParameterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.StringParameterProps",
    jsii_struct_bases=[ParameterOptions],
    name_mapping={
        "allowed_pattern": "allowedPattern",
        "description": "description",
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "tier": "tier",
        "string_value": "stringValue",
        "type": "type",
    },
)
class StringParameterProps(ParameterOptions):
    def __init__(
        self,
        *,
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional[ParameterTier] = None,
        string_value: builtins.str,
        type: typing.Optional[ParameterType] = None,
    ) -> None:
        '''(experimental) Properties needed to create a String SSM parameter.

        :param allowed_pattern: (experimental) A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: - no validation is performed
        :param description: (experimental) Information about the parameter that you want to add to the system. Default: - none
        :param parameter_name: (experimental) The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: (experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: (experimental) The tier of the string parameter. Default: - undefined
        :param string_value: (experimental) The value of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        :param type: (experimental) The type of the string parameter. Default: ParameterType.STRING

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "string_value": string_value,
        }
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if description is not None:
            self._values["description"] = description
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if tier is not None:
            self._values["tier"] = tier
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''(experimental) A regular expression used to validate the parameter value.

        For example, for String types with values restricted to
        numbers, you can specify the following: ``^\\d+$``

        :default: - no validation is performed

        :stability: experimental
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Information about the parameter that you want to add to the system.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the parameter.

        :default: - a name will be generated by CloudFormation

        :stability: experimental
        '''
        result = self._values.get("parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates of the parameter name is a simple name (i.e. does not include "/" separators).

        This is only required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``

        :stability: experimental
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tier(self) -> typing.Optional[ParameterTier]:
        '''(experimental) The tier of the string parameter.

        :default: - undefined

        :stability: experimental
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[ParameterTier], result)

    @builtins.property
    def string_value(self) -> builtins.str:
        '''(experimental) The value of the parameter.

        It may not reference another parameter and ``{{}}`` cannot be used in the value.

        :stability: experimental
        '''
        result = self._values.get("string_value")
        assert result is not None, "Required property 'string_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> typing.Optional[ParameterType]:
        '''(experimental) The type of the string parameter.

        :default: ParameterType.STRING

        :stability: experimental
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[ParameterType], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StringParameterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAssociation",
    "CfnAssociationProps",
    "CfnDocument",
    "CfnDocumentProps",
    "CfnMaintenanceWindow",
    "CfnMaintenanceWindowProps",
    "CfnMaintenanceWindowTarget",
    "CfnMaintenanceWindowTargetProps",
    "CfnMaintenanceWindowTask",
    "CfnMaintenanceWindowTaskProps",
    "CfnParameter",
    "CfnParameterProps",
    "CfnPatchBaseline",
    "CfnPatchBaselineProps",
    "CfnResourceDataSync",
    "CfnResourceDataSyncProps",
    "CommonStringParameterAttributes",
    "IParameter",
    "IStringListParameter",
    "IStringParameter",
    "ParameterOptions",
    "ParameterTier",
    "ParameterType",
    "SecureStringParameterAttributes",
    "StringListParameter",
    "StringListParameterProps",
    "StringParameter",
    "StringParameterAttributes",
    "StringParameterProps",
]

publication.publish()
