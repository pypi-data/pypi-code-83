'''
[![NPM version](https://badge.fury.io/js/cdk-quicksight-constructs.svg)](https://badge.fury.io/js/cdk-quicksight-constructs)
[![PyPI version](https://badge.fury.io/py/cdk-quicksight-constructs.svg)](https://badge.fury.io/py/cdk-quicksight-constructs)
![Release](https://github.com/mmuller88/cdk-quicksight-constructs/workflows/Release/badge.svg)

# cdk-quicksight-constructs

This an AWS CDK Custom Constructs repository for AWS QuickSight resources which are currently not supported by Cloudformation. That are currently:

* DataSource
* DataSet

The Repository is build and managed by Projen. [Projen](https://github.com/projen/projen) is used to manage the Github TypeScript AWS CDK setup. It is developed and maintained from the AWS CDK Community and the favorite framework to manage those AWS CDK project setups.

# Example

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
users = ["martin"]

datasource = DataSource(stack, "DataSource",
    name="cdkdatasource",
    type="ATHENA",
    data_source_parameters={
        "athena_parameters": {
            "work_group": "ddbworkgroup"
        }
    },
    users=users
)

DataSet(stack, "DataSet",
    name="cdkdataset",
    users=users,
    physical_table_map={
        "users": {
            "custom_sql": {
                "data_source_arn": datasource.data_source_arn,
                "name": "users",
                "sql_query": "SELECT primarypractice, dateofbirth FROM \"ddbconnector\".\"martin1\".\"martin1\" WHERE groupid = 'users' AND firstname is not null",
                "columns": [{"name": "primarypractice", "type": "STRING"}, {"name": "dateofbirth", "type": "STRING"}
                ]
            }
        },
        "practices": {
            "custom_sql": {
                "data_source_arn": datasource.data_source_arn,
                "name": "practices",
                "sql_query": "SELECT id, name FROM \"ddbconnector\".\"martin1\".\"martin1\" WHERE groupid = 'medical-practices' AND name is not null",
                "columns": [{"name": "id", "type": "STRING"}, {"name": "name", "type": "STRING"}
                ]
            }
        }
    },
    logical_table_map={
        "users": {
            "alias": "users",
            "source": {
                "physical_table_id": "users"
            }
        },
        "practices": {
            "alias": "practices",
            "source": {
                "physical_table_id": "practices"
            }
        },
        "users-practices": {
            "alias": "users-practices",
            "source": {
                "join_instruction": {
                    "left_operand": "users",
                    "right_operand": "practices",
                    "type": "INNER",
                    "on_clause": "primarypractice = id"
                }
            },
            "data_transforms": [{
                "create_columns_operation": {
                    "columns": [{
                        "column_name": "age",
                        "column_id": "age",
                        "expression": "dateDiff(parseDate(dateofbirth, \"YYYY-MM-dd'T'HH:mm:ssZ\"),now(), \"YYYY\")"
                    }
                    ]
                }
            }
            ]
        }
    }
)
```

Main benefits of that are:

* managing the cdk dependencies and cdk commands like `yarn deploy`
* managing the node and github config files
* a standardized way of how to setup AWS CDK repos

# Types

The types for the DataSource and DataSet constructs are generated from the AWS SDK lib and stored in src/sdk/quicksight.ts . Steps to produce the quicksight.ts file:

* extracting the quicksight.d.ts from node_modules/aws-sdk
* renaming it to quicksight.ts and use VS to auto-fix alle issues in it
* removing the first and last parts which are not needed for the types
* replacing the properties with readonly notation
* replacing the first letter with a small letter to be camel case aligned

# Planed Features / Ideas

* ...

## Helpful Resources

* https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html
* API https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Operations.html
* SDK https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/QuickSight.html#createDataSource-property

# Troubleshooting

* ...

# Thanks To

* The CDK Community cdk-dev.slack.com
* [Projen](https://github.com/projen/projen) project and the community around it
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.core


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AccountCustomization",
    jsii_struct_bases=[],
    name_mapping={"default_theme": "defaultTheme"},
)
class AccountCustomization:
    def __init__(self, *, default_theme: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default_theme: The default theme for this QuickSight subscription.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if default_theme is not None:
            self._values["default_theme"] = default_theme

    @builtins.property
    def default_theme(self) -> typing.Optional[builtins.str]:
        '''The default theme for this QuickSight subscription.'''
        result = self._values.get("default_theme")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountCustomization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AccountSettings",
    jsii_struct_bases=[],
    name_mapping={
        "account_name": "accountName",
        "default_namespace": "defaultNamespace",
        "edition": "edition",
        "notification_email": "notificationEmail",
    },
)
class AccountSettings:
    def __init__(
        self,
        *,
        account_name: typing.Optional[builtins.str] = None,
        default_namespace: typing.Optional[builtins.str] = None,
        edition: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_name: The "account name" you provided for the QuickSight subscription in your AWS account. You create this name when you sign up for QuickSight. It is unique in all of AWS and it appears only in the console when users sign in.
        :param default_namespace: The default QuickSight namespace for your AWS account.
        :param edition: The edition of QuickSight that you're currently subscribed to: Enterprise edition or Standard edition.
        :param notification_email: The main notification email for your QuickSight subscription.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if account_name is not None:
            self._values["account_name"] = account_name
        if default_namespace is not None:
            self._values["default_namespace"] = default_namespace
        if edition is not None:
            self._values["edition"] = edition
        if notification_email is not None:
            self._values["notification_email"] = notification_email

    @builtins.property
    def account_name(self) -> typing.Optional[builtins.str]:
        '''The "account name" you provided for the QuickSight subscription in your AWS account.

        You create this name when you sign up for QuickSight. It is unique in all of AWS and it appears only in the console when users sign in.
        '''
        result = self._values.get("account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_namespace(self) -> typing.Optional[builtins.str]:
        '''The default QuickSight namespace for your AWS account.'''
        result = self._values.get("default_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def edition(self) -> typing.Optional[builtins.str]:
        '''The edition of QuickSight that you're currently subscribed to: Enterprise edition or Standard edition.'''
        result = self._values.get("edition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_email(self) -> typing.Optional[builtins.str]:
        '''The main notification email for your QuickSight subscription.'''
        result = self._values.get("notification_email")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ActiveIAMPolicyAssignment",
    jsii_struct_bases=[],
    name_mapping={"assignment_name": "assignmentName", "policy_arn": "policyArn"},
)
class ActiveIAMPolicyAssignment:
    def __init__(
        self,
        *,
        assignment_name: typing.Optional[builtins.str] = None,
        policy_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param assignment_name: A name for the IAM policy assignment.
        :param policy_arn: The Amazon Resource Name (ARN) of the resource.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if assignment_name is not None:
            self._values["assignment_name"] = assignment_name
        if policy_arn is not None:
            self._values["policy_arn"] = policy_arn

    @builtins.property
    def assignment_name(self) -> typing.Optional[builtins.str]:
        '''A name for the IAM policy assignment.'''
        result = self._values.get("assignment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("policy_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActiveIAMPolicyAssignment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AdHocFilteringOption",
    jsii_struct_bases=[],
    name_mapping={"availability_status": "availabilityStatus"},
)
class AdHocFilteringOption:
    def __init__(
        self,
        *,
        availability_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability_status: Availability status.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if availability_status is not None:
            self._values["availability_status"] = availability_status

    @builtins.property
    def availability_status(self) -> typing.Optional[builtins.str]:
        '''Availability status.'''
        result = self._values.get("availability_status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AdHocFilteringOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AmazonElasticsearchParameters",
    jsii_struct_bases=[],
    name_mapping={"domain": "domain"},
)
class AmazonElasticsearchParameters:
    def __init__(self, *, domain: builtins.str) -> None:
        '''
        :param domain: The Amazon Elasticsearch Service domain.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "domain": domain,
        }

    @builtins.property
    def domain(self) -> builtins.str:
        '''The Amazon Elasticsearch Service domain.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AmazonElasticsearchParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.Analysis",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_id": "analysisId",
        "arn": "arn",
        "created_time": "createdTime",
        "data_set_arns": "dataSetArns",
        "errors": "errors",
        "last_updated_time": "lastUpdatedTime",
        "name": "name",
        "sheets": "sheets",
        "status": "status",
        "theme_arn": "themeArn",
    },
)
class Analysis:
    def __init__(
        self,
        *,
        analysis_id: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        data_set_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        errors: typing.Optional[typing.Sequence["AnalysisError"]] = None,
        last_updated_time: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[builtins.str] = None,
        sheets: typing.Optional[typing.Sequence["Sheet"]] = None,
        status: typing.Optional[builtins.str] = None,
        theme_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param analysis_id: The ID of the analysis.
        :param arn: The Amazon Resource Name (ARN) of the analysis.
        :param created_time: The time that the analysis was created.
        :param data_set_arns: The ARNs of the datasets of the analysis.
        :param errors: Errors associated with the analysis.
        :param last_updated_time: The time that the analysis was last updated.
        :param name: The descriptive name of the analysis.
        :param sheets: A list of the associated sheets with the unique identifier and name of each sheet.
        :param status: Status associated with the analysis.
        :param theme_arn: The ARN of the theme of the analysis.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if analysis_id is not None:
            self._values["analysis_id"] = analysis_id
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if data_set_arns is not None:
            self._values["data_set_arns"] = data_set_arns
        if errors is not None:
            self._values["errors"] = errors
        if last_updated_time is not None:
            self._values["last_updated_time"] = last_updated_time
        if name is not None:
            self._values["name"] = name
        if sheets is not None:
            self._values["sheets"] = sheets
        if status is not None:
            self._values["status"] = status
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn

    @builtins.property
    def analysis_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the analysis.'''
        result = self._values.get("analysis_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the analysis.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that the analysis was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def data_set_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the datasets of the analysis.'''
        result = self._values.get("data_set_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def errors(self) -> typing.Optional[typing.List["AnalysisError"]]:
        '''Errors associated with the analysis.'''
        result = self._values.get("errors")
        return typing.cast(typing.Optional[typing.List["AnalysisError"]], result)

    @builtins.property
    def last_updated_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that the analysis was last updated.'''
        result = self._values.get("last_updated_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The descriptive name of the analysis.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sheets(self) -> typing.Optional[typing.List["Sheet"]]:
        '''A list of the associated sheets with the unique identifier and name of each sheet.'''
        result = self._values.get("sheets")
        return typing.cast(typing.Optional[typing.List["Sheet"]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Status associated with the analysis.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the theme of the analysis.'''
        result = self._values.get("theme_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Analysis(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AnalysisError",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "type": "type"},
)
class AnalysisError:
    def __init__(
        self,
        *,
        message: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: The message associated with the analysis error.
        :param type: The type of the analysis error.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The message associated with the analysis error.'''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the analysis error.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnalysisError(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AnalysisSearchFilter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "operator": "operator", "value": "value"},
)
class AnalysisSearchFilter:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the value that you want to use as a filter, for example "Name": "QUICKSIGHT_USER".
        :param operator: The comparison operator that you want to use as a filter, for example "Operator": "StringEquals".
        :param value: The value of the named item, in this case QUICKSIGHT_USER, that you want to use as a filter, for example "Value". An example is "arn:aws:quicksight:us-east-1:1:user/default/UserName1".
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if operator is not None:
            self._values["operator"] = operator
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the value that you want to use as a filter, for example "Name": "QUICKSIGHT_USER".'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''The comparison operator that you want to use as a filter, for example "Operator": "StringEquals".'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value of the named item, in this case QUICKSIGHT_USER, that you want to use as a filter, for example "Value".

        An example is "arn:aws:quicksight:us-east-1:1:user/default/UserName1".
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnalysisSearchFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AnalysisSourceEntity",
    jsii_struct_bases=[],
    name_mapping={"source_template": "sourceTemplate"},
)
class AnalysisSourceEntity:
    def __init__(
        self,
        *,
        source_template: typing.Optional["AnalysisSourceTemplate"] = None,
    ) -> None:
        '''
        :param source_template: The source template for the source entity of the analysis.
        '''
        if isinstance(source_template, dict):
            source_template = AnalysisSourceTemplate(**source_template)
        self._values: typing.Dict[str, typing.Any] = {}
        if source_template is not None:
            self._values["source_template"] = source_template

    @builtins.property
    def source_template(self) -> typing.Optional["AnalysisSourceTemplate"]:
        '''The source template for the source entity of the analysis.'''
        result = self._values.get("source_template")
        return typing.cast(typing.Optional["AnalysisSourceTemplate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnalysisSourceEntity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AnalysisSourceTemplate",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "data_set_references": "dataSetReferences"},
)
class AnalysisSourceTemplate:
    def __init__(
        self,
        *,
        arn: builtins.str,
        data_set_references: typing.Sequence["DataSetReference"],
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the source template of an analysis.
        :param data_set_references: The dataset references of the source template of an analysis.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
            "data_set_references": data_set_references,
        }

    @builtins.property
    def arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the source template of an analysis.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_references(self) -> typing.List["DataSetReference"]:
        '''The dataset references of the source template of an analysis.'''
        result = self._values.get("data_set_references")
        assert result is not None, "Required property 'data_set_references' is missing"
        return typing.cast(typing.List["DataSetReference"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnalysisSourceTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AnalysisSummary",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_id": "analysisId",
        "arn": "arn",
        "created_time": "createdTime",
        "last_updated_time": "lastUpdatedTime",
        "name": "name",
        "status": "status",
    },
)
class AnalysisSummary:
    def __init__(
        self,
        *,
        analysis_id: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        last_updated_time: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param analysis_id: The ID of the analysis. This ID displays in the URL.
        :param arn: The Amazon Resource Name (ARN) for the analysis.
        :param created_time: The time that the analysis was created.
        :param last_updated_time: The time that the analysis was last updated.
        :param name: The name of the analysis. This name is displayed in the QuickSight console.
        :param status: The last known status for the analysis.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if analysis_id is not None:
            self._values["analysis_id"] = analysis_id
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if last_updated_time is not None:
            self._values["last_updated_time"] = last_updated_time
        if name is not None:
            self._values["name"] = name
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def analysis_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the analysis.

        This ID displays in the URL.
        '''
        result = self._values.get("analysis_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the analysis.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that the analysis was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def last_updated_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that the analysis was last updated.'''
        result = self._values.get("last_updated_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the analysis.

        This name is displayed in the QuickSight console.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The last known status for the analysis.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnalysisSummary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AthenaParameters",
    jsii_struct_bases=[],
    name_mapping={"work_group": "workGroup"},
)
class AthenaParameters:
    def __init__(self, *, work_group: typing.Optional[builtins.str] = None) -> None:
        '''
        :param work_group: The workgroup that Amazon Athena uses.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if work_group is not None:
            self._values["work_group"] = work_group

    @builtins.property
    def work_group(self) -> typing.Optional[builtins.str]:
        '''The workgroup that Amazon Athena uses.'''
        result = self._values.get("work_group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AthenaParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AuroraParameters",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class AuroraParameters:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Database.
        :param host: Host.
        :param port: Port.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Database.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Host.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuroraParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AuroraPostgreSqlParameters",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class AuroraPostgreSqlParameters:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Database.
        :param host: Host.
        :param port: Port.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Database.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Host.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuroraPostgreSqlParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.AwsIotAnalyticsParameters",
    jsii_struct_bases=[],
    name_mapping={"data_set_name": "dataSetName"},
)
class AwsIotAnalyticsParameters:
    def __init__(self, *, data_set_name: builtins.str) -> None:
        '''
        :param data_set_name: Dataset name.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "data_set_name": data_set_name,
        }

    @builtins.property
    def data_set_name(self) -> builtins.str:
        '''Dataset name.'''
        result = self._values.get("data_set_name")
        assert result is not None, "Required property 'data_set_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsIotAnalyticsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.BorderStyle",
    jsii_struct_bases=[],
    name_mapping={"show": "show"},
)
class BorderStyle:
    def __init__(self, *, show: typing.Optional[builtins.bool] = None) -> None:
        '''
        :param show: The option to enable display of borders for visuals.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if show is not None:
            self._values["show"] = show

    @builtins.property
    def show(self) -> typing.Optional[builtins.bool]:
        '''The option to enable display of borders for visuals.'''
        result = self._values.get("show")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BorderStyle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CalculatedColumn",
    jsii_struct_bases=[],
    name_mapping={
        "column_id": "columnId",
        "column_name": "columnName",
        "expression": "expression",
    },
)
class CalculatedColumn:
    def __init__(
        self,
        *,
        column_id: builtins.str,
        column_name: builtins.str,
        expression: builtins.str,
    ) -> None:
        '''
        :param column_id: A unique ID to identify a calculated column. During a dataset update, if the column ID of a calculated column matches that of an existing calculated column, Amazon QuickSight preserves the existing calculated column.
        :param column_name: Column name.
        :param expression: An expression that defines the calculated column.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "column_id": column_id,
            "column_name": column_name,
            "expression": expression,
        }

    @builtins.property
    def column_id(self) -> builtins.str:
        '''A unique ID to identify a calculated column.

        During a dataset update, if the column ID of a calculated column matches that of an existing calculated column, Amazon QuickSight preserves the existing calculated column.
        '''
        result = self._values.get("column_id")
        assert result is not None, "Required property 'column_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def column_name(self) -> builtins.str:
        '''Column name.'''
        result = self._values.get("column_name")
        assert result is not None, "Required property 'column_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> builtins.str:
        '''An expression that defines the calculated column.'''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CalculatedColumn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CancelIngestionRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_set_id": "dataSetId",
        "ingestion_id": "ingestionId",
    },
)
class CancelIngestionRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_id: builtins.str,
        ingestion_id: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_set_id: The ID of the dataset used in the ingestion.
        :param ingestion_id: An ID for the ingestion.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_id": data_set_id,
            "ingestion_id": ingestion_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The ID of the dataset used in the ingestion.'''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ingestion_id(self) -> builtins.str:
        '''An ID for the ingestion.'''
        result = self._values.get("ingestion_id")
        assert result is not None, "Required property 'ingestion_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CancelIngestionRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CancelIngestionResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "ingestion_id": "ingestionId",
        "request_id": "requestId",
        "status": "status",
    },
)
class CancelIngestionResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        ingestion_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) for the data ingestion.
        :param ingestion_id: An ID for the ingestion.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if ingestion_id is not None:
            self._values["ingestion_id"] = ingestion_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the data ingestion.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingestion_id(self) -> typing.Optional[builtins.str]:
        '''An ID for the ingestion.'''
        result = self._values.get("ingestion_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CancelIngestionResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CastColumnTypeOperation",
    jsii_struct_bases=[],
    name_mapping={
        "column_name": "columnName",
        "new_column_type": "newColumnType",
        "format": "format",
    },
)
class CastColumnTypeOperation:
    def __init__(
        self,
        *,
        column_name: builtins.str,
        new_column_type: builtins.str,
        format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param column_name: Column name.
        :param new_column_type: New column data type.
        :param format: When casting a column from string to datetime type, you can supply a string in a format supported by Amazon QuickSight to denote the source data format.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "column_name": column_name,
            "new_column_type": new_column_type,
        }
        if format is not None:
            self._values["format"] = format

    @builtins.property
    def column_name(self) -> builtins.str:
        '''Column name.'''
        result = self._values.get("column_name")
        assert result is not None, "Required property 'column_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def new_column_type(self) -> builtins.str:
        '''New column data type.'''
        result = self._values.get("new_column_type")
        assert result is not None, "Required property 'new_column_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> typing.Optional[builtins.str]:
        '''When casting a column from string to datetime type, you can supply a string in a format supported by Amazon QuickSight to denote the source data format.'''
        result = self._values.get("format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CastColumnTypeOperation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ClientApiVersions",
    jsii_struct_bases=[],
    name_mapping={"api_version": "apiVersion"},
)
class ClientApiVersions:
    def __init__(self, *, api_version: typing.Optional[builtins.str] = None) -> None:
        '''
        :param api_version: A string in YYYY-MM-DD format that represents the latest possible API version that can be used in this service. Specify 'latest' to use the latest possible version.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if api_version is not None:
            self._values["api_version"] = api_version

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''A string in YYYY-MM-DD format that represents the latest possible API version that can be used in this service.

        Specify 'latest' to use the latest possible version.
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClientApiVersions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ColumnDescription",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class ColumnDescription:
    def __init__(self, *, text: typing.Optional[builtins.str] = None) -> None:
        '''
        :param text: The text of a description for a column.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''The text of a description for a column.'''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ColumnDescription(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ColumnGroup",
    jsii_struct_bases=[],
    name_mapping={"geo_spatial_column_group": "geoSpatialColumnGroup"},
)
class ColumnGroup:
    def __init__(
        self,
        *,
        geo_spatial_column_group: typing.Optional["GeoSpatialColumnGroup"] = None,
    ) -> None:
        '''
        :param geo_spatial_column_group: Geospatial column group that denotes a hierarchy.
        '''
        if isinstance(geo_spatial_column_group, dict):
            geo_spatial_column_group = GeoSpatialColumnGroup(**geo_spatial_column_group)
        self._values: typing.Dict[str, typing.Any] = {}
        if geo_spatial_column_group is not None:
            self._values["geo_spatial_column_group"] = geo_spatial_column_group

    @builtins.property
    def geo_spatial_column_group(self) -> typing.Optional["GeoSpatialColumnGroup"]:
        '''Geospatial column group that denotes a hierarchy.'''
        result = self._values.get("geo_spatial_column_group")
        return typing.cast(typing.Optional["GeoSpatialColumnGroup"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ColumnGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ColumnGroupColumnSchema",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class ColumnGroupColumnSchema:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: The name of the column group's column schema.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the column group's column schema.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ColumnGroupColumnSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ColumnGroupSchema",
    jsii_struct_bases=[],
    name_mapping={
        "column_group_column_schema_list": "columnGroupColumnSchemaList",
        "name": "name",
    },
)
class ColumnGroupSchema:
    def __init__(
        self,
        *,
        column_group_column_schema_list: typing.Optional[typing.Sequence[ColumnGroupColumnSchema]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param column_group_column_schema_list: A structure containing the list of schemas for column group columns.
        :param name: The name of the column group schema.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if column_group_column_schema_list is not None:
            self._values["column_group_column_schema_list"] = column_group_column_schema_list
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def column_group_column_schema_list(
        self,
    ) -> typing.Optional[typing.List[ColumnGroupColumnSchema]]:
        '''A structure containing the list of schemas for column group columns.'''
        result = self._values.get("column_group_column_schema_list")
        return typing.cast(typing.Optional[typing.List[ColumnGroupColumnSchema]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the column group schema.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ColumnGroupSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ColumnLevelPermissionRule",
    jsii_struct_bases=[],
    name_mapping={"column_names": "columnNames", "principals": "principals"},
)
class ColumnLevelPermissionRule:
    def __init__(
        self,
        *,
        column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        principals: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param column_names: An array of column names.
        :param principals: An array of Amazon Resource Names (ARNs) for QuickSight users or groups.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if column_names is not None:
            self._values["column_names"] = column_names
        if principals is not None:
            self._values["principals"] = principals

    @builtins.property
    def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of column names.'''
        result = self._values.get("column_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of Amazon Resource Names (ARNs) for QuickSight users or groups.'''
        result = self._values.get("principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ColumnLevelPermissionRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ColumnSchema",
    jsii_struct_bases=[],
    name_mapping={
        "data_type": "dataType",
        "geographic_role": "geographicRole",
        "name": "name",
    },
)
class ColumnSchema:
    def __init__(
        self,
        *,
        data_type: typing.Optional[builtins.str] = None,
        geographic_role: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_type: The data type of the column schema.
        :param geographic_role: The geographic role of the column schema.
        :param name: The name of the column schema.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if data_type is not None:
            self._values["data_type"] = data_type
        if geographic_role is not None:
            self._values["geographic_role"] = geographic_role
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The data type of the column schema.'''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def geographic_role(self) -> typing.Optional[builtins.str]:
        '''The geographic role of the column schema.'''
        result = self._values.get("geographic_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the column schema.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ColumnSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ColumnTag",
    jsii_struct_bases=[],
    name_mapping={
        "column_description": "columnDescription",
        "column_geographic_role": "columnGeographicRole",
    },
)
class ColumnTag:
    def __init__(
        self,
        *,
        column_description: typing.Optional[ColumnDescription] = None,
        column_geographic_role: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param column_description: A description for a column.
        :param column_geographic_role: A geospatial role for a column.
        '''
        if isinstance(column_description, dict):
            column_description = ColumnDescription(**column_description)
        self._values: typing.Dict[str, typing.Any] = {}
        if column_description is not None:
            self._values["column_description"] = column_description
        if column_geographic_role is not None:
            self._values["column_geographic_role"] = column_geographic_role

    @builtins.property
    def column_description(self) -> typing.Optional[ColumnDescription]:
        '''A description for a column.'''
        result = self._values.get("column_description")
        return typing.cast(typing.Optional[ColumnDescription], result)

    @builtins.property
    def column_geographic_role(self) -> typing.Optional[builtins.str]:
        '''A geospatial role for a column.'''
        result = self._values.get("column_geographic_role")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ColumnTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateAccountCustomizationRequest",
    jsii_struct_bases=[],
    name_mapping={
        "account_customization": "accountCustomization",
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "tags": "tags",
    },
)
class CreateAccountCustomizationRequest:
    def __init__(
        self,
        *,
        account_customization: AccountCustomization,
        aws_account_id: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence["Tag"]] = None,
    ) -> None:
        '''
        :param account_customization: The QuickSight customizations you're adding in the current AWS Region. You can add these to an AWS account and a QuickSight namespace. For example, you can add a default theme by setting AccountCustomization to the midnight theme: "AccountCustomization": { "DefaultTheme": "arn:aws:quicksight::aws:theme/MIDNIGHT" }. Or, you can add a custom theme by specifying "AccountCustomization": { "DefaultTheme": "arn:aws:quicksight:us-west-2:111122223333:theme/bdb844d0-0fe9-4d9d-b520-0fe602d93639" }.
        :param aws_account_id: The ID for the AWS account that you want to customize QuickSight for.
        :param namespace: The QuickSight namespace that you want to add customizations to.
        :param tags: A list of the tags that you want to attach to this resource.
        '''
        if isinstance(account_customization, dict):
            account_customization = AccountCustomization(**account_customization)
        self._values: typing.Dict[str, typing.Any] = {
            "account_customization": account_customization,
            "aws_account_id": aws_account_id,
        }
        if namespace is not None:
            self._values["namespace"] = namespace
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def account_customization(self) -> AccountCustomization:
        '''The QuickSight customizations you're adding in the current AWS Region.

        You can add these to an AWS account and a QuickSight namespace.  For example, you can add a default theme by setting AccountCustomization to the midnight theme: "AccountCustomization": { "DefaultTheme": "arn:aws:quicksight::aws:theme/MIDNIGHT" }. Or, you can add a custom theme by specifying "AccountCustomization": { "DefaultTheme": "arn:aws:quicksight:us-west-2:111122223333:theme/bdb844d0-0fe9-4d9d-b520-0fe602d93639" }.
        '''
        result = self._values.get("account_customization")
        assert result is not None, "Required property 'account_customization' is missing"
        return typing.cast(AccountCustomization, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that you want to customize QuickSight for.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The QuickSight namespace that you want to add customizations to.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''A list of the tags that you want to attach to this resource.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateAccountCustomizationRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateAccountCustomizationResponse",
    jsii_struct_bases=[],
    name_mapping={
        "account_customization": "accountCustomization",
        "arn": "arn",
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "request_id": "requestId",
        "status": "status",
    },
)
class CreateAccountCustomizationResponse:
    def __init__(
        self,
        *,
        account_customization: typing.Optional[AccountCustomization] = None,
        arn: typing.Optional[builtins.str] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param account_customization: The QuickSight customizations you're adding in the current AWS Region.
        :param arn: The Amazon Resource Name (ARN) for the customization that you created for this AWS account.
        :param aws_account_id: The ID for the AWS account that you want to customize QuickSight for.
        :param namespace: The namespace associated with the customization you're creating.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(account_customization, dict):
            account_customization = AccountCustomization(**account_customization)
        self._values: typing.Dict[str, typing.Any] = {}
        if account_customization is not None:
            self._values["account_customization"] = account_customization
        if arn is not None:
            self._values["arn"] = arn
        if aws_account_id is not None:
            self._values["aws_account_id"] = aws_account_id
        if namespace is not None:
            self._values["namespace"] = namespace
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def account_customization(self) -> typing.Optional[AccountCustomization]:
        '''The QuickSight customizations you're adding in the current AWS Region.'''
        result = self._values.get("account_customization")
        return typing.cast(typing.Optional[AccountCustomization], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the customization that you created for this AWS account.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the AWS account that you want to customize QuickSight for.'''
        result = self._values.get("aws_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace associated with the customization you're creating.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateAccountCustomizationResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateAnalysisRequest",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_id": "analysisId",
        "aws_account_id": "awsAccountId",
        "name": "name",
        "source_entity": "sourceEntity",
        "parameters": "parameters",
        "permissions": "permissions",
        "tags": "tags",
        "theme_arn": "themeArn",
    },
)
class CreateAnalysisRequest:
    def __init__(
        self,
        *,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
        name: builtins.str,
        source_entity: AnalysisSourceEntity,
        parameters: typing.Optional["Parameters"] = None,
        permissions: typing.Optional[typing.Sequence["ResourcePermission"]] = None,
        tags: typing.Optional[typing.Sequence["Tag"]] = None,
        theme_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param analysis_id: The ID for the analysis that you're creating. This ID displays in the URL of the analysis.
        :param aws_account_id: The ID of the AWS account where you are creating an analysis.
        :param name: A descriptive name for the analysis that you're creating. This name displays for the analysis in the QuickSight console.
        :param source_entity: A source entity to use for the analysis that you're creating. This metadata structure contains details that describe a source template and one or more datasets.
        :param parameters: The parameter names and override values that you want to use. An analysis can have any parameter type, and some parameters might accept multiple values.
        :param permissions: A structure that describes the principals and the resource-level permissions on an analysis. You can use the Permissions structure to grant permissions by providing a list of AWS Identity and Access Management (IAM) action information for each principal listed by Amazon Resource Name (ARN). To specify no permissions, omit Permissions.
        :param tags: Contains a map of the key-value pairs for the resource tag or tags assigned to the analysis.
        :param theme_arn: The ARN for the theme to apply to the analysis that you're creating. To see the theme in the QuickSight console, make sure that you have access to it.
        '''
        if isinstance(source_entity, dict):
            source_entity = AnalysisSourceEntity(**source_entity)
        if isinstance(parameters, dict):
            parameters = Parameters(**parameters)
        self._values: typing.Dict[str, typing.Any] = {
            "analysis_id": analysis_id,
            "aws_account_id": aws_account_id,
            "name": name,
            "source_entity": source_entity,
        }
        if parameters is not None:
            self._values["parameters"] = parameters
        if permissions is not None:
            self._values["permissions"] = permissions
        if tags is not None:
            self._values["tags"] = tags
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn

    @builtins.property
    def analysis_id(self) -> builtins.str:
        '''The ID for the analysis that you're creating.

        This ID displays in the URL of the analysis.
        '''
        result = self._values.get("analysis_id")
        assert result is not None, "Required property 'analysis_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account where you are creating an analysis.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A descriptive name for the analysis that you're creating.

        This name displays for the analysis in the QuickSight console.
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_entity(self) -> AnalysisSourceEntity:
        '''A source entity to use for the analysis that you're creating.

        This metadata structure contains details that describe a source template and one or more datasets.
        '''
        result = self._values.get("source_entity")
        assert result is not None, "Required property 'source_entity' is missing"
        return typing.cast(AnalysisSourceEntity, result)

    @builtins.property
    def parameters(self) -> typing.Optional["Parameters"]:
        '''The parameter names and override values that you want to use.

        An analysis can have any parameter type, and some parameters might accept multiple values.
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["Parameters"], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List["ResourcePermission"]]:
        '''A structure that describes the principals and the resource-level permissions on an analysis.

        You can use the Permissions structure to grant permissions by providing a list of AWS Identity and Access Management (IAM) action information for each principal listed by Amazon Resource Name (ARN).  To specify no permissions, omit Permissions.
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List["ResourcePermission"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''Contains a map of the key-value pairs for the resource tag or tags assigned to the analysis.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the theme to apply to the analysis that you're creating.

        To see the theme in the QuickSight console, make sure that you have access to it.
        '''
        result = self._values.get("theme_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateAnalysisRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateAnalysisResponse",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_id": "analysisId",
        "arn": "arn",
        "creation_status": "creationStatus",
        "request_id": "requestId",
        "status": "status",
    },
)
class CreateAnalysisResponse:
    def __init__(
        self,
        *,
        analysis_id: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        creation_status: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param analysis_id: The ID of the analysis.
        :param arn: The ARN for the analysis.
        :param creation_status: The status of the creation of the analysis.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if analysis_id is not None:
            self._values["analysis_id"] = analysis_id
        if arn is not None:
            self._values["arn"] = arn
        if creation_status is not None:
            self._values["creation_status"] = creation_status
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def analysis_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the analysis.'''
        result = self._values.get("analysis_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the analysis.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_status(self) -> typing.Optional[builtins.str]:
        '''The status of the creation of the analysis.'''
        result = self._values.get("creation_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateAnalysisResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateColumnsOperation",
    jsii_struct_bases=[],
    name_mapping={"columns": "columns"},
)
class CreateColumnsOperation:
    def __init__(self, *, columns: typing.Sequence[CalculatedColumn]) -> None:
        '''
        :param columns: Calculated columns to create.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "columns": columns,
        }

    @builtins.property
    def columns(self) -> typing.List[CalculatedColumn]:
        '''Calculated columns to create.'''
        result = self._values.get("columns")
        assert result is not None, "Required property 'columns' is missing"
        return typing.cast(typing.List[CalculatedColumn], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateColumnsOperation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateDashboardRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dashboard_id": "dashboardId",
        "name": "name",
        "source_entity": "sourceEntity",
        "dashboard_publish_options": "dashboardPublishOptions",
        "parameters": "parameters",
        "permissions": "permissions",
        "tags": "tags",
        "theme_arn": "themeArn",
        "version_description": "versionDescription",
    },
)
class CreateDashboardRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
        name: builtins.str,
        source_entity: "DashboardSourceEntity",
        dashboard_publish_options: typing.Optional["DashboardPublishOptions"] = None,
        parameters: typing.Optional["Parameters"] = None,
        permissions: typing.Optional[typing.Sequence["ResourcePermission"]] = None,
        tags: typing.Optional[typing.Sequence["Tag"]] = None,
        theme_arn: typing.Optional[builtins.str] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account where you want to create the dashboard.
        :param dashboard_id: The ID for the dashboard, also added to the IAM policy.
        :param name: The display name of the dashboard.
        :param source_entity: The entity that you are using as a source when you create the dashboard. In SourceEntity, you specify the type of object you're using as source. You can only create a dashboard from a template, so you use a SourceTemplate entity. If you need to create a dashboard from an analysis, first convert the analysis to a template by using the CreateTemplate API operation. For SourceTemplate, specify the Amazon Resource Name (ARN) of the source template. The SourceTemplateARN can contain any AWS Account and any QuickSight-supported AWS Region. Use the DataSetReferences entity within SourceTemplate to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder.
        :param dashboard_publish_options: Options for publishing the dashboard when you create it: AvailabilityStatus for AdHocFilteringOption - This status can be either ENABLED or DISABLED. When this is set to DISABLED, QuickSight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is ENABLED by default. AvailabilityStatus for ExportToCSVOption - This status can be either ENABLED or DISABLED. The visual option to export data to .CSV format isn't enabled when this is set to DISABLED. This option is ENABLED by default. VisibilityState for SheetControlsOption - This visibility state can be either COLLAPSED or EXPANDED. This option is COLLAPSED by default.
        :param parameters: The parameters for the creation of the dashboard, which you want to use to override the default settings. A dashboard can have any type of parameters, and some parameters might accept multiple values.
        :param permissions: A structure that contains the permissions of the dashboard. You can use this structure for granting permissions by providing a list of IAM action information for each principal ARN. To specify no permissions, omit the permissions list.
        :param tags: Contains a map of the key-value pairs for the resource tag or tags assigned to the dashboard.
        :param theme_arn: The Amazon Resource Name (ARN) of the theme that is being used for this dashboard. If you add a value for this field, it overrides the value that is used in the source entity. The theme ARN must exist in the same AWS account where you create the dashboard.
        :param version_description: A description for the first version of the dashboard being created.
        '''
        if isinstance(source_entity, dict):
            source_entity = DashboardSourceEntity(**source_entity)
        if isinstance(dashboard_publish_options, dict):
            dashboard_publish_options = DashboardPublishOptions(**dashboard_publish_options)
        if isinstance(parameters, dict):
            parameters = Parameters(**parameters)
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_id": dashboard_id,
            "name": name,
            "source_entity": source_entity,
        }
        if dashboard_publish_options is not None:
            self._values["dashboard_publish_options"] = dashboard_publish_options
        if parameters is not None:
            self._values["parameters"] = parameters
        if permissions is not None:
            self._values["permissions"] = permissions
        if tags is not None:
            self._values["tags"] = tags
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account where you want to create the dashboard.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        '''The ID for the dashboard, also added to the IAM policy.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The display name of the dashboard.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_entity(self) -> "DashboardSourceEntity":
        '''The entity that you are using as a source when you create the dashboard.

        In SourceEntity, you specify the type of object you're using as source. You can only create a dashboard from a template, so you use a SourceTemplate entity. If you need to create a dashboard from an analysis, first convert the analysis to a template by using the CreateTemplate API operation. For SourceTemplate, specify the Amazon Resource Name (ARN) of the source template. The SourceTemplateARN can contain any AWS Account and any QuickSight-supported AWS Region.  Use the DataSetReferences entity within SourceTemplate to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder.
        '''
        result = self._values.get("source_entity")
        assert result is not None, "Required property 'source_entity' is missing"
        return typing.cast("DashboardSourceEntity", result)

    @builtins.property
    def dashboard_publish_options(self) -> typing.Optional["DashboardPublishOptions"]:
        '''Options for publishing the dashboard when you create it:    AvailabilityStatus for AdHocFilteringOption - This status can be either ENABLED or DISABLED.

        When this is set to DISABLED, QuickSight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is ENABLED by default.     AvailabilityStatus for ExportToCSVOption - This status can be either ENABLED or DISABLED. The visual option to export data to .CSV format isn't enabled when this is set to DISABLED. This option is ENABLED by default.     VisibilityState for SheetControlsOption - This visibility state can be either COLLAPSED or EXPANDED. This option is COLLAPSED by default.
        '''
        result = self._values.get("dashboard_publish_options")
        return typing.cast(typing.Optional["DashboardPublishOptions"], result)

    @builtins.property
    def parameters(self) -> typing.Optional["Parameters"]:
        '''The parameters for the creation of the dashboard, which you want to use to override the default settings.

        A dashboard can have any type of parameters, and some parameters might accept multiple values.
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["Parameters"], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List["ResourcePermission"]]:
        '''A structure that contains the permissions of the dashboard.

        You can use this structure for granting permissions by providing a list of IAM action information for each principal ARN.  To specify no permissions, omit the permissions list.
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List["ResourcePermission"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''Contains a map of the key-value pairs for the resource tag or tags assigned to the dashboard.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the theme that is being used for this dashboard.

        If you add a value for this field, it overrides the value that is used in the source entity. The theme ARN must exist in the same AWS account where you create the dashboard.
        '''
        result = self._values.get("theme_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''A description for the first version of the dashboard being created.'''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateDashboardRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateDashboardResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "creation_status": "creationStatus",
        "dashboard_id": "dashboardId",
        "request_id": "requestId",
        "status": "status",
        "version_arn": "versionArn",
    },
)
class CreateDashboardResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        creation_status: typing.Optional[builtins.str] = None,
        dashboard_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The ARN of the dashboard.
        :param creation_status: The status of the dashboard creation request.
        :param dashboard_id: The ID for the dashboard.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param version_arn: The ARN of the dashboard, including the version number of the first version that is created.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if creation_status is not None:
            self._values["creation_status"] = creation_status
        if dashboard_id is not None:
            self._values["dashboard_id"] = dashboard_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if version_arn is not None:
            self._values["version_arn"] = version_arn

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the dashboard.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_status(self) -> typing.Optional[builtins.str]:
        '''The status of the dashboard creation request.'''
        result = self._values.get("creation_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dashboard_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the dashboard.'''
        result = self._values.get("dashboard_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the dashboard, including the version number of the first version that is created.'''
        result = self._values.get("version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateDashboardResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateDataSetRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_set_id": "dataSetId",
        "import_mode": "importMode",
        "name": "name",
        "physical_table_map": "physicalTableMap",
        "column_groups": "columnGroups",
        "column_level_permission_rules": "columnLevelPermissionRules",
        "field_folders": "fieldFolders",
        "logical_table_map": "logicalTableMap",
        "permissions": "permissions",
        "row_level_permission_data_set": "rowLevelPermissionDataSet",
        "tags": "tags",
    },
)
class CreateDataSetRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_id: builtins.str,
        import_mode: builtins.str,
        name: builtins.str,
        physical_table_map: typing.Mapping[builtins.str, "PhysicalTable"],
        column_groups: typing.Optional[typing.Sequence[ColumnGroup]] = None,
        column_level_permission_rules: typing.Optional[typing.Sequence[ColumnLevelPermissionRule]] = None,
        field_folders: typing.Optional[typing.Mapping[builtins.str, "FieldFolder"]] = None,
        logical_table_map: typing.Optional[typing.Mapping[builtins.str, "LogicalTable"]] = None,
        permissions: typing.Optional[typing.Sequence["ResourcePermission"]] = None,
        row_level_permission_data_set: typing.Optional["RowLevelPermissionDataSet"] = None,
        tags: typing.Optional[typing.Sequence["Tag"]] = None,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_set_id: An ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.
        :param import_mode: Indicates whether you want to import the data into SPICE.
        :param name: The display name for the dataset.
        :param physical_table_map: Declares the physical tables that are available in the underlying data sources.
        :param column_groups: Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.
        :param column_level_permission_rules: A set of one or more definitions of a ColumnLevelPermissionRule .
        :param field_folders: The folder that contains fields and nested subfolders for your dataset.
        :param logical_table_map: Configures the combination and transformation of the data from the physical tables.
        :param permissions: A list of resource permissions on the dataset.
        :param row_level_permission_data_set: The row-level security configuration for the data that you want to create.
        :param tags: Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.
        '''
        if isinstance(row_level_permission_data_set, dict):
            row_level_permission_data_set = RowLevelPermissionDataSet(**row_level_permission_data_set)
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_id": data_set_id,
            "import_mode": import_mode,
            "name": name,
            "physical_table_map": physical_table_map,
        }
        if column_groups is not None:
            self._values["column_groups"] = column_groups
        if column_level_permission_rules is not None:
            self._values["column_level_permission_rules"] = column_level_permission_rules
        if field_folders is not None:
            self._values["field_folders"] = field_folders
        if logical_table_map is not None:
            self._values["logical_table_map"] = logical_table_map
        if permissions is not None:
            self._values["permissions"] = permissions
        if row_level_permission_data_set is not None:
            self._values["row_level_permission_data_set"] = row_level_permission_data_set
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''An ID for the dataset that you want to create.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def import_mode(self) -> builtins.str:
        '''Indicates whether you want to import the data into SPICE.'''
        result = self._values.get("import_mode")
        assert result is not None, "Required property 'import_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The display name for the dataset.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def physical_table_map(self) -> typing.Mapping[builtins.str, "PhysicalTable"]:
        '''Declares the physical tables that are available in the underlying data sources.'''
        result = self._values.get("physical_table_map")
        assert result is not None, "Required property 'physical_table_map' is missing"
        return typing.cast(typing.Mapping[builtins.str, "PhysicalTable"], result)

    @builtins.property
    def column_groups(self) -> typing.Optional[typing.List[ColumnGroup]]:
        '''Groupings of columns that work together in certain QuickSight features.

        Currently, only geospatial hierarchy is supported.
        '''
        result = self._values.get("column_groups")
        return typing.cast(typing.Optional[typing.List[ColumnGroup]], result)

    @builtins.property
    def column_level_permission_rules(
        self,
    ) -> typing.Optional[typing.List[ColumnLevelPermissionRule]]:
        '''A set of one or more definitions of a  ColumnLevelPermissionRule .'''
        result = self._values.get("column_level_permission_rules")
        return typing.cast(typing.Optional[typing.List[ColumnLevelPermissionRule]], result)

    @builtins.property
    def field_folders(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "FieldFolder"]]:
        '''The folder that contains fields and nested subfolders for your dataset.'''
        result = self._values.get("field_folders")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "FieldFolder"]], result)

    @builtins.property
    def logical_table_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "LogicalTable"]]:
        '''Configures the combination and transformation of the data from the physical tables.'''
        result = self._values.get("logical_table_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "LogicalTable"]], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List["ResourcePermission"]]:
        '''A list of resource permissions on the dataset.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List["ResourcePermission"]], result)

    @builtins.property
    def row_level_permission_data_set(
        self,
    ) -> typing.Optional["RowLevelPermissionDataSet"]:
        '''The row-level security configuration for the data that you want to create.'''
        result = self._values.get("row_level_permission_data_set")
        return typing.cast(typing.Optional["RowLevelPermissionDataSet"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateDataSetRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateDataSetResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "data_set_id": "dataSetId",
        "ingestion_arn": "ingestionArn",
        "ingestion_id": "ingestionId",
        "request_id": "requestId",
        "status": "status",
    },
)
class CreateDataSetResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        data_set_id: typing.Optional[builtins.str] = None,
        ingestion_arn: typing.Optional[builtins.str] = None,
        ingestion_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the dataset.
        :param data_set_id: The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.
        :param ingestion_arn: The ARN for the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.
        :param ingestion_id: The ID of the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if data_set_id is not None:
            self._values["data_set_id"] = data_set_id
        if ingestion_arn is not None:
            self._values["ingestion_arn"] = ingestion_arn
        if ingestion_id is not None:
            self._values["ingestion_id"] = ingestion_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the dataset.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_set_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the dataset that you want to create.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingestion_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.'''
        result = self._values.get("ingestion_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingestion_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.'''
        result = self._values.get("ingestion_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateDataSetResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateDataSourceRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_source_id": "dataSourceId",
        "name": "name",
        "type": "type",
        "credentials": "credentials",
        "data_source_parameters": "dataSourceParameters",
        "permissions": "permissions",
        "ssl_properties": "sslProperties",
        "tags": "tags",
        "vpc_connection_properties": "vpcConnectionProperties",
    },
)
class CreateDataSourceRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_source_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        credentials: typing.Optional["DataSourceCredentials"] = None,
        data_source_parameters: typing.Optional["DataSourceParameters"] = None,
        permissions: typing.Optional[typing.Sequence["ResourcePermission"]] = None,
        ssl_properties: typing.Optional["SslProperties"] = None,
        tags: typing.Optional[typing.Sequence["Tag"]] = None,
        vpc_connection_properties: typing.Optional["VpcConnectionProperties"] = None,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_source_id: An ID for the data source. This ID is unique per AWS Region for each AWS account.
        :param name: A display name for the data source.
        :param type: The type of the data source. Currently, the supported types for this operation are: ATHENA, AURORA, AURORA_POSTGRESQL, AMAZON_ELASTICSEARCH, MARIADB, MYSQL, POSTGRESQL, PRESTO, REDSHIFT, S3, SNOWFLAKE, SPARK, SQLSERVER, TERADATA. Use ListDataSources to return a list of all data sources. AMAZON_ELASTICSEARCH is for Amazon managed Elasticsearch Service.
        :param credentials: The credentials QuickSight that uses to connect to your underlying source. Currently, only credentials based on user name and password are supported.
        :param data_source_parameters: The parameters that QuickSight uses to connect to your underlying source.
        :param permissions: A list of resource permissions on the data source.
        :param ssl_properties: Secure Socket Layer (SSL) properties that apply when QuickSight connects to your underlying source.
        :param tags: Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.
        :param vpc_connection_properties: Use this parameter only when you want QuickSight to use a VPC connection when connecting to your underlying source.
        '''
        if isinstance(credentials, dict):
            credentials = DataSourceCredentials(**credentials)
        if isinstance(data_source_parameters, dict):
            data_source_parameters = DataSourceParameters(**data_source_parameters)
        if isinstance(ssl_properties, dict):
            ssl_properties = SslProperties(**ssl_properties)
        if isinstance(vpc_connection_properties, dict):
            vpc_connection_properties = VpcConnectionProperties(**vpc_connection_properties)
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_source_id": data_source_id,
            "name": name,
            "type": type,
        }
        if credentials is not None:
            self._values["credentials"] = credentials
        if data_source_parameters is not None:
            self._values["data_source_parameters"] = data_source_parameters
        if permissions is not None:
            self._values["permissions"] = permissions
        if ssl_properties is not None:
            self._values["ssl_properties"] = ssl_properties
        if tags is not None:
            self._values["tags"] = tags
        if vpc_connection_properties is not None:
            self._values["vpc_connection_properties"] = vpc_connection_properties

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''An ID for the data source.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A display name for the data source.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the data source.

        Currently, the supported types for this operation are: ATHENA, AURORA, AURORA_POSTGRESQL, AMAZON_ELASTICSEARCH, MARIADB, MYSQL, POSTGRESQL, PRESTO, REDSHIFT, S3, SNOWFLAKE, SPARK, SQLSERVER, TERADATA. Use ListDataSources to return a list of all data sources.  AMAZON_ELASTICSEARCH is for Amazon managed Elasticsearch Service.
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credentials(self) -> typing.Optional["DataSourceCredentials"]:
        '''The credentials QuickSight that uses to connect to your underlying source.

        Currently, only credentials based on user name and password are supported.
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional["DataSourceCredentials"], result)

    @builtins.property
    def data_source_parameters(self) -> typing.Optional["DataSourceParameters"]:
        '''The parameters that QuickSight uses to connect to your underlying source.'''
        result = self._values.get("data_source_parameters")
        return typing.cast(typing.Optional["DataSourceParameters"], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List["ResourcePermission"]]:
        '''A list of resource permissions on the data source.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List["ResourcePermission"]], result)

    @builtins.property
    def ssl_properties(self) -> typing.Optional["SslProperties"]:
        '''Secure Socket Layer (SSL) properties that apply when QuickSight connects to your underlying source.'''
        result = self._values.get("ssl_properties")
        return typing.cast(typing.Optional["SslProperties"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    @builtins.property
    def vpc_connection_properties(self) -> typing.Optional["VpcConnectionProperties"]:
        '''Use this parameter only when you want QuickSight to use a VPC connection when connecting to your underlying source.'''
        result = self._values.get("vpc_connection_properties")
        return typing.cast(typing.Optional["VpcConnectionProperties"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateDataSourceRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateDataSourceResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "creation_status": "creationStatus",
        "data_source_id": "dataSourceId",
        "request_id": "requestId",
        "status": "status",
    },
)
class CreateDataSourceResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        creation_status: typing.Optional[builtins.str] = None,
        data_source_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the data source.
        :param creation_status: The status of creating the data source.
        :param data_source_id: The ID of the data source. This ID is unique per AWS Region for each AWS account.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if creation_status is not None:
            self._values["creation_status"] = creation_status
        if data_source_id is not None:
            self._values["data_source_id"] = data_source_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the data source.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_status(self) -> typing.Optional[builtins.str]:
        '''The status of creating the data source.'''
        result = self._values.get("creation_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_source_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the data source.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_source_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateDataSourceResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateGroupMembershipRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "group_name": "groupName",
        "member_name": "memberName",
        "namespace": "namespace",
    },
)
class CreateGroupMembershipRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        group_name: builtins.str,
        member_name: builtins.str,
        namespace: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param group_name: The name of the group that you want to add the user to.
        :param member_name: The name of the user that you want to add to the group membership.
        :param namespace: The namespace. Currently, you should set this to default.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "group_name": group_name,
            "member_name": member_name,
            "namespace": namespace,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the group is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The name of the group that you want to add the user to.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_name(self) -> builtins.str:
        '''The name of the user that you want to add to the group membership.'''
        result = self._values.get("member_name")
        assert result is not None, "Required property 'member_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateGroupMembershipRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateGroupMembershipResponse",
    jsii_struct_bases=[],
    name_mapping={
        "group_member": "groupMember",
        "request_id": "requestId",
        "status": "status",
    },
)
class CreateGroupMembershipResponse:
    def __init__(
        self,
        *,
        group_member: typing.Optional["GroupMember"] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group_member: The group member.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(group_member, dict):
            group_member = GroupMember(**group_member)
        self._values: typing.Dict[str, typing.Any] = {}
        if group_member is not None:
            self._values["group_member"] = group_member
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def group_member(self) -> typing.Optional["GroupMember"]:
        '''The group member.'''
        result = self._values.get("group_member")
        return typing.cast(typing.Optional["GroupMember"], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateGroupMembershipResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateGroupRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "group_name": "groupName",
        "namespace": "namespace",
        "description": "description",
    },
)
class CreateGroupRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        group_name: builtins.str,
        namespace: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param group_name: A name for the group that you want to create.
        :param namespace: The namespace. Currently, you should set this to default.
        :param description: A description for the group that you want to create.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "group_name": group_name,
            "namespace": namespace,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the group is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> builtins.str:
        '''A name for the group that you want to create.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the group that you want to create.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateGroupRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateGroupResponse",
    jsii_struct_bases=[],
    name_mapping={"group": "group", "request_id": "requestId", "status": "status"},
)
class CreateGroupResponse:
    def __init__(
        self,
        *,
        group: typing.Optional["Group"] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group: The name of the group.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(group, dict):
            group = Group(**group)
        self._values: typing.Dict[str, typing.Any] = {}
        if group is not None:
            self._values["group"] = group
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def group(self) -> typing.Optional["Group"]:
        '''The name of the group.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional["Group"], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateGroupResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateIAMPolicyAssignmentRequest",
    jsii_struct_bases=[],
    name_mapping={
        "assignment_name": "assignmentName",
        "assignment_status": "assignmentStatus",
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "identities": "identities",
        "policy_arn": "policyArn",
    },
)
class CreateIAMPolicyAssignmentRequest:
    def __init__(
        self,
        *,
        assignment_name: builtins.str,
        assignment_status: builtins.str,
        aws_account_id: builtins.str,
        namespace: builtins.str,
        identities: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[builtins.str]]] = None,
        policy_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param assignment_name: The name of the assignment, also called a rule. It must be unique within an AWS account.
        :param assignment_status: The status of the assignment. Possible values are as follows: ENABLED - Anything specified in this assignment is used when creating the data source. DISABLED - This assignment isn't used when creating the data source. DRAFT - This assignment is an unfinished draft and isn't used when creating the data source.
        :param aws_account_id: The ID of the AWS account where you want to assign an IAM policy to QuickSight users or groups.
        :param namespace: The namespace that contains the assignment.
        :param identities: The QuickSight users, groups, or both that you want to assign the policy to.
        :param policy_arn: The ARN for the IAM policy to apply to the QuickSight users and groups specified in this assignment.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "assignment_name": assignment_name,
            "assignment_status": assignment_status,
            "aws_account_id": aws_account_id,
            "namespace": namespace,
        }
        if identities is not None:
            self._values["identities"] = identities
        if policy_arn is not None:
            self._values["policy_arn"] = policy_arn

    @builtins.property
    def assignment_name(self) -> builtins.str:
        '''The name of the assignment, also called a rule.

        It must be unique within an AWS account.
        '''
        result = self._values.get("assignment_name")
        assert result is not None, "Required property 'assignment_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assignment_status(self) -> builtins.str:
        '''The status of the assignment.

        Possible values are as follows:    ENABLED - Anything specified in this assignment is used when creating the data source.    DISABLED - This assignment isn't used when creating the data source.    DRAFT - This assignment is an unfinished draft and isn't used when creating the data source.
        '''
        result = self._values.get("assignment_status")
        assert result is not None, "Required property 'assignment_status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account where you want to assign an IAM policy to QuickSight users or groups.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace that contains the assignment.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identities(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]]:
        '''The QuickSight users, groups, or both that you want to assign the policy to.'''
        result = self._values.get("identities")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]], result)

    @builtins.property
    def policy_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the IAM policy to apply to the QuickSight users and groups specified in this assignment.'''
        result = self._values.get("policy_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateIAMPolicyAssignmentRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateIAMPolicyAssignmentResponse",
    jsii_struct_bases=[],
    name_mapping={
        "assignment_id": "assignmentId",
        "assignment_name": "assignmentName",
        "assignment_status": "assignmentStatus",
        "identities": "identities",
        "policy_arn": "policyArn",
        "request_id": "requestId",
        "status": "status",
    },
)
class CreateIAMPolicyAssignmentResponse:
    def __init__(
        self,
        *,
        assignment_id: typing.Optional[builtins.str] = None,
        assignment_name: typing.Optional[builtins.str] = None,
        assignment_status: typing.Optional[builtins.str] = None,
        identities: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[builtins.str]]] = None,
        policy_arn: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param assignment_id: The ID for the assignment.
        :param assignment_name: The name of the assignment. This name must be unique within the AWS account.
        :param assignment_status: The status of the assignment. Possible values are as follows: ENABLED - Anything specified in this assignment is used when creating the data source. DISABLED - This assignment isn't used when creating the data source. DRAFT - This assignment is an unfinished draft and isn't used when creating the data source.
        :param identities: The QuickSight users, groups, or both that the IAM policy is assigned to.
        :param policy_arn: The ARN for the IAM policy that is applied to the QuickSight users and groups specified in this assignment.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if assignment_id is not None:
            self._values["assignment_id"] = assignment_id
        if assignment_name is not None:
            self._values["assignment_name"] = assignment_name
        if assignment_status is not None:
            self._values["assignment_status"] = assignment_status
        if identities is not None:
            self._values["identities"] = identities
        if policy_arn is not None:
            self._values["policy_arn"] = policy_arn
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def assignment_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the assignment.'''
        result = self._values.get("assignment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assignment_name(self) -> typing.Optional[builtins.str]:
        '''The name of the assignment.

        This name must be unique within the AWS account.
        '''
        result = self._values.get("assignment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assignment_status(self) -> typing.Optional[builtins.str]:
        '''The status of the assignment.

        Possible values are as follows:    ENABLED - Anything specified in this assignment is used when creating the data source.    DISABLED - This assignment isn't used when creating the data source.    DRAFT - This assignment is an unfinished draft and isn't used when creating the data source.
        '''
        result = self._values.get("assignment_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identities(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]]:
        '''The QuickSight users, groups, or both that the IAM policy is assigned to.'''
        result = self._values.get("identities")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]], result)

    @builtins.property
    def policy_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the IAM policy that is applied to the QuickSight users and groups specified in this assignment.'''
        result = self._values.get("policy_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateIAMPolicyAssignmentResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateIngestionRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_set_id": "dataSetId",
        "ingestion_id": "ingestionId",
    },
)
class CreateIngestionRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_id: builtins.str,
        ingestion_id: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_set_id: The ID of the dataset used in the ingestion.
        :param ingestion_id: An ID for the ingestion.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_id": data_set_id,
            "ingestion_id": ingestion_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The ID of the dataset used in the ingestion.'''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ingestion_id(self) -> builtins.str:
        '''An ID for the ingestion.'''
        result = self._values.get("ingestion_id")
        assert result is not None, "Required property 'ingestion_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateIngestionRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateIngestionResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "ingestion_id": "ingestionId",
        "ingestion_status": "ingestionStatus",
        "request_id": "requestId",
        "status": "status",
    },
)
class CreateIngestionResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        ingestion_id: typing.Optional[builtins.str] = None,
        ingestion_status: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) for the data ingestion.
        :param ingestion_id: An ID for the ingestion.
        :param ingestion_status: The ingestion status.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if ingestion_id is not None:
            self._values["ingestion_id"] = ingestion_id
        if ingestion_status is not None:
            self._values["ingestion_status"] = ingestion_status
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the data ingestion.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingestion_id(self) -> typing.Optional[builtins.str]:
        '''An ID for the ingestion.'''
        result = self._values.get("ingestion_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingestion_status(self) -> typing.Optional[builtins.str]:
        '''The ingestion status.'''
        result = self._values.get("ingestion_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateIngestionResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateNamespaceRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "identity_store": "identityStore",
        "namespace": "namespace",
        "tags": "tags",
    },
)
class CreateNamespaceRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        identity_store: builtins.str,
        namespace: builtins.str,
        tags: typing.Optional[typing.Sequence["Tag"]] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that you want to create the QuickSight namespace in.
        :param identity_store: Specifies the type of your user identity directory. Currently, this supports users with an identity type of QUICKSIGHT.
        :param namespace: The name that you want to use to describe the new namespace.
        :param tags: The tags that you want to associate with the namespace that you're creating.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "identity_store": identity_store,
            "namespace": namespace,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that you want to create the QuickSight namespace in.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_store(self) -> builtins.str:
        '''Specifies the type of your user identity directory.

        Currently, this supports users with an identity type of QUICKSIGHT.
        '''
        result = self._values.get("identity_store")
        assert result is not None, "Required property 'identity_store' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The name that you want to use to describe the new namespace.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''The tags that you want to associate with the namespace that you're creating.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateNamespaceRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateNamespaceResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "capacity_region": "capacityRegion",
        "creation_status": "creationStatus",
        "identity_store": "identityStore",
        "name": "name",
        "request_id": "requestId",
        "status": "status",
    },
)
class CreateNamespaceResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        capacity_region: typing.Optional[builtins.str] = None,
        creation_status: typing.Optional[builtins.str] = None,
        identity_store: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The ARN of the QuickSight namespace you created.
        :param capacity_region: The AWS Region that you want to use for the free SPICE capacity for the new namespace. This is set to the region that you run CreateNamespace in.
        :param creation_status: The status of the creation of the namespace. This is an asynchronous process. A status of CREATED means that your namespace is ready to use. If an error occurs, it indicates if the process is retryable or non-retryable. In the case of a non-retryable error, refer to the error message for follow-up tasks.
        :param identity_store: Specifies the type of your user identity directory. Currently, this supports users with an identity type of QUICKSIGHT.
        :param name: The name of the new namespace that you created.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if capacity_region is not None:
            self._values["capacity_region"] = capacity_region
        if creation_status is not None:
            self._values["creation_status"] = creation_status
        if identity_store is not None:
            self._values["identity_store"] = identity_store
        if name is not None:
            self._values["name"] = name
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the QuickSight namespace you created.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_region(self) -> typing.Optional[builtins.str]:
        '''The AWS Region that you want to use for the free SPICE capacity for the new namespace.

        This is set to the region that you run CreateNamespace in.
        '''
        result = self._values.get("capacity_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_status(self) -> typing.Optional[builtins.str]:
        '''The status of the creation of the namespace.

        This is an asynchronous process. A status of CREATED means that your namespace is ready to use. If an error occurs, it indicates if the process is retryable or non-retryable. In the case of a non-retryable error, refer to the error message for follow-up tasks.
        '''
        result = self._values.get("creation_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_store(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of your user identity directory.

        Currently, this supports users with an identity type of QUICKSIGHT.
        '''
        result = self._values.get("identity_store")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new namespace that you created.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateNamespaceResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateTemplateAliasRequest",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "aws_account_id": "awsAccountId",
        "template_id": "templateId",
        "template_version_number": "templateVersionNumber",
    },
)
class CreateTemplateAliasRequest:
    def __init__(
        self,
        *,
        alias_name: builtins.str,
        aws_account_id: builtins.str,
        template_id: builtins.str,
        template_version_number: jsii.Number,
    ) -> None:
        '''
        :param alias_name: The name that you want to give to the template alias that you're creating. Don't start the alias name with the $ character. Alias names that start with $ are reserved by QuickSight.
        :param aws_account_id: The ID of the AWS account that contains the template that you creating an alias for.
        :param template_id: An ID for the template.
        :param template_version_number: The version number of the template.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alias_name": alias_name,
            "aws_account_id": aws_account_id,
            "template_id": template_id,
            "template_version_number": template_version_number,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''The name that you want to give to the template alias that you're creating.

        Don't start the alias name with the $ character. Alias names that start with $ are reserved by QuickSight.
        '''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the template that you creating an alias for.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''An ID for the template.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_version_number(self) -> jsii.Number:
        '''The version number of the template.'''
        result = self._values.get("template_version_number")
        assert result is not None, "Required property 'template_version_number' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateTemplateAliasRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateTemplateAliasResponse",
    jsii_struct_bases=[],
    name_mapping={
        "request_id": "requestId",
        "status": "status",
        "template_alias": "templateAlias",
    },
)
class CreateTemplateAliasResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template_alias: typing.Optional["TemplateAlias"] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template_alias: Information about the template alias.
        '''
        if isinstance(template_alias, dict):
            template_alias = TemplateAlias(**template_alias)
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template_alias is not None:
            self._values["template_alias"] = template_alias

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template_alias(self) -> typing.Optional["TemplateAlias"]:
        '''Information about the template alias.'''
        result = self._values.get("template_alias")
        return typing.cast(typing.Optional["TemplateAlias"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateTemplateAliasResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateTemplateRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "source_entity": "sourceEntity",
        "template_id": "templateId",
        "name": "name",
        "permissions": "permissions",
        "tags": "tags",
        "version_description": "versionDescription",
    },
)
class CreateTemplateRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        source_entity: "TemplateSourceEntity",
        template_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Sequence["ResourcePermission"]] = None,
        tags: typing.Optional[typing.Sequence["Tag"]] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param source_entity: The entity that you are using as a source when you create the template. In SourceEntity, you specify the type of object you're using as source: SourceTemplate for a template or SourceAnalysis for an analysis. Both of these require an Amazon Resource Name (ARN). For SourceTemplate, specify the ARN of the source template. For SourceAnalysis, specify the ARN of the source analysis. The SourceTemplate ARN can contain any AWS Account and any QuickSight-supported AWS Region. Use the DataSetReferences entity within SourceTemplate or SourceAnalysis to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder.
        :param template_id: An ID for the template that you want to create. This template is unique per AWS Region in each AWS account.
        :param name: A display name for the template.
        :param permissions: A list of resource permissions to be set on the template.
        :param tags: Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.
        :param version_description: A description of the current template version being created. This API operation creates the first version of the template. Every time UpdateTemplate is called, a new version is created. Each version of the template maintains a description of the version in the VersionDescription field.
        '''
        if isinstance(source_entity, dict):
            source_entity = TemplateSourceEntity(**source_entity)
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "source_entity": source_entity,
            "template_id": template_id,
        }
        if name is not None:
            self._values["name"] = name
        if permissions is not None:
            self._values["permissions"] = permissions
        if tags is not None:
            self._values["tags"] = tags
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the group is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_entity(self) -> "TemplateSourceEntity":
        '''The entity that you are using as a source when you create the template.

        In SourceEntity, you specify the type of object you're using as source: SourceTemplate for a template or SourceAnalysis for an analysis. Both of these require an Amazon Resource Name (ARN). For SourceTemplate, specify the ARN of the source template. For SourceAnalysis, specify the ARN of the source analysis. The SourceTemplate ARN can contain any AWS Account and any QuickSight-supported AWS Region.  Use the DataSetReferences entity within SourceTemplate or SourceAnalysis to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder.
        '''
        result = self._values.get("source_entity")
        assert result is not None, "Required property 'source_entity' is missing"
        return typing.cast("TemplateSourceEntity", result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''An ID for the template that you want to create.

        This template is unique per AWS Region in each AWS account.
        '''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A display name for the template.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List["ResourcePermission"]]:
        '''A list of resource permissions to be set on the template.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List["ResourcePermission"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''A description of the current template version being created.

        This API operation creates the first version of the template. Every time UpdateTemplate is called, a new version is created. Each version of the template maintains a description of the version in the VersionDescription field.
        '''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateTemplateRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateTemplateResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "creation_status": "creationStatus",
        "request_id": "requestId",
        "status": "status",
        "template_id": "templateId",
        "version_arn": "versionArn",
    },
)
class CreateTemplateResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        creation_status: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template_id: typing.Optional[builtins.str] = None,
        version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The ARN for the template.
        :param creation_status: The template creation status.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template_id: The ID of the template.
        :param version_arn: The ARN for the template, including the version information of the first version.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if creation_status is not None:
            self._values["creation_status"] = creation_status
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template_id is not None:
            self._values["template_id"] = template_id
        if version_arn is not None:
            self._values["version_arn"] = version_arn

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the template.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_status(self) -> typing.Optional[builtins.str]:
        '''The template creation status.'''
        result = self._values.get("creation_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the template.'''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the template, including the version information of the first version.'''
        result = self._values.get("version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateTemplateResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateThemeAliasRequest",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "aws_account_id": "awsAccountId",
        "theme_id": "themeId",
        "theme_version_number": "themeVersionNumber",
    },
)
class CreateThemeAliasRequest:
    def __init__(
        self,
        *,
        alias_name: builtins.str,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
        theme_version_number: jsii.Number,
    ) -> None:
        '''
        :param alias_name: The name that you want to give to the theme alias that you are creating. The alias name can't begin with a $. Alias names that start with $ are reserved by Amazon QuickSight.
        :param aws_account_id: The ID of the AWS account that contains the theme for the new theme alias.
        :param theme_id: An ID for the theme alias.
        :param theme_version_number: The version number of the theme.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alias_name": alias_name,
            "aws_account_id": aws_account_id,
            "theme_id": theme_id,
            "theme_version_number": theme_version_number,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''The name that you want to give to the theme alias that you are creating.

        The alias name can't begin with a $. Alias names that start with $ are reserved by Amazon QuickSight.
        '''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the theme for the new theme alias.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''An ID for the theme alias.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_version_number(self) -> jsii.Number:
        '''The version number of the theme.'''
        result = self._values.get("theme_version_number")
        assert result is not None, "Required property 'theme_version_number' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateThemeAliasRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateThemeAliasResponse",
    jsii_struct_bases=[],
    name_mapping={
        "request_id": "requestId",
        "status": "status",
        "theme_alias": "themeAlias",
    },
)
class CreateThemeAliasResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme_alias: typing.Optional["ThemeAlias"] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme_alias: Information about the theme alias.
        '''
        if isinstance(theme_alias, dict):
            theme_alias = ThemeAlias(**theme_alias)
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme_alias is not None:
            self._values["theme_alias"] = theme_alias

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme_alias(self) -> typing.Optional["ThemeAlias"]:
        '''Information about the theme alias.'''
        result = self._values.get("theme_alias")
        return typing.cast(typing.Optional["ThemeAlias"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateThemeAliasResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateThemeRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "base_theme_id": "baseThemeId",
        "configuration": "configuration",
        "name": "name",
        "theme_id": "themeId",
        "permissions": "permissions",
        "tags": "tags",
        "version_description": "versionDescription",
    },
)
class CreateThemeRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        base_theme_id: builtins.str,
        configuration: "ThemeConfiguration",
        name: builtins.str,
        theme_id: builtins.str,
        permissions: typing.Optional[typing.Sequence["ResourcePermission"]] = None,
        tags: typing.Optional[typing.Sequence["Tag"]] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account where you want to store the new theme.
        :param base_theme_id: The ID of the theme that a custom theme will inherit from. All themes inherit from one of the starting themes defined by Amazon QuickSight. For a list of the starting themes, use ListThemes or choose Themes from within a QuickSight analysis.
        :param configuration: The theme configuration, which contains the theme display properties.
        :param name: A display name for the theme.
        :param theme_id: An ID for the theme that you want to create. The theme ID is unique per AWS Region in each AWS account.
        :param permissions: A valid grouping of resource permissions to apply to the new theme.
        :param tags: A map of the key-value pairs for the resource tag or tags that you want to add to the resource.
        :param version_description: A description of the first version of the theme that you're creating. Every time UpdateTheme is called, a new version is created. Each version of the theme has a description of the version in the VersionDescription field.
        '''
        if isinstance(configuration, dict):
            configuration = ThemeConfiguration(**configuration)
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "base_theme_id": base_theme_id,
            "configuration": configuration,
            "name": name,
            "theme_id": theme_id,
        }
        if permissions is not None:
            self._values["permissions"] = permissions
        if tags is not None:
            self._values["tags"] = tags
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account where you want to store the new theme.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_theme_id(self) -> builtins.str:
        '''The ID of the theme that a custom theme will inherit from.

        All themes inherit from one of the starting themes defined by Amazon QuickSight. For a list of the starting themes, use ListThemes or choose Themes from within a QuickSight analysis.
        '''
        result = self._values.get("base_theme_id")
        assert result is not None, "Required property 'base_theme_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(self) -> "ThemeConfiguration":
        '''The theme configuration, which contains the theme display properties.'''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast("ThemeConfiguration", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A display name for the theme.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''An ID for the theme that you want to create.

        The theme ID is unique per AWS Region in each AWS account.
        '''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List["ResourcePermission"]]:
        '''A valid grouping of resource permissions to apply to the new theme.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List["ResourcePermission"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''A map of the key-value pairs for the resource tag or tags that you want to add to the resource.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''A description of the first version of the theme that you're creating.

        Every time UpdateTheme is called, a new version is created. Each version of the theme has a description of the version in the VersionDescription field.
        '''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateThemeRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CreateThemeResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "creation_status": "creationStatus",
        "request_id": "requestId",
        "status": "status",
        "theme_id": "themeId",
        "version_arn": "versionArn",
    },
)
class CreateThemeResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        creation_status: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme_id: typing.Optional[builtins.str] = None,
        version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) for the theme.
        :param creation_status: The theme creation status.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme_id: The ID of the theme.
        :param version_arn: The Amazon Resource Name (ARN) for the new theme.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if creation_status is not None:
            self._values["creation_status"] = creation_status
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme_id is not None:
            self._values["theme_id"] = theme_id
        if version_arn is not None:
            self._values["version_arn"] = version_arn

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the theme.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_status(self) -> typing.Optional[builtins.str]:
        '''The theme creation status.'''
        result = self._values.get("creation_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the theme.'''
        result = self._values.get("theme_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the new theme.'''
        result = self._values.get("version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateThemeResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CredentialPair",
    jsii_struct_bases=[],
    name_mapping={
        "password": "password",
        "username": "username",
        "alternate_data_source_parameters": "alternateDataSourceParameters",
    },
)
class CredentialPair:
    def __init__(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
        alternate_data_source_parameters: typing.Optional[typing.Sequence["DataSourceParameters"]] = None,
    ) -> None:
        '''
        :param password: Password.
        :param username: User name.
        :param alternate_data_source_parameters: A set of alternate data source parameters that you want to share for these credentials. The credentials are applied in tandem with the data source parameters when you copy a data source by using a create or update request. The API operation compares the DataSourceParameters structure that's in the request with the structures in the AlternateDataSourceParameters allow list. If the structures are an exact match, the request is allowed to use the new data source with the existing credentials. If the AlternateDataSourceParameters list is null, the DataSourceParameters originally used with these Credentials is automatically allowed.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }
        if alternate_data_source_parameters is not None:
            self._values["alternate_data_source_parameters"] = alternate_data_source_parameters

    @builtins.property
    def password(self) -> builtins.str:
        '''Password.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''User name.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alternate_data_source_parameters(
        self,
    ) -> typing.Optional[typing.List["DataSourceParameters"]]:
        '''A set of alternate data source parameters that you want to share for these credentials.

        The credentials are applied in tandem with the data source parameters when you copy a data source by using a create or update request. The API operation compares the DataSourceParameters structure that's in the request with the structures in the AlternateDataSourceParameters allow list. If the structures are an exact match, the request is allowed to use the new data source with the existing credentials. If the AlternateDataSourceParameters list is null, the DataSourceParameters originally used with these Credentials is automatically allowed.
        '''
        result = self._values.get("alternate_data_source_parameters")
        return typing.cast(typing.Optional[typing.List["DataSourceParameters"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialPair(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.CustomSql",
    jsii_struct_bases=[],
    name_mapping={
        "data_source_arn": "dataSourceArn",
        "name": "name",
        "sql_query": "sqlQuery",
        "columns": "columns",
    },
)
class CustomSql:
    def __init__(
        self,
        *,
        data_source_arn: builtins.str,
        name: builtins.str,
        sql_query: builtins.str,
        columns: typing.Optional[typing.Sequence["InputColumn"]] = None,
    ) -> None:
        '''
        :param data_source_arn: The Amazon Resource Name (ARN) of the data source.
        :param name: A display name for the SQL query result.
        :param sql_query: The SQL query.
        :param columns: The column schema from the SQL query result set.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "data_source_arn": data_source_arn,
            "name": name,
            "sql_query": sql_query,
        }
        if columns is not None:
            self._values["columns"] = columns

    @builtins.property
    def data_source_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the data source.'''
        result = self._values.get("data_source_arn")
        assert result is not None, "Required property 'data_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A display name for the SQL query result.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_query(self) -> builtins.str:
        '''The SQL query.'''
        result = self._values.get("sql_query")
        assert result is not None, "Required property 'sql_query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def columns(self) -> typing.Optional[typing.List["InputColumn"]]:
        '''The column schema from the SQL query result set.'''
        result = self._values.get("columns")
        return typing.cast(typing.Optional[typing.List["InputColumn"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomSql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.Dashboard",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "created_time": "createdTime",
        "dashboard_id": "dashboardId",
        "last_published_time": "lastPublishedTime",
        "last_updated_time": "lastUpdatedTime",
        "name": "name",
        "version": "version",
    },
)
class Dashboard:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        dashboard_id: typing.Optional[builtins.str] = None,
        last_published_time: typing.Optional[datetime.datetime] = None,
        last_updated_time: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[builtins.str] = None,
        version: typing.Optional["DashboardVersion"] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param created_time: The time that this dataset was created.
        :param dashboard_id: Dashboard ID.
        :param last_published_time: The last time that this dataset was published.
        :param last_updated_time: The last time that this dataset was updated.
        :param name: A display name for the dashboard.
        :param version: Version.
        '''
        if isinstance(version, dict):
            version = DashboardVersion(**version)
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if dashboard_id is not None:
            self._values["dashboard_id"] = dashboard_id
        if last_published_time is not None:
            self._values["last_published_time"] = last_published_time
        if last_updated_time is not None:
            self._values["last_updated_time"] = last_updated_time
        if name is not None:
            self._values["name"] = name
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that this dataset was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def dashboard_id(self) -> typing.Optional[builtins.str]:
        '''Dashboard ID.'''
        result = self._values.get("dashboard_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_published_time(self) -> typing.Optional[datetime.datetime]:
        '''The last time that this dataset was published.'''
        result = self._values.get("last_published_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def last_updated_time(self) -> typing.Optional[datetime.datetime]:
        '''The last time that this dataset was updated.'''
        result = self._values.get("last_updated_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A display name for the dashboard.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional["DashboardVersion"]:
        '''Version.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional["DashboardVersion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Dashboard(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DashboardError",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "type": "type"},
)
class DashboardError:
    def __init__(
        self,
        *,
        message: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: Message.
        :param type: Type.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Message.'''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardError(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DashboardPublishOptions",
    jsii_struct_bases=[],
    name_mapping={
        "ad_hoc_filtering_option": "adHocFilteringOption",
        "export_to_csv_option": "exportToCSVOption",
        "sheet_controls_option": "sheetControlsOption",
    },
)
class DashboardPublishOptions:
    def __init__(
        self,
        *,
        ad_hoc_filtering_option: typing.Optional[AdHocFilteringOption] = None,
        export_to_csv_option: typing.Optional["ExportToCSVOption"] = None,
        sheet_controls_option: typing.Optional["SheetControlsOption"] = None,
    ) -> None:
        '''
        :param ad_hoc_filtering_option: Ad hoc (one-time) filtering option.
        :param export_to_csv_option: Export to .csv option.
        :param sheet_controls_option: Sheet controls option.
        '''
        if isinstance(ad_hoc_filtering_option, dict):
            ad_hoc_filtering_option = AdHocFilteringOption(**ad_hoc_filtering_option)
        if isinstance(export_to_csv_option, dict):
            export_to_csv_option = ExportToCSVOption(**export_to_csv_option)
        if isinstance(sheet_controls_option, dict):
            sheet_controls_option = SheetControlsOption(**sheet_controls_option)
        self._values: typing.Dict[str, typing.Any] = {}
        if ad_hoc_filtering_option is not None:
            self._values["ad_hoc_filtering_option"] = ad_hoc_filtering_option
        if export_to_csv_option is not None:
            self._values["export_to_csv_option"] = export_to_csv_option
        if sheet_controls_option is not None:
            self._values["sheet_controls_option"] = sheet_controls_option

    @builtins.property
    def ad_hoc_filtering_option(self) -> typing.Optional[AdHocFilteringOption]:
        '''Ad hoc (one-time) filtering option.'''
        result = self._values.get("ad_hoc_filtering_option")
        return typing.cast(typing.Optional[AdHocFilteringOption], result)

    @builtins.property
    def export_to_csv_option(self) -> typing.Optional["ExportToCSVOption"]:
        '''Export to .csv option.'''
        result = self._values.get("export_to_csv_option")
        return typing.cast(typing.Optional["ExportToCSVOption"], result)

    @builtins.property
    def sheet_controls_option(self) -> typing.Optional["SheetControlsOption"]:
        '''Sheet controls option.'''
        result = self._values.get("sheet_controls_option")
        return typing.cast(typing.Optional["SheetControlsOption"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardPublishOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DashboardSearchFilter",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "name": "name", "value": "value"},
)
class DashboardSearchFilter:
    def __init__(
        self,
        *,
        operator: builtins.str,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param operator: The comparison operator that you want to use as a filter, for example, "Operator": "StringEquals".
        :param name: The name of the value that you want to use as a filter, for example, "Name": "QUICKSIGHT_USER".
        :param value: The value of the named item, in this case QUICKSIGHT_USER, that you want to use as a filter, for example, "Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1".
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def operator(self) -> builtins.str:
        '''The comparison operator that you want to use as a filter, for example, "Operator": "StringEquals".'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the value that you want to use as a filter, for example, "Name": "QUICKSIGHT_USER".'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value of the named item, in this case QUICKSIGHT_USER, that you want to use as a filter, for example, "Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1".'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardSearchFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DashboardSourceEntity",
    jsii_struct_bases=[],
    name_mapping={"source_template": "sourceTemplate"},
)
class DashboardSourceEntity:
    def __init__(
        self,
        *,
        source_template: typing.Optional["DashboardSourceTemplate"] = None,
    ) -> None:
        '''
        :param source_template: Source template.
        '''
        if isinstance(source_template, dict):
            source_template = DashboardSourceTemplate(**source_template)
        self._values: typing.Dict[str, typing.Any] = {}
        if source_template is not None:
            self._values["source_template"] = source_template

    @builtins.property
    def source_template(self) -> typing.Optional["DashboardSourceTemplate"]:
        '''Source template.'''
        result = self._values.get("source_template")
        return typing.cast(typing.Optional["DashboardSourceTemplate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardSourceEntity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DashboardSourceTemplate",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "data_set_references": "dataSetReferences"},
)
class DashboardSourceTemplate:
    def __init__(
        self,
        *,
        arn: builtins.str,
        data_set_references: typing.Sequence["DataSetReference"],
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param data_set_references: Dataset references.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
            "data_set_references": data_set_references,
        }

    @builtins.property
    def arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_references(self) -> typing.List["DataSetReference"]:
        '''Dataset references.'''
        result = self._values.get("data_set_references")
        assert result is not None, "Required property 'data_set_references' is missing"
        return typing.cast(typing.List["DataSetReference"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardSourceTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DashboardSummary",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "created_time": "createdTime",
        "dashboard_id": "dashboardId",
        "last_published_time": "lastPublishedTime",
        "last_updated_time": "lastUpdatedTime",
        "name": "name",
        "published_version_number": "publishedVersionNumber",
    },
)
class DashboardSummary:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        dashboard_id: typing.Optional[builtins.str] = None,
        last_published_time: typing.Optional[datetime.datetime] = None,
        last_updated_time: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[builtins.str] = None,
        published_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param created_time: The time that this dashboard was created.
        :param dashboard_id: Dashboard ID.
        :param last_published_time: The last time that this dashboard was published.
        :param last_updated_time: The last time that this dashboard was updated.
        :param name: A display name for the dashboard.
        :param published_version_number: Published version number.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if dashboard_id is not None:
            self._values["dashboard_id"] = dashboard_id
        if last_published_time is not None:
            self._values["last_published_time"] = last_published_time
        if last_updated_time is not None:
            self._values["last_updated_time"] = last_updated_time
        if name is not None:
            self._values["name"] = name
        if published_version_number is not None:
            self._values["published_version_number"] = published_version_number

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that this dashboard was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def dashboard_id(self) -> typing.Optional[builtins.str]:
        '''Dashboard ID.'''
        result = self._values.get("dashboard_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_published_time(self) -> typing.Optional[datetime.datetime]:
        '''The last time that this dashboard was published.'''
        result = self._values.get("last_published_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def last_updated_time(self) -> typing.Optional[datetime.datetime]:
        '''The last time that this dashboard was updated.'''
        result = self._values.get("last_updated_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A display name for the dashboard.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def published_version_number(self) -> typing.Optional[jsii.Number]:
        '''Published version number.'''
        result = self._values.get("published_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardSummary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DashboardVersion",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "created_time": "createdTime",
        "data_set_arns": "dataSetArns",
        "description": "description",
        "errors": "errors",
        "sheets": "sheets",
        "source_entity_arn": "sourceEntityArn",
        "status": "status",
        "theme_arn": "themeArn",
        "version_number": "versionNumber",
    },
)
class DashboardVersion:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        data_set_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        errors: typing.Optional[typing.Sequence[DashboardError]] = None,
        sheets: typing.Optional[typing.Sequence["Sheet"]] = None,
        source_entity_arn: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        theme_arn: typing.Optional[builtins.str] = None,
        version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param created_time: The time that this dashboard version was created.
        :param data_set_arns: The Amazon Resource Numbers (ARNs) for the datasets that are associated with this version of the dashboard.
        :param description: Description.
        :param errors: Errors associated with this dashboard version.
        :param sheets: A list of the associated sheets with the unique identifier and name of each sheet.
        :param source_entity_arn: Source entity ARN.
        :param status: The HTTP status of the request.
        :param theme_arn: The ARN of the theme associated with a version of the dashboard.
        :param version_number: Version number for this version of the dashboard.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if data_set_arns is not None:
            self._values["data_set_arns"] = data_set_arns
        if description is not None:
            self._values["description"] = description
        if errors is not None:
            self._values["errors"] = errors
        if sheets is not None:
            self._values["sheets"] = sheets
        if source_entity_arn is not None:
            self._values["source_entity_arn"] = source_entity_arn
        if status is not None:
            self._values["status"] = status
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that this dashboard version was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def data_set_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Numbers (ARNs) for the datasets that are associated with this version of the dashboard.'''
        result = self._values.get("data_set_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def errors(self) -> typing.Optional[typing.List[DashboardError]]:
        '''Errors associated with this dashboard version.'''
        result = self._values.get("errors")
        return typing.cast(typing.Optional[typing.List[DashboardError]], result)

    @builtins.property
    def sheets(self) -> typing.Optional[typing.List["Sheet"]]:
        '''A list of the associated sheets with the unique identifier and name of each sheet.'''
        result = self._values.get("sheets")
        return typing.cast(typing.Optional[typing.List["Sheet"]], result)

    @builtins.property
    def source_entity_arn(self) -> typing.Optional[builtins.str]:
        '''Source entity ARN.'''
        result = self._values.get("source_entity_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the theme associated with a version of the dashboard.'''
        result = self._values.get("theme_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_number(self) -> typing.Optional[jsii.Number]:
        '''Version number for this version of the dashboard.'''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DashboardVersionSummary",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "created_time": "createdTime",
        "description": "description",
        "source_entity_arn": "sourceEntityArn",
        "status": "status",
        "version_number": "versionNumber",
    },
)
class DashboardVersionSummary:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        description: typing.Optional[builtins.str] = None,
        source_entity_arn: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param created_time: The time that this dashboard version was created.
        :param description: Description.
        :param source_entity_arn: Source entity ARN.
        :param status: The HTTP status of the request.
        :param version_number: Version number.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if description is not None:
            self._values["description"] = description
        if source_entity_arn is not None:
            self._values["source_entity_arn"] = source_entity_arn
        if status is not None:
            self._values["status"] = status
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that this dashboard version was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_entity_arn(self) -> typing.Optional[builtins.str]:
        '''Source entity ARN.'''
        result = self._values.get("source_entity_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_number(self) -> typing.Optional[jsii.Number]:
        '''Version number.'''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardVersionSummary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DataColorPalette",
    jsii_struct_bases=[],
    name_mapping={
        "colors": "colors",
        "empty_fill_color": "emptyFillColor",
        "min_max_gradient": "minMaxGradient",
    },
)
class DataColorPalette:
    def __init__(
        self,
        *,
        colors: typing.Optional[typing.Sequence[builtins.str]] = None,
        empty_fill_color: typing.Optional[builtins.str] = None,
        min_max_gradient: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param colors: The hexadecimal codes for the colors.
        :param empty_fill_color: The hexadecimal code of a color that applies to charts where a lack of data is highlighted.
        :param min_max_gradient: The minimum and maximum hexadecimal codes that describe a color gradient.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if colors is not None:
            self._values["colors"] = colors
        if empty_fill_color is not None:
            self._values["empty_fill_color"] = empty_fill_color
        if min_max_gradient is not None:
            self._values["min_max_gradient"] = min_max_gradient

    @builtins.property
    def colors(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The hexadecimal codes for the colors.'''
        result = self._values.get("colors")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def empty_fill_color(self) -> typing.Optional[builtins.str]:
        '''The hexadecimal code of a color that applies to charts where a lack of data is highlighted.'''
        result = self._values.get("empty_fill_color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_max_gradient(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The minimum and maximum hexadecimal codes that describe a color gradient.'''
        result = self._values.get("min_max_gradient")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataColorPalette(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DataSet",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "column_groups": "columnGroups",
        "column_level_permission_rules": "columnLevelPermissionRules",
        "consumed_spice_capacity_in_bytes": "consumedSpiceCapacityInBytes",
        "created_time": "createdTime",
        "data_set_id": "dataSetId",
        "field_folders": "fieldFolders",
        "import_mode": "importMode",
        "last_updated_time": "lastUpdatedTime",
        "logical_table_map": "logicalTableMap",
        "name": "name",
        "output_columns": "outputColumns",
        "physical_table_map": "physicalTableMap",
        "row_level_permission_data_set": "rowLevelPermissionDataSet",
    },
)
class DataSet:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        column_groups: typing.Optional[typing.Sequence[ColumnGroup]] = None,
        column_level_permission_rules: typing.Optional[typing.Sequence[ColumnLevelPermissionRule]] = None,
        consumed_spice_capacity_in_bytes: typing.Optional[jsii.Number] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        data_set_id: typing.Optional[builtins.str] = None,
        field_folders: typing.Optional[typing.Mapping[builtins.str, "FieldFolder"]] = None,
        import_mode: typing.Optional[builtins.str] = None,
        last_updated_time: typing.Optional[datetime.datetime] = None,
        logical_table_map: typing.Optional[typing.Mapping[builtins.str, "LogicalTable"]] = None,
        name: typing.Optional[builtins.str] = None,
        output_columns: typing.Optional[typing.Sequence["OutputColumn"]] = None,
        physical_table_map: typing.Optional[typing.Mapping[builtins.str, "PhysicalTable"]] = None,
        row_level_permission_data_set: typing.Optional["RowLevelPermissionDataSet"] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param column_groups: Groupings of columns that work together in certain Amazon QuickSight features. Currently, only geospatial hierarchy is supported.
        :param column_level_permission_rules: A set of one or more definitions of a ColumnLevelPermissionRule .
        :param consumed_spice_capacity_in_bytes: The amount of SPICE capacity used by this dataset. This is 0 if the dataset isn't imported into SPICE.
        :param created_time: The time that this dataset was created.
        :param data_set_id: The ID of the dataset.
        :param field_folders: The folder that contains fields and nested subfolders for your dataset.
        :param import_mode: A value that indicates whether you want to import the data into SPICE.
        :param last_updated_time: The last time that this dataset was updated.
        :param logical_table_map: Configures the combination and transformation of the data from the physical tables.
        :param name: A display name for the dataset.
        :param output_columns: The list of columns after all transforms. These columns are available in templates, analyses, and dashboards.
        :param physical_table_map: Declares the physical tables that are available in the underlying data sources.
        :param row_level_permission_data_set: The row-level security configuration for the dataset.
        '''
        if isinstance(row_level_permission_data_set, dict):
            row_level_permission_data_set = RowLevelPermissionDataSet(**row_level_permission_data_set)
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if column_groups is not None:
            self._values["column_groups"] = column_groups
        if column_level_permission_rules is not None:
            self._values["column_level_permission_rules"] = column_level_permission_rules
        if consumed_spice_capacity_in_bytes is not None:
            self._values["consumed_spice_capacity_in_bytes"] = consumed_spice_capacity_in_bytes
        if created_time is not None:
            self._values["created_time"] = created_time
        if data_set_id is not None:
            self._values["data_set_id"] = data_set_id
        if field_folders is not None:
            self._values["field_folders"] = field_folders
        if import_mode is not None:
            self._values["import_mode"] = import_mode
        if last_updated_time is not None:
            self._values["last_updated_time"] = last_updated_time
        if logical_table_map is not None:
            self._values["logical_table_map"] = logical_table_map
        if name is not None:
            self._values["name"] = name
        if output_columns is not None:
            self._values["output_columns"] = output_columns
        if physical_table_map is not None:
            self._values["physical_table_map"] = physical_table_map
        if row_level_permission_data_set is not None:
            self._values["row_level_permission_data_set"] = row_level_permission_data_set

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column_groups(self) -> typing.Optional[typing.List[ColumnGroup]]:
        '''Groupings of columns that work together in certain Amazon QuickSight features.

        Currently, only geospatial hierarchy is supported.
        '''
        result = self._values.get("column_groups")
        return typing.cast(typing.Optional[typing.List[ColumnGroup]], result)

    @builtins.property
    def column_level_permission_rules(
        self,
    ) -> typing.Optional[typing.List[ColumnLevelPermissionRule]]:
        '''A set of one or more definitions of a  ColumnLevelPermissionRule .'''
        result = self._values.get("column_level_permission_rules")
        return typing.cast(typing.Optional[typing.List[ColumnLevelPermissionRule]], result)

    @builtins.property
    def consumed_spice_capacity_in_bytes(self) -> typing.Optional[jsii.Number]:
        '''The amount of SPICE capacity used by this dataset.

        This is 0 if the dataset isn't imported into SPICE.
        '''
        result = self._values.get("consumed_spice_capacity_in_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that this dataset was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def data_set_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the dataset.'''
        result = self._values.get("data_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def field_folders(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "FieldFolder"]]:
        '''The folder that contains fields and nested subfolders for your dataset.'''
        result = self._values.get("field_folders")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "FieldFolder"]], result)

    @builtins.property
    def import_mode(self) -> typing.Optional[builtins.str]:
        '''A value that indicates whether you want to import the data into SPICE.'''
        result = self._values.get("import_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_updated_time(self) -> typing.Optional[datetime.datetime]:
        '''The last time that this dataset was updated.'''
        result = self._values.get("last_updated_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def logical_table_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "LogicalTable"]]:
        '''Configures the combination and transformation of the data from the physical tables.'''
        result = self._values.get("logical_table_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "LogicalTable"]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A display name for the dataset.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_columns(self) -> typing.Optional[typing.List["OutputColumn"]]:
        '''The list of columns after all transforms.

        These columns are available in templates, analyses, and dashboards.
        '''
        result = self._values.get("output_columns")
        return typing.cast(typing.Optional[typing.List["OutputColumn"]], result)

    @builtins.property
    def physical_table_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "PhysicalTable"]]:
        '''Declares the physical tables that are available in the underlying data sources.'''
        result = self._values.get("physical_table_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "PhysicalTable"]], result)

    @builtins.property
    def row_level_permission_data_set(
        self,
    ) -> typing.Optional["RowLevelPermissionDataSet"]:
        '''The row-level security configuration for the dataset.'''
        result = self._values.get("row_level_permission_data_set")
        return typing.cast(typing.Optional["RowLevelPermissionDataSet"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DataSetConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "column_group_schema_list": "columnGroupSchemaList",
        "data_set_schema": "dataSetSchema",
        "placeholder": "placeholder",
    },
)
class DataSetConfiguration:
    def __init__(
        self,
        *,
        column_group_schema_list: typing.Optional[typing.Sequence[ColumnGroupSchema]] = None,
        data_set_schema: typing.Optional["DataSetSchema"] = None,
        placeholder: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param column_group_schema_list: A structure containing the list of column group schemas.
        :param data_set_schema: Dataset schema.
        :param placeholder: Placeholder.
        '''
        if isinstance(data_set_schema, dict):
            data_set_schema = DataSetSchema(**data_set_schema)
        self._values: typing.Dict[str, typing.Any] = {}
        if column_group_schema_list is not None:
            self._values["column_group_schema_list"] = column_group_schema_list
        if data_set_schema is not None:
            self._values["data_set_schema"] = data_set_schema
        if placeholder is not None:
            self._values["placeholder"] = placeholder

    @builtins.property
    def column_group_schema_list(
        self,
    ) -> typing.Optional[typing.List[ColumnGroupSchema]]:
        '''A structure containing the list of column group schemas.'''
        result = self._values.get("column_group_schema_list")
        return typing.cast(typing.Optional[typing.List[ColumnGroupSchema]], result)

    @builtins.property
    def data_set_schema(self) -> typing.Optional["DataSetSchema"]:
        '''Dataset schema.'''
        result = self._values.get("data_set_schema")
        return typing.cast(typing.Optional["DataSetSchema"], result)

    @builtins.property
    def placeholder(self) -> typing.Optional[builtins.str]:
        '''Placeholder.'''
        result = self._values.get("placeholder")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSetConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataSetConstruct(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-quicksight-constructs.DataSetConstruct",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        logical_table_map: typing.Mapping[builtins.str, "LogicalTable"],
        physical_table_map: typing.Mapping[builtins.str, "PhysicalTable"],
        name: builtins.str,
        users: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param logical_table_map: 
        :param physical_table_map: 
        :param name: 
        :param users: QuickSight Users you want to give access to. In the end the permission arn are looking like arn:aws:quicksight:us-east-1:1234:user/default/martin.mueller@take2.co. If you want to see available users, use aws cli described here https://github.com/Reliantid/cypresspoint-infrastructure/tree/cdk#list-datasets
        '''
        props = DataSetProps(
            logical_table_map=logical_table_map,
            physical_table_map=physical_table_map,
            name=name,
            users=users,
        )

        jsii.create(DataSetConstruct, self, [scope, id, props])


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DataSetReference",
    jsii_struct_bases=[],
    name_mapping={
        "data_set_arn": "dataSetArn",
        "data_set_placeholder": "dataSetPlaceholder",
    },
)
class DataSetReference:
    def __init__(
        self,
        *,
        data_set_arn: builtins.str,
        data_set_placeholder: builtins.str,
    ) -> None:
        '''
        :param data_set_arn: Dataset Amazon Resource Name (ARN).
        :param data_set_placeholder: Dataset placeholder.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "data_set_arn": data_set_arn,
            "data_set_placeholder": data_set_placeholder,
        }

    @builtins.property
    def data_set_arn(self) -> builtins.str:
        '''Dataset Amazon Resource Name (ARN).'''
        result = self._values.get("data_set_arn")
        assert result is not None, "Required property 'data_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_placeholder(self) -> builtins.str:
        '''Dataset placeholder.'''
        result = self._values.get("data_set_placeholder")
        assert result is not None, "Required property 'data_set_placeholder' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DataSetSchema",
    jsii_struct_bases=[],
    name_mapping={"column_schema_list": "columnSchemaList"},
)
class DataSetSchema:
    def __init__(
        self,
        *,
        column_schema_list: typing.Optional[typing.Sequence[ColumnSchema]] = None,
    ) -> None:
        '''
        :param column_schema_list: A structure containing the list of column schemas.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if column_schema_list is not None:
            self._values["column_schema_list"] = column_schema_list

    @builtins.property
    def column_schema_list(self) -> typing.Optional[typing.List[ColumnSchema]]:
        '''A structure containing the list of column schemas.'''
        result = self._values.get("column_schema_list")
        return typing.cast(typing.Optional[typing.List[ColumnSchema]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSetSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DataSetSummary",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "column_level_permission_rules_applied": "columnLevelPermissionRulesApplied",
        "created_time": "createdTime",
        "data_set_id": "dataSetId",
        "import_mode": "importMode",
        "last_updated_time": "lastUpdatedTime",
        "name": "name",
        "row_level_permission_data_set": "rowLevelPermissionDataSet",
    },
)
class DataSetSummary:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        column_level_permission_rules_applied: typing.Optional[builtins.bool] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        data_set_id: typing.Optional[builtins.str] = None,
        import_mode: typing.Optional[builtins.str] = None,
        last_updated_time: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[builtins.str] = None,
        row_level_permission_data_set: typing.Optional["RowLevelPermissionDataSet"] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the dataset.
        :param column_level_permission_rules_applied: A value that indicates if the dataset has column level permission configured.
        :param created_time: The time that this dataset was created.
        :param data_set_id: The ID of the dataset.
        :param import_mode: A value that indicates whether you want to import the data into SPICE.
        :param last_updated_time: The last time that this dataset was updated.
        :param name: A display name for the dataset.
        :param row_level_permission_data_set: The row-level security configuration for the dataset.
        '''
        if isinstance(row_level_permission_data_set, dict):
            row_level_permission_data_set = RowLevelPermissionDataSet(**row_level_permission_data_set)
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if column_level_permission_rules_applied is not None:
            self._values["column_level_permission_rules_applied"] = column_level_permission_rules_applied
        if created_time is not None:
            self._values["created_time"] = created_time
        if data_set_id is not None:
            self._values["data_set_id"] = data_set_id
        if import_mode is not None:
            self._values["import_mode"] = import_mode
        if last_updated_time is not None:
            self._values["last_updated_time"] = last_updated_time
        if name is not None:
            self._values["name"] = name
        if row_level_permission_data_set is not None:
            self._values["row_level_permission_data_set"] = row_level_permission_data_set

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the dataset.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column_level_permission_rules_applied(self) -> typing.Optional[builtins.bool]:
        '''A value that indicates if the dataset has column level permission configured.'''
        result = self._values.get("column_level_permission_rules_applied")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that this dataset was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def data_set_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the dataset.'''
        result = self._values.get("data_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def import_mode(self) -> typing.Optional[builtins.str]:
        '''A value that indicates whether you want to import the data into SPICE.'''
        result = self._values.get("import_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_updated_time(self) -> typing.Optional[datetime.datetime]:
        '''The last time that this dataset was updated.'''
        result = self._values.get("last_updated_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A display name for the dataset.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def row_level_permission_data_set(
        self,
    ) -> typing.Optional["RowLevelPermissionDataSet"]:
        '''The row-level security configuration for the dataset.'''
        result = self._values.get("row_level_permission_data_set")
        return typing.cast(typing.Optional["RowLevelPermissionDataSet"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSetSummary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DataSource",
    jsii_struct_bases=[],
    name_mapping={
        "alternate_data_source_parameters": "alternateDataSourceParameters",
        "arn": "arn",
        "created_time": "createdTime",
        "data_source_id": "dataSourceId",
        "data_source_parameters": "dataSourceParameters",
        "error_info": "errorInfo",
        "last_updated_time": "lastUpdatedTime",
        "name": "name",
        "ssl_properties": "sslProperties",
        "status": "status",
        "type": "type",
        "vpc_connection_properties": "vpcConnectionProperties",
    },
)
class DataSource:
    def __init__(
        self,
        *,
        alternate_data_source_parameters: typing.Optional[typing.Sequence["DataSourceParameters"]] = None,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        data_source_id: typing.Optional[builtins.str] = None,
        data_source_parameters: typing.Optional["DataSourceParameters"] = None,
        error_info: typing.Optional["DataSourceErrorInfo"] = None,
        last_updated_time: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[builtins.str] = None,
        ssl_properties: typing.Optional["SslProperties"] = None,
        status: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        vpc_connection_properties: typing.Optional["VpcConnectionProperties"] = None,
    ) -> None:
        '''
        :param alternate_data_source_parameters: A set of alternate data source parameters that you want to share for the credentials stored with this data source. The credentials are applied in tandem with the data source parameters when you copy a data source by using a create or update request. The API operation compares the DataSourceParameters structure that's in the request with the structures in the AlternateDataSourceParameters allow list. If the structures are an exact match, the request is allowed to use the credentials from this existing data source. If the AlternateDataSourceParameters list is null, the Credentials originally used with this DataSourceParameters are automatically allowed.
        :param arn: The Amazon Resource Name (ARN) of the data source.
        :param created_time: The time that this data source was created.
        :param data_source_id: The ID of the data source. This ID is unique per AWS Region for each AWS account.
        :param data_source_parameters: The parameters that Amazon QuickSight uses to connect to your underlying source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.
        :param error_info: Error information from the last update or the creation of the data source.
        :param last_updated_time: The last time that this data source was updated.
        :param name: A display name for the data source.
        :param ssl_properties: Secure Socket Layer (SSL) properties that apply when QuickSight connects to your underlying source.
        :param status: The HTTP status of the request.
        :param type: The type of the data source. This type indicates which database engine the data source connects to.
        :param vpc_connection_properties: The VPC connection information. You need to use this parameter only when you want QuickSight to use a VPC connection when connecting to your underlying source.
        '''
        if isinstance(data_source_parameters, dict):
            data_source_parameters = DataSourceParameters(**data_source_parameters)
        if isinstance(error_info, dict):
            error_info = DataSourceErrorInfo(**error_info)
        if isinstance(ssl_properties, dict):
            ssl_properties = SslProperties(**ssl_properties)
        if isinstance(vpc_connection_properties, dict):
            vpc_connection_properties = VpcConnectionProperties(**vpc_connection_properties)
        self._values: typing.Dict[str, typing.Any] = {}
        if alternate_data_source_parameters is not None:
            self._values["alternate_data_source_parameters"] = alternate_data_source_parameters
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if data_source_id is not None:
            self._values["data_source_id"] = data_source_id
        if data_source_parameters is not None:
            self._values["data_source_parameters"] = data_source_parameters
        if error_info is not None:
            self._values["error_info"] = error_info
        if last_updated_time is not None:
            self._values["last_updated_time"] = last_updated_time
        if name is not None:
            self._values["name"] = name
        if ssl_properties is not None:
            self._values["ssl_properties"] = ssl_properties
        if status is not None:
            self._values["status"] = status
        if type is not None:
            self._values["type"] = type
        if vpc_connection_properties is not None:
            self._values["vpc_connection_properties"] = vpc_connection_properties

    @builtins.property
    def alternate_data_source_parameters(
        self,
    ) -> typing.Optional[typing.List["DataSourceParameters"]]:
        '''A set of alternate data source parameters that you want to share for the credentials stored with this data source.

        The credentials are applied in tandem with the data source parameters when you copy a data source by using a create or update request. The API operation compares the DataSourceParameters structure that's in the request with the structures in the AlternateDataSourceParameters allow list. If the structures are an exact match, the request is allowed to use the credentials from this existing data source. If the AlternateDataSourceParameters list is null, the Credentials originally used with this DataSourceParameters are automatically allowed.
        '''
        result = self._values.get("alternate_data_source_parameters")
        return typing.cast(typing.Optional[typing.List["DataSourceParameters"]], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the data source.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that this data source was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def data_source_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the data source.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_source_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_source_parameters(self) -> typing.Optional["DataSourceParameters"]:
        '''The parameters that Amazon QuickSight uses to connect to your underlying source.

        This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.
        '''
        result = self._values.get("data_source_parameters")
        return typing.cast(typing.Optional["DataSourceParameters"], result)

    @builtins.property
    def error_info(self) -> typing.Optional["DataSourceErrorInfo"]:
        '''Error information from the last update or the creation of the data source.'''
        result = self._values.get("error_info")
        return typing.cast(typing.Optional["DataSourceErrorInfo"], result)

    @builtins.property
    def last_updated_time(self) -> typing.Optional[datetime.datetime]:
        '''The last time that this data source was updated.'''
        result = self._values.get("last_updated_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A display name for the data source.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_properties(self) -> typing.Optional["SslProperties"]:
        '''Secure Socket Layer (SSL) properties that apply when QuickSight connects to your underlying source.'''
        result = self._values.get("ssl_properties")
        return typing.cast(typing.Optional["SslProperties"], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the data source.

        This type indicates which database engine the data source connects to.
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_connection_properties(self) -> typing.Optional["VpcConnectionProperties"]:
        '''The VPC connection information.

        You need to use this parameter only when you want QuickSight to use a VPC connection when connecting to your underlying source.
        '''
        result = self._values.get("vpc_connection_properties")
        return typing.cast(typing.Optional["VpcConnectionProperties"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataSourceConstruct(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-quicksight-constructs.DataSourceConstruct",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        data_source_parameters: "DataSourceParameters",
        type: builtins.str,
        name: builtins.str,
        users: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param data_source_parameters: 
        :param type: 
        :param name: 
        :param users: QuickSight Users you want to give access to. In the end the permission arn are looking like arn:aws:quicksight:us-east-1:1234:user/default/martin.mueller@take2.co. If you want to see available users, use aws cli described here https://github.com/Reliantid/cypresspoint-infrastructure/tree/cdk#list-datasets
        '''
        props = DataSourceProps(
            data_source_parameters=data_source_parameters,
            type=type,
            name=name,
            users=users,
        )

        jsii.create(DataSourceConstruct, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataSourceArn")
    def data_source_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSourceArn"))

    @data_source_arn.setter
    def data_source_arn(self, value: builtins.str) -> None:
        jsii.set(self, "dataSourceArn", value)


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DataSourceCredentials",
    jsii_struct_bases=[],
    name_mapping={
        "copy_source_arn": "copySourceArn",
        "credential_pair": "credentialPair",
    },
)
class DataSourceCredentials:
    def __init__(
        self,
        *,
        copy_source_arn: typing.Optional[builtins.str] = None,
        credential_pair: typing.Optional[CredentialPair] = None,
    ) -> None:
        '''
        :param copy_source_arn: The Amazon Resource Name (ARN) of a data source that has the credential pair that you want to use. When CopySourceArn is not null, the credential pair from the data source in the ARN is used as the credentials for the DataSourceCredentials structure.
        :param credential_pair: Credential pair. For more information, see CredentialPair.
        '''
        if isinstance(credential_pair, dict):
            credential_pair = CredentialPair(**credential_pair)
        self._values: typing.Dict[str, typing.Any] = {}
        if copy_source_arn is not None:
            self._values["copy_source_arn"] = copy_source_arn
        if credential_pair is not None:
            self._values["credential_pair"] = credential_pair

    @builtins.property
    def copy_source_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of a data source that has the credential pair that you want to use.

        When CopySourceArn is not null, the credential pair from the data source in the ARN is used as the credentials for the DataSourceCredentials structure.
        '''
        result = self._values.get("copy_source_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credential_pair(self) -> typing.Optional[CredentialPair]:
        '''Credential pair.

        For more information, see CredentialPair.
        '''
        result = self._values.get("credential_pair")
        return typing.cast(typing.Optional[CredentialPair], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DataSourceErrorInfo",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "type": "type"},
)
class DataSourceErrorInfo:
    def __init__(
        self,
        *,
        message: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: Error message.
        :param type: Error type.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Error message.'''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Error type.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceErrorInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DataSourceParameters",
    jsii_struct_bases=[],
    name_mapping={
        "amazon_elasticsearch_parameters": "amazonElasticsearchParameters",
        "athena_parameters": "athenaParameters",
        "aurora_parameters": "auroraParameters",
        "aurora_postgre_sql_parameters": "auroraPostgreSqlParameters",
        "aws_iot_analytics_parameters": "awsIotAnalyticsParameters",
        "jira_parameters": "jiraParameters",
        "maria_db_parameters": "mariaDbParameters",
        "my_sql_parameters": "mySqlParameters",
        "oracle_parameters": "oracleParameters",
        "postgre_sql_parameters": "postgreSqlParameters",
        "presto_parameters": "prestoParameters",
        "rds_parameters": "rdsParameters",
        "redshift_parameters": "redshiftParameters",
        "s3_parameters": "s3Parameters",
        "service_now_parameters": "serviceNowParameters",
        "snowflake_parameters": "snowflakeParameters",
        "spark_parameters": "sparkParameters",
        "sql_server_parameters": "sqlServerParameters",
        "teradata_parameters": "teradataParameters",
        "twitter_parameters": "twitterParameters",
    },
)
class DataSourceParameters:
    def __init__(
        self,
        *,
        amazon_elasticsearch_parameters: typing.Optional[AmazonElasticsearchParameters] = None,
        athena_parameters: typing.Optional[AthenaParameters] = None,
        aurora_parameters: typing.Optional[AuroraParameters] = None,
        aurora_postgre_sql_parameters: typing.Optional[AuroraPostgreSqlParameters] = None,
        aws_iot_analytics_parameters: typing.Optional[AwsIotAnalyticsParameters] = None,
        jira_parameters: typing.Optional["JiraParameters"] = None,
        maria_db_parameters: typing.Optional["MariaDbParameters"] = None,
        my_sql_parameters: typing.Optional["MySqlParameters"] = None,
        oracle_parameters: typing.Optional["OracleParameters"] = None,
        postgre_sql_parameters: typing.Optional["PostgreSqlParameters"] = None,
        presto_parameters: typing.Optional["PrestoParameters"] = None,
        rds_parameters: typing.Optional["RdsParameters"] = None,
        redshift_parameters: typing.Optional["RedshiftParameters"] = None,
        s3_parameters: typing.Optional["S3Parameters"] = None,
        service_now_parameters: typing.Optional["ServiceNowParameters"] = None,
        snowflake_parameters: typing.Optional["SnowflakeParameters"] = None,
        spark_parameters: typing.Optional["SparkParameters"] = None,
        sql_server_parameters: typing.Optional["SqlServerParameters"] = None,
        teradata_parameters: typing.Optional["TeradataParameters"] = None,
        twitter_parameters: typing.Optional["TwitterParameters"] = None,
    ) -> None:
        '''
        :param amazon_elasticsearch_parameters: Amazon Elasticsearch Service parameters.
        :param athena_parameters: Amazon Athena parameters.
        :param aurora_parameters: Amazon Aurora MySQL parameters.
        :param aurora_postgre_sql_parameters: Aurora PostgreSQL parameters.
        :param aws_iot_analytics_parameters: AWS IoT Analytics parameters.
        :param jira_parameters: Jira parameters.
        :param maria_db_parameters: MariaDB parameters.
        :param my_sql_parameters: MySQL parameters.
        :param oracle_parameters: Oracle parameters.
        :param postgre_sql_parameters: PostgreSQL parameters.
        :param presto_parameters: Presto parameters.
        :param rds_parameters: Amazon RDS parameters.
        :param redshift_parameters: Amazon Redshift parameters.
        :param s3_parameters: S3 parameters.
        :param service_now_parameters: ServiceNow parameters.
        :param snowflake_parameters: Snowflake parameters.
        :param spark_parameters: Spark parameters.
        :param sql_server_parameters: SQL Server parameters.
        :param teradata_parameters: Teradata parameters.
        :param twitter_parameters: Twitter parameters.
        '''
        if isinstance(amazon_elasticsearch_parameters, dict):
            amazon_elasticsearch_parameters = AmazonElasticsearchParameters(**amazon_elasticsearch_parameters)
        if isinstance(athena_parameters, dict):
            athena_parameters = AthenaParameters(**athena_parameters)
        if isinstance(aurora_parameters, dict):
            aurora_parameters = AuroraParameters(**aurora_parameters)
        if isinstance(aurora_postgre_sql_parameters, dict):
            aurora_postgre_sql_parameters = AuroraPostgreSqlParameters(**aurora_postgre_sql_parameters)
        if isinstance(aws_iot_analytics_parameters, dict):
            aws_iot_analytics_parameters = AwsIotAnalyticsParameters(**aws_iot_analytics_parameters)
        if isinstance(jira_parameters, dict):
            jira_parameters = JiraParameters(**jira_parameters)
        if isinstance(maria_db_parameters, dict):
            maria_db_parameters = MariaDbParameters(**maria_db_parameters)
        if isinstance(my_sql_parameters, dict):
            my_sql_parameters = MySqlParameters(**my_sql_parameters)
        if isinstance(oracle_parameters, dict):
            oracle_parameters = OracleParameters(**oracle_parameters)
        if isinstance(postgre_sql_parameters, dict):
            postgre_sql_parameters = PostgreSqlParameters(**postgre_sql_parameters)
        if isinstance(presto_parameters, dict):
            presto_parameters = PrestoParameters(**presto_parameters)
        if isinstance(rds_parameters, dict):
            rds_parameters = RdsParameters(**rds_parameters)
        if isinstance(redshift_parameters, dict):
            redshift_parameters = RedshiftParameters(**redshift_parameters)
        if isinstance(s3_parameters, dict):
            s3_parameters = S3Parameters(**s3_parameters)
        if isinstance(service_now_parameters, dict):
            service_now_parameters = ServiceNowParameters(**service_now_parameters)
        if isinstance(snowflake_parameters, dict):
            snowflake_parameters = SnowflakeParameters(**snowflake_parameters)
        if isinstance(spark_parameters, dict):
            spark_parameters = SparkParameters(**spark_parameters)
        if isinstance(sql_server_parameters, dict):
            sql_server_parameters = SqlServerParameters(**sql_server_parameters)
        if isinstance(teradata_parameters, dict):
            teradata_parameters = TeradataParameters(**teradata_parameters)
        if isinstance(twitter_parameters, dict):
            twitter_parameters = TwitterParameters(**twitter_parameters)
        self._values: typing.Dict[str, typing.Any] = {}
        if amazon_elasticsearch_parameters is not None:
            self._values["amazon_elasticsearch_parameters"] = amazon_elasticsearch_parameters
        if athena_parameters is not None:
            self._values["athena_parameters"] = athena_parameters
        if aurora_parameters is not None:
            self._values["aurora_parameters"] = aurora_parameters
        if aurora_postgre_sql_parameters is not None:
            self._values["aurora_postgre_sql_parameters"] = aurora_postgre_sql_parameters
        if aws_iot_analytics_parameters is not None:
            self._values["aws_iot_analytics_parameters"] = aws_iot_analytics_parameters
        if jira_parameters is not None:
            self._values["jira_parameters"] = jira_parameters
        if maria_db_parameters is not None:
            self._values["maria_db_parameters"] = maria_db_parameters
        if my_sql_parameters is not None:
            self._values["my_sql_parameters"] = my_sql_parameters
        if oracle_parameters is not None:
            self._values["oracle_parameters"] = oracle_parameters
        if postgre_sql_parameters is not None:
            self._values["postgre_sql_parameters"] = postgre_sql_parameters
        if presto_parameters is not None:
            self._values["presto_parameters"] = presto_parameters
        if rds_parameters is not None:
            self._values["rds_parameters"] = rds_parameters
        if redshift_parameters is not None:
            self._values["redshift_parameters"] = redshift_parameters
        if s3_parameters is not None:
            self._values["s3_parameters"] = s3_parameters
        if service_now_parameters is not None:
            self._values["service_now_parameters"] = service_now_parameters
        if snowflake_parameters is not None:
            self._values["snowflake_parameters"] = snowflake_parameters
        if spark_parameters is not None:
            self._values["spark_parameters"] = spark_parameters
        if sql_server_parameters is not None:
            self._values["sql_server_parameters"] = sql_server_parameters
        if teradata_parameters is not None:
            self._values["teradata_parameters"] = teradata_parameters
        if twitter_parameters is not None:
            self._values["twitter_parameters"] = twitter_parameters

    @builtins.property
    def amazon_elasticsearch_parameters(
        self,
    ) -> typing.Optional[AmazonElasticsearchParameters]:
        '''Amazon Elasticsearch Service parameters.'''
        result = self._values.get("amazon_elasticsearch_parameters")
        return typing.cast(typing.Optional[AmazonElasticsearchParameters], result)

    @builtins.property
    def athena_parameters(self) -> typing.Optional[AthenaParameters]:
        '''Amazon Athena parameters.'''
        result = self._values.get("athena_parameters")
        return typing.cast(typing.Optional[AthenaParameters], result)

    @builtins.property
    def aurora_parameters(self) -> typing.Optional[AuroraParameters]:
        '''Amazon Aurora MySQL parameters.'''
        result = self._values.get("aurora_parameters")
        return typing.cast(typing.Optional[AuroraParameters], result)

    @builtins.property
    def aurora_postgre_sql_parameters(
        self,
    ) -> typing.Optional[AuroraPostgreSqlParameters]:
        '''Aurora PostgreSQL parameters.'''
        result = self._values.get("aurora_postgre_sql_parameters")
        return typing.cast(typing.Optional[AuroraPostgreSqlParameters], result)

    @builtins.property
    def aws_iot_analytics_parameters(
        self,
    ) -> typing.Optional[AwsIotAnalyticsParameters]:
        '''AWS IoT Analytics parameters.'''
        result = self._values.get("aws_iot_analytics_parameters")
        return typing.cast(typing.Optional[AwsIotAnalyticsParameters], result)

    @builtins.property
    def jira_parameters(self) -> typing.Optional["JiraParameters"]:
        '''Jira parameters.'''
        result = self._values.get("jira_parameters")
        return typing.cast(typing.Optional["JiraParameters"], result)

    @builtins.property
    def maria_db_parameters(self) -> typing.Optional["MariaDbParameters"]:
        '''MariaDB parameters.'''
        result = self._values.get("maria_db_parameters")
        return typing.cast(typing.Optional["MariaDbParameters"], result)

    @builtins.property
    def my_sql_parameters(self) -> typing.Optional["MySqlParameters"]:
        '''MySQL parameters.'''
        result = self._values.get("my_sql_parameters")
        return typing.cast(typing.Optional["MySqlParameters"], result)

    @builtins.property
    def oracle_parameters(self) -> typing.Optional["OracleParameters"]:
        '''Oracle parameters.'''
        result = self._values.get("oracle_parameters")
        return typing.cast(typing.Optional["OracleParameters"], result)

    @builtins.property
    def postgre_sql_parameters(self) -> typing.Optional["PostgreSqlParameters"]:
        '''PostgreSQL parameters.'''
        result = self._values.get("postgre_sql_parameters")
        return typing.cast(typing.Optional["PostgreSqlParameters"], result)

    @builtins.property
    def presto_parameters(self) -> typing.Optional["PrestoParameters"]:
        '''Presto parameters.'''
        result = self._values.get("presto_parameters")
        return typing.cast(typing.Optional["PrestoParameters"], result)

    @builtins.property
    def rds_parameters(self) -> typing.Optional["RdsParameters"]:
        '''Amazon RDS parameters.'''
        result = self._values.get("rds_parameters")
        return typing.cast(typing.Optional["RdsParameters"], result)

    @builtins.property
    def redshift_parameters(self) -> typing.Optional["RedshiftParameters"]:
        '''Amazon Redshift parameters.'''
        result = self._values.get("redshift_parameters")
        return typing.cast(typing.Optional["RedshiftParameters"], result)

    @builtins.property
    def s3_parameters(self) -> typing.Optional["S3Parameters"]:
        '''S3 parameters.'''
        result = self._values.get("s3_parameters")
        return typing.cast(typing.Optional["S3Parameters"], result)

    @builtins.property
    def service_now_parameters(self) -> typing.Optional["ServiceNowParameters"]:
        '''ServiceNow parameters.'''
        result = self._values.get("service_now_parameters")
        return typing.cast(typing.Optional["ServiceNowParameters"], result)

    @builtins.property
    def snowflake_parameters(self) -> typing.Optional["SnowflakeParameters"]:
        '''Snowflake parameters.'''
        result = self._values.get("snowflake_parameters")
        return typing.cast(typing.Optional["SnowflakeParameters"], result)

    @builtins.property
    def spark_parameters(self) -> typing.Optional["SparkParameters"]:
        '''Spark parameters.'''
        result = self._values.get("spark_parameters")
        return typing.cast(typing.Optional["SparkParameters"], result)

    @builtins.property
    def sql_server_parameters(self) -> typing.Optional["SqlServerParameters"]:
        '''SQL Server parameters.'''
        result = self._values.get("sql_server_parameters")
        return typing.cast(typing.Optional["SqlServerParameters"], result)

    @builtins.property
    def teradata_parameters(self) -> typing.Optional["TeradataParameters"]:
        '''Teradata parameters.'''
        result = self._values.get("teradata_parameters")
        return typing.cast(typing.Optional["TeradataParameters"], result)

    @builtins.property
    def twitter_parameters(self) -> typing.Optional["TwitterParameters"]:
        '''Twitter parameters.'''
        result = self._values.get("twitter_parameters")
        return typing.cast(typing.Optional["TwitterParameters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DateTimeParameter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class DateTimeParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[datetime.datetime],
    ) -> None:
        '''
        :param name: A display name for the date-time parameter.
        :param values: The values for the date-time parameter.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''A display name for the date-time parameter.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[datetime.datetime]:
        '''The values for the date-time parameter.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[datetime.datetime], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DateTimeParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DecimalParameter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class DecimalParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param name: A display name for the decimal parameter.
        :param values: The values for the decimal parameter.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''A display name for the decimal parameter.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[jsii.Number]:
        '''The values for the decimal parameter.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DecimalParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteAccountCustomizationRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId", "namespace": "namespace"},
)
class DeleteAccountCustomizationRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that you want to delete QuickSight customizations from in this AWS Region.
        :param namespace: The QuickSight namespace that you're deleting the customizations from.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
        }
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that you want to delete QuickSight customizations from in this AWS Region.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The QuickSight namespace that you're deleting the customizations from.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteAccountCustomizationRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteAccountCustomizationResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status"},
)
class DeleteAccountCustomizationResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteAccountCustomizationResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteAnalysisRequest",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_id": "analysisId",
        "aws_account_id": "awsAccountId",
        "force_delete_without_recovery": "forceDeleteWithoutRecovery",
        "recovery_window_in_days": "recoveryWindowInDays",
    },
)
class DeleteAnalysisRequest:
    def __init__(
        self,
        *,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
        force_delete_without_recovery: typing.Optional[builtins.bool] = None,
        recovery_window_in_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param analysis_id: The ID of the analysis that you're deleting.
        :param aws_account_id: The ID of the AWS account where you want to delete an analysis.
        :param force_delete_without_recovery: This option defaults to the value NoForceDeleteWithoutRecovery. To immediately delete the analysis, add the ForceDeleteWithoutRecovery option. You can't restore an analysis after it's deleted.
        :param recovery_window_in_days: A value that specifies the number of days that QuickSight waits before it deletes the analysis. You can't use this parameter with the ForceDeleteWithoutRecovery option in the same API call. The default value is 30.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "analysis_id": analysis_id,
            "aws_account_id": aws_account_id,
        }
        if force_delete_without_recovery is not None:
            self._values["force_delete_without_recovery"] = force_delete_without_recovery
        if recovery_window_in_days is not None:
            self._values["recovery_window_in_days"] = recovery_window_in_days

    @builtins.property
    def analysis_id(self) -> builtins.str:
        '''The ID of the analysis that you're deleting.'''
        result = self._values.get("analysis_id")
        assert result is not None, "Required property 'analysis_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account where you want to delete an analysis.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def force_delete_without_recovery(self) -> typing.Optional[builtins.bool]:
        '''This option defaults to the value NoForceDeleteWithoutRecovery.

        To immediately delete the analysis, add the ForceDeleteWithoutRecovery option. You can't restore an analysis after it's deleted.
        '''
        result = self._values.get("force_delete_without_recovery")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def recovery_window_in_days(self) -> typing.Optional[jsii.Number]:
        '''A value that specifies the number of days that QuickSight waits before it deletes the analysis.

        You can't use this parameter with the ForceDeleteWithoutRecovery option in the same API call. The default value is 30.
        '''
        result = self._values.get("recovery_window_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteAnalysisRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteAnalysisResponse",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_id": "analysisId",
        "arn": "arn",
        "deletion_time": "deletionTime",
        "request_id": "requestId",
        "status": "status",
    },
)
class DeleteAnalysisResponse:
    def __init__(
        self,
        *,
        analysis_id: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        deletion_time: typing.Optional[datetime.datetime] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param analysis_id: The ID of the deleted analysis.
        :param arn: The Amazon Resource Name (ARN) of the deleted analysis.
        :param deletion_time: The date and time that the analysis is scheduled to be deleted.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if analysis_id is not None:
            self._values["analysis_id"] = analysis_id
        if arn is not None:
            self._values["arn"] = arn
        if deletion_time is not None:
            self._values["deletion_time"] = deletion_time
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def analysis_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the deleted analysis.'''
        result = self._values.get("analysis_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the deleted analysis.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deletion_time(self) -> typing.Optional[datetime.datetime]:
        '''The date and time that the analysis is scheduled to be deleted.'''
        result = self._values.get("deletion_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteAnalysisResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteDashboardRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dashboard_id": "dashboardId",
        "version_number": "versionNumber",
    },
)
class DeleteDashboardRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
        version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the dashboard that you're deleting.
        :param dashboard_id: The ID for the dashboard.
        :param version_number: The version number of the dashboard. If the version number property is provided, only the specified version of the dashboard is deleted.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_id": dashboard_id,
        }
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the dashboard that you're deleting.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        '''The ID for the dashboard.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number of the dashboard.

        If the version number property is provided, only the specified version of the dashboard is deleted.
        '''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteDashboardRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteDashboardResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "dashboard_id": "dashboardId",
        "request_id": "requestId",
        "status": "status",
    },
)
class DeleteDashboardResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        dashboard_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Secure Socket Layer (SSL) properties that apply for the resource.
        :param dashboard_id: The ID of the dashboard.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if dashboard_id is not None:
            self._values["dashboard_id"] = dashboard_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Secure Socket Layer (SSL) properties that apply for the resource.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dashboard_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the dashboard.'''
        result = self._values.get("dashboard_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteDashboardResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteDataSetRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId", "data_set_id": "dataSetId"},
)
class DeleteDataSetRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_id: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_set_id: The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_id": data_set_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The ID for the dataset that you want to create.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteDataSetRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteDataSetResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "data_set_id": "dataSetId",
        "request_id": "requestId",
        "status": "status",
    },
)
class DeleteDataSetResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        data_set_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the dataset.
        :param data_set_id: The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if data_set_id is not None:
            self._values["data_set_id"] = data_set_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the dataset.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_set_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the dataset that you want to create.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteDataSetResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteDataSourceRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId", "data_source_id": "dataSourceId"},
)
class DeleteDataSourceRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_source_id: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_source_id: The ID of the data source. This ID is unique per AWS Region for each AWS account.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_source_id": data_source_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''The ID of the data source.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteDataSourceRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteDataSourceResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "data_source_id": "dataSourceId",
        "request_id": "requestId",
        "status": "status",
    },
)
class DeleteDataSourceResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        data_source_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the data source that you deleted.
        :param data_source_id: The ID of the data source. This ID is unique per AWS Region for each AWS account.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if data_source_id is not None:
            self._values["data_source_id"] = data_source_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the data source that you deleted.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_source_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the data source.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_source_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteDataSourceResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteGroupMembershipRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "group_name": "groupName",
        "member_name": "memberName",
        "namespace": "namespace",
    },
)
class DeleteGroupMembershipRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        group_name: builtins.str,
        member_name: builtins.str,
        namespace: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param group_name: The name of the group that you want to delete the user from.
        :param member_name: The name of the user that you want to delete from the group membership.
        :param namespace: The namespace. Currently, you should set this to default.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "group_name": group_name,
            "member_name": member_name,
            "namespace": namespace,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the group is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The name of the group that you want to delete the user from.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_name(self) -> builtins.str:
        '''The name of the user that you want to delete from the group membership.'''
        result = self._values.get("member_name")
        assert result is not None, "Required property 'member_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteGroupMembershipRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteGroupMembershipResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status"},
)
class DeleteGroupMembershipResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteGroupMembershipResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteGroupRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "group_name": "groupName",
        "namespace": "namespace",
    },
)
class DeleteGroupRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        group_name: builtins.str,
        namespace: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param group_name: The name of the group that you want to delete.
        :param namespace: The namespace. Currently, you should set this to default.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "group_name": group_name,
            "namespace": namespace,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the group is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The name of the group that you want to delete.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteGroupRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteGroupResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status"},
)
class DeleteGroupResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteGroupResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteIAMPolicyAssignmentRequest",
    jsii_struct_bases=[],
    name_mapping={
        "assignment_name": "assignmentName",
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
    },
)
class DeleteIAMPolicyAssignmentRequest:
    def __init__(
        self,
        *,
        assignment_name: builtins.str,
        aws_account_id: builtins.str,
        namespace: builtins.str,
    ) -> None:
        '''
        :param assignment_name: The name of the assignment.
        :param aws_account_id: The AWS account ID where you want to delete the IAM policy assignment.
        :param namespace: The namespace that contains the assignment.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "assignment_name": assignment_name,
            "aws_account_id": aws_account_id,
            "namespace": namespace,
        }

    @builtins.property
    def assignment_name(self) -> builtins.str:
        '''The name of the assignment.'''
        result = self._values.get("assignment_name")
        assert result is not None, "Required property 'assignment_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID where you want to delete the IAM policy assignment.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace that contains the assignment.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteIAMPolicyAssignmentRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteIAMPolicyAssignmentResponse",
    jsii_struct_bases=[],
    name_mapping={
        "assignment_name": "assignmentName",
        "request_id": "requestId",
        "status": "status",
    },
)
class DeleteIAMPolicyAssignmentResponse:
    def __init__(
        self,
        *,
        assignment_name: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param assignment_name: The name of the assignment.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if assignment_name is not None:
            self._values["assignment_name"] = assignment_name
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def assignment_name(self) -> typing.Optional[builtins.str]:
        '''The name of the assignment.'''
        result = self._values.get("assignment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteIAMPolicyAssignmentResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteNamespaceRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId", "namespace": "namespace"},
)
class DeleteNamespaceRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        namespace: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that you want to delete the QuickSight namespace from.
        :param namespace: The namespace that you want to delete.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "namespace": namespace,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that you want to delete the QuickSight namespace from.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace that you want to delete.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteNamespaceRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteNamespaceResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status"},
)
class DeleteNamespaceResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteNamespaceResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteTemplateAliasRequest",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "aws_account_id": "awsAccountId",
        "template_id": "templateId",
    },
)
class DeleteTemplateAliasRequest:
    def __init__(
        self,
        *,
        alias_name: builtins.str,
        aws_account_id: builtins.str,
        template_id: builtins.str,
    ) -> None:
        '''
        :param alias_name: The name for the template alias. To delete a specific alias, you delete the version that the alias points to. You can specify the alias name, or specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter.
        :param aws_account_id: The ID of the AWS account that contains the item to delete.
        :param template_id: The ID for the template that the specified alias is for.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alias_name": alias_name,
            "aws_account_id": aws_account_id,
            "template_id": template_id,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''The name for the template alias.

        To delete a specific alias, you delete the version that the alias points to. You can specify the alias name, or specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter.
        '''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the item to delete.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The ID for the template that the specified alias is for.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteTemplateAliasRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteTemplateAliasResponse",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "arn": "arn",
        "request_id": "requestId",
        "status": "status",
        "template_id": "templateId",
    },
)
class DeleteTemplateAliasResponse:
    def __init__(
        self,
        *,
        alias_name: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias_name: The name for the template alias.
        :param arn: The Amazon Resource Name (ARN) of the template you want to delete.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template_id: An ID for the template associated with the deletion.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if alias_name is not None:
            self._values["alias_name"] = alias_name
        if arn is not None:
            self._values["arn"] = arn
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template_id is not None:
            self._values["template_id"] = template_id

    @builtins.property
    def alias_name(self) -> typing.Optional[builtins.str]:
        '''The name for the template alias.'''
        result = self._values.get("alias_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the template you want to delete.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''An ID for the template associated with the deletion.'''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteTemplateAliasResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteTemplateRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "template_id": "templateId",
        "version_number": "versionNumber",
    },
)
class DeleteTemplateRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        template_id: builtins.str,
        version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the template that you're deleting.
        :param template_id: An ID for the template you want to delete.
        :param version_number: Specifies the version of the template that you want to delete. If you don't provide a version number, DeleteTemplate deletes all versions of the template.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "template_id": template_id,
        }
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the template that you're deleting.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''An ID for the template you want to delete.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_number(self) -> typing.Optional[jsii.Number]:
        '''Specifies the version of the template that you want to delete.

        If you don't provide a version number, DeleteTemplate deletes all versions of the template.
        '''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteTemplateRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteTemplateResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "request_id": "requestId",
        "status": "status",
        "template_id": "templateId",
    },
)
class DeleteTemplateResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template_id: An ID for the template.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template_id is not None:
            self._values["template_id"] = template_id

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''An ID for the template.'''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteTemplateResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteThemeAliasRequest",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "aws_account_id": "awsAccountId",
        "theme_id": "themeId",
    },
)
class DeleteThemeAliasRequest:
    def __init__(
        self,
        *,
        alias_name: builtins.str,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
    ) -> None:
        '''
        :param alias_name: The unique name for the theme alias to delete.
        :param aws_account_id: The ID of the AWS account that contains the theme alias to delete.
        :param theme_id: The ID for the theme that the specified alias is for.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alias_name": alias_name,
            "aws_account_id": aws_account_id,
            "theme_id": theme_id,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''The unique name for the theme alias to delete.'''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the theme alias to delete.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''The ID for the theme that the specified alias is for.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteThemeAliasRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteThemeAliasResponse",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "arn": "arn",
        "request_id": "requestId",
        "status": "status",
        "theme_id": "themeId",
    },
)
class DeleteThemeAliasResponse:
    def __init__(
        self,
        *,
        alias_name: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias_name: The name for the theme alias.
        :param arn: The Amazon Resource Name (ARN) of the theme resource using the deleted alias.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme_id: An ID for the theme associated with the deletion.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if alias_name is not None:
            self._values["alias_name"] = alias_name
        if arn is not None:
            self._values["arn"] = arn
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme_id is not None:
            self._values["theme_id"] = theme_id

    @builtins.property
    def alias_name(self) -> typing.Optional[builtins.str]:
        '''The name for the theme alias.'''
        result = self._values.get("alias_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the theme resource using the deleted alias.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme_id(self) -> typing.Optional[builtins.str]:
        '''An ID for the theme associated with the deletion.'''
        result = self._values.get("theme_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteThemeAliasResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteThemeRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "theme_id": "themeId",
        "version_number": "versionNumber",
    },
)
class DeleteThemeRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
        version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the theme that you're deleting.
        :param theme_id: An ID for the theme that you want to delete.
        :param version_number: The version of the theme that you want to delete. Note: If you don't provide a version number, you're using this call to DeleteTheme to delete all versions of the theme.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "theme_id": theme_id,
        }
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the theme that you're deleting.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''An ID for the theme that you want to delete.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_number(self) -> typing.Optional[jsii.Number]:
        '''The version of the theme that you want to delete.

        Note: If you don't provide a version number, you're using this call to DeleteTheme to delete all versions of the theme.
        '''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteThemeRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteThemeResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "request_id": "requestId",
        "status": "status",
        "theme_id": "themeId",
    },
)
class DeleteThemeResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme_id: An ID for the theme.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme_id is not None:
            self._values["theme_id"] = theme_id

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme_id(self) -> typing.Optional[builtins.str]:
        '''An ID for the theme.'''
        result = self._values.get("theme_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteThemeResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteUserByPrincipalIdRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "principal_id": "principalId",
    },
)
class DeleteUserByPrincipalIdRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        namespace: builtins.str,
        principal_id: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param namespace: The namespace. Currently, you should set this to default.
        :param principal_id: The principal ID of the user.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "namespace": namespace,
            "principal_id": principal_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the user is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_id(self) -> builtins.str:
        '''The principal ID of the user.'''
        result = self._values.get("principal_id")
        assert result is not None, "Required property 'principal_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteUserByPrincipalIdRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteUserByPrincipalIdResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status"},
)
class DeleteUserByPrincipalIdResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteUserByPrincipalIdResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteUserRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "user_name": "userName",
    },
)
class DeleteUserRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        namespace: builtins.str,
        user_name: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param namespace: The namespace. Currently, you should set this to default.
        :param user_name: The name of the user that you want to delete.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "namespace": namespace,
            "user_name": user_name,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the user is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The name of the user that you want to delete.'''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteUserRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DeleteUserResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status"},
)
class DeleteUserResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeleteUserResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeAccountCustomizationRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "resolved": "resolved",
    },
)
class DescribeAccountCustomizationRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
        resolved: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that you want to describe QuickSight customizations for.
        :param namespace: The QuickSight namespace that you want to describe QuickSight customizations for.
        :param resolved: The Resolved flag works with the other parameters to determine which view of QuickSight customizations is returned. You can add this flag to your command to use the same view that QuickSight uses to identify which customizations to apply to the console. Omit this flag, or set it to no-resolved, to reveal customizations that are configured at different levels.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
        }
        if namespace is not None:
            self._values["namespace"] = namespace
        if resolved is not None:
            self._values["resolved"] = resolved

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that you want to describe QuickSight customizations for.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The QuickSight namespace that you want to describe QuickSight customizations for.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolved(self) -> typing.Optional[builtins.bool]:
        '''The Resolved flag works with the other parameters to determine which view of QuickSight customizations is returned.

        You can add this flag to your command to use the same view that QuickSight uses to identify which customizations to apply to the console. Omit this flag, or set it to no-resolved, to reveal customizations that are configured at different levels.
        '''
        result = self._values.get("resolved")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeAccountCustomizationRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeAccountCustomizationResponse",
    jsii_struct_bases=[],
    name_mapping={
        "account_customization": "accountCustomization",
        "arn": "arn",
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeAccountCustomizationResponse:
    def __init__(
        self,
        *,
        account_customization: typing.Optional[AccountCustomization] = None,
        arn: typing.Optional[builtins.str] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param account_customization: The QuickSight customizations that exist in the current AWS Region.
        :param arn: The Amazon Resource Name (ARN) of the customization that's associated with this AWS account.
        :param aws_account_id: The ID for the AWS account that you're describing.
        :param namespace: The QuickSight namespace that you're describing.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(account_customization, dict):
            account_customization = AccountCustomization(**account_customization)
        self._values: typing.Dict[str, typing.Any] = {}
        if account_customization is not None:
            self._values["account_customization"] = account_customization
        if arn is not None:
            self._values["arn"] = arn
        if aws_account_id is not None:
            self._values["aws_account_id"] = aws_account_id
        if namespace is not None:
            self._values["namespace"] = namespace
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def account_customization(self) -> typing.Optional[AccountCustomization]:
        '''The QuickSight customizations that exist in the current AWS Region.'''
        result = self._values.get("account_customization")
        return typing.cast(typing.Optional[AccountCustomization], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the customization that's associated with this AWS account.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the AWS account that you're describing.'''
        result = self._values.get("aws_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The QuickSight namespace that you're describing.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeAccountCustomizationResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeAccountSettingsRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId"},
)
class DescribeAccountSettingsRequest:
    def __init__(self, *, aws_account_id: builtins.str) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that contains the settings that you want to list.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that contains the settings that you want to list.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeAccountSettingsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeAccountSettingsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "account_settings": "accountSettings",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeAccountSettingsResponse:
    def __init__(
        self,
        *,
        account_settings: typing.Optional[AccountSettings] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param account_settings: The QuickSight settings for this AWS account. This information includes the edition of Amazon QuickSight that you subscribed to (Standard or Enterprise) and the notification email for the QuickSight subscription. In the QuickSight console, the QuickSight subscription is sometimes referred to as a QuickSight "account" even though it's technically not an account by itself. Instead, it's a subscription to the QuickSight service for your AWS account. The edition that you subscribe to applies to QuickSight in every AWS Region where you use it.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(account_settings, dict):
            account_settings = AccountSettings(**account_settings)
        self._values: typing.Dict[str, typing.Any] = {}
        if account_settings is not None:
            self._values["account_settings"] = account_settings
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def account_settings(self) -> typing.Optional[AccountSettings]:
        '''The QuickSight settings for this AWS account.

        This information includes the edition of Amazon QuickSight that you subscribed to (Standard or Enterprise) and the notification email for the QuickSight subscription. In the QuickSight console, the QuickSight subscription is sometimes referred to as a QuickSight "account" even though it's technically not an account by itself. Instead, it's a subscription to the QuickSight service for your AWS account. The edition that you subscribe to applies to QuickSight in every AWS Region where you use it.
        '''
        result = self._values.get("account_settings")
        return typing.cast(typing.Optional[AccountSettings], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeAccountSettingsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeAnalysisPermissionsRequest",
    jsii_struct_bases=[],
    name_mapping={"analysis_id": "analysisId", "aws_account_id": "awsAccountId"},
)
class DescribeAnalysisPermissionsRequest:
    def __init__(
        self,
        *,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
    ) -> None:
        '''
        :param analysis_id: The ID of the analysis whose permissions you're describing. The ID is part of the analysis URL.
        :param aws_account_id: The ID of the AWS account that contains the analysis whose permissions you're describing. You must be using the AWS account that the analysis is in.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "analysis_id": analysis_id,
            "aws_account_id": aws_account_id,
        }

    @builtins.property
    def analysis_id(self) -> builtins.str:
        '''The ID of the analysis whose permissions you're describing.

        The ID is part of the analysis URL.
        '''
        result = self._values.get("analysis_id")
        assert result is not None, "Required property 'analysis_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the analysis whose permissions you're describing.

        You must be using the AWS account that the analysis is in.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeAnalysisPermissionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeAnalysisPermissionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_arn": "analysisArn",
        "analysis_id": "analysisId",
        "permissions": "permissions",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeAnalysisPermissionsResponse:
    def __init__(
        self,
        *,
        analysis_arn: typing.Optional[builtins.str] = None,
        analysis_id: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Sequence["ResourcePermission"]] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param analysis_arn: The Amazon Resource Name (ARN) of the analysis whose permissions you're describing.
        :param analysis_id: The ID of the analysis whose permissions you're describing.
        :param permissions: A structure that describes the principals and the resource-level permissions on an analysis.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if analysis_arn is not None:
            self._values["analysis_arn"] = analysis_arn
        if analysis_id is not None:
            self._values["analysis_id"] = analysis_id
        if permissions is not None:
            self._values["permissions"] = permissions
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def analysis_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the analysis whose permissions you're describing.'''
        result = self._values.get("analysis_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def analysis_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the analysis whose permissions you're describing.'''
        result = self._values.get("analysis_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List["ResourcePermission"]]:
        '''A structure that describes the principals and the resource-level permissions on an analysis.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List["ResourcePermission"]], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeAnalysisPermissionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeAnalysisRequest",
    jsii_struct_bases=[],
    name_mapping={"analysis_id": "analysisId", "aws_account_id": "awsAccountId"},
)
class DescribeAnalysisRequest:
    def __init__(
        self,
        *,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
    ) -> None:
        '''
        :param analysis_id: The ID of the analysis that you're describing. The ID is part of the URL of the analysis.
        :param aws_account_id: The ID of the AWS account that contains the analysis. You must be using the AWS account that the analysis is in.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "analysis_id": analysis_id,
            "aws_account_id": aws_account_id,
        }

    @builtins.property
    def analysis_id(self) -> builtins.str:
        '''The ID of the analysis that you're describing.

        The ID is part of the URL of the analysis.
        '''
        result = self._values.get("analysis_id")
        assert result is not None, "Required property 'analysis_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the analysis.

        You must be using the AWS account that the analysis is in.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeAnalysisRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeAnalysisResponse",
    jsii_struct_bases=[],
    name_mapping={
        "analysis": "analysis",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeAnalysisResponse:
    def __init__(
        self,
        *,
        analysis: typing.Optional[Analysis] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param analysis: A metadata structure that contains summary information for the analysis that you're describing.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(analysis, dict):
            analysis = Analysis(**analysis)
        self._values: typing.Dict[str, typing.Any] = {}
        if analysis is not None:
            self._values["analysis"] = analysis
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def analysis(self) -> typing.Optional[Analysis]:
        '''A metadata structure that contains summary information for the analysis that you're describing.'''
        result = self._values.get("analysis")
        return typing.cast(typing.Optional[Analysis], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeAnalysisResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeDashboardPermissionsRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId", "dashboard_id": "dashboardId"},
)
class DescribeDashboardPermissionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the dashboard that you're describing permissions for.
        :param dashboard_id: The ID for the dashboard, also added to the IAM policy.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_id": dashboard_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the dashboard that you're describing permissions for.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        '''The ID for the dashboard, also added to the IAM policy.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeDashboardPermissionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeDashboardPermissionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_arn": "dashboardArn",
        "dashboard_id": "dashboardId",
        "permissions": "permissions",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeDashboardPermissionsResponse:
    def __init__(
        self,
        *,
        dashboard_arn: typing.Optional[builtins.str] = None,
        dashboard_id: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Sequence["ResourcePermission"]] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dashboard_arn: The Amazon Resource Name (ARN) of the dashboard.
        :param dashboard_id: The ID for the dashboard.
        :param permissions: A structure that contains the permissions for the dashboard.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if dashboard_arn is not None:
            self._values["dashboard_arn"] = dashboard_arn
        if dashboard_id is not None:
            self._values["dashboard_id"] = dashboard_id
        if permissions is not None:
            self._values["permissions"] = permissions
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def dashboard_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the dashboard.'''
        result = self._values.get("dashboard_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dashboard_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the dashboard.'''
        result = self._values.get("dashboard_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List["ResourcePermission"]]:
        '''A structure that contains the permissions for the dashboard.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List["ResourcePermission"]], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeDashboardPermissionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeDashboardRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dashboard_id": "dashboardId",
        "alias_name": "aliasName",
        "version_number": "versionNumber",
    },
)
class DescribeDashboardRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
        alias_name: typing.Optional[builtins.str] = None,
        version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the dashboard that you're describing.
        :param dashboard_id: The ID for the dashboard.
        :param alias_name: The alias name.
        :param version_number: The version number for the dashboard. If a version number isn't passed, the latest published dashboard version is described.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_id": dashboard_id,
        }
        if alias_name is not None:
            self._values["alias_name"] = alias_name
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the dashboard that you're describing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        '''The ID for the dashboard.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias_name(self) -> typing.Optional[builtins.str]:
        '''The alias name.'''
        result = self._values.get("alias_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number for the dashboard.

        If a version number isn't passed, the latest published dashboard version is described.
        '''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeDashboardRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeDashboardResponse",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard": "dashboard",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeDashboardResponse:
    def __init__(
        self,
        *,
        dashboard: typing.Optional[Dashboard] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dashboard: Information about the dashboard.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of this request.
        '''
        if isinstance(dashboard, dict):
            dashboard = Dashboard(**dashboard)
        self._values: typing.Dict[str, typing.Any] = {}
        if dashboard is not None:
            self._values["dashboard"] = dashboard
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def dashboard(self) -> typing.Optional[Dashboard]:
        '''Information about the dashboard.'''
        result = self._values.get("dashboard")
        return typing.cast(typing.Optional[Dashboard], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of this request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeDashboardResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeDataSetPermissionsRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId", "data_set_id": "dataSetId"},
)
class DescribeDataSetPermissionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_id: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_set_id: The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_id": data_set_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The ID for the dataset that you want to create.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeDataSetPermissionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeDataSetPermissionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "data_set_arn": "dataSetArn",
        "data_set_id": "dataSetId",
        "permissions": "permissions",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeDataSetPermissionsResponse:
    def __init__(
        self,
        *,
        data_set_arn: typing.Optional[builtins.str] = None,
        data_set_id: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Sequence["ResourcePermission"]] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param data_set_arn: The Amazon Resource Name (ARN) of the dataset.
        :param data_set_id: The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.
        :param permissions: A list of resource permissions on the dataset.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if data_set_arn is not None:
            self._values["data_set_arn"] = data_set_arn
        if data_set_id is not None:
            self._values["data_set_id"] = data_set_id
        if permissions is not None:
            self._values["permissions"] = permissions
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def data_set_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the dataset.'''
        result = self._values.get("data_set_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_set_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the dataset that you want to create.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List["ResourcePermission"]]:
        '''A list of resource permissions on the dataset.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List["ResourcePermission"]], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeDataSetPermissionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeDataSetRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId", "data_set_id": "dataSetId"},
)
class DescribeDataSetRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_id: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_set_id: The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_id": data_set_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The ID for the dataset that you want to create.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeDataSetRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeDataSetResponse",
    jsii_struct_bases=[],
    name_mapping={
        "data_set": "dataSet",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeDataSetResponse:
    def __init__(
        self,
        *,
        data_set: typing.Optional[DataSet] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param data_set: Information on the dataset.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(data_set, dict):
            data_set = DataSet(**data_set)
        self._values: typing.Dict[str, typing.Any] = {}
        if data_set is not None:
            self._values["data_set"] = data_set
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def data_set(self) -> typing.Optional[DataSet]:
        '''Information on the dataset.'''
        result = self._values.get("data_set")
        return typing.cast(typing.Optional[DataSet], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeDataSetResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeDataSourcePermissionsRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId", "data_source_id": "dataSourceId"},
)
class DescribeDataSourcePermissionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_source_id: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_source_id: The ID of the data source. This ID is unique per AWS Region for each AWS account.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_source_id": data_source_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''The ID of the data source.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeDataSourcePermissionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeDataSourcePermissionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "data_source_arn": "dataSourceArn",
        "data_source_id": "dataSourceId",
        "permissions": "permissions",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeDataSourcePermissionsResponse:
    def __init__(
        self,
        *,
        data_source_arn: typing.Optional[builtins.str] = None,
        data_source_id: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Sequence["ResourcePermission"]] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param data_source_arn: The Amazon Resource Name (ARN) of the data source.
        :param data_source_id: The ID of the data source. This ID is unique per AWS Region for each AWS account.
        :param permissions: A list of resource permissions on the data source.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if data_source_arn is not None:
            self._values["data_source_arn"] = data_source_arn
        if data_source_id is not None:
            self._values["data_source_id"] = data_source_id
        if permissions is not None:
            self._values["permissions"] = permissions
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def data_source_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the data source.'''
        result = self._values.get("data_source_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_source_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the data source.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_source_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List["ResourcePermission"]]:
        '''A list of resource permissions on the data source.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List["ResourcePermission"]], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeDataSourcePermissionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeDataSourceRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId", "data_source_id": "dataSourceId"},
)
class DescribeDataSourceRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_source_id: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_source_id: The ID of the data source. This ID is unique per AWS Region for each AWS account.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_source_id": data_source_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''The ID of the data source.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeDataSourceRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeDataSourceResponse",
    jsii_struct_bases=[],
    name_mapping={
        "data_source": "dataSource",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeDataSourceResponse:
    def __init__(
        self,
        *,
        data_source: typing.Optional[DataSource] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param data_source: The information on the data source.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(data_source, dict):
            data_source = DataSource(**data_source)
        self._values: typing.Dict[str, typing.Any] = {}
        if data_source is not None:
            self._values["data_source"] = data_source
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def data_source(self) -> typing.Optional[DataSource]:
        '''The information on the data source.'''
        result = self._values.get("data_source")
        return typing.cast(typing.Optional[DataSource], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeDataSourceResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeGroupRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "group_name": "groupName",
        "namespace": "namespace",
    },
)
class DescribeGroupRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        group_name: builtins.str,
        namespace: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param group_name: The name of the group that you want to describe.
        :param namespace: The namespace. Currently, you should set this to default.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "group_name": group_name,
            "namespace": namespace,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the group is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The name of the group that you want to describe.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeGroupRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeGroupResponse",
    jsii_struct_bases=[],
    name_mapping={"group": "group", "request_id": "requestId", "status": "status"},
)
class DescribeGroupResponse:
    def __init__(
        self,
        *,
        group: typing.Optional["Group"] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group: The name of the group.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(group, dict):
            group = Group(**group)
        self._values: typing.Dict[str, typing.Any] = {}
        if group is not None:
            self._values["group"] = group
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def group(self) -> typing.Optional["Group"]:
        '''The name of the group.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional["Group"], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeGroupResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeIAMPolicyAssignmentRequest",
    jsii_struct_bases=[],
    name_mapping={
        "assignment_name": "assignmentName",
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
    },
)
class DescribeIAMPolicyAssignmentRequest:
    def __init__(
        self,
        *,
        assignment_name: builtins.str,
        aws_account_id: builtins.str,
        namespace: builtins.str,
    ) -> None:
        '''
        :param assignment_name: The name of the assignment, also called a rule.
        :param aws_account_id: The ID of the AWS account that contains the assignment that you want to describe.
        :param namespace: The namespace that contains the assignment.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "assignment_name": assignment_name,
            "aws_account_id": aws_account_id,
            "namespace": namespace,
        }

    @builtins.property
    def assignment_name(self) -> builtins.str:
        '''The name of the assignment, also called a rule.'''
        result = self._values.get("assignment_name")
        assert result is not None, "Required property 'assignment_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the assignment that you want to describe.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace that contains the assignment.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeIAMPolicyAssignmentRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeIAMPolicyAssignmentResponse",
    jsii_struct_bases=[],
    name_mapping={
        "i_am_policy_assignment": "iAMPolicyAssignment",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeIAMPolicyAssignmentResponse:
    def __init__(
        self,
        *,
        i_am_policy_assignment: typing.Optional["IAMPolicyAssignment"] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param i_am_policy_assignment: Information describing the IAM policy assignment.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if i_am_policy_assignment is not None:
            self._values["i_am_policy_assignment"] = i_am_policy_assignment
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def i_am_policy_assignment(self) -> typing.Optional["IAMPolicyAssignment"]:
        '''Information describing the IAM policy assignment.'''
        result = self._values.get("i_am_policy_assignment")
        return typing.cast(typing.Optional["IAMPolicyAssignment"], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeIAMPolicyAssignmentResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeIngestionRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_set_id": "dataSetId",
        "ingestion_id": "ingestionId",
    },
)
class DescribeIngestionRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_id: builtins.str,
        ingestion_id: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_set_id: The ID of the dataset used in the ingestion.
        :param ingestion_id: An ID for the ingestion.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_id": data_set_id,
            "ingestion_id": ingestion_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The ID of the dataset used in the ingestion.'''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ingestion_id(self) -> builtins.str:
        '''An ID for the ingestion.'''
        result = self._values.get("ingestion_id")
        assert result is not None, "Required property 'ingestion_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeIngestionRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeIngestionResponse",
    jsii_struct_bases=[],
    name_mapping={
        "ingestion": "ingestion",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeIngestionResponse:
    def __init__(
        self,
        *,
        ingestion: typing.Optional["Ingestion"] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param ingestion: Information about the ingestion.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(ingestion, dict):
            ingestion = Ingestion(**ingestion)
        self._values: typing.Dict[str, typing.Any] = {}
        if ingestion is not None:
            self._values["ingestion"] = ingestion
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def ingestion(self) -> typing.Optional["Ingestion"]:
        '''Information about the ingestion.'''
        result = self._values.get("ingestion")
        return typing.cast(typing.Optional["Ingestion"], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeIngestionResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeNamespaceRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId", "namespace": "namespace"},
)
class DescribeNamespaceRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        namespace: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that contains the QuickSight namespace that you want to describe.
        :param namespace: The namespace that you want to describe.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "namespace": namespace,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that contains the QuickSight namespace that you want to describe.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace that you want to describe.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeNamespaceRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeNamespaceResponse",
    jsii_struct_bases=[],
    name_mapping={
        "namespace": "namespace",
        "request_id": "requestId",
        "status": "status",
    },
)
class DescribeNamespaceResponse:
    def __init__(
        self,
        *,
        namespace: typing.Optional["NamespaceInfoV2"] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param namespace: The information about the namespace that you're describing. The response includes the namespace ARN, name, AWS Region, creation status, and identity store. DescribeNamespace also works for namespaces that are in the process of being created. For incomplete namespaces, this API operation lists the namespace error types and messages associated with the creation process.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(namespace, dict):
            namespace = NamespaceInfoV2(**namespace)
        self._values: typing.Dict[str, typing.Any] = {}
        if namespace is not None:
            self._values["namespace"] = namespace
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def namespace(self) -> typing.Optional["NamespaceInfoV2"]:
        '''The information about the namespace that you're describing.

        The response includes the namespace ARN, name, AWS Region, creation status, and identity store. DescribeNamespace also works for namespaces that are in the process of being created. For incomplete namespaces, this API operation lists the namespace error types and messages associated with the creation process.
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional["NamespaceInfoV2"], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeNamespaceResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeTemplateAliasRequest",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "aws_account_id": "awsAccountId",
        "template_id": "templateId",
    },
)
class DescribeTemplateAliasRequest:
    def __init__(
        self,
        *,
        alias_name: builtins.str,
        aws_account_id: builtins.str,
        template_id: builtins.str,
    ) -> None:
        '''
        :param alias_name: The name of the template alias that you want to describe. If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter. The keyword $PUBLISHED doesn't apply to templates.
        :param aws_account_id: The ID of the AWS account that contains the template alias that you're describing.
        :param template_id: The ID for the template.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alias_name": alias_name,
            "aws_account_id": aws_account_id,
            "template_id": template_id,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''The name of the template alias that you want to describe.

        If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter. The keyword $PUBLISHED doesn't apply to templates.
        '''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the template alias that you're describing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The ID for the template.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeTemplateAliasRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeTemplateAliasResponse",
    jsii_struct_bases=[],
    name_mapping={
        "request_id": "requestId",
        "status": "status",
        "template_alias": "templateAlias",
    },
)
class DescribeTemplateAliasResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template_alias: typing.Optional["TemplateAlias"] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template_alias: Information about the template alias.
        '''
        if isinstance(template_alias, dict):
            template_alias = TemplateAlias(**template_alias)
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template_alias is not None:
            self._values["template_alias"] = template_alias

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template_alias(self) -> typing.Optional["TemplateAlias"]:
        '''Information about the template alias.'''
        result = self._values.get("template_alias")
        return typing.cast(typing.Optional["TemplateAlias"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeTemplateAliasResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeTemplatePermissionsRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId", "template_id": "templateId"},
)
class DescribeTemplatePermissionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        template_id: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the template that you're describing.
        :param template_id: The ID for the template.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "template_id": template_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the template that you're describing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The ID for the template.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeTemplatePermissionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeTemplatePermissionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "permissions": "permissions",
        "request_id": "requestId",
        "status": "status",
        "template_arn": "templateArn",
        "template_id": "templateId",
    },
)
class DescribeTemplatePermissionsResponse:
    def __init__(
        self,
        *,
        permissions: typing.Optional[typing.Sequence["ResourcePermission"]] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template_arn: typing.Optional[builtins.str] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param permissions: A list of resource permissions to be set on the template.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template_arn: The Amazon Resource Name (ARN) of the template.
        :param template_id: The ID for the template.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if permissions is not None:
            self._values["permissions"] = permissions
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template_arn is not None:
            self._values["template_arn"] = template_arn
        if template_id is not None:
            self._values["template_id"] = template_id

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List["ResourcePermission"]]:
        '''A list of resource permissions to be set on the template.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List["ResourcePermission"]], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the template.'''
        result = self._values.get("template_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the template.'''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeTemplatePermissionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeTemplateRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "template_id": "templateId",
        "alias_name": "aliasName",
        "version_number": "versionNumber",
    },
)
class DescribeTemplateRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        template_id: builtins.str,
        alias_name: typing.Optional[builtins.str] = None,
        version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the template that you're describing.
        :param template_id: The ID for the template.
        :param alias_name: The alias of the template that you want to describe. If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter. The keyword $PUBLISHED doesn't apply to templates.
        :param version_number: (Optional) The number for the version to describe. If a VersionNumber parameter value isn't provided, the latest version of the template is described.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "template_id": template_id,
        }
        if alias_name is not None:
            self._values["alias_name"] = alias_name
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the template that you're describing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The ID for the template.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias_name(self) -> typing.Optional[builtins.str]:
        '''The alias of the template that you want to describe.

        If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter. The keyword $PUBLISHED doesn't apply to templates.
        '''
        result = self._values.get("alias_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_number(self) -> typing.Optional[jsii.Number]:
        '''(Optional) The number for the version to describe.

        If a VersionNumber parameter value isn't provided, the latest version of the template is described.
        '''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeTemplateRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeTemplateResponse",
    jsii_struct_bases=[],
    name_mapping={
        "request_id": "requestId",
        "status": "status",
        "template": "template",
    },
)
class DescribeTemplateResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template: typing.Optional["Template"] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template: The template structure for the object you want to describe.
        '''
        if isinstance(template, dict):
            template = Template(**template)
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template is not None:
            self._values["template"] = template

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template(self) -> typing.Optional["Template"]:
        '''The template structure for the object you want to describe.'''
        result = self._values.get("template")
        return typing.cast(typing.Optional["Template"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeTemplateResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeThemeAliasRequest",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "aws_account_id": "awsAccountId",
        "theme_id": "themeId",
    },
)
class DescribeThemeAliasRequest:
    def __init__(
        self,
        *,
        alias_name: builtins.str,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
    ) -> None:
        '''
        :param alias_name: The name of the theme alias that you want to describe.
        :param aws_account_id: The ID of the AWS account that contains the theme alias that you're describing.
        :param theme_id: The ID for the theme.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alias_name": alias_name,
            "aws_account_id": aws_account_id,
            "theme_id": theme_id,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''The name of the theme alias that you want to describe.'''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the theme alias that you're describing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''The ID for the theme.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeThemeAliasRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeThemeAliasResponse",
    jsii_struct_bases=[],
    name_mapping={
        "request_id": "requestId",
        "status": "status",
        "theme_alias": "themeAlias",
    },
)
class DescribeThemeAliasResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme_alias: typing.Optional["ThemeAlias"] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme_alias: Information about the theme alias.
        '''
        if isinstance(theme_alias, dict):
            theme_alias = ThemeAlias(**theme_alias)
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme_alias is not None:
            self._values["theme_alias"] = theme_alias

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme_alias(self) -> typing.Optional["ThemeAlias"]:
        '''Information about the theme alias.'''
        result = self._values.get("theme_alias")
        return typing.cast(typing.Optional["ThemeAlias"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeThemeAliasResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeThemePermissionsRequest",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId", "theme_id": "themeId"},
)
class DescribeThemePermissionsRequest:
    def __init__(self, *, aws_account_id: builtins.str, theme_id: builtins.str) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the theme that you're describing.
        :param theme_id: The ID for the theme that you want to describe permissions for.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "theme_id": theme_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the theme that you're describing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''The ID for the theme that you want to describe permissions for.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeThemePermissionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeThemePermissionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "permissions": "permissions",
        "request_id": "requestId",
        "status": "status",
        "theme_arn": "themeArn",
        "theme_id": "themeId",
    },
)
class DescribeThemePermissionsResponse:
    def __init__(
        self,
        *,
        permissions: typing.Optional[typing.Sequence["ResourcePermission"]] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme_arn: typing.Optional[builtins.str] = None,
        theme_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param permissions: A list of resource permissions set on the theme.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme_arn: The Amazon Resource Name (ARN) of the theme.
        :param theme_id: The ID for the theme.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if permissions is not None:
            self._values["permissions"] = permissions
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn
        if theme_id is not None:
            self._values["theme_id"] = theme_id

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List["ResourcePermission"]]:
        '''A list of resource permissions set on the theme.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List["ResourcePermission"]], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the theme.'''
        result = self._values.get("theme_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def theme_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the theme.'''
        result = self._values.get("theme_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeThemePermissionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeThemeRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "theme_id": "themeId",
        "alias_name": "aliasName",
        "version_number": "versionNumber",
    },
)
class DescribeThemeRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
        alias_name: typing.Optional[builtins.str] = None,
        version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the theme that you're describing.
        :param theme_id: The ID for the theme.
        :param alias_name: The alias of the theme that you want to describe. If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the theme by providing the keyword $LATEST in the AliasName parameter. The keyword $PUBLISHED doesn't apply to themes.
        :param version_number: The version number for the version to describe. If a VersionNumber parameter value isn't provided, the latest version of the theme is described.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "theme_id": theme_id,
        }
        if alias_name is not None:
            self._values["alias_name"] = alias_name
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the theme that you're describing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''The ID for the theme.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias_name(self) -> typing.Optional[builtins.str]:
        '''The alias of the theme that you want to describe.

        If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the theme by providing the keyword $LATEST in the AliasName parameter. The keyword $PUBLISHED doesn't apply to themes.
        '''
        result = self._values.get("alias_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number for the version to describe.

        If a VersionNumber parameter value isn't provided, the latest version of the theme is described.
        '''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeThemeRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeThemeResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status", "theme": "theme"},
)
class DescribeThemeResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme: typing.Optional["Theme"] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme: The information about the theme that you are describing.
        '''
        if isinstance(theme, dict):
            theme = Theme(**theme)
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme is not None:
            self._values["theme"] = theme

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme(self) -> typing.Optional["Theme"]:
        '''The information about the theme that you are describing.'''
        result = self._values.get("theme")
        return typing.cast(typing.Optional["Theme"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeThemeResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeUserRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "user_name": "userName",
    },
)
class DescribeUserRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        namespace: builtins.str,
        user_name: builtins.str,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param namespace: The namespace. Currently, you should set this to default.
        :param user_name: The name of the user that you want to describe.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "namespace": namespace,
            "user_name": user_name,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the user is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The name of the user that you want to describe.'''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeUserRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DescribeUserResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status", "user": "user"},
)
class DescribeUserResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        user: typing.Optional["User"] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param user: The user name.
        '''
        if isinstance(user, dict):
            user = User(**user)
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user(self) -> typing.Optional["User"]:
        '''The user name.'''
        result = self._values.get("user")
        return typing.cast(typing.Optional["User"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DescribeUserResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ErrorInfo",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "type": "type"},
)
class ErrorInfo:
    def __init__(
        self,
        *,
        message: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: Error message.
        :param type: Error type.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Error message.'''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Error type.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ErrorInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ExportToCSVOption",
    jsii_struct_bases=[],
    name_mapping={"availability_status": "availabilityStatus"},
)
class ExportToCSVOption:
    def __init__(
        self,
        *,
        availability_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability_status: Availability status.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if availability_status is not None:
            self._values["availability_status"] = availability_status

    @builtins.property
    def availability_status(self) -> typing.Optional[builtins.str]:
        '''Availability status.'''
        result = self._values.get("availability_status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExportToCSVOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.FieldFolder",
    jsii_struct_bases=[],
    name_mapping={"columns": "columns", "description": "description"},
)
class FieldFolder:
    def __init__(
        self,
        *,
        columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param columns: A folder has a list of columns. A column can only be in one folder.
        :param description: The description for a field folder.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if columns is not None:
            self._values["columns"] = columns
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def columns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A folder has a list of columns.

        A column can only be in one folder.
        '''
        result = self._values.get("columns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for a field folder.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FieldFolder(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.FilterOperation",
    jsii_struct_bases=[],
    name_mapping={"condition_expression": "conditionExpression"},
)
class FilterOperation:
    def __init__(self, *, condition_expression: builtins.str) -> None:
        '''
        :param condition_expression: An expression that must evaluate to a Boolean value. Rows for which the expression evaluates to true are kept in the dataset.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "condition_expression": condition_expression,
        }

    @builtins.property
    def condition_expression(self) -> builtins.str:
        '''An expression that must evaluate to a Boolean value.

        Rows for which the expression evaluates to true are kept in the dataset.
        '''
        result = self._values.get("condition_expression")
        assert result is not None, "Required property 'condition_expression' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FilterOperation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.GeoSpatialColumnGroup",
    jsii_struct_bases=[],
    name_mapping={"columns": "columns", "country_code": "countryCode", "name": "name"},
)
class GeoSpatialColumnGroup:
    def __init__(
        self,
        *,
        columns: typing.Sequence[builtins.str],
        country_code: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param columns: Columns in this hierarchy.
        :param country_code: Country code.
        :param name: A display name for the hierarchy.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "columns": columns,
            "country_code": country_code,
            "name": name,
        }

    @builtins.property
    def columns(self) -> typing.List[builtins.str]:
        '''Columns in this hierarchy.'''
        result = self._values.get("columns")
        assert result is not None, "Required property 'columns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def country_code(self) -> builtins.str:
        '''Country code.'''
        result = self._values.get("country_code")
        assert result is not None, "Required property 'country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A display name for the hierarchy.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GeoSpatialColumnGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.GetDashboardEmbedUrlRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dashboard_id": "dashboardId",
        "identity_type": "identityType",
        "additional_dashboard_ids": "additionalDashboardIds",
        "namespace": "namespace",
        "reset_disabled": "resetDisabled",
        "session_lifetime_in_minutes": "sessionLifetimeInMinutes",
        "state_persistence_enabled": "statePersistenceEnabled",
        "undo_redo_disabled": "undoRedoDisabled",
        "user_arn": "userArn",
    },
)
class GetDashboardEmbedUrlRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
        identity_type: builtins.str,
        additional_dashboard_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        reset_disabled: typing.Optional[builtins.bool] = None,
        session_lifetime_in_minutes: typing.Optional[jsii.Number] = None,
        state_persistence_enabled: typing.Optional[builtins.bool] = None,
        undo_redo_disabled: typing.Optional[builtins.bool] = None,
        user_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that contains the dashboard that you're embedding.
        :param dashboard_id: The ID for the dashboard, also added to the AWS Identity and Access Management (IAM) policy.
        :param identity_type: The authentication method that the user uses to sign in.
        :param additional_dashboard_ids: A list of one or more dashboard IDs that you want to add to a session that includes anonymous users. The IdentityType parameter must be set to ANONYMOUS for this to work, because other identity types authenticate as QuickSight or IAM users. For example, if you set "--dashboard-id dash_id1 --dashboard-id dash_id2 dash_id3 identity-type ANONYMOUS", the session can access all three dashboards.
        :param namespace: The QuickSight namespace that contains the dashboard IDs in this request. If you're not using a custom namespace, set this to "default".
        :param reset_disabled: Remove the reset button on the embedded dashboard. The default is FALSE, which enables the reset button.
        :param session_lifetime_in_minutes: How many minutes the session is valid. The session lifetime must be 15-600 minutes.
        :param state_persistence_enabled: Adds persistence of state for the user session in an embedded dashboard. Persistence applies to the sheet and the parameter settings. These are control settings that the dashboard subscriber (QuickSight reader) chooses while viewing the dashboard. If this is set to TRUE, the settings are the same when the subscriber reopens the same dashboard URL. The state is stored in QuickSight, not in a browser cookie. If this is set to FALSE, the state of the user session is not persisted. The default is FALSE.
        :param undo_redo_disabled: Remove the undo/redo button on the embedded dashboard. The default is FALSE, which enables the undo/redo button.
        :param user_arn: The Amazon QuickSight user's Amazon Resource Name (ARN), for use with QUICKSIGHT identity type. You can use this for any Amazon QuickSight users in your account (readers, authors, or admins) authenticated as one of the following: Active Directory (AD) users or group members Invited nonfederated users IAM users and IAM role-based sessions authenticated through Federated Single Sign-On using SAML, OpenID Connect, or IAM federation. Omit this parameter for users in the third group – IAM users and IAM role-based sessions.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_id": dashboard_id,
            "identity_type": identity_type,
        }
        if additional_dashboard_ids is not None:
            self._values["additional_dashboard_ids"] = additional_dashboard_ids
        if namespace is not None:
            self._values["namespace"] = namespace
        if reset_disabled is not None:
            self._values["reset_disabled"] = reset_disabled
        if session_lifetime_in_minutes is not None:
            self._values["session_lifetime_in_minutes"] = session_lifetime_in_minutes
        if state_persistence_enabled is not None:
            self._values["state_persistence_enabled"] = state_persistence_enabled
        if undo_redo_disabled is not None:
            self._values["undo_redo_disabled"] = undo_redo_disabled
        if user_arn is not None:
            self._values["user_arn"] = user_arn

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that contains the dashboard that you're embedding.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        '''The ID for the dashboard, also added to the AWS Identity and Access Management (IAM) policy.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_type(self) -> builtins.str:
        '''The authentication method that the user uses to sign in.'''
        result = self._values.get("identity_type")
        assert result is not None, "Required property 'identity_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_dashboard_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of one or more dashboard IDs that you want to add to a session that includes anonymous users.

        The IdentityType parameter must be set to ANONYMOUS for this to work, because other identity types authenticate as QuickSight or IAM users. For example, if you set "--dashboard-id dash_id1 --dashboard-id dash_id2 dash_id3 identity-type ANONYMOUS", the session can access all three dashboards.
        '''
        result = self._values.get("additional_dashboard_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The QuickSight namespace that contains the dashboard IDs in this request.

        If you're not using a custom namespace, set this to "default".
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reset_disabled(self) -> typing.Optional[builtins.bool]:
        '''Remove the reset button on the embedded dashboard.

        The default is FALSE, which enables the reset button.
        '''
        result = self._values.get("reset_disabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def session_lifetime_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''How many minutes the session is valid.

        The session lifetime must be 15-600 minutes.
        '''
        result = self._values.get("session_lifetime_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def state_persistence_enabled(self) -> typing.Optional[builtins.bool]:
        '''Adds persistence of state for the user session in an embedded dashboard.

        Persistence applies to the sheet and the parameter settings. These are control settings that the dashboard subscriber (QuickSight reader) chooses while viewing the dashboard. If this is set to TRUE, the settings are the same when the subscriber reopens the same dashboard URL. The state is stored in QuickSight, not in a browser cookie. If this is set to FALSE, the state of the user session is not persisted. The default is FALSE.
        '''
        result = self._values.get("state_persistence_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def undo_redo_disabled(self) -> typing.Optional[builtins.bool]:
        '''Remove the undo/redo button on the embedded dashboard.

        The default is FALSE, which enables the undo/redo button.
        '''
        result = self._values.get("undo_redo_disabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def user_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon QuickSight user's Amazon Resource Name (ARN), for use with QUICKSIGHT identity type.

        You can use this for any Amazon QuickSight users in your account (readers, authors, or admins) authenticated as one of the following:   Active Directory (AD) users or group members   Invited nonfederated users   IAM users and IAM role-based sessions authenticated through Federated Single Sign-On using SAML, OpenID Connect, or IAM federation.   Omit this parameter for users in the third group – IAM users and IAM role-based sessions.
        '''
        result = self._values.get("user_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GetDashboardEmbedUrlRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.GetDashboardEmbedUrlResponse",
    jsii_struct_bases=[],
    name_mapping={
        "embed_url": "embedUrl",
        "request_id": "requestId",
        "status": "status",
    },
)
class GetDashboardEmbedUrlResponse:
    def __init__(
        self,
        *,
        embed_url: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param embed_url: A single-use URL that you can put into your server-side webpage to embed your dashboard. This URL is valid for 5 minutes. The API operation provides the URL with an auth_code value that enables one (and only one) sign-on to a user session that is valid for 10 hours.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if embed_url is not None:
            self._values["embed_url"] = embed_url
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def embed_url(self) -> typing.Optional[builtins.str]:
        '''A single-use URL that you can put into your server-side webpage to embed your dashboard.

        This URL is valid for 5 minutes. The API operation provides the URL with an auth_code value that enables one (and only one) sign-on to a user session that is valid for 10 hours.
        '''
        result = self._values.get("embed_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GetDashboardEmbedUrlResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.GetSessionEmbedUrlRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "entry_point": "entryPoint",
        "session_lifetime_in_minutes": "sessionLifetimeInMinutes",
        "user_arn": "userArn",
    },
)
class GetSessionEmbedUrlRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        entry_point: typing.Optional[builtins.str] = None,
        session_lifetime_in_minutes: typing.Optional[jsii.Number] = None,
        user_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account associated with your QuickSight subscription.
        :param entry_point: The URL you use to access the embedded session. The entry point URL is constrained to the following paths: /start /start/analyses /start/dashboards /start/favorites /dashboards/DashboardId - where DashboardId is the actual ID key from the QuickSight console URL of the dashboard /analyses/AnalysisId - where AnalysisId is the actual ID key from the QuickSight console URL of the analysis
        :param session_lifetime_in_minutes: How many minutes the session is valid. The session lifetime must be 15-600 minutes.
        :param user_arn: The Amazon QuickSight user's Amazon Resource Name (ARN), for use with QUICKSIGHT identity type. You can use this for any type of Amazon QuickSight users in your account (readers, authors, or admins). They need to be authenticated as one of the following: Active Directory (AD) users or group members Invited nonfederated users AWS Identity and Access Management (IAM) users and IAM role-based sessions authenticated through Federated Single Sign-On using SAML, OpenID Connect, or IAM federation Omit this parameter for users in the third group, IAM users and IAM role-based sessions.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
        }
        if entry_point is not None:
            self._values["entry_point"] = entry_point
        if session_lifetime_in_minutes is not None:
            self._values["session_lifetime_in_minutes"] = session_lifetime_in_minutes
        if user_arn is not None:
            self._values["user_arn"] = user_arn

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account associated with your QuickSight subscription.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entry_point(self) -> typing.Optional[builtins.str]:
        '''The URL you use to access the embedded session.

        The entry point URL is constrained to the following paths:    /start     /start/analyses     /start/dashboards     /start/favorites     /dashboards/DashboardId  - where DashboardId is the actual ID key from the QuickSight console URL of the dashboard    /analyses/AnalysisId  - where AnalysisId is the actual ID key from the QuickSight console URL of the analysis
        '''
        result = self._values.get("entry_point")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_lifetime_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''How many minutes the session is valid.

        The session lifetime must be 15-600 minutes.
        '''
        result = self._values.get("session_lifetime_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon QuickSight user's Amazon Resource Name (ARN), for use with QUICKSIGHT identity type.

        You can use this for any type of Amazon QuickSight users in your account (readers, authors, or admins). They need to be authenticated as one of the following:   Active Directory (AD) users or group members   Invited nonfederated users   AWS Identity and Access Management (IAM) users and IAM role-based sessions authenticated through Federated Single Sign-On using SAML, OpenID Connect, or IAM federation   Omit this parameter for users in the third group, IAM users and IAM role-based sessions.
        '''
        result = self._values.get("user_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GetSessionEmbedUrlRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.GetSessionEmbedUrlResponse",
    jsii_struct_bases=[],
    name_mapping={
        "embed_url": "embedUrl",
        "request_id": "requestId",
        "status": "status",
    },
)
class GetSessionEmbedUrlResponse:
    def __init__(
        self,
        *,
        embed_url: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param embed_url: A single-use URL that you can put into your server-side web page to embed your QuickSight session. This URL is valid for 5 minutes. The API operation provides the URL with an auth_code value that enables one (and only one) sign-on to a user session that is valid for 10 hours.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if embed_url is not None:
            self._values["embed_url"] = embed_url
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def embed_url(self) -> typing.Optional[builtins.str]:
        '''A single-use URL that you can put into your server-side web page to embed your QuickSight session.

        This URL is valid for 5 minutes. The API operation provides the URL with an auth_code value that enables one (and only one) sign-on to a user session that is valid for 10 hours.
        '''
        result = self._values.get("embed_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GetSessionEmbedUrlResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.Group",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "description": "description",
        "group_name": "groupName",
        "principal_id": "principalId",
    },
)
class Group:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        group_name: typing.Optional[builtins.str] = None,
        principal_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) for the group.
        :param description: The group description.
        :param group_name: The name of the group.
        :param principal_id: The principal ID of the group.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if description is not None:
            self._values["description"] = description
        if group_name is not None:
            self._values["group_name"] = group_name
        if principal_id is not None:
            self._values["principal_id"] = principal_id

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the group.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The group description.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the group.'''
        result = self._values.get("group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def principal_id(self) -> typing.Optional[builtins.str]:
        '''The principal ID of the group.'''
        result = self._values.get("principal_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Group(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.GroupMember",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "member_name": "memberName"},
)
class GroupMember:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        member_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) for the group member (user).
        :param member_name: The name of the group member (user).
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if member_name is not None:
            self._values["member_name"] = member_name

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the group member (user).'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def member_name(self) -> typing.Optional[builtins.str]:
        '''The name of the group member (user).'''
        result = self._values.get("member_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupMember(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.GutterStyle",
    jsii_struct_bases=[],
    name_mapping={"show": "show"},
)
class GutterStyle:
    def __init__(self, *, show: typing.Optional[builtins.bool] = None) -> None:
        '''
        :param show: This Boolean value controls whether to display a gutter space between sheet tiles.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if show is not None:
            self._values["show"] = show

    @builtins.property
    def show(self) -> typing.Optional[builtins.bool]:
        '''This Boolean value controls whether to display a gutter space between sheet tiles.'''
        result = self._values.get("show")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GutterStyle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="cdk-quicksight-constructs.IAMPolicyAssignment")
class IAMPolicyAssignment(typing_extensions.Protocol):
    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IAMPolicyAssignmentProxy"]:
        return _IAMPolicyAssignmentProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assignmentId")
    def assignment_id(self) -> typing.Optional[builtins.str]:
        '''Assignment ID.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assignmentName")
    def assignment_name(self) -> typing.Optional[builtins.str]:
        '''Assignment name.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assignmentStatus")
    def assignment_status(self) -> typing.Optional[builtins.str]:
        '''Assignment status.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identities")
    def identities(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]]:
        '''Identities.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policyArn")
    def policy_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the IAM policy.'''
        ...


class _IAMPolicyAssignmentProxy:
    __jsii_type__: typing.ClassVar[str] = "cdk-quicksight-constructs.IAMPolicyAssignment"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assignmentId")
    def assignment_id(self) -> typing.Optional[builtins.str]:
        '''Assignment ID.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assignmentId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assignmentName")
    def assignment_name(self) -> typing.Optional[builtins.str]:
        '''Assignment name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assignmentName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assignmentStatus")
    def assignment_status(self) -> typing.Optional[builtins.str]:
        '''Assignment status.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assignmentStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsAccountId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identities")
    def identities(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]]:
        '''Identities.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]], jsii.get(self, "identities"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policyArn")
    def policy_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the IAM policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyArn"))


@jsii.interface(jsii_type="cdk-quicksight-constructs.IAMPolicyAssignmentSummary")
class IAMPolicyAssignmentSummary(typing_extensions.Protocol):
    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IAMPolicyAssignmentSummaryProxy"]:
        return _IAMPolicyAssignmentSummaryProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assignmentName")
    def assignment_name(self) -> typing.Optional[builtins.str]:
        '''Assignment name.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assignmentStatus")
    def assignment_status(self) -> typing.Optional[builtins.str]:
        '''Assignment status.'''
        ...


class _IAMPolicyAssignmentSummaryProxy:
    __jsii_type__: typing.ClassVar[str] = "cdk-quicksight-constructs.IAMPolicyAssignmentSummary"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assignmentName")
    def assignment_name(self) -> typing.Optional[builtins.str]:
        '''Assignment name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assignmentName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assignmentStatus")
    def assignment_status(self) -> typing.Optional[builtins.str]:
        '''Assignment status.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assignmentStatus"))


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.Ingestion",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "created_time": "createdTime",
        "ingestion_status": "ingestionStatus",
        "error_info": "errorInfo",
        "ingestion_id": "ingestionId",
        "ingestion_size_in_bytes": "ingestionSizeInBytes",
        "ingestion_time_in_seconds": "ingestionTimeInSeconds",
        "queue_info": "queueInfo",
        "request_source": "requestSource",
        "request_type": "requestType",
        "row_info": "rowInfo",
    },
)
class Ingestion:
    def __init__(
        self,
        *,
        arn: builtins.str,
        created_time: datetime.datetime,
        ingestion_status: builtins.str,
        error_info: typing.Optional[ErrorInfo] = None,
        ingestion_id: typing.Optional[builtins.str] = None,
        ingestion_size_in_bytes: typing.Optional[jsii.Number] = None,
        ingestion_time_in_seconds: typing.Optional[jsii.Number] = None,
        queue_info: typing.Optional["QueueInfo"] = None,
        request_source: typing.Optional[builtins.str] = None,
        request_type: typing.Optional[builtins.str] = None,
        row_info: typing.Optional["RowInfo"] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param created_time: The time that this ingestion started.
        :param ingestion_status: Ingestion status.
        :param error_info: Error information for this ingestion.
        :param ingestion_id: Ingestion ID.
        :param ingestion_size_in_bytes: The size of the data ingested, in bytes.
        :param ingestion_time_in_seconds: The time that this ingestion took, measured in seconds.
        :param queue_info: 
        :param request_source: Event source for this ingestion.
        :param request_type: Type of this ingestion.
        :param row_info: 
        '''
        if isinstance(error_info, dict):
            error_info = ErrorInfo(**error_info)
        if isinstance(queue_info, dict):
            queue_info = QueueInfo(**queue_info)
        if isinstance(row_info, dict):
            row_info = RowInfo(**row_info)
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
            "created_time": created_time,
            "ingestion_status": ingestion_status,
        }
        if error_info is not None:
            self._values["error_info"] = error_info
        if ingestion_id is not None:
            self._values["ingestion_id"] = ingestion_id
        if ingestion_size_in_bytes is not None:
            self._values["ingestion_size_in_bytes"] = ingestion_size_in_bytes
        if ingestion_time_in_seconds is not None:
            self._values["ingestion_time_in_seconds"] = ingestion_time_in_seconds
        if queue_info is not None:
            self._values["queue_info"] = queue_info
        if request_source is not None:
            self._values["request_source"] = request_source
        if request_type is not None:
            self._values["request_type"] = request_type
        if row_info is not None:
            self._values["row_info"] = row_info

    @builtins.property
    def arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def created_time(self) -> datetime.datetime:
        '''The time that this ingestion started.'''
        result = self._values.get("created_time")
        assert result is not None, "Required property 'created_time' is missing"
        return typing.cast(datetime.datetime, result)

    @builtins.property
    def ingestion_status(self) -> builtins.str:
        '''Ingestion status.'''
        result = self._values.get("ingestion_status")
        assert result is not None, "Required property 'ingestion_status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_info(self) -> typing.Optional[ErrorInfo]:
        '''Error information for this ingestion.'''
        result = self._values.get("error_info")
        return typing.cast(typing.Optional[ErrorInfo], result)

    @builtins.property
    def ingestion_id(self) -> typing.Optional[builtins.str]:
        '''Ingestion ID.'''
        result = self._values.get("ingestion_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingestion_size_in_bytes(self) -> typing.Optional[jsii.Number]:
        '''The size of the data ingested, in bytes.'''
        result = self._values.get("ingestion_size_in_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ingestion_time_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time that this ingestion took, measured in seconds.'''
        result = self._values.get("ingestion_time_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def queue_info(self) -> typing.Optional["QueueInfo"]:
        result = self._values.get("queue_info")
        return typing.cast(typing.Optional["QueueInfo"], result)

    @builtins.property
    def request_source(self) -> typing.Optional[builtins.str]:
        '''Event source for this ingestion.'''
        result = self._values.get("request_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_type(self) -> typing.Optional[builtins.str]:
        '''Type of this ingestion.'''
        result = self._values.get("request_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def row_info(self) -> typing.Optional["RowInfo"]:
        result = self._values.get("row_info")
        return typing.cast(typing.Optional["RowInfo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ingestion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.InputColumn",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class InputColumn:
    def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
        '''
        :param name: The name of this column in the underlying data source.
        :param type: The data type of the column.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of this column in the underlying data source.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The data type of the column.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InputColumn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.IntegerParameter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class IntegerParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param name: The name of the integer parameter.
        :param values: The values for the integer parameter.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the integer parameter.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[jsii.Number]:
        '''The values for the integer parameter.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegerParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.JiraParameters",
    jsii_struct_bases=[],
    name_mapping={"site_base_url": "siteBaseUrl"},
)
class JiraParameters:
    def __init__(self, *, site_base_url: builtins.str) -> None:
        '''
        :param site_base_url: The base URL of the Jira site.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "site_base_url": site_base_url,
        }

    @builtins.property
    def site_base_url(self) -> builtins.str:
        '''The base URL of the Jira site.'''
        result = self._values.get("site_base_url")
        assert result is not None, "Required property 'site_base_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JiraParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.JoinInstruction",
    jsii_struct_bases=[],
    name_mapping={
        "left_operand": "leftOperand",
        "on_clause": "onClause",
        "right_operand": "rightOperand",
        "type": "type",
        "left_join_key_properties": "leftJoinKeyProperties",
        "right_join_key_properties": "rightJoinKeyProperties",
    },
)
class JoinInstruction:
    def __init__(
        self,
        *,
        left_operand: builtins.str,
        on_clause: builtins.str,
        right_operand: builtins.str,
        type: builtins.str,
        left_join_key_properties: typing.Optional["JoinKeyProperties"] = None,
        right_join_key_properties: typing.Optional["JoinKeyProperties"] = None,
    ) -> None:
        '''
        :param left_operand: The operand on the left side of a join.
        :param on_clause: The join instructions provided in the ON clause of a join.
        :param right_operand: The operand on the right side of a join.
        :param type: The type of join that it is.
        :param left_join_key_properties: Join key properties of the left operand.
        :param right_join_key_properties: Join key properties of the right operand.
        '''
        if isinstance(left_join_key_properties, dict):
            left_join_key_properties = JoinKeyProperties(**left_join_key_properties)
        if isinstance(right_join_key_properties, dict):
            right_join_key_properties = JoinKeyProperties(**right_join_key_properties)
        self._values: typing.Dict[str, typing.Any] = {
            "left_operand": left_operand,
            "on_clause": on_clause,
            "right_operand": right_operand,
            "type": type,
        }
        if left_join_key_properties is not None:
            self._values["left_join_key_properties"] = left_join_key_properties
        if right_join_key_properties is not None:
            self._values["right_join_key_properties"] = right_join_key_properties

    @builtins.property
    def left_operand(self) -> builtins.str:
        '''The operand on the left side of a join.'''
        result = self._values.get("left_operand")
        assert result is not None, "Required property 'left_operand' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def on_clause(self) -> builtins.str:
        '''The join instructions provided in the ON clause of a join.'''
        result = self._values.get("on_clause")
        assert result is not None, "Required property 'on_clause' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def right_operand(self) -> builtins.str:
        '''The operand on the right side of a join.'''
        result = self._values.get("right_operand")
        assert result is not None, "Required property 'right_operand' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of join that it is.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def left_join_key_properties(self) -> typing.Optional["JoinKeyProperties"]:
        '''Join key properties of the left operand.'''
        result = self._values.get("left_join_key_properties")
        return typing.cast(typing.Optional["JoinKeyProperties"], result)

    @builtins.property
    def right_join_key_properties(self) -> typing.Optional["JoinKeyProperties"]:
        '''Join key properties of the right operand.'''
        result = self._values.get("right_join_key_properties")
        return typing.cast(typing.Optional["JoinKeyProperties"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JoinInstruction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.JoinKeyProperties",
    jsii_struct_bases=[],
    name_mapping={"unique_key": "uniqueKey"},
)
class JoinKeyProperties:
    def __init__(self, *, unique_key: typing.Optional[builtins.bool] = None) -> None:
        '''
        :param unique_key: A value that indicates that a row in a table is uniquely identified by the columns in a join key. This is used by QuickSight to optimize query performance.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if unique_key is not None:
            self._values["unique_key"] = unique_key

    @builtins.property
    def unique_key(self) -> typing.Optional[builtins.bool]:
        '''A value that indicates that a row in a table is uniquely identified by the columns in a join key.

        This is used by QuickSight to optimize query performance.
        '''
        result = self._values.get("unique_key")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JoinKeyProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListAnalysesRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListAnalysesRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the analyses.
        :param max_results: The maximum number of results to return.
        :param next_token: A pagination token that can be used in a subsequent request.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the analyses.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to return.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListAnalysesRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListAnalysesResponse",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_summary_list": "analysisSummaryList",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class ListAnalysesResponse:
    def __init__(
        self,
        *,
        analysis_summary_list: typing.Optional[typing.Sequence[AnalysisSummary]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param analysis_summary_list: Metadata describing each of the analyses that are listed.
        :param next_token: A pagination token that can be used in a subsequent request.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if analysis_summary_list is not None:
            self._values["analysis_summary_list"] = analysis_summary_list
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def analysis_summary_list(self) -> typing.Optional[typing.List[AnalysisSummary]]:
        '''Metadata describing each of the analyses that are listed.'''
        result = self._values.get("analysis_summary_list")
        return typing.cast(typing.Optional[typing.List[AnalysisSummary]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListAnalysesResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListDashboardVersionsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dashboard_id": "dashboardId",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListDashboardVersionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the dashboard that you're listing versions for.
        :param dashboard_id: The ID for the dashboard.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_id": dashboard_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the dashboard that you're listing versions for.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        '''The ID for the dashboard.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListDashboardVersionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListDashboardVersionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_version_summary_list": "dashboardVersionSummaryList",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class ListDashboardVersionsResponse:
    def __init__(
        self,
        *,
        dashboard_version_summary_list: typing.Optional[typing.Sequence[DashboardVersionSummary]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dashboard_version_summary_list: A structure that contains information about each version of the dashboard.
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if dashboard_version_summary_list is not None:
            self._values["dashboard_version_summary_list"] = dashboard_version_summary_list
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def dashboard_version_summary_list(
        self,
    ) -> typing.Optional[typing.List[DashboardVersionSummary]]:
        '''A structure that contains information about each version of the dashboard.'''
        result = self._values.get("dashboard_version_summary_list")
        return typing.cast(typing.Optional[typing.List[DashboardVersionSummary]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListDashboardVersionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListDashboardsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListDashboardsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the dashboards that you're listing.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the dashboards that you're listing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListDashboardsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListDashboardsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_summary_list": "dashboardSummaryList",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class ListDashboardsResponse:
    def __init__(
        self,
        *,
        dashboard_summary_list: typing.Optional[typing.Sequence[DashboardSummary]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dashboard_summary_list: A structure that contains all of the dashboards in your AWS account. This structure provides basic information about the dashboards.
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if dashboard_summary_list is not None:
            self._values["dashboard_summary_list"] = dashboard_summary_list
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def dashboard_summary_list(self) -> typing.Optional[typing.List[DashboardSummary]]:
        '''A structure that contains all of the dashboards in your AWS account.

        This structure provides basic information about the dashboards.
        '''
        result = self._values.get("dashboard_summary_list")
        return typing.cast(typing.Optional[typing.List[DashboardSummary]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListDashboardsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListDataSetsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListDataSetsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListDataSetsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListDataSetsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "data_set_summaries": "dataSetSummaries",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class ListDataSetsResponse:
    def __init__(
        self,
        *,
        data_set_summaries: typing.Optional[typing.Sequence[DataSetSummary]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param data_set_summaries: The list of dataset summaries.
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if data_set_summaries is not None:
            self._values["data_set_summaries"] = data_set_summaries
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def data_set_summaries(self) -> typing.Optional[typing.List[DataSetSummary]]:
        '''The list of dataset summaries.'''
        result = self._values.get("data_set_summaries")
        return typing.cast(typing.Optional[typing.List[DataSetSummary]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListDataSetsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListDataSourcesRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListDataSourcesRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListDataSourcesRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListDataSourcesResponse",
    jsii_struct_bases=[],
    name_mapping={
        "data_sources": "dataSources",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class ListDataSourcesResponse:
    def __init__(
        self,
        *,
        data_sources: typing.Optional[typing.Sequence[DataSource]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param data_sources: A list of data sources.
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if data_sources is not None:
            self._values["data_sources"] = data_sources
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def data_sources(self) -> typing.Optional[typing.List[DataSource]]:
        '''A list of data sources.'''
        result = self._values.get("data_sources")
        return typing.cast(typing.Optional[typing.List[DataSource]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListDataSourcesResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListGroupMembershipsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "group_name": "groupName",
        "namespace": "namespace",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListGroupMembershipsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        group_name: builtins.str,
        namespace: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param group_name: The name of the group that you want to see a membership list of.
        :param namespace: The namespace. Currently, you should set this to default.
        :param max_results: The maximum number of results to return from this request.
        :param next_token: A pagination token that can be used in a subsequent request.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "group_name": group_name,
            "namespace": namespace,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the group is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The name of the group that you want to see a membership list of.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to return from this request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListGroupMembershipsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListGroupMembershipsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "group_member_list": "groupMemberList",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class ListGroupMembershipsResponse:
    def __init__(
        self,
        *,
        group_member_list: typing.Optional[typing.Sequence[GroupMember]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group_member_list: The list of the members of the group.
        :param next_token: A pagination token that can be used in a subsequent request.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if group_member_list is not None:
            self._values["group_member_list"] = group_member_list
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def group_member_list(self) -> typing.Optional[typing.List[GroupMember]]:
        '''The list of the members of the group.'''
        result = self._values.get("group_member_list")
        return typing.cast(typing.Optional[typing.List[GroupMember]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListGroupMembershipsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListGroupsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListGroupsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        namespace: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param namespace: The namespace. Currently, you should set this to default.
        :param max_results: The maximum number of results to return.
        :param next_token: A pagination token that can be used in a subsequent request.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "namespace": namespace,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the group is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to return.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListGroupsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListGroupsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "group_list": "groupList",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class ListGroupsResponse:
    def __init__(
        self,
        *,
        group_list: typing.Optional[typing.Sequence[Group]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group_list: The list of the groups.
        :param next_token: A pagination token that can be used in a subsequent request.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if group_list is not None:
            self._values["group_list"] = group_list
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def group_list(self) -> typing.Optional[typing.List[Group]]:
        '''The list of the groups.'''
        result = self._values.get("group_list")
        return typing.cast(typing.Optional[typing.List[Group]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListGroupsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListIAMPolicyAssignmentsForUserRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "user_name": "userName",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListIAMPolicyAssignmentsForUserRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        namespace: builtins.str,
        user_name: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the assignments.
        :param namespace: The namespace of the assignment.
        :param user_name: The name of the user.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "namespace": namespace,
            "user_name": user_name,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the assignments.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace of the assignment.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The name of the user.'''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListIAMPolicyAssignmentsForUserRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListIAMPolicyAssignmentsForUserResponse",
    jsii_struct_bases=[],
    name_mapping={
        "active_assignments": "activeAssignments",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class ListIAMPolicyAssignmentsForUserResponse:
    def __init__(
        self,
        *,
        active_assignments: typing.Optional[typing.Sequence[ActiveIAMPolicyAssignment]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param active_assignments: The active assignments for this user.
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if active_assignments is not None:
            self._values["active_assignments"] = active_assignments
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def active_assignments(
        self,
    ) -> typing.Optional[typing.List[ActiveIAMPolicyAssignment]]:
        '''The active assignments for this user.'''
        result = self._values.get("active_assignments")
        return typing.cast(typing.Optional[typing.List[ActiveIAMPolicyAssignment]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListIAMPolicyAssignmentsForUserResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListIAMPolicyAssignmentsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "assignment_status": "assignmentStatus",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListIAMPolicyAssignmentsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        namespace: builtins.str,
        assignment_status: typing.Optional[builtins.str] = None,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains these IAM policy assignments.
        :param namespace: The namespace for the assignments.
        :param assignment_status: The status of the assignments.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "namespace": namespace,
        }
        if assignment_status is not None:
            self._values["assignment_status"] = assignment_status
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains these IAM policy assignments.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace for the assignments.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assignment_status(self) -> typing.Optional[builtins.str]:
        '''The status of the assignments.'''
        result = self._values.get("assignment_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListIAMPolicyAssignmentsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListIAMPolicyAssignmentsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "i_am_policy_assignments": "iAMPolicyAssignments",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class ListIAMPolicyAssignmentsResponse:
    def __init__(
        self,
        *,
        i_am_policy_assignments: typing.Optional[typing.Sequence[IAMPolicyAssignmentSummary]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param i_am_policy_assignments: Information describing the IAM policy assignments.
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if i_am_policy_assignments is not None:
            self._values["i_am_policy_assignments"] = i_am_policy_assignments
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def i_am_policy_assignments(
        self,
    ) -> typing.Optional[typing.List[IAMPolicyAssignmentSummary]]:
        '''Information describing the IAM policy assignments.'''
        result = self._values.get("i_am_policy_assignments")
        return typing.cast(typing.Optional[typing.List[IAMPolicyAssignmentSummary]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListIAMPolicyAssignmentsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListIngestionsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_set_id": "dataSetId",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListIngestionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_set_id: The ID of the dataset used in the ingestion.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_id": data_set_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The ID of the dataset used in the ingestion.'''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListIngestionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListIngestionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "ingestions": "ingestions",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class ListIngestionsResponse:
    def __init__(
        self,
        *,
        ingestions: typing.Optional[typing.Sequence[Ingestion]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param ingestions: A list of the ingestions.
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ingestions is not None:
            self._values["ingestions"] = ingestions
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def ingestions(self) -> typing.Optional[typing.List[Ingestion]]:
        '''A list of the ingestions.'''
        result = self._values.get("ingestions")
        return typing.cast(typing.Optional[typing.List[Ingestion]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListIngestionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListNamespacesRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListNamespacesRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that contains the QuickSight namespaces that you want to list.
        :param max_results: The maximum number of results to return.
        :param next_token: A pagination token that can be used in a subsequent request.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that contains the QuickSight namespaces that you want to list.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to return.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListNamespacesRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListNamespacesResponse",
    jsii_struct_bases=[],
    name_mapping={
        "namespaces": "namespaces",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class ListNamespacesResponse:
    def __init__(
        self,
        *,
        namespaces: typing.Optional[typing.Sequence["NamespaceInfoV2"]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param namespaces: The information about the namespaces in this AWS account. The response includes the namespace ARN, name, AWS Region, notification email address, creation status, and identity store.
        :param next_token: A pagination token that can be used in a subsequent request.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List["NamespaceInfoV2"]]:
        '''The information about the namespaces in this AWS account.

        The response includes the namespace ARN, name, AWS Region, notification email address, creation status, and identity store.
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List["NamespaceInfoV2"]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListNamespacesResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListTagsForResourceRequest",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn"},
)
class ListTagsForResourceRequest:
    def __init__(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want a list of tags for.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource that you want a list of tags for.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListTagsForResourceRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListTagsForResourceResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status", "tags": "tags"},
)
class ListTagsForResourceResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence["Tag"]] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param tags: Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListTagsForResourceResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListTemplateAliasesRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "template_id": "templateId",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListTemplateAliasesRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        template_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the template aliases that you're listing.
        :param template_id: The ID for the template.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "template_id": template_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the template aliases that you're listing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The ID for the template.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListTemplateAliasesRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListTemplateAliasesResponse",
    jsii_struct_bases=[],
    name_mapping={
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
        "template_alias_list": "templateAliasList",
    },
)
class ListTemplateAliasesResponse:
    def __init__(
        self,
        *,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template_alias_list: typing.Optional[typing.Sequence["TemplateAlias"]] = None,
    ) -> None:
        '''
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template_alias_list: A structure containing the list of the template's aliases.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template_alias_list is not None:
            self._values["template_alias_list"] = template_alias_list

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template_alias_list(self) -> typing.Optional[typing.List["TemplateAlias"]]:
        '''A structure containing the list of the template's aliases.'''
        result = self._values.get("template_alias_list")
        return typing.cast(typing.Optional[typing.List["TemplateAlias"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListTemplateAliasesResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListTemplateVersionsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "template_id": "templateId",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListTemplateVersionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        template_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the templates that you're listing.
        :param template_id: The ID for the template.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "template_id": template_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the templates that you're listing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The ID for the template.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListTemplateVersionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListTemplateVersionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
        "template_version_summary_list": "templateVersionSummaryList",
    },
)
class ListTemplateVersionsResponse:
    def __init__(
        self,
        *,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template_version_summary_list: typing.Optional[typing.Sequence["TemplateVersionSummary"]] = None,
    ) -> None:
        '''
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template_version_summary_list: A structure containing a list of all the versions of the specified template.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template_version_summary_list is not None:
            self._values["template_version_summary_list"] = template_version_summary_list

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template_version_summary_list(
        self,
    ) -> typing.Optional[typing.List["TemplateVersionSummary"]]:
        '''A structure containing a list of all the versions of the specified template.'''
        result = self._values.get("template_version_summary_list")
        return typing.cast(typing.Optional[typing.List["TemplateVersionSummary"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListTemplateVersionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListTemplatesRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListTemplatesRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the templates that you're listing.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the templates that you're listing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListTemplatesRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListTemplatesResponse",
    jsii_struct_bases=[],
    name_mapping={
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
        "template_summary_list": "templateSummaryList",
    },
)
class ListTemplatesResponse:
    def __init__(
        self,
        *,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template_summary_list: typing.Optional[typing.Sequence["TemplateSummary"]] = None,
    ) -> None:
        '''
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template_summary_list: A structure containing information about the templates in the list.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template_summary_list is not None:
            self._values["template_summary_list"] = template_summary_list

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template_summary_list(self) -> typing.Optional[typing.List["TemplateSummary"]]:
        '''A structure containing information about the templates in the list.'''
        result = self._values.get("template_summary_list")
        return typing.cast(typing.Optional[typing.List["TemplateSummary"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListTemplatesResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListThemeAliasesRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "theme_id": "themeId",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListThemeAliasesRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the theme aliases that you're listing.
        :param theme_id: The ID for the theme.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "theme_id": theme_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the theme aliases that you're listing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''The ID for the theme.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListThemeAliasesRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListThemeAliasesResponse",
    jsii_struct_bases=[],
    name_mapping={
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
        "theme_alias_list": "themeAliasList",
    },
)
class ListThemeAliasesResponse:
    def __init__(
        self,
        *,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme_alias_list: typing.Optional[typing.Sequence["ThemeAlias"]] = None,
    ) -> None:
        '''
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme_alias_list: A structure containing the list of the theme's aliases.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme_alias_list is not None:
            self._values["theme_alias_list"] = theme_alias_list

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme_alias_list(self) -> typing.Optional[typing.List["ThemeAlias"]]:
        '''A structure containing the list of the theme's aliases.'''
        result = self._values.get("theme_alias_list")
        return typing.cast(typing.Optional[typing.List["ThemeAlias"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListThemeAliasesResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListThemeVersionsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "theme_id": "themeId",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListThemeVersionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the themes that you're listing.
        :param theme_id: The ID for the theme.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "theme_id": theme_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the themes that you're listing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''The ID for the theme.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListThemeVersionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListThemeVersionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
        "theme_version_summary_list": "themeVersionSummaryList",
    },
)
class ListThemeVersionsResponse:
    def __init__(
        self,
        *,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme_version_summary_list: typing.Optional[typing.Sequence["ThemeVersionSummary"]] = None,
    ) -> None:
        '''
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme_version_summary_list: A structure containing a list of all the versions of the specified theme.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme_version_summary_list is not None:
            self._values["theme_version_summary_list"] = theme_version_summary_list

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme_version_summary_list(
        self,
    ) -> typing.Optional[typing.List["ThemeVersionSummary"]]:
        '''A structure containing a list of all the versions of the specified theme.'''
        result = self._values.get("theme_version_summary_list")
        return typing.cast(typing.Optional[typing.List["ThemeVersionSummary"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListThemeVersionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListThemesRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "max_results": "maxResults",
        "next_token": "nextToken",
        "type": "type",
    },
)
class ListThemesRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the themes that you're listing.
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param type: The type of themes that you want to list. Valid options include the following: ALL (default)- Display all existing themes. CUSTOM - Display only the themes created by people using Amazon QuickSight. QUICKSIGHT - Display only the starting themes defined by QuickSight.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the themes that you're listing.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of themes that you want to list.

        Valid options include the following:    ALL (default)- Display all existing themes.    CUSTOM - Display only the themes created by people using Amazon QuickSight.    QUICKSIGHT - Display only the starting themes defined by QuickSight.
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListThemesRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListThemesResponse",
    jsii_struct_bases=[],
    name_mapping={
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
        "theme_summary_list": "themeSummaryList",
    },
)
class ListThemesResponse:
    def __init__(
        self,
        *,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme_summary_list: typing.Optional[typing.Sequence["ThemeSummary"]] = None,
    ) -> None:
        '''
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme_summary_list: Information about the themes in the list.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme_summary_list is not None:
            self._values["theme_summary_list"] = theme_summary_list

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme_summary_list(self) -> typing.Optional[typing.List["ThemeSummary"]]:
        '''Information about the themes in the list.'''
        result = self._values.get("theme_summary_list")
        return typing.cast(typing.Optional[typing.List["ThemeSummary"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListThemesResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListUserGroupsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "user_name": "userName",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListUserGroupsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        namespace: builtins.str,
        user_name: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param namespace: The namespace. Currently, you should set this to default.
        :param user_name: The Amazon QuickSight user name that you want to list group memberships for.
        :param max_results: The maximum number of results to return from this request.
        :param next_token: A pagination token that can be used in a subsequent request.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "namespace": namespace,
            "user_name": user_name,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID that the user is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The Amazon QuickSight user name that you want to list group memberships for.'''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to return from this request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListUserGroupsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListUserGroupsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "group_list": "groupList",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class ListUserGroupsResponse:
    def __init__(
        self,
        *,
        group_list: typing.Optional[typing.Sequence[Group]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group_list: The list of groups the user is a member of.
        :param next_token: A pagination token that can be used in a subsequent request.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if group_list is not None:
            self._values["group_list"] = group_list
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def group_list(self) -> typing.Optional[typing.List[Group]]:
        '''The list of groups the user is a member of.'''
        result = self._values.get("group_list")
        return typing.cast(typing.Optional[typing.List[Group]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListUserGroupsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListUsersRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class ListUsersRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        namespace: builtins.str,
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param namespace: The namespace. Currently, you should set this to default.
        :param max_results: The maximum number of results to return from this request.
        :param next_token: A pagination token that can be used in a subsequent request.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "namespace": namespace,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the user is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to return from this request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListUsersRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ListUsersResponse",
    jsii_struct_bases=[],
    name_mapping={
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
        "user_list": "userList",
    },
)
class ListUsersResponse:
    def __init__(
        self,
        *,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        user_list: typing.Optional[typing.Sequence["User"]] = None,
    ) -> None:
        '''
        :param next_token: A pagination token that can be used in a subsequent request.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param user_list: The list of users.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if user_list is not None:
            self._values["user_list"] = user_list

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user_list(self) -> typing.Optional[typing.List["User"]]:
        '''The list of users.'''
        result = self._values.get("user_list")
        return typing.cast(typing.Optional[typing.List["User"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListUsersResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.LogicalTable",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "source": "source",
        "data_transforms": "dataTransforms",
    },
)
class LogicalTable:
    def __init__(
        self,
        *,
        alias: builtins.str,
        source: "LogicalTableSource",
        data_transforms: typing.Optional[typing.Sequence["TransformOperation"]] = None,
    ) -> None:
        '''
        :param alias: A display name for the logical table.
        :param source: Source of this logical table.
        :param data_transforms: Transform operations that act on this logical table.
        '''
        if isinstance(source, dict):
            source = LogicalTableSource(**source)
        self._values: typing.Dict[str, typing.Any] = {
            "alias": alias,
            "source": source,
        }
        if data_transforms is not None:
            self._values["data_transforms"] = data_transforms

    @builtins.property
    def alias(self) -> builtins.str:
        '''A display name for the logical table.'''
        result = self._values.get("alias")
        assert result is not None, "Required property 'alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> "LogicalTableSource":
        '''Source of this logical table.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast("LogicalTableSource", result)

    @builtins.property
    def data_transforms(self) -> typing.Optional[typing.List["TransformOperation"]]:
        '''Transform operations that act on this logical table.'''
        result = self._values.get("data_transforms")
        return typing.cast(typing.Optional[typing.List["TransformOperation"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicalTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.LogicalTableSource",
    jsii_struct_bases=[],
    name_mapping={
        "join_instruction": "joinInstruction",
        "physical_table_id": "physicalTableId",
    },
)
class LogicalTableSource:
    def __init__(
        self,
        *,
        join_instruction: typing.Optional[JoinInstruction] = None,
        physical_table_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param join_instruction: Specifies the result of a join of two logical tables.
        :param physical_table_id: Physical table ID.
        '''
        if isinstance(join_instruction, dict):
            join_instruction = JoinInstruction(**join_instruction)
        self._values: typing.Dict[str, typing.Any] = {}
        if join_instruction is not None:
            self._values["join_instruction"] = join_instruction
        if physical_table_id is not None:
            self._values["physical_table_id"] = physical_table_id

    @builtins.property
    def join_instruction(self) -> typing.Optional[JoinInstruction]:
        '''Specifies the result of a join of two logical tables.'''
        result = self._values.get("join_instruction")
        return typing.cast(typing.Optional[JoinInstruction], result)

    @builtins.property
    def physical_table_id(self) -> typing.Optional[builtins.str]:
        '''Physical table ID.'''
        result = self._values.get("physical_table_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicalTableSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ManifestFileLocation",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "key": "key"},
)
class ManifestFileLocation:
    def __init__(self, *, bucket: builtins.str, key: builtins.str) -> None:
        '''
        :param bucket: Amazon S3 bucket.
        :param key: Amazon S3 key that identifies an object.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "key": key,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Amazon S3 bucket.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Amazon S3 key that identifies an object.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManifestFileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.MarginStyle",
    jsii_struct_bases=[],
    name_mapping={"show": "show"},
)
class MarginStyle:
    def __init__(self, *, show: typing.Optional[builtins.bool] = None) -> None:
        '''
        :param show: This Boolean value controls whether to display sheet margins.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if show is not None:
            self._values["show"] = show

    @builtins.property
    def show(self) -> typing.Optional[builtins.bool]:
        '''This Boolean value controls whether to display sheet margins.'''
        result = self._values.get("show")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MarginStyle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.MariaDbParameters",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class MariaDbParameters:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Database.
        :param host: Host.
        :param port: Port.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Database.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Host.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MariaDbParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.MySqlParameters",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class MySqlParameters:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Database.
        :param host: Host.
        :param port: Port.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Database.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Host.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MySqlParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.NamespaceError",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "type": "type"},
)
class NamespaceError:
    def __init__(
        self,
        *,
        message: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: The message for the error.
        :param type: The error type.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The message for the error.'''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The error type.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NamespaceError(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.NamespaceInfoV2",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "capacity_region": "capacityRegion",
        "creation_status": "creationStatus",
        "identity_store": "identityStore",
        "name": "name",
        "namespace_error": "namespaceError",
    },
)
class NamespaceInfoV2:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        capacity_region: typing.Optional[builtins.str] = None,
        creation_status: typing.Optional[builtins.str] = None,
        identity_store: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace_error: typing.Optional[NamespaceError] = None,
    ) -> None:
        '''
        :param arn: The namespace ARN.
        :param capacity_region: The namespace AWS Region.
        :param creation_status: The creation status of a namespace that is not yet completely created.
        :param identity_store: The identity store used for the namespace.
        :param name: The name of the error.
        :param namespace_error: An error that occurred when the namespace was created.
        '''
        if isinstance(namespace_error, dict):
            namespace_error = NamespaceError(**namespace_error)
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if capacity_region is not None:
            self._values["capacity_region"] = capacity_region
        if creation_status is not None:
            self._values["creation_status"] = creation_status
        if identity_store is not None:
            self._values["identity_store"] = identity_store
        if name is not None:
            self._values["name"] = name
        if namespace_error is not None:
            self._values["namespace_error"] = namespace_error

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The namespace ARN.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_region(self) -> typing.Optional[builtins.str]:
        '''The namespace AWS Region.'''
        result = self._values.get("capacity_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_status(self) -> typing.Optional[builtins.str]:
        '''The creation status of a namespace that is not yet completely created.'''
        result = self._values.get("creation_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_store(self) -> typing.Optional[builtins.str]:
        '''The identity store used for the namespace.'''
        result = self._values.get("identity_store")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the error.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace_error(self) -> typing.Optional[NamespaceError]:
        '''An error that occurred when the namespace was created.'''
        result = self._values.get("namespace_error")
        return typing.cast(typing.Optional[NamespaceError], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NamespaceInfoV2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.OracleParameters",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class OracleParameters:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Database.
        :param host: An Oracle host.
        :param port: Port.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Database.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''An Oracle host.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OracleParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.OutputColumn",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "name": "name", "type": "type"},
)
class OutputColumn:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param description: A description for a column.
        :param name: A display name for the dataset.
        :param type: Type.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for a column.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A display name for the dataset.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OutputColumn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.Parameters",
    jsii_struct_bases=[],
    name_mapping={
        "date_time_parameters": "dateTimeParameters",
        "decimal_parameters": "decimalParameters",
        "integer_parameters": "integerParameters",
        "string_parameters": "stringParameters",
    },
)
class Parameters:
    def __init__(
        self,
        *,
        date_time_parameters: typing.Optional[typing.Sequence[DateTimeParameter]] = None,
        decimal_parameters: typing.Optional[typing.Sequence[DecimalParameter]] = None,
        integer_parameters: typing.Optional[typing.Sequence[IntegerParameter]] = None,
        string_parameters: typing.Optional[typing.Sequence["StringParameter"]] = None,
    ) -> None:
        '''
        :param date_time_parameters: Date-time parameters.
        :param decimal_parameters: Decimal parameters.
        :param integer_parameters: Integer parameters.
        :param string_parameters: String parameters.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if date_time_parameters is not None:
            self._values["date_time_parameters"] = date_time_parameters
        if decimal_parameters is not None:
            self._values["decimal_parameters"] = decimal_parameters
        if integer_parameters is not None:
            self._values["integer_parameters"] = integer_parameters
        if string_parameters is not None:
            self._values["string_parameters"] = string_parameters

    @builtins.property
    def date_time_parameters(self) -> typing.Optional[typing.List[DateTimeParameter]]:
        '''Date-time parameters.'''
        result = self._values.get("date_time_parameters")
        return typing.cast(typing.Optional[typing.List[DateTimeParameter]], result)

    @builtins.property
    def decimal_parameters(self) -> typing.Optional[typing.List[DecimalParameter]]:
        '''Decimal parameters.'''
        result = self._values.get("decimal_parameters")
        return typing.cast(typing.Optional[typing.List[DecimalParameter]], result)

    @builtins.property
    def integer_parameters(self) -> typing.Optional[typing.List[IntegerParameter]]:
        '''Integer parameters.'''
        result = self._values.get("integer_parameters")
        return typing.cast(typing.Optional[typing.List[IntegerParameter]], result)

    @builtins.property
    def string_parameters(self) -> typing.Optional[typing.List["StringParameter"]]:
        '''String parameters.'''
        result = self._values.get("string_parameters")
        return typing.cast(typing.Optional[typing.List["StringParameter"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Parameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.PhysicalTable",
    jsii_struct_bases=[],
    name_mapping={
        "custom_sql": "customSql",
        "relational_table": "relationalTable",
        "s3_source": "s3Source",
    },
)
class PhysicalTable:
    def __init__(
        self,
        *,
        custom_sql: typing.Optional[CustomSql] = None,
        relational_table: typing.Optional["RelationalTable"] = None,
        s3_source: typing.Optional["S3Source"] = None,
    ) -> None:
        '''
        :param custom_sql: A physical table type built from the results of the custom SQL query.
        :param relational_table: A physical table type for relational data sources.
        :param s3_source: A physical table type for as S3 data source.
        '''
        if isinstance(custom_sql, dict):
            custom_sql = CustomSql(**custom_sql)
        if isinstance(relational_table, dict):
            relational_table = RelationalTable(**relational_table)
        if isinstance(s3_source, dict):
            s3_source = S3Source(**s3_source)
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_sql is not None:
            self._values["custom_sql"] = custom_sql
        if relational_table is not None:
            self._values["relational_table"] = relational_table
        if s3_source is not None:
            self._values["s3_source"] = s3_source

    @builtins.property
    def custom_sql(self) -> typing.Optional[CustomSql]:
        '''A physical table type built from the results of the custom SQL query.'''
        result = self._values.get("custom_sql")
        return typing.cast(typing.Optional[CustomSql], result)

    @builtins.property
    def relational_table(self) -> typing.Optional["RelationalTable"]:
        '''A physical table type for relational data sources.'''
        result = self._values.get("relational_table")
        return typing.cast(typing.Optional["RelationalTable"], result)

    @builtins.property
    def s3_source(self) -> typing.Optional["S3Source"]:
        '''A physical table type for as S3 data source.'''
        result = self._values.get("s3_source")
        return typing.cast(typing.Optional["S3Source"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PhysicalTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.PostgreSqlParameters",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class PostgreSqlParameters:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Database.
        :param host: Host.
        :param port: Port.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Database.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Host.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PostgreSqlParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.PrestoParameters",
    jsii_struct_bases=[],
    name_mapping={"catalog": "catalog", "host": "host", "port": "port"},
)
class PrestoParameters:
    def __init__(
        self,
        *,
        catalog: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param catalog: Catalog.
        :param host: Host.
        :param port: Port.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "catalog": catalog,
            "host": host,
            "port": port,
        }

    @builtins.property
    def catalog(self) -> builtins.str:
        '''Catalog.'''
        result = self._values.get("catalog")
        assert result is not None, "Required property 'catalog' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Host.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrestoParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ProjectOperation",
    jsii_struct_bases=[],
    name_mapping={"projected_columns": "projectedColumns"},
)
class ProjectOperation:
    def __init__(self, *, projected_columns: typing.Sequence[builtins.str]) -> None:
        '''
        :param projected_columns: Projected columns.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "projected_columns": projected_columns,
        }

    @builtins.property
    def projected_columns(self) -> typing.List[builtins.str]:
        '''Projected columns.'''
        result = self._values.get("projected_columns")
        assert result is not None, "Required property 'projected_columns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectOperation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.QSCommonProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "users": "users"},
)
class QSCommonProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        users: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: 
        :param users: QuickSight Users you want to give access to. In the end the permission arn are looking like arn:aws:quicksight:us-east-1:1234:user/default/martin.mueller@take2.co. If you want to see available users, use aws cli described here https://github.com/Reliantid/cypresspoint-infrastructure/tree/cdk#list-datasets
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "users": users,
        }

    @builtins.property
    def name(self) -> builtins.str:
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def users(self) -> typing.List[builtins.str]:
        '''QuickSight Users you want to give access to. In the end the permission arn are looking like arn:aws:quicksight:us-east-1:1234:user/default/martin.mueller@take2.co.

        If you want to see available users, use aws cli described here https://github.com/Reliantid/cypresspoint-infrastructure/tree/cdk#list-datasets
        '''
        result = self._values.get("users")
        assert result is not None, "Required property 'users' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QSCommonProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.QueueInfo",
    jsii_struct_bases=[],
    name_mapping={
        "queued_ingestion": "queuedIngestion",
        "waiting_on_ingestion": "waitingOnIngestion",
    },
)
class QueueInfo:
    def __init__(
        self,
        *,
        queued_ingestion: builtins.str,
        waiting_on_ingestion: builtins.str,
    ) -> None:
        '''
        :param queued_ingestion: The ID of the ongoing ingestion. The queued ingestion is waiting for the ongoing ingestion to complete.
        :param waiting_on_ingestion: The ID of the queued ingestion.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "queued_ingestion": queued_ingestion,
            "waiting_on_ingestion": waiting_on_ingestion,
        }

    @builtins.property
    def queued_ingestion(self) -> builtins.str:
        '''The ID of the ongoing ingestion.

        The queued ingestion is waiting for the ongoing ingestion to complete.
        '''
        result = self._values.get("queued_ingestion")
        assert result is not None, "Required property 'queued_ingestion' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def waiting_on_ingestion(self) -> builtins.str:
        '''The ID of the queued ingestion.'''
        result = self._values.get("waiting_on_ingestion")
        assert result is not None, "Required property 'waiting_on_ingestion' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueueInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.RdsParameters",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "instance_id": "instanceId"},
)
class RdsParameters:
    def __init__(self, *, database: builtins.str, instance_id: builtins.str) -> None:
        '''
        :param database: Database.
        :param instance_id: Instance ID.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "instance_id": instance_id,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Database.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Instance ID.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RdsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.RedshiftParameters",
    jsii_struct_bases=[],
    name_mapping={
        "database": "database",
        "cluster_id": "clusterId",
        "host": "host",
        "port": "port",
    },
)
class RedshiftParameters:
    def __init__(
        self,
        *,
        database: builtins.str,
        cluster_id: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param database: Database.
        :param cluster_id: Cluster ID. This field can be blank if the Host and Port are provided.
        :param host: Host. This field can be blank if ClusterId is provided.
        :param port: Port. This field can be blank if the ClusterId is provided.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
        }
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def database(self) -> builtins.str:
        '''Database.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Cluster ID.

        This field can be blank if the Host and Port are provided.
        '''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Host.

        This field can be blank if ClusterId is provided.
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port.

        This field can be blank if the ClusterId is provided.
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedshiftParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.RegisterUserRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "email": "email",
        "identity_type": "identityType",
        "namespace": "namespace",
        "user_role": "userRole",
        "custom_permissions_name": "customPermissionsName",
        "iam_arn": "iamArn",
        "session_name": "sessionName",
        "user_name": "userName",
    },
)
class RegisterUserRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        email: builtins.str,
        identity_type: builtins.str,
        namespace: builtins.str,
        user_role: builtins.str,
        custom_permissions_name: typing.Optional[builtins.str] = None,
        iam_arn: typing.Optional[builtins.str] = None,
        session_name: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param email: The email address of the user that you want to register.
        :param identity_type: Amazon QuickSight supports several ways of managing the identity of users. This parameter accepts two values: IAM: A user whose identity maps to an existing IAM user or role. QUICKSIGHT: A user whose identity is owned and managed internally by Amazon QuickSight.
        :param namespace: The namespace. Currently, you should set this to default.
        :param user_role: The Amazon QuickSight role for the user. The user role can be one of the following: READER: A user who has read-only access to dashboards. AUTHOR: A user who can create data sources, datasets, analyses, and dashboards. ADMIN: A user who is an author, who can also manage Amazon QuickSight settings. RESTRICTED_READER: This role isn't currently available for use. RESTRICTED_AUTHOR: This role isn't currently available for use.
        :param custom_permissions_name: (Enterprise edition only) The name of the custom permissions profile that you want to assign to this user. Customized permissions allows you to control a user's access by restricting access the following operations: Create and update data sources Create and update datasets Create and update email reports Subscribe to email reports To add custom permissions to an existing user, use UpdateUser instead. A set of custom permissions includes any combination of these restrictions. Currently, you need to create the profile names for custom permission sets by using the QuickSight console. Then, you use the RegisterUser API operation to assign the named set of permissions to a QuickSight user. QuickSight custom permissions are applied through IAM policies. Therefore, they override the permissions typically granted by assigning QuickSight users to one of the default security cohorts in QuickSight (admin, author, reader). This feature is available only to QuickSight Enterprise edition subscriptions that use SAML 2.0-Based Federation for Single Sign-On (SSO).
        :param iam_arn: The ARN of the IAM user or role that you are registering with Amazon QuickSight.
        :param session_name: You need to use this parameter only when you register one or more users using an assumed IAM role. You don't need to provide the session name for other scenarios, for example when you are registering an IAM user or an Amazon QuickSight user. You can register multiple users using the same IAM role if each user has a different session name. For more information on assuming IAM roles, see assume-role in the AWS CLI Reference.
        :param user_name: The Amazon QuickSight user name that you want to create for the user you are registering.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "email": email,
            "identity_type": identity_type,
            "namespace": namespace,
            "user_role": user_role,
        }
        if custom_permissions_name is not None:
            self._values["custom_permissions_name"] = custom_permissions_name
        if iam_arn is not None:
            self._values["iam_arn"] = iam_arn
        if session_name is not None:
            self._values["session_name"] = session_name
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the user is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''The email address of the user that you want to register.'''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_type(self) -> builtins.str:
        '''Amazon QuickSight supports several ways of managing the identity of users.

        This parameter accepts two values:    IAM: A user whose identity maps to an existing IAM user or role.     QUICKSIGHT: A user whose identity is owned and managed internally by Amazon QuickSight.
        '''
        result = self._values.get("identity_type")
        assert result is not None, "Required property 'identity_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_role(self) -> builtins.str:
        '''The Amazon QuickSight role for the user.

        The user role can be one of the following:    READER: A user who has read-only access to dashboards.    AUTHOR: A user who can create data sources, datasets, analyses, and dashboards.    ADMIN: A user who is an author, who can also manage Amazon QuickSight settings.    RESTRICTED_READER: This role isn't currently available for use.    RESTRICTED_AUTHOR: This role isn't currently available for use.
        '''
        result = self._values.get("user_role")
        assert result is not None, "Required property 'user_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_permissions_name(self) -> typing.Optional[builtins.str]:
        '''(Enterprise edition only) The name of the custom permissions profile that you want to assign to this user.

        Customized permissions allows you to control a user's access by restricting access the following operations:   Create and update data sources   Create and update datasets   Create and update email reports   Subscribe to email reports   To add custom permissions to an existing user, use  UpdateUser  instead. A set of custom permissions includes any combination of these restrictions. Currently, you need to create the profile names for custom permission sets by using the QuickSight console. Then, you use the RegisterUser API operation to assign the named set of permissions to a QuickSight user.  QuickSight custom permissions are applied through IAM policies. Therefore, they override the permissions typically granted by assigning QuickSight users to one of the default security cohorts in QuickSight (admin, author, reader). This feature is available only to QuickSight Enterprise edition subscriptions that use SAML 2.0-Based Federation for Single Sign-On (SSO).
        '''
        result = self._values.get("custom_permissions_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM user or role that you are registering with Amazon QuickSight.'''
        result = self._values.get("iam_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_name(self) -> typing.Optional[builtins.str]:
        '''You need to use this parameter only when you register one or more users using an assumed IAM role.

        You don't need to provide the session name for other scenarios, for example when you are registering an IAM user or an Amazon QuickSight user. You can register multiple users using the same IAM role if each user has a different session name. For more information on assuming IAM roles, see  assume-role  in the AWS CLI Reference.
        '''
        result = self._values.get("session_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''The Amazon QuickSight user name that you want to create for the user you are registering.'''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegisterUserRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.RegisterUserResponse",
    jsii_struct_bases=[],
    name_mapping={
        "request_id": "requestId",
        "status": "status",
        "user": "user",
        "user_invitation_url": "userInvitationUrl",
    },
)
class RegisterUserResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        user: typing.Optional["User"] = None,
        user_invitation_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param user: The user's user name.
        :param user_invitation_url: The URL the user visits to complete registration and provide a password. This is returned only for users with an identity type of QUICKSIGHT.
        '''
        if isinstance(user, dict):
            user = User(**user)
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if user is not None:
            self._values["user"] = user
        if user_invitation_url is not None:
            self._values["user_invitation_url"] = user_invitation_url

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user(self) -> typing.Optional["User"]:
        '''The user's user name.'''
        result = self._values.get("user")
        return typing.cast(typing.Optional["User"], result)

    @builtins.property
    def user_invitation_url(self) -> typing.Optional[builtins.str]:
        '''The URL the user visits to complete registration and provide a password.

        This is returned only for users with an identity type of QUICKSIGHT.
        '''
        result = self._values.get("user_invitation_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegisterUserResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.RelationalTable",
    jsii_struct_bases=[],
    name_mapping={
        "data_source_arn": "dataSourceArn",
        "input_columns": "inputColumns",
        "name": "name",
        "catalog": "catalog",
        "schema": "schema",
    },
)
class RelationalTable:
    def __init__(
        self,
        *,
        data_source_arn: builtins.str,
        input_columns: typing.Sequence[InputColumn],
        name: builtins.str,
        catalog: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_source_arn: The Amazon Resource Name (ARN) for the data source.
        :param input_columns: The column schema of the table.
        :param name: The name of the relational table.
        :param catalog: The catalog associated with a table.
        :param schema: The schema name. This name applies to certain relational database engines.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "data_source_arn": data_source_arn,
            "input_columns": input_columns,
            "name": name,
        }
        if catalog is not None:
            self._values["catalog"] = catalog
        if schema is not None:
            self._values["schema"] = schema

    @builtins.property
    def data_source_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the data source.'''
        result = self._values.get("data_source_arn")
        assert result is not None, "Required property 'data_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_columns(self) -> typing.List[InputColumn]:
        '''The column schema of the table.'''
        result = self._values.get("input_columns")
        assert result is not None, "Required property 'input_columns' is missing"
        return typing.cast(typing.List[InputColumn], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the relational table.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog(self) -> typing.Optional[builtins.str]:
        '''The catalog associated with a table.'''
        result = self._values.get("catalog")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''The schema name.

        This name applies to certain relational database engines.
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RelationalTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.RenameColumnOperation",
    jsii_struct_bases=[],
    name_mapping={"column_name": "columnName", "new_column_name": "newColumnName"},
)
class RenameColumnOperation:
    def __init__(
        self,
        *,
        column_name: builtins.str,
        new_column_name: builtins.str,
    ) -> None:
        '''
        :param column_name: The name of the column to be renamed.
        :param new_column_name: The new name for the column.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "column_name": column_name,
            "new_column_name": new_column_name,
        }

    @builtins.property
    def column_name(self) -> builtins.str:
        '''The name of the column to be renamed.'''
        result = self._values.get("column_name")
        assert result is not None, "Required property 'column_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def new_column_name(self) -> builtins.str:
        '''The new name for the column.'''
        result = self._values.get("new_column_name")
        assert result is not None, "Required property 'new_column_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RenameColumnOperation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ResourcePermission",
    jsii_struct_bases=[],
    name_mapping={"actions": "actions", "principal": "principal"},
)
class ResourcePermission:
    def __init__(
        self,
        *,
        actions: typing.Sequence[builtins.str],
        principal: builtins.str,
    ) -> None:
        '''
        :param actions: The IAM action to grant or revoke permissions on.
        :param principal: The Amazon Resource Name (ARN) of the principal. This can be one of the following: The ARN of an Amazon QuickSight user or group associated with a data source or dataset. (This is common.) The ARN of an Amazon QuickSight user, group, or namespace associated with an analysis, dashboard, template, or theme. (This is common.) The ARN of an AWS account root: This is an IAM ARN rather than a QuickSight ARN. Use this option only to share resources (templates) across AWS accounts. (This is less common.)
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
            "principal": principal,
        }

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        '''The IAM action to grant or revoke permissions on.'''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the principal.

        This can be one of the following:   The ARN of an Amazon QuickSight user or group associated with a data source or dataset. (This is common.)   The ARN of an Amazon QuickSight user, group, or namespace associated with an analysis, dashboard, template, or theme. (This is common.)   The ARN of an AWS account root: This is an IAM ARN rather than a QuickSight ARN. Use this option only to share resources (templates) across AWS accounts. (This is less common.)
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.RestoreAnalysisRequest",
    jsii_struct_bases=[],
    name_mapping={"analysis_id": "analysisId", "aws_account_id": "awsAccountId"},
)
class RestoreAnalysisRequest:
    def __init__(
        self,
        *,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
    ) -> None:
        '''
        :param analysis_id: The ID of the analysis that you're restoring.
        :param aws_account_id: The ID of the AWS account that contains the analysis.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "analysis_id": analysis_id,
            "aws_account_id": aws_account_id,
        }

    @builtins.property
    def analysis_id(self) -> builtins.str:
        '''The ID of the analysis that you're restoring.'''
        result = self._values.get("analysis_id")
        assert result is not None, "Required property 'analysis_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the analysis.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RestoreAnalysisRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.RestoreAnalysisResponse",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_id": "analysisId",
        "arn": "arn",
        "request_id": "requestId",
        "status": "status",
    },
)
class RestoreAnalysisResponse:
    def __init__(
        self,
        *,
        analysis_id: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param analysis_id: The ID of the analysis that you're restoring.
        :param arn: The Amazon Resource Name (ARN) of the analysis that you're restoring.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if analysis_id is not None:
            self._values["analysis_id"] = analysis_id
        if arn is not None:
            self._values["arn"] = arn
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def analysis_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the analysis that you're restoring.'''
        result = self._values.get("analysis_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the analysis that you're restoring.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RestoreAnalysisResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.RowInfo",
    jsii_struct_bases=[],
    name_mapping={"rows_dropped": "rowsDropped", "rows_ingested": "rowsIngested"},
)
class RowInfo:
    def __init__(
        self,
        *,
        rows_dropped: typing.Optional[jsii.Number] = None,
        rows_ingested: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param rows_dropped: The number of rows that were not ingested.
        :param rows_ingested: The number of rows that were ingested.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if rows_dropped is not None:
            self._values["rows_dropped"] = rows_dropped
        if rows_ingested is not None:
            self._values["rows_ingested"] = rows_ingested

    @builtins.property
    def rows_dropped(self) -> typing.Optional[jsii.Number]:
        '''The number of rows that were not ingested.'''
        result = self._values.get("rows_dropped")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rows_ingested(self) -> typing.Optional[jsii.Number]:
        '''The number of rows that were ingested.'''
        result = self._values.get("rows_ingested")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RowInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.RowLevelPermissionDataSet",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "permission_policy": "permissionPolicy",
        "namespace": "namespace",
    },
)
class RowLevelPermissionDataSet:
    def __init__(
        self,
        *,
        arn: builtins.str,
        permission_policy: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the dataset that contains permissions for RLS.
        :param permission_policy: The type of permissions to use when interpretting the permissions for RLS. DENY_ACCESS is included for backward compatibility only.
        :param namespace: The namespace associated with the dataset that contains permissions for RLS.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
            "permission_policy": permission_policy,
        }
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset that contains permissions for RLS.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permission_policy(self) -> builtins.str:
        '''The type of permissions to use when interpretting the permissions for RLS.

        DENY_ACCESS is included for backward compatibility only.
        '''
        result = self._values.get("permission_policy")
        assert result is not None, "Required property 'permission_policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace associated with the dataset that contains permissions for RLS.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RowLevelPermissionDataSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.S3Parameters",
    jsii_struct_bases=[],
    name_mapping={"manifest_file_location": "manifestFileLocation"},
)
class S3Parameters:
    def __init__(self, *, manifest_file_location: ManifestFileLocation) -> None:
        '''
        :param manifest_file_location: Location of the Amazon S3 manifest file. This is NULL if the manifest file was uploaded in the console.
        '''
        if isinstance(manifest_file_location, dict):
            manifest_file_location = ManifestFileLocation(**manifest_file_location)
        self._values: typing.Dict[str, typing.Any] = {
            "manifest_file_location": manifest_file_location,
        }

    @builtins.property
    def manifest_file_location(self) -> ManifestFileLocation:
        '''Location of the Amazon S3 manifest file.

        This is NULL if the manifest file was uploaded in the console.
        '''
        result = self._values.get("manifest_file_location")
        assert result is not None, "Required property 'manifest_file_location' is missing"
        return typing.cast(ManifestFileLocation, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3Parameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.S3Source",
    jsii_struct_bases=[],
    name_mapping={
        "data_source_arn": "dataSourceArn",
        "input_columns": "inputColumns",
        "upload_settings": "uploadSettings",
    },
)
class S3Source:
    def __init__(
        self,
        *,
        data_source_arn: builtins.str,
        input_columns: typing.Sequence[InputColumn],
        upload_settings: typing.Optional["UploadSettings"] = None,
    ) -> None:
        '''
        :param data_source_arn: The Amazon Resource Name (ARN) for the data source.
        :param input_columns: A physical table type for as S3 data source.
        :param upload_settings: Information about the format for the S3 source file or files.
        '''
        if isinstance(upload_settings, dict):
            upload_settings = UploadSettings(**upload_settings)
        self._values: typing.Dict[str, typing.Any] = {
            "data_source_arn": data_source_arn,
            "input_columns": input_columns,
        }
        if upload_settings is not None:
            self._values["upload_settings"] = upload_settings

    @builtins.property
    def data_source_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the data source.'''
        result = self._values.get("data_source_arn")
        assert result is not None, "Required property 'data_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_columns(self) -> typing.List[InputColumn]:
        '''A physical table type for as S3 data source.'''
        result = self._values.get("input_columns")
        assert result is not None, "Required property 'input_columns' is missing"
        return typing.cast(typing.List[InputColumn], result)

    @builtins.property
    def upload_settings(self) -> typing.Optional["UploadSettings"]:
        '''Information about the format for the S3 source file or files.'''
        result = self._values.get("upload_settings")
        return typing.cast(typing.Optional["UploadSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3Source(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.SearchAnalysesRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "filters": "filters",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class SearchAnalysesRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        filters: typing.Sequence[AnalysisSearchFilter],
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the analyses that you're searching for.
        :param filters: The structure for the search filters that you want to apply to your search.
        :param max_results: The maximum number of results to return.
        :param next_token: A pagination token that can be used in a subsequent request.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "filters": filters,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the analyses that you're searching for.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filters(self) -> typing.List[AnalysisSearchFilter]:
        '''The structure for the search filters that you want to apply to your search.'''
        result = self._values.get("filters")
        assert result is not None, "Required property 'filters' is missing"
        return typing.cast(typing.List[AnalysisSearchFilter], result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to return.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SearchAnalysesRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.SearchAnalysesResponse",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_summary_list": "analysisSummaryList",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class SearchAnalysesResponse:
    def __init__(
        self,
        *,
        analysis_summary_list: typing.Optional[typing.Sequence[AnalysisSummary]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param analysis_summary_list: Metadata describing the analyses that you searched for.
        :param next_token: A pagination token that can be used in a subsequent request.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if analysis_summary_list is not None:
            self._values["analysis_summary_list"] = analysis_summary_list
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def analysis_summary_list(self) -> typing.Optional[typing.List[AnalysisSummary]]:
        '''Metadata describing the analyses that you searched for.'''
        result = self._values.get("analysis_summary_list")
        return typing.cast(typing.Optional[typing.List[AnalysisSummary]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''A pagination token that can be used in a subsequent request.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SearchAnalysesResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.SearchDashboardsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "filters": "filters",
        "max_results": "maxResults",
        "next_token": "nextToken",
    },
)
class SearchDashboardsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        filters: typing.Sequence[DashboardSearchFilter],
        max_results: typing.Optional[jsii.Number] = None,
        next_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the user whose dashboards you're searching for.
        :param filters: The filters to apply to the search. Currently, you can search only by user name, for example, "Filters": [ { "Name": "QUICKSIGHT_USER", "Operator": "StringEquals", "Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1" } ]
        :param max_results: The maximum number of results to be returned per request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "filters": filters,
        }
        if max_results is not None:
            self._values["max_results"] = max_results
        if next_token is not None:
            self._values["next_token"] = next_token

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the user whose dashboards you're searching for.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filters(self) -> typing.List[DashboardSearchFilter]:
        '''The filters to apply to the search.

        Currently, you can search only by user name, for example, "Filters": [ { "Name": "QUICKSIGHT_USER", "Operator": "StringEquals", "Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1" } ]
        '''
        result = self._values.get("filters")
        assert result is not None, "Required property 'filters' is missing"
        return typing.cast(typing.List[DashboardSearchFilter], result)

    @builtins.property
    def max_results(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of results to be returned per request.'''
        result = self._values.get("max_results")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SearchDashboardsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.SearchDashboardsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_summary_list": "dashboardSummaryList",
        "next_token": "nextToken",
        "request_id": "requestId",
        "status": "status",
    },
)
class SearchDashboardsResponse:
    def __init__(
        self,
        *,
        dashboard_summary_list: typing.Optional[typing.Sequence[DashboardSummary]] = None,
        next_token: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dashboard_summary_list: The list of dashboards owned by the user specified in Filters in your request.
        :param next_token: The token for the next set of results, or null if there are no more results.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if dashboard_summary_list is not None:
            self._values["dashboard_summary_list"] = dashboard_summary_list
        if next_token is not None:
            self._values["next_token"] = next_token
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def dashboard_summary_list(self) -> typing.Optional[typing.List[DashboardSummary]]:
        '''The list of dashboards owned by the user specified in Filters in your request.'''
        result = self._values.get("dashboard_summary_list")
        return typing.cast(typing.Optional[typing.List[DashboardSummary]], result)

    @builtins.property
    def next_token(self) -> typing.Optional[builtins.str]:
        '''The token for the next set of results, or null if there are no more results.'''
        result = self._values.get("next_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SearchDashboardsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ServiceNowParameters",
    jsii_struct_bases=[],
    name_mapping={"site_base_url": "siteBaseUrl"},
)
class ServiceNowParameters:
    def __init__(self, *, site_base_url: builtins.str) -> None:
        '''
        :param site_base_url: URL of the base site.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "site_base_url": site_base_url,
        }

    @builtins.property
    def site_base_url(self) -> builtins.str:
        '''URL of the base site.'''
        result = self._values.get("site_base_url")
        assert result is not None, "Required property 'site_base_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceNowParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.Sheet",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "sheet_id": "sheetId"},
)
class Sheet:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        sheet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of a sheet. This name is displayed on the sheet's tab in the QuickSight console.
        :param sheet_id: The unique identifier associated with a sheet.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if sheet_id is not None:
            self._values["sheet_id"] = sheet_id

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of a sheet.

        This name is displayed on the sheet's tab in the QuickSight console.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sheet_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier associated with a sheet.'''
        result = self._values.get("sheet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Sheet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.SheetControlsOption",
    jsii_struct_bases=[],
    name_mapping={"visibility_state": "visibilityState"},
)
class SheetControlsOption:
    def __init__(
        self,
        *,
        visibility_state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param visibility_state: Visibility state.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if visibility_state is not None:
            self._values["visibility_state"] = visibility_state

    @builtins.property
    def visibility_state(self) -> typing.Optional[builtins.str]:
        '''Visibility state.'''
        result = self._values.get("visibility_state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SheetControlsOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.SheetStyle",
    jsii_struct_bases=[],
    name_mapping={"tile": "tile", "tile_layout": "tileLayout"},
)
class SheetStyle:
    def __init__(
        self,
        *,
        tile: typing.Optional["TileStyle"] = None,
        tile_layout: typing.Optional["TileLayoutStyle"] = None,
    ) -> None:
        '''
        :param tile: The display options for tiles.
        :param tile_layout: The layout options for tiles.
        '''
        if isinstance(tile, dict):
            tile = TileStyle(**tile)
        if isinstance(tile_layout, dict):
            tile_layout = TileLayoutStyle(**tile_layout)
        self._values: typing.Dict[str, typing.Any] = {}
        if tile is not None:
            self._values["tile"] = tile
        if tile_layout is not None:
            self._values["tile_layout"] = tile_layout

    @builtins.property
    def tile(self) -> typing.Optional["TileStyle"]:
        '''The display options for tiles.'''
        result = self._values.get("tile")
        return typing.cast(typing.Optional["TileStyle"], result)

    @builtins.property
    def tile_layout(self) -> typing.Optional["TileLayoutStyle"]:
        '''The layout options for tiles.'''
        result = self._values.get("tile_layout")
        return typing.cast(typing.Optional["TileLayoutStyle"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SheetStyle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.SnowflakeParameters",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "warehouse": "warehouse"},
)
class SnowflakeParameters:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        warehouse: builtins.str,
    ) -> None:
        '''
        :param database: Database.
        :param host: Host.
        :param warehouse: Warehouse.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "host": host,
            "warehouse": warehouse,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Database.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Host.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def warehouse(self) -> builtins.str:
        '''Warehouse.'''
        result = self._values.get("warehouse")
        assert result is not None, "Required property 'warehouse' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnowflakeParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.SparkParameters",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port"},
)
class SparkParameters:
    def __init__(self, *, host: builtins.str, port: jsii.Number) -> None:
        '''
        :param host: Host.
        :param port: Port.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "host": host,
            "port": port,
        }

    @builtins.property
    def host(self) -> builtins.str:
        '''Host.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SparkParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.SqlServerParameters",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class SqlServerParameters:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Database.
        :param host: Host.
        :param port: Port.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Database.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Host.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlServerParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.SslProperties",
    jsii_struct_bases=[],
    name_mapping={"disable_ssl": "disableSsl"},
)
class SslProperties:
    def __init__(self, *, disable_ssl: typing.Optional[builtins.bool] = None) -> None:
        '''
        :param disable_ssl: A Boolean option to control whether SSL should be disabled.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if disable_ssl is not None:
            self._values["disable_ssl"] = disable_ssl

    @builtins.property
    def disable_ssl(self) -> typing.Optional[builtins.bool]:
        '''A Boolean option to control whether SSL should be disabled.'''
        result = self._values.get("disable_ssl")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SslProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.StringParameter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class StringParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: A display name for a string parameter.
        :param values: The values of a string parameter.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''A display name for a string parameter.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''The values of a string parameter.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StringParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.Tag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Tag:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Tag key.
        :param value: Tag value.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Tag key.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Tag value.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Tag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TagColumnOperation",
    jsii_struct_bases=[],
    name_mapping={"column_name": "columnName", "tags": "tags"},
)
class TagColumnOperation:
    def __init__(
        self,
        *,
        column_name: builtins.str,
        tags: typing.Sequence[ColumnTag],
    ) -> None:
        '''
        :param column_name: The column that this operation acts on.
        :param tags: The dataset column tag, currently only used for geospatial type tagging. . This is not tags for the AWS tagging feature. .
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "column_name": column_name,
            "tags": tags,
        }

    @builtins.property
    def column_name(self) -> builtins.str:
        '''The column that this operation acts on.'''
        result = self._values.get("column_name")
        assert result is not None, "Required property 'column_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.List[ColumnTag]:
        '''The dataset column tag, currently only used for geospatial type tagging.

        .  This is not tags for the AWS tagging feature. .
        '''
        result = self._values.get("tags")
        assert result is not None, "Required property 'tags' is missing"
        return typing.cast(typing.List[ColumnTag], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagColumnOperation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TagResourceRequest",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "tags": "tags"},
)
class TagResourceRequest:
    def __init__(
        self,
        *,
        resource_arn: builtins.str,
        tags: typing.Sequence[Tag],
    ) -> None:
        '''
        :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to tag.
        :param tags: Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource that you want to tag.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.List[Tag]:
        '''Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.'''
        result = self._values.get("tags")
        assert result is not None, "Required property 'tags' is missing"
        return typing.cast(typing.List[Tag], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagResourceRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TagResourceResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status"},
)
class TagResourceResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagResourceResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.Template",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "created_time": "createdTime",
        "last_updated_time": "lastUpdatedTime",
        "name": "name",
        "template_id": "templateId",
        "version": "version",
    },
)
class Template:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        last_updated_time: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[builtins.str] = None,
        template_id: typing.Optional[builtins.str] = None,
        version: typing.Optional["TemplateVersion"] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the template.
        :param created_time: Time when this was created.
        :param last_updated_time: Time when this was last updated.
        :param name: The display name of the template.
        :param template_id: The ID for the template. This is unique per AWS Region for each AWS account.
        :param version: A structure describing the versions of the template.
        '''
        if isinstance(version, dict):
            version = TemplateVersion(**version)
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if last_updated_time is not None:
            self._values["last_updated_time"] = last_updated_time
        if name is not None:
            self._values["name"] = name
        if template_id is not None:
            self._values["template_id"] = template_id
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the template.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''Time when this was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def last_updated_time(self) -> typing.Optional[datetime.datetime]:
        '''Time when this was last updated.'''
        result = self._values.get("last_updated_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The display name of the template.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the template.

        This is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional["TemplateVersion"]:
        '''A structure describing the versions of the template.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional["TemplateVersion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Template(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TemplateAlias",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "arn": "arn",
        "template_version_number": "templateVersionNumber",
    },
)
class TemplateAlias:
    def __init__(
        self,
        *,
        alias_name: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        template_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param alias_name: The display name of the template alias.
        :param arn: The Amazon Resource Name (ARN) of the template alias.
        :param template_version_number: The version number of the template alias.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if alias_name is not None:
            self._values["alias_name"] = alias_name
        if arn is not None:
            self._values["arn"] = arn
        if template_version_number is not None:
            self._values["template_version_number"] = template_version_number

    @builtins.property
    def alias_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the template alias.'''
        result = self._values.get("alias_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the template alias.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number of the template alias.'''
        result = self._values.get("template_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateAlias(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TemplateError",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "type": "type"},
)
class TemplateError:
    def __init__(
        self,
        *,
        message: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: Description of the error type.
        :param type: Type of error.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Description of the error type.'''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type of error.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateError(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TemplateSourceAnalysis",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "data_set_references": "dataSetReferences"},
)
class TemplateSourceAnalysis:
    def __init__(
        self,
        *,
        arn: builtins.str,
        data_set_references: typing.Sequence[DataSetReference],
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param data_set_references: A structure containing information about the dataset references used as placeholders in the template.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
            "data_set_references": data_set_references,
        }

    @builtins.property
    def arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_references(self) -> typing.List[DataSetReference]:
        '''A structure containing information about the dataset references used as placeholders in the template.'''
        result = self._values.get("data_set_references")
        assert result is not None, "Required property 'data_set_references' is missing"
        return typing.cast(typing.List[DataSetReference], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateSourceAnalysis(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TemplateSourceEntity",
    jsii_struct_bases=[],
    name_mapping={
        "source_analysis": "sourceAnalysis",
        "source_template": "sourceTemplate",
    },
)
class TemplateSourceEntity:
    def __init__(
        self,
        *,
        source_analysis: typing.Optional[TemplateSourceAnalysis] = None,
        source_template: typing.Optional["TemplateSourceTemplate"] = None,
    ) -> None:
        '''
        :param source_analysis: The source analysis, if it is based on an analysis.
        :param source_template: The source template, if it is based on an template.
        '''
        if isinstance(source_analysis, dict):
            source_analysis = TemplateSourceAnalysis(**source_analysis)
        if isinstance(source_template, dict):
            source_template = TemplateSourceTemplate(**source_template)
        self._values: typing.Dict[str, typing.Any] = {}
        if source_analysis is not None:
            self._values["source_analysis"] = source_analysis
        if source_template is not None:
            self._values["source_template"] = source_template

    @builtins.property
    def source_analysis(self) -> typing.Optional[TemplateSourceAnalysis]:
        '''The source analysis, if it is based on an analysis.'''
        result = self._values.get("source_analysis")
        return typing.cast(typing.Optional[TemplateSourceAnalysis], result)

    @builtins.property
    def source_template(self) -> typing.Optional["TemplateSourceTemplate"]:
        '''The source template, if it is based on an template.'''
        result = self._values.get("source_template")
        return typing.cast(typing.Optional["TemplateSourceTemplate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateSourceEntity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TemplateSourceTemplate",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn"},
)
class TemplateSourceTemplate:
    def __init__(self, *, arn: builtins.str) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
        }

    @builtins.property
    def arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateSourceTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TemplateSummary",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "created_time": "createdTime",
        "last_updated_time": "lastUpdatedTime",
        "latest_version_number": "latestVersionNumber",
        "name": "name",
        "template_id": "templateId",
    },
)
class TemplateSummary:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        last_updated_time: typing.Optional[datetime.datetime] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: A summary of a template.
        :param created_time: The last time that this template was created.
        :param last_updated_time: The last time that this template was updated.
        :param latest_version_number: A structure containing a list of version numbers for the template summary.
        :param name: A display name for the template.
        :param template_id: The ID of the template. This ID is unique per AWS Region for each AWS account.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if last_updated_time is not None:
            self._values["last_updated_time"] = last_updated_time
        if latest_version_number is not None:
            self._values["latest_version_number"] = latest_version_number
        if name is not None:
            self._values["name"] = name
        if template_id is not None:
            self._values["template_id"] = template_id

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''A summary of a template.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The last time that this template was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def last_updated_time(self) -> typing.Optional[datetime.datetime]:
        '''The last time that this template was updated.'''
        result = self._values.get("last_updated_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''A structure containing a list of version numbers for the template summary.'''
        result = self._values.get("latest_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A display name for the template.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the template.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateSummary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TemplateVersion",
    jsii_struct_bases=[],
    name_mapping={
        "created_time": "createdTime",
        "data_set_configurations": "dataSetConfigurations",
        "description": "description",
        "errors": "errors",
        "sheets": "sheets",
        "source_entity_arn": "sourceEntityArn",
        "status": "status",
        "theme_arn": "themeArn",
        "version_number": "versionNumber",
    },
)
class TemplateVersion:
    def __init__(
        self,
        *,
        created_time: typing.Optional[datetime.datetime] = None,
        data_set_configurations: typing.Optional[typing.Sequence[DataSetConfiguration]] = None,
        description: typing.Optional[builtins.str] = None,
        errors: typing.Optional[typing.Sequence[TemplateError]] = None,
        sheets: typing.Optional[typing.Sequence[Sheet]] = None,
        source_entity_arn: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        theme_arn: typing.Optional[builtins.str] = None,
        version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param created_time: The time that this template version was created.
        :param data_set_configurations: Schema of the dataset identified by the placeholder. Any dashboard created from this template should be bound to new datasets matching the same schema described through this API operation.
        :param description: The description of the template.
        :param errors: Errors associated with this template version.
        :param sheets: A list of the associated sheets with the unique identifier and name of each sheet.
        :param source_entity_arn: The Amazon Resource Name (ARN) of an analysis or template that was used to create this template.
        :param status: The HTTP status of the request.
        :param theme_arn: The ARN of the theme associated with this version of the template.
        :param version_number: The version number of the template version.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if created_time is not None:
            self._values["created_time"] = created_time
        if data_set_configurations is not None:
            self._values["data_set_configurations"] = data_set_configurations
        if description is not None:
            self._values["description"] = description
        if errors is not None:
            self._values["errors"] = errors
        if sheets is not None:
            self._values["sheets"] = sheets
        if source_entity_arn is not None:
            self._values["source_entity_arn"] = source_entity_arn
        if status is not None:
            self._values["status"] = status
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that this template version was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def data_set_configurations(
        self,
    ) -> typing.Optional[typing.List[DataSetConfiguration]]:
        '''Schema of the dataset identified by the placeholder.

        Any dashboard created from this template should be bound to new datasets matching the same schema described through this API operation.
        '''
        result = self._values.get("data_set_configurations")
        return typing.cast(typing.Optional[typing.List[DataSetConfiguration]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the template.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def errors(self) -> typing.Optional[typing.List[TemplateError]]:
        '''Errors associated with this template version.'''
        result = self._values.get("errors")
        return typing.cast(typing.Optional[typing.List[TemplateError]], result)

    @builtins.property
    def sheets(self) -> typing.Optional[typing.List[Sheet]]:
        '''A list of the associated sheets with the unique identifier and name of each sheet.'''
        result = self._values.get("sheets")
        return typing.cast(typing.Optional[typing.List[Sheet]], result)

    @builtins.property
    def source_entity_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an analysis or template that was used to create this template.'''
        result = self._values.get("source_entity_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the theme associated with this version of the template.'''
        result = self._values.get("theme_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number of the template version.'''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TemplateVersionSummary",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "created_time": "createdTime",
        "description": "description",
        "status": "status",
        "version_number": "versionNumber",
    },
)
class TemplateVersionSummary:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        description: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the template version.
        :param created_time: The time that this template version was created.
        :param description: The description of the template version.
        :param status: The status of the template version.
        :param version_number: The version number of the template version.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if description is not None:
            self._values["description"] = description
        if status is not None:
            self._values["status"] = status
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the template version.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The time that this template version was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the template version.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the template version.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number of the template version.'''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateVersionSummary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TeradataParameters",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class TeradataParameters:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Database.
        :param host: Host.
        :param port: Port.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Database.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Host.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeradataParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.Theme",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "created_time": "createdTime",
        "last_updated_time": "lastUpdatedTime",
        "name": "name",
        "theme_id": "themeId",
        "type": "type",
        "version": "version",
    },
)
class Theme:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        last_updated_time: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[builtins.str] = None,
        theme_id: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        version: typing.Optional["ThemeVersion"] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the theme.
        :param created_time: The date and time that the theme was created.
        :param last_updated_time: The date and time that the theme was last updated.
        :param name: The name that the user gives to the theme.
        :param theme_id: The identifier that the user gives to the theme.
        :param type: The type of theme, based on how it was created. Valid values include: QUICKSIGHT and CUSTOM.
        :param version: 
        '''
        if isinstance(version, dict):
            version = ThemeVersion(**version)
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if last_updated_time is not None:
            self._values["last_updated_time"] = last_updated_time
        if name is not None:
            self._values["name"] = name
        if theme_id is not None:
            self._values["theme_id"] = theme_id
        if type is not None:
            self._values["type"] = type
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the theme.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The date and time that the theme was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def last_updated_time(self) -> typing.Optional[datetime.datetime]:
        '''The date and time that the theme was last updated.'''
        result = self._values.get("last_updated_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name that the user gives to the theme.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def theme_id(self) -> typing.Optional[builtins.str]:
        '''The identifier that the user gives to the theme.'''
        result = self._values.get("theme_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of theme, based on how it was created.

        Valid values include: QUICKSIGHT and CUSTOM.
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional["ThemeVersion"]:
        result = self._values.get("version")
        return typing.cast(typing.Optional["ThemeVersion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Theme(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ThemeAlias",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "arn": "arn",
        "theme_version_number": "themeVersionNumber",
    },
)
class ThemeAlias:
    def __init__(
        self,
        *,
        alias_name: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        theme_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param alias_name: The display name of the theme alias.
        :param arn: The Amazon Resource Name (ARN) of the theme alias.
        :param theme_version_number: The version number of the theme alias.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if alias_name is not None:
            self._values["alias_name"] = alias_name
        if arn is not None:
            self._values["arn"] = arn
        if theme_version_number is not None:
            self._values["theme_version_number"] = theme_version_number

    @builtins.property
    def alias_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the theme alias.'''
        result = self._values.get("alias_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the theme alias.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def theme_version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number of the theme alias.'''
        result = self._values.get("theme_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThemeAlias(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ThemeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "data_color_palette": "dataColorPalette",
        "sheet": "sheet",
        "u_i_color_palette": "uIColorPalette",
    },
)
class ThemeConfiguration:
    def __init__(
        self,
        *,
        data_color_palette: typing.Optional[DataColorPalette] = None,
        sheet: typing.Optional[SheetStyle] = None,
        u_i_color_palette: typing.Optional["UIColorPalette"] = None,
    ) -> None:
        '''
        :param data_color_palette: Color properties that apply to chart data colors.
        :param sheet: Display options related to sheets.
        :param u_i_color_palette: Color properties that apply to the UI and to charts, excluding the colors that apply to data.
        '''
        if isinstance(data_color_palette, dict):
            data_color_palette = DataColorPalette(**data_color_palette)
        if isinstance(sheet, dict):
            sheet = SheetStyle(**sheet)
        if isinstance(u_i_color_palette, dict):
            u_i_color_palette = UIColorPalette(**u_i_color_palette)
        self._values: typing.Dict[str, typing.Any] = {}
        if data_color_palette is not None:
            self._values["data_color_palette"] = data_color_palette
        if sheet is not None:
            self._values["sheet"] = sheet
        if u_i_color_palette is not None:
            self._values["u_i_color_palette"] = u_i_color_palette

    @builtins.property
    def data_color_palette(self) -> typing.Optional[DataColorPalette]:
        '''Color properties that apply to chart data colors.'''
        result = self._values.get("data_color_palette")
        return typing.cast(typing.Optional[DataColorPalette], result)

    @builtins.property
    def sheet(self) -> typing.Optional[SheetStyle]:
        '''Display options related to sheets.'''
        result = self._values.get("sheet")
        return typing.cast(typing.Optional[SheetStyle], result)

    @builtins.property
    def u_i_color_palette(self) -> typing.Optional["UIColorPalette"]:
        '''Color properties that apply to the UI and to charts, excluding the colors that apply to data.'''
        result = self._values.get("u_i_color_palette")
        return typing.cast(typing.Optional["UIColorPalette"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThemeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ThemeError",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "type": "type"},
)
class ThemeError:
    def __init__(
        self,
        *,
        message: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: The error message.
        :param type: The type of error.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The error message.'''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of error.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThemeError(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ThemeSummary",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "created_time": "createdTime",
        "last_updated_time": "lastUpdatedTime",
        "latest_version_number": "latestVersionNumber",
        "name": "name",
        "theme_id": "themeId",
    },
)
class ThemeSummary:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        last_updated_time: typing.Optional[datetime.datetime] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        theme_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param created_time: The date and time that this theme was created.
        :param last_updated_time: The last date and time that this theme was updated.
        :param latest_version_number: The latest version number for the theme.
        :param name: the display name for the theme.
        :param theme_id: The ID of the theme. This ID is unique per AWS Region for each AWS account.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if last_updated_time is not None:
            self._values["last_updated_time"] = last_updated_time
        if latest_version_number is not None:
            self._values["latest_version_number"] = latest_version_number
        if name is not None:
            self._values["name"] = name
        if theme_id is not None:
            self._values["theme_id"] = theme_id

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The date and time that this theme was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def last_updated_time(self) -> typing.Optional[datetime.datetime]:
        '''The last date and time that this theme was updated.'''
        result = self._values.get("last_updated_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''The latest version number for the theme.'''
        result = self._values.get("latest_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''the display name for the theme.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def theme_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the theme.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("theme_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThemeSummary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ThemeVersion",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "base_theme_id": "baseThemeId",
        "configuration": "configuration",
        "created_time": "createdTime",
        "description": "description",
        "errors": "errors",
        "status": "status",
        "version_number": "versionNumber",
    },
)
class ThemeVersion:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        base_theme_id: typing.Optional[builtins.str] = None,
        configuration: typing.Optional[ThemeConfiguration] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        description: typing.Optional[builtins.str] = None,
        errors: typing.Optional[typing.Sequence[ThemeError]] = None,
        status: typing.Optional[builtins.str] = None,
        version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param base_theme_id: The Amazon QuickSight-defined ID of the theme that a custom theme inherits from. All themes initially inherit from a default QuickSight theme.
        :param configuration: The theme configuration, which contains all the theme display properties.
        :param created_time: The date and time that this theme version was created.
        :param description: The description of the theme.
        :param errors: Errors associated with the theme.
        :param status: The status of the theme version.
        :param version_number: The version number of the theme.
        '''
        if isinstance(configuration, dict):
            configuration = ThemeConfiguration(**configuration)
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if base_theme_id is not None:
            self._values["base_theme_id"] = base_theme_id
        if configuration is not None:
            self._values["configuration"] = configuration
        if created_time is not None:
            self._values["created_time"] = created_time
        if description is not None:
            self._values["description"] = description
        if errors is not None:
            self._values["errors"] = errors
        if status is not None:
            self._values["status"] = status
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def base_theme_id(self) -> typing.Optional[builtins.str]:
        '''The Amazon QuickSight-defined ID of the theme that a custom theme inherits from.

        All themes initially inherit from a default QuickSight theme.
        '''
        result = self._values.get("base_theme_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configuration(self) -> typing.Optional[ThemeConfiguration]:
        '''The theme configuration, which contains all the theme display properties.'''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[ThemeConfiguration], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The date and time that this theme version was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the theme.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def errors(self) -> typing.Optional[typing.List[ThemeError]]:
        '''Errors associated with the theme.'''
        result = self._values.get("errors")
        return typing.cast(typing.Optional[typing.List[ThemeError]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the theme version.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number of the theme.'''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThemeVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.ThemeVersionSummary",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "created_time": "createdTime",
        "description": "description",
        "status": "status",
        "version_number": "versionNumber",
    },
)
class ThemeVersionSummary:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        created_time: typing.Optional[datetime.datetime] = None,
        description: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the theme version.
        :param created_time: The date and time that this theme version was created.
        :param description: The description of the theme version.
        :param status: The status of the theme version.
        :param version_number: The version number of the theme version.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if created_time is not None:
            self._values["created_time"] = created_time
        if description is not None:
            self._values["description"] = description
        if status is not None:
            self._values["status"] = status
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the theme version.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_time(self) -> typing.Optional[datetime.datetime]:
        '''The date and time that this theme version was created.'''
        result = self._values.get("created_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the theme version.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the theme version.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number of the theme version.'''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThemeVersionSummary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TileLayoutStyle",
    jsii_struct_bases=[],
    name_mapping={"gutter": "gutter", "margin": "margin"},
)
class TileLayoutStyle:
    def __init__(
        self,
        *,
        gutter: typing.Optional[GutterStyle] = None,
        margin: typing.Optional[MarginStyle] = None,
    ) -> None:
        '''
        :param gutter: The gutter settings that apply between tiles.
        :param margin: The margin settings that apply around the outside edge of sheets.
        '''
        if isinstance(gutter, dict):
            gutter = GutterStyle(**gutter)
        if isinstance(margin, dict):
            margin = MarginStyle(**margin)
        self._values: typing.Dict[str, typing.Any] = {}
        if gutter is not None:
            self._values["gutter"] = gutter
        if margin is not None:
            self._values["margin"] = margin

    @builtins.property
    def gutter(self) -> typing.Optional[GutterStyle]:
        '''The gutter settings that apply between tiles.'''
        result = self._values.get("gutter")
        return typing.cast(typing.Optional[GutterStyle], result)

    @builtins.property
    def margin(self) -> typing.Optional[MarginStyle]:
        '''The margin settings that apply around the outside edge of sheets.'''
        result = self._values.get("margin")
        return typing.cast(typing.Optional[MarginStyle], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TileLayoutStyle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TileStyle",
    jsii_struct_bases=[],
    name_mapping={"border": "border"},
)
class TileStyle:
    def __init__(self, *, border: typing.Optional[BorderStyle] = None) -> None:
        '''
        :param border: The border around a tile.
        '''
        if isinstance(border, dict):
            border = BorderStyle(**border)
        self._values: typing.Dict[str, typing.Any] = {}
        if border is not None:
            self._values["border"] = border

    @builtins.property
    def border(self) -> typing.Optional[BorderStyle]:
        '''The border around a tile.'''
        result = self._values.get("border")
        return typing.cast(typing.Optional[BorderStyle], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TileStyle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TransformOperation",
    jsii_struct_bases=[],
    name_mapping={
        "cast_column_type_operation": "castColumnTypeOperation",
        "create_columns_operation": "createColumnsOperation",
        "filter_operation": "filterOperation",
        "project_operation": "projectOperation",
        "rename_column_operation": "renameColumnOperation",
        "tag_column_operation": "tagColumnOperation",
    },
)
class TransformOperation:
    def __init__(
        self,
        *,
        cast_column_type_operation: typing.Optional[CastColumnTypeOperation] = None,
        create_columns_operation: typing.Optional[CreateColumnsOperation] = None,
        filter_operation: typing.Optional[FilterOperation] = None,
        project_operation: typing.Optional[ProjectOperation] = None,
        rename_column_operation: typing.Optional[RenameColumnOperation] = None,
        tag_column_operation: typing.Optional[TagColumnOperation] = None,
    ) -> None:
        '''
        :param cast_column_type_operation: A transform operation that casts a column to a different type.
        :param create_columns_operation: An operation that creates calculated columns. Columns created in one such operation form a lexical closure.
        :param filter_operation: An operation that filters rows based on some condition.
        :param project_operation: An operation that projects columns. Operations that come after a projection can only refer to projected columns.
        :param rename_column_operation: An operation that renames a column.
        :param tag_column_operation: An operation that tags a column with additional information.
        '''
        if isinstance(cast_column_type_operation, dict):
            cast_column_type_operation = CastColumnTypeOperation(**cast_column_type_operation)
        if isinstance(create_columns_operation, dict):
            create_columns_operation = CreateColumnsOperation(**create_columns_operation)
        if isinstance(filter_operation, dict):
            filter_operation = FilterOperation(**filter_operation)
        if isinstance(project_operation, dict):
            project_operation = ProjectOperation(**project_operation)
        if isinstance(rename_column_operation, dict):
            rename_column_operation = RenameColumnOperation(**rename_column_operation)
        if isinstance(tag_column_operation, dict):
            tag_column_operation = TagColumnOperation(**tag_column_operation)
        self._values: typing.Dict[str, typing.Any] = {}
        if cast_column_type_operation is not None:
            self._values["cast_column_type_operation"] = cast_column_type_operation
        if create_columns_operation is not None:
            self._values["create_columns_operation"] = create_columns_operation
        if filter_operation is not None:
            self._values["filter_operation"] = filter_operation
        if project_operation is not None:
            self._values["project_operation"] = project_operation
        if rename_column_operation is not None:
            self._values["rename_column_operation"] = rename_column_operation
        if tag_column_operation is not None:
            self._values["tag_column_operation"] = tag_column_operation

    @builtins.property
    def cast_column_type_operation(self) -> typing.Optional[CastColumnTypeOperation]:
        '''A transform operation that casts a column to a different type.'''
        result = self._values.get("cast_column_type_operation")
        return typing.cast(typing.Optional[CastColumnTypeOperation], result)

    @builtins.property
    def create_columns_operation(self) -> typing.Optional[CreateColumnsOperation]:
        '''An operation that creates calculated columns.

        Columns created in one such operation form a lexical closure.
        '''
        result = self._values.get("create_columns_operation")
        return typing.cast(typing.Optional[CreateColumnsOperation], result)

    @builtins.property
    def filter_operation(self) -> typing.Optional[FilterOperation]:
        '''An operation that filters rows based on some condition.'''
        result = self._values.get("filter_operation")
        return typing.cast(typing.Optional[FilterOperation], result)

    @builtins.property
    def project_operation(self) -> typing.Optional[ProjectOperation]:
        '''An operation that projects columns.

        Operations that come after a projection can only refer to projected columns.
        '''
        result = self._values.get("project_operation")
        return typing.cast(typing.Optional[ProjectOperation], result)

    @builtins.property
    def rename_column_operation(self) -> typing.Optional[RenameColumnOperation]:
        '''An operation that renames a column.'''
        result = self._values.get("rename_column_operation")
        return typing.cast(typing.Optional[RenameColumnOperation], result)

    @builtins.property
    def tag_column_operation(self) -> typing.Optional[TagColumnOperation]:
        '''An operation that tags a column with additional information.'''
        result = self._values.get("tag_column_operation")
        return typing.cast(typing.Optional[TagColumnOperation], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransformOperation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.TwitterParameters",
    jsii_struct_bases=[],
    name_mapping={"max_rows": "maxRows", "query": "query"},
)
class TwitterParameters:
    def __init__(self, *, max_rows: jsii.Number, query: builtins.str) -> None:
        '''
        :param max_rows: Maximum number of rows to query Twitter.
        :param query: Twitter query string.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "max_rows": max_rows,
            "query": query,
        }

    @builtins.property
    def max_rows(self) -> jsii.Number:
        '''Maximum number of rows to query Twitter.'''
        result = self._values.get("max_rows")
        assert result is not None, "Required property 'max_rows' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Twitter query string.'''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TwitterParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UIColorPalette",
    jsii_struct_bases=[],
    name_mapping={
        "accent": "accent",
        "accent_foreground": "accentForeground",
        "danger": "danger",
        "danger_foreground": "dangerForeground",
        "dimension": "dimension",
        "dimension_foreground": "dimensionForeground",
        "measure": "measure",
        "measure_foreground": "measureForeground",
        "primary_background": "primaryBackground",
        "primary_foreground": "primaryForeground",
        "secondary_background": "secondaryBackground",
        "secondary_foreground": "secondaryForeground",
        "success": "success",
        "success_foreground": "successForeground",
        "warning": "warning",
        "warning_foreground": "warningForeground",
    },
)
class UIColorPalette:
    def __init__(
        self,
        *,
        accent: typing.Optional[builtins.str] = None,
        accent_foreground: typing.Optional[builtins.str] = None,
        danger: typing.Optional[builtins.str] = None,
        danger_foreground: typing.Optional[builtins.str] = None,
        dimension: typing.Optional[builtins.str] = None,
        dimension_foreground: typing.Optional[builtins.str] = None,
        measure: typing.Optional[builtins.str] = None,
        measure_foreground: typing.Optional[builtins.str] = None,
        primary_background: typing.Optional[builtins.str] = None,
        primary_foreground: typing.Optional[builtins.str] = None,
        secondary_background: typing.Optional[builtins.str] = None,
        secondary_foreground: typing.Optional[builtins.str] = None,
        success: typing.Optional[builtins.str] = None,
        success_foreground: typing.Optional[builtins.str] = None,
        warning: typing.Optional[builtins.str] = None,
        warning_foreground: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accent: This color is that applies to selected states and buttons.
        :param accent_foreground: The foreground color that applies to any text or other elements that appear over the accent color.
        :param danger: The color that applies to error messages.
        :param danger_foreground: The foreground color that applies to any text or other elements that appear over the error color.
        :param dimension: The color that applies to the names of fields that are identified as dimensions.
        :param dimension_foreground: The foreground color that applies to any text or other elements that appear over the dimension color.
        :param measure: The color that applies to the names of fields that are identified as measures.
        :param measure_foreground: The foreground color that applies to any text or other elements that appear over the measure color.
        :param primary_background: The background color that applies to visuals and other high emphasis UI.
        :param primary_foreground: The color of text and other foreground elements that appear over the primary background regions, such as grid lines, borders, table banding, icons, and so on.
        :param secondary_background: The background color that applies to the sheet background and sheet controls.
        :param secondary_foreground: The foreground color that applies to any sheet title, sheet control text, or UI that appears over the secondary background.
        :param success: The color that applies to success messages, for example the check mark for a successful download.
        :param success_foreground: The foreground color that applies to any text or other elements that appear over the success color.
        :param warning: This color that applies to warning and informational messages.
        :param warning_foreground: The foreground color that applies to any text or other elements that appear over the warning color.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if accent is not None:
            self._values["accent"] = accent
        if accent_foreground is not None:
            self._values["accent_foreground"] = accent_foreground
        if danger is not None:
            self._values["danger"] = danger
        if danger_foreground is not None:
            self._values["danger_foreground"] = danger_foreground
        if dimension is not None:
            self._values["dimension"] = dimension
        if dimension_foreground is not None:
            self._values["dimension_foreground"] = dimension_foreground
        if measure is not None:
            self._values["measure"] = measure
        if measure_foreground is not None:
            self._values["measure_foreground"] = measure_foreground
        if primary_background is not None:
            self._values["primary_background"] = primary_background
        if primary_foreground is not None:
            self._values["primary_foreground"] = primary_foreground
        if secondary_background is not None:
            self._values["secondary_background"] = secondary_background
        if secondary_foreground is not None:
            self._values["secondary_foreground"] = secondary_foreground
        if success is not None:
            self._values["success"] = success
        if success_foreground is not None:
            self._values["success_foreground"] = success_foreground
        if warning is not None:
            self._values["warning"] = warning
        if warning_foreground is not None:
            self._values["warning_foreground"] = warning_foreground

    @builtins.property
    def accent(self) -> typing.Optional[builtins.str]:
        '''This color is that applies to selected states and buttons.'''
        result = self._values.get("accent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def accent_foreground(self) -> typing.Optional[builtins.str]:
        '''The foreground color that applies to any text or other elements that appear over the accent color.'''
        result = self._values.get("accent_foreground")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def danger(self) -> typing.Optional[builtins.str]:
        '''The color that applies to error messages.'''
        result = self._values.get("danger")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def danger_foreground(self) -> typing.Optional[builtins.str]:
        '''The foreground color that applies to any text or other elements that appear over the error color.'''
        result = self._values.get("danger_foreground")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimension(self) -> typing.Optional[builtins.str]:
        '''The color that applies to the names of fields that are identified as dimensions.'''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimension_foreground(self) -> typing.Optional[builtins.str]:
        '''The foreground color that applies to any text or other elements that appear over the dimension color.'''
        result = self._values.get("dimension_foreground")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def measure(self) -> typing.Optional[builtins.str]:
        '''The color that applies to the names of fields that are identified as measures.'''
        result = self._values.get("measure")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def measure_foreground(self) -> typing.Optional[builtins.str]:
        '''The foreground color that applies to any text or other elements that appear over the measure color.'''
        result = self._values.get("measure_foreground")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_background(self) -> typing.Optional[builtins.str]:
        '''The background color that applies to visuals and other high emphasis UI.'''
        result = self._values.get("primary_background")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_foreground(self) -> typing.Optional[builtins.str]:
        '''The color of text and other foreground elements that appear over the primary background regions, such as grid lines, borders, table banding, icons, and so on.'''
        result = self._values.get("primary_foreground")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secondary_background(self) -> typing.Optional[builtins.str]:
        '''The background color that applies to the sheet background and sheet controls.'''
        result = self._values.get("secondary_background")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secondary_foreground(self) -> typing.Optional[builtins.str]:
        '''The foreground color that applies to any sheet title, sheet control text, or UI that appears over the secondary background.'''
        result = self._values.get("secondary_foreground")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def success(self) -> typing.Optional[builtins.str]:
        '''The color that applies to success messages, for example the check mark for a successful download.'''
        result = self._values.get("success")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def success_foreground(self) -> typing.Optional[builtins.str]:
        '''The foreground color that applies to any text or other elements that appear over the success color.'''
        result = self._values.get("success_foreground")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warning(self) -> typing.Optional[builtins.str]:
        '''This color that applies to warning and informational messages.'''
        result = self._values.get("warning")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warning_foreground(self) -> typing.Optional[builtins.str]:
        '''The foreground color that applies to any text or other elements that appear over the warning color.'''
        result = self._values.get("warning_foreground")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UIColorPalette(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UntagResourceRequest",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "tag_keys": "tagKeys"},
)
class UntagResourceRequest:
    def __init__(
        self,
        *,
        resource_arn: builtins.str,
        tag_keys: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to untag.
        :param tag_keys: The keys of the key-value pairs for the resource tag or tags assigned to the resource.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource that you want to untag.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag_keys(self) -> typing.List[builtins.str]:
        '''The keys of the key-value pairs for the resource tag or tags assigned to the resource.'''
        result = self._values.get("tag_keys")
        assert result is not None, "Required property 'tag_keys' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UntagResourceRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UntagResourceResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status"},
)
class UntagResourceResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UntagResourceResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateAccountCustomizationRequest",
    jsii_struct_bases=[],
    name_mapping={
        "account_customization": "accountCustomization",
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
    },
)
class UpdateAccountCustomizationRequest:
    def __init__(
        self,
        *,
        account_customization: AccountCustomization,
        aws_account_id: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_customization: The QuickSight customizations you're updating in the current AWS Region.
        :param aws_account_id: The ID for the AWS account that you want to update QuickSight customizations for.
        :param namespace: The namespace that you want to update QuickSight customizations for.
        '''
        if isinstance(account_customization, dict):
            account_customization = AccountCustomization(**account_customization)
        self._values: typing.Dict[str, typing.Any] = {
            "account_customization": account_customization,
            "aws_account_id": aws_account_id,
        }
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def account_customization(self) -> AccountCustomization:
        '''The QuickSight customizations you're updating in the current AWS Region.'''
        result = self._values.get("account_customization")
        assert result is not None, "Required property 'account_customization' is missing"
        return typing.cast(AccountCustomization, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that you want to update QuickSight customizations for.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace that you want to update QuickSight customizations for.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateAccountCustomizationRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateAccountCustomizationResponse",
    jsii_struct_bases=[],
    name_mapping={
        "account_customization": "accountCustomization",
        "arn": "arn",
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "request_id": "requestId",
        "status": "status",
    },
)
class UpdateAccountCustomizationResponse:
    def __init__(
        self,
        *,
        account_customization: typing.Optional[AccountCustomization] = None,
        arn: typing.Optional[builtins.str] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param account_customization: The QuickSight customizations you're updating in the current AWS Region.
        :param arn: The Amazon Resource Name (ARN) for the updated customization for this AWS account.
        :param aws_account_id: The ID for the AWS account that you want to update QuickSight customizations for.
        :param namespace: The namespace associated with the customization that you're updating.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(account_customization, dict):
            account_customization = AccountCustomization(**account_customization)
        self._values: typing.Dict[str, typing.Any] = {}
        if account_customization is not None:
            self._values["account_customization"] = account_customization
        if arn is not None:
            self._values["arn"] = arn
        if aws_account_id is not None:
            self._values["aws_account_id"] = aws_account_id
        if namespace is not None:
            self._values["namespace"] = namespace
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def account_customization(self) -> typing.Optional[AccountCustomization]:
        '''The QuickSight customizations you're updating in the current AWS Region.'''
        result = self._values.get("account_customization")
        return typing.cast(typing.Optional[AccountCustomization], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the updated customization for this AWS account.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the AWS account that you want to update QuickSight customizations for.'''
        result = self._values.get("aws_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace associated with the customization that you're updating.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateAccountCustomizationResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateAccountSettingsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "default_namespace": "defaultNamespace",
        "notification_email": "notificationEmail",
    },
)
class UpdateAccountSettingsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        default_namespace: builtins.str,
        notification_email: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that contains the QuickSight settings that you want to list.
        :param default_namespace: The default namespace for this AWS account. Currently, the default is default. AWS Identity and Access Management (IAM) users that register for the first time with QuickSight provide an email that becomes associated with the default namespace.
        :param notification_email: The email address that you want QuickSight to send notifications to regarding your AWS account or QuickSight subscription.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "default_namespace": default_namespace,
        }
        if notification_email is not None:
            self._values["notification_email"] = notification_email

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that contains the QuickSight settings that you want to list.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_namespace(self) -> builtins.str:
        '''The default namespace for this AWS account.

        Currently, the default is default. AWS Identity and Access Management (IAM) users that register for the first time with QuickSight provide an email that becomes associated with the default namespace.
        '''
        result = self._values.get("default_namespace")
        assert result is not None, "Required property 'default_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notification_email(self) -> typing.Optional[builtins.str]:
        '''The email address that you want QuickSight to send notifications to regarding your AWS account or QuickSight subscription.'''
        result = self._values.get("notification_email")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateAccountSettingsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateAccountSettingsResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status"},
)
class UpdateAccountSettingsResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateAccountSettingsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateAnalysisPermissionsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_id": "analysisId",
        "aws_account_id": "awsAccountId",
        "grant_permissions": "grantPermissions",
        "revoke_permissions": "revokePermissions",
    },
)
class UpdateAnalysisPermissionsRequest:
    def __init__(
        self,
        *,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
        grant_permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
        revoke_permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
    ) -> None:
        '''
        :param analysis_id: The ID of the analysis whose permissions you're updating. The ID is part of the analysis URL.
        :param aws_account_id: The ID of the AWS account that contains the analysis whose permissions you're updating. You must be using the AWS account that the analysis is in.
        :param grant_permissions: A structure that describes the permissions to add and the principal to add them to.
        :param revoke_permissions: A structure that describes the permissions to remove and the principal to remove them from.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "analysis_id": analysis_id,
            "aws_account_id": aws_account_id,
        }
        if grant_permissions is not None:
            self._values["grant_permissions"] = grant_permissions
        if revoke_permissions is not None:
            self._values["revoke_permissions"] = revoke_permissions

    @builtins.property
    def analysis_id(self) -> builtins.str:
        '''The ID of the analysis whose permissions you're updating.

        The ID is part of the analysis URL.
        '''
        result = self._values.get("analysis_id")
        assert result is not None, "Required property 'analysis_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the analysis whose permissions you're updating.

        You must be using the AWS account that the analysis is in.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def grant_permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''A structure that describes the permissions to add and the principal to add them to.'''
        result = self._values.get("grant_permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    @builtins.property
    def revoke_permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''A structure that describes the permissions to remove and the principal to remove them from.'''
        result = self._values.get("revoke_permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateAnalysisPermissionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateAnalysisPermissionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_arn": "analysisArn",
        "analysis_id": "analysisId",
        "permissions": "permissions",
        "request_id": "requestId",
        "status": "status",
    },
)
class UpdateAnalysisPermissionsResponse:
    def __init__(
        self,
        *,
        analysis_arn: typing.Optional[builtins.str] = None,
        analysis_id: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param analysis_arn: The Amazon Resource Name (ARN) of the analysis that you updated.
        :param analysis_id: The ID of the analysis that you updated permissions for.
        :param permissions: A structure that describes the principals and the resource-level permissions on an analysis.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if analysis_arn is not None:
            self._values["analysis_arn"] = analysis_arn
        if analysis_id is not None:
            self._values["analysis_id"] = analysis_id
        if permissions is not None:
            self._values["permissions"] = permissions
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def analysis_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the analysis that you updated.'''
        result = self._values.get("analysis_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def analysis_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the analysis that you updated permissions for.'''
        result = self._values.get("analysis_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''A structure that describes the principals and the resource-level permissions on an analysis.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateAnalysisPermissionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateAnalysisRequest",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_id": "analysisId",
        "aws_account_id": "awsAccountId",
        "name": "name",
        "source_entity": "sourceEntity",
        "parameters": "parameters",
        "theme_arn": "themeArn",
    },
)
class UpdateAnalysisRequest:
    def __init__(
        self,
        *,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
        name: builtins.str,
        source_entity: AnalysisSourceEntity,
        parameters: typing.Optional[Parameters] = None,
        theme_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param analysis_id: The ID for the analysis that you're updating. This ID displays in the URL of the analysis.
        :param aws_account_id: The ID of the AWS account that contains the analysis that you're updating.
        :param name: A descriptive name for the analysis that you're updating. This name displays for the analysis in the QuickSight console.
        :param source_entity: A source entity to use for the analysis that you're updating. This metadata structure contains details that describe a source template and one or more datasets.
        :param parameters: The parameter names and override values that you want to use. An analysis can have any parameter type, and some parameters might accept multiple values.
        :param theme_arn: The Amazon Resource Name (ARN) for the theme to apply to the analysis that you're creating. To see the theme in the QuickSight console, make sure that you have access to it.
        '''
        if isinstance(source_entity, dict):
            source_entity = AnalysisSourceEntity(**source_entity)
        if isinstance(parameters, dict):
            parameters = Parameters(**parameters)
        self._values: typing.Dict[str, typing.Any] = {
            "analysis_id": analysis_id,
            "aws_account_id": aws_account_id,
            "name": name,
            "source_entity": source_entity,
        }
        if parameters is not None:
            self._values["parameters"] = parameters
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn

    @builtins.property
    def analysis_id(self) -> builtins.str:
        '''The ID for the analysis that you're updating.

        This ID displays in the URL of the analysis.
        '''
        result = self._values.get("analysis_id")
        assert result is not None, "Required property 'analysis_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the analysis that you're updating.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A descriptive name for the analysis that you're updating.

        This name displays for the analysis in the QuickSight console.
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_entity(self) -> AnalysisSourceEntity:
        '''A source entity to use for the analysis that you're updating.

        This metadata structure contains details that describe a source template and one or more datasets.
        '''
        result = self._values.get("source_entity")
        assert result is not None, "Required property 'source_entity' is missing"
        return typing.cast(AnalysisSourceEntity, result)

    @builtins.property
    def parameters(self) -> typing.Optional[Parameters]:
        '''The parameter names and override values that you want to use.

        An analysis can have any parameter type, and some parameters might accept multiple values.
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[Parameters], result)

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the theme to apply to the analysis that you're creating.

        To see the theme in the QuickSight console, make sure that you have access to it.
        '''
        result = self._values.get("theme_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateAnalysisRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateAnalysisResponse",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_id": "analysisId",
        "arn": "arn",
        "request_id": "requestId",
        "status": "status",
        "update_status": "updateStatus",
    },
)
class UpdateAnalysisResponse:
    def __init__(
        self,
        *,
        analysis_id: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        update_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param analysis_id: The ID of the analysis.
        :param arn: The ARN of the analysis that you're updating.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param update_status: The update status of the last update that was made to the analysis.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if analysis_id is not None:
            self._values["analysis_id"] = analysis_id
        if arn is not None:
            self._values["arn"] = arn
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if update_status is not None:
            self._values["update_status"] = update_status

    @builtins.property
    def analysis_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the analysis.'''
        result = self._values.get("analysis_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the analysis that you're updating.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def update_status(self) -> typing.Optional[builtins.str]:
        '''The update status of the last update that was made to the analysis.'''
        result = self._values.get("update_status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateAnalysisResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDashboardPermissionsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dashboard_id": "dashboardId",
        "grant_permissions": "grantPermissions",
        "revoke_permissions": "revokePermissions",
    },
)
class UpdateDashboardPermissionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
        grant_permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
        revoke_permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the dashboard whose permissions you're updating.
        :param dashboard_id: The ID for the dashboard.
        :param grant_permissions: The permissions that you want to grant on this resource.
        :param revoke_permissions: The permissions that you want to revoke from this resource.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_id": dashboard_id,
        }
        if grant_permissions is not None:
            self._values["grant_permissions"] = grant_permissions
        if revoke_permissions is not None:
            self._values["revoke_permissions"] = revoke_permissions

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the dashboard whose permissions you're updating.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        '''The ID for the dashboard.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def grant_permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''The permissions that you want to grant on this resource.'''
        result = self._values.get("grant_permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    @builtins.property
    def revoke_permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''The permissions that you want to revoke from this resource.'''
        result = self._values.get("revoke_permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDashboardPermissionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDashboardPermissionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_arn": "dashboardArn",
        "dashboard_id": "dashboardId",
        "permissions": "permissions",
        "request_id": "requestId",
        "status": "status",
    },
)
class UpdateDashboardPermissionsResponse:
    def __init__(
        self,
        *,
        dashboard_arn: typing.Optional[builtins.str] = None,
        dashboard_id: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dashboard_arn: The Amazon Resource Name (ARN) of the dashboard.
        :param dashboard_id: The ID for the dashboard.
        :param permissions: Information about the permissions on the dashboard.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if dashboard_arn is not None:
            self._values["dashboard_arn"] = dashboard_arn
        if dashboard_id is not None:
            self._values["dashboard_id"] = dashboard_id
        if permissions is not None:
            self._values["permissions"] = permissions
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def dashboard_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the dashboard.'''
        result = self._values.get("dashboard_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dashboard_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the dashboard.'''
        result = self._values.get("dashboard_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''Information about the permissions on the dashboard.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDashboardPermissionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDashboardPublishedVersionRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dashboard_id": "dashboardId",
        "version_number": "versionNumber",
    },
)
class UpdateDashboardPublishedVersionRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
        version_number: jsii.Number,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the dashboard that you're updating.
        :param dashboard_id: The ID for the dashboard.
        :param version_number: The version number of the dashboard.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_id": dashboard_id,
            "version_number": version_number,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the dashboard that you're updating.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        '''The ID for the dashboard.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_number(self) -> jsii.Number:
        '''The version number of the dashboard.'''
        result = self._values.get("version_number")
        assert result is not None, "Required property 'version_number' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDashboardPublishedVersionRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDashboardPublishedVersionResponse",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_arn": "dashboardArn",
        "dashboard_id": "dashboardId",
        "request_id": "requestId",
        "status": "status",
    },
)
class UpdateDashboardPublishedVersionResponse:
    def __init__(
        self,
        *,
        dashboard_arn: typing.Optional[builtins.str] = None,
        dashboard_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dashboard_arn: The Amazon Resource Name (ARN) of the dashboard.
        :param dashboard_id: The ID for the dashboard.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if dashboard_arn is not None:
            self._values["dashboard_arn"] = dashboard_arn
        if dashboard_id is not None:
            self._values["dashboard_id"] = dashboard_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def dashboard_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the dashboard.'''
        result = self._values.get("dashboard_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dashboard_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the dashboard.'''
        result = self._values.get("dashboard_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDashboardPublishedVersionResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDashboardRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dashboard_id": "dashboardId",
        "name": "name",
        "source_entity": "sourceEntity",
        "dashboard_publish_options": "dashboardPublishOptions",
        "parameters": "parameters",
        "theme_arn": "themeArn",
        "version_description": "versionDescription",
    },
)
class UpdateDashboardRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_id: builtins.str,
        name: builtins.str,
        source_entity: DashboardSourceEntity,
        dashboard_publish_options: typing.Optional[DashboardPublishOptions] = None,
        parameters: typing.Optional[Parameters] = None,
        theme_arn: typing.Optional[builtins.str] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the dashboard that you're updating.
        :param dashboard_id: The ID for the dashboard.
        :param name: The display name of the dashboard.
        :param source_entity: The entity that you are using as a source when you update the dashboard. In SourceEntity, you specify the type of object you're using as source. You can only update a dashboard from a template, so you use a SourceTemplate entity. If you need to update a dashboard from an analysis, first convert the analysis to a template by using the CreateTemplate API operation. For SourceTemplate, specify the Amazon Resource Name (ARN) of the source template. The SourceTemplate ARN can contain any AWS Account and any QuickSight-supported AWS Region. Use the DataSetReferences entity within SourceTemplate to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder.
        :param dashboard_publish_options: Options for publishing the dashboard when you create it: AvailabilityStatus for AdHocFilteringOption - This status can be either ENABLED or DISABLED. When this is set to DISABLED, QuickSight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is ENABLED by default. AvailabilityStatus for ExportToCSVOption - This status can be either ENABLED or DISABLED. The visual option to export data to .CSV format isn't enabled when this is set to DISABLED. This option is ENABLED by default. VisibilityState for SheetControlsOption - This visibility state can be either COLLAPSED or EXPANDED. This option is COLLAPSED by default.
        :param parameters: A structure that contains the parameters of the dashboard. These are parameter overrides for a dashboard. A dashboard can have any type of parameters, and some parameters might accept multiple values.
        :param theme_arn: The Amazon Resource Name (ARN) of the theme that is being used for this dashboard. If you add a value for this field, it overrides the value that was originally associated with the entity. The theme ARN must exist in the same AWS account where you create the dashboard.
        :param version_description: A description for the first version of the dashboard being created.
        '''
        if isinstance(source_entity, dict):
            source_entity = DashboardSourceEntity(**source_entity)
        if isinstance(dashboard_publish_options, dict):
            dashboard_publish_options = DashboardPublishOptions(**dashboard_publish_options)
        if isinstance(parameters, dict):
            parameters = Parameters(**parameters)
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_id": dashboard_id,
            "name": name,
            "source_entity": source_entity,
        }
        if dashboard_publish_options is not None:
            self._values["dashboard_publish_options"] = dashboard_publish_options
        if parameters is not None:
            self._values["parameters"] = parameters
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the dashboard that you're updating.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        '''The ID for the dashboard.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The display name of the dashboard.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_entity(self) -> DashboardSourceEntity:
        '''The entity that you are using as a source when you update the dashboard.

        In SourceEntity, you specify the type of object you're using as source. You can only update a dashboard from a template, so you use a SourceTemplate entity. If you need to update a dashboard from an analysis, first convert the analysis to a template by using the CreateTemplate API operation. For SourceTemplate, specify the Amazon Resource Name (ARN) of the source template. The SourceTemplate ARN can contain any AWS Account and any QuickSight-supported AWS Region.  Use the DataSetReferences entity within SourceTemplate to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder.
        '''
        result = self._values.get("source_entity")
        assert result is not None, "Required property 'source_entity' is missing"
        return typing.cast(DashboardSourceEntity, result)

    @builtins.property
    def dashboard_publish_options(self) -> typing.Optional[DashboardPublishOptions]:
        '''Options for publishing the dashboard when you create it:    AvailabilityStatus for AdHocFilteringOption - This status can be either ENABLED or DISABLED.

        When this is set to DISABLED, QuickSight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is ENABLED by default.     AvailabilityStatus for ExportToCSVOption - This status can be either ENABLED or DISABLED. The visual option to export data to .CSV format isn't enabled when this is set to DISABLED. This option is ENABLED by default.     VisibilityState for SheetControlsOption - This visibility state can be either COLLAPSED or EXPANDED. This option is COLLAPSED by default.
        '''
        result = self._values.get("dashboard_publish_options")
        return typing.cast(typing.Optional[DashboardPublishOptions], result)

    @builtins.property
    def parameters(self) -> typing.Optional[Parameters]:
        '''A structure that contains the parameters of the dashboard.

        These are parameter overrides for a dashboard. A dashboard can have any type of parameters, and some parameters might accept multiple values.
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[Parameters], result)

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the theme that is being used for this dashboard.

        If you add a value for this field, it overrides the value that was originally associated with the entity. The theme ARN must exist in the same AWS account where you create the dashboard.
        '''
        result = self._values.get("theme_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''A description for the first version of the dashboard being created.'''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDashboardRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDashboardResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "creation_status": "creationStatus",
        "dashboard_id": "dashboardId",
        "request_id": "requestId",
        "status": "status",
        "version_arn": "versionArn",
    },
)
class UpdateDashboardResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        creation_status: typing.Optional[builtins.str] = None,
        dashboard_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the resource.
        :param creation_status: The creation status of the request.
        :param dashboard_id: The ID for the dashboard.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param version_arn: The ARN of the dashboard, including the version number.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if creation_status is not None:
            self._values["creation_status"] = creation_status
        if dashboard_id is not None:
            self._values["dashboard_id"] = dashboard_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if version_arn is not None:
            self._values["version_arn"] = version_arn

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_status(self) -> typing.Optional[builtins.str]:
        '''The creation status of the request.'''
        result = self._values.get("creation_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dashboard_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the dashboard.'''
        result = self._values.get("dashboard_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the dashboard, including the version number.'''
        result = self._values.get("version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDashboardResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDataSetPermissionsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_set_id": "dataSetId",
        "grant_permissions": "grantPermissions",
        "revoke_permissions": "revokePermissions",
    },
)
class UpdateDataSetPermissionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_id: builtins.str,
        grant_permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
        revoke_permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_set_id: The ID for the dataset whose permissions you want to update. This ID is unique per AWS Region for each AWS account.
        :param grant_permissions: The resource permissions that you want to grant to the dataset.
        :param revoke_permissions: The resource permissions that you want to revoke from the dataset.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_id": data_set_id,
        }
        if grant_permissions is not None:
            self._values["grant_permissions"] = grant_permissions
        if revoke_permissions is not None:
            self._values["revoke_permissions"] = revoke_permissions

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The ID for the dataset whose permissions you want to update.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def grant_permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''The resource permissions that you want to grant to the dataset.'''
        result = self._values.get("grant_permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    @builtins.property
    def revoke_permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''The resource permissions that you want to revoke from the dataset.'''
        result = self._values.get("revoke_permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDataSetPermissionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDataSetPermissionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "data_set_arn": "dataSetArn",
        "data_set_id": "dataSetId",
        "request_id": "requestId",
        "status": "status",
    },
)
class UpdateDataSetPermissionsResponse:
    def __init__(
        self,
        *,
        data_set_arn: typing.Optional[builtins.str] = None,
        data_set_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param data_set_arn: The Amazon Resource Name (ARN) of the dataset.
        :param data_set_id: The ID for the dataset whose permissions you want to update. This ID is unique per AWS Region for each AWS account.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if data_set_arn is not None:
            self._values["data_set_arn"] = data_set_arn
        if data_set_id is not None:
            self._values["data_set_id"] = data_set_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def data_set_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the dataset.'''
        result = self._values.get("data_set_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_set_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the dataset whose permissions you want to update.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDataSetPermissionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDataSetRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_set_id": "dataSetId",
        "import_mode": "importMode",
        "name": "name",
        "physical_table_map": "physicalTableMap",
        "column_groups": "columnGroups",
        "column_level_permission_rules": "columnLevelPermissionRules",
        "field_folders": "fieldFolders",
        "logical_table_map": "logicalTableMap",
        "row_level_permission_data_set": "rowLevelPermissionDataSet",
    },
)
class UpdateDataSetRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_id: builtins.str,
        import_mode: builtins.str,
        name: builtins.str,
        physical_table_map: typing.Mapping[builtins.str, PhysicalTable],
        column_groups: typing.Optional[typing.Sequence[ColumnGroup]] = None,
        column_level_permission_rules: typing.Optional[typing.Sequence[ColumnLevelPermissionRule]] = None,
        field_folders: typing.Optional[typing.Mapping[builtins.str, FieldFolder]] = None,
        logical_table_map: typing.Optional[typing.Mapping[builtins.str, LogicalTable]] = None,
        row_level_permission_data_set: typing.Optional[RowLevelPermissionDataSet] = None,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_set_id: The ID for the dataset that you want to update. This ID is unique per AWS Region for each AWS account.
        :param import_mode: Indicates whether you want to import the data into SPICE.
        :param name: The display name for the dataset.
        :param physical_table_map: Declares the physical tables that are available in the underlying data sources.
        :param column_groups: Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.
        :param column_level_permission_rules: A set of one or more definitions of a ColumnLevelPermissionRule .
        :param field_folders: The folder that contains fields and nested subfolders for your dataset.
        :param logical_table_map: Configures the combination and transformation of the data from the physical tables.
        :param row_level_permission_data_set: The row-level security configuration for the data you want to create.
        '''
        if isinstance(row_level_permission_data_set, dict):
            row_level_permission_data_set = RowLevelPermissionDataSet(**row_level_permission_data_set)
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_id": data_set_id,
            "import_mode": import_mode,
            "name": name,
            "physical_table_map": physical_table_map,
        }
        if column_groups is not None:
            self._values["column_groups"] = column_groups
        if column_level_permission_rules is not None:
            self._values["column_level_permission_rules"] = column_level_permission_rules
        if field_folders is not None:
            self._values["field_folders"] = field_folders
        if logical_table_map is not None:
            self._values["logical_table_map"] = logical_table_map
        if row_level_permission_data_set is not None:
            self._values["row_level_permission_data_set"] = row_level_permission_data_set

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The ID for the dataset that you want to update.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def import_mode(self) -> builtins.str:
        '''Indicates whether you want to import the data into SPICE.'''
        result = self._values.get("import_mode")
        assert result is not None, "Required property 'import_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The display name for the dataset.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def physical_table_map(self) -> typing.Mapping[builtins.str, PhysicalTable]:
        '''Declares the physical tables that are available in the underlying data sources.'''
        result = self._values.get("physical_table_map")
        assert result is not None, "Required property 'physical_table_map' is missing"
        return typing.cast(typing.Mapping[builtins.str, PhysicalTable], result)

    @builtins.property
    def column_groups(self) -> typing.Optional[typing.List[ColumnGroup]]:
        '''Groupings of columns that work together in certain QuickSight features.

        Currently, only geospatial hierarchy is supported.
        '''
        result = self._values.get("column_groups")
        return typing.cast(typing.Optional[typing.List[ColumnGroup]], result)

    @builtins.property
    def column_level_permission_rules(
        self,
    ) -> typing.Optional[typing.List[ColumnLevelPermissionRule]]:
        '''A set of one or more definitions of a  ColumnLevelPermissionRule .'''
        result = self._values.get("column_level_permission_rules")
        return typing.cast(typing.Optional[typing.List[ColumnLevelPermissionRule]], result)

    @builtins.property
    def field_folders(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, FieldFolder]]:
        '''The folder that contains fields and nested subfolders for your dataset.'''
        result = self._values.get("field_folders")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, FieldFolder]], result)

    @builtins.property
    def logical_table_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, LogicalTable]]:
        '''Configures the combination and transformation of the data from the physical tables.'''
        result = self._values.get("logical_table_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, LogicalTable]], result)

    @builtins.property
    def row_level_permission_data_set(
        self,
    ) -> typing.Optional[RowLevelPermissionDataSet]:
        '''The row-level security configuration for the data you want to create.'''
        result = self._values.get("row_level_permission_data_set")
        return typing.cast(typing.Optional[RowLevelPermissionDataSet], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDataSetRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDataSetResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "data_set_id": "dataSetId",
        "ingestion_arn": "ingestionArn",
        "ingestion_id": "ingestionId",
        "request_id": "requestId",
        "status": "status",
    },
)
class UpdateDataSetResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        data_set_id: typing.Optional[builtins.str] = None,
        ingestion_arn: typing.Optional[builtins.str] = None,
        ingestion_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the dataset.
        :param data_set_id: The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.
        :param ingestion_arn: The ARN for the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.
        :param ingestion_id: The ID of the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if data_set_id is not None:
            self._values["data_set_id"] = data_set_id
        if ingestion_arn is not None:
            self._values["ingestion_arn"] = ingestion_arn
        if ingestion_id is not None:
            self._values["ingestion_id"] = ingestion_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the dataset.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_set_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the dataset that you want to create.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingestion_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.'''
        result = self._values.get("ingestion_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingestion_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.'''
        result = self._values.get("ingestion_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDataSetResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDataSourcePermissionsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_source_id": "dataSourceId",
        "grant_permissions": "grantPermissions",
        "revoke_permissions": "revokePermissions",
    },
)
class UpdateDataSourcePermissionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_source_id: builtins.str,
        grant_permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
        revoke_permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_source_id: The ID of the data source. This ID is unique per AWS Region for each AWS account.
        :param grant_permissions: A list of resource permissions that you want to grant on the data source.
        :param revoke_permissions: A list of resource permissions that you want to revoke on the data source.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_source_id": data_source_id,
        }
        if grant_permissions is not None:
            self._values["grant_permissions"] = grant_permissions
        if revoke_permissions is not None:
            self._values["revoke_permissions"] = revoke_permissions

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''The ID of the data source.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def grant_permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''A list of resource permissions that you want to grant on the data source.'''
        result = self._values.get("grant_permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    @builtins.property
    def revoke_permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''A list of resource permissions that you want to revoke on the data source.'''
        result = self._values.get("revoke_permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDataSourcePermissionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDataSourcePermissionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "data_source_arn": "dataSourceArn",
        "data_source_id": "dataSourceId",
        "request_id": "requestId",
        "status": "status",
    },
)
class UpdateDataSourcePermissionsResponse:
    def __init__(
        self,
        *,
        data_source_arn: typing.Optional[builtins.str] = None,
        data_source_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param data_source_arn: The Amazon Resource Name (ARN) of the data source.
        :param data_source_id: The ID of the data source. This ID is unique per AWS Region for each AWS account.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if data_source_arn is not None:
            self._values["data_source_arn"] = data_source_arn
        if data_source_id is not None:
            self._values["data_source_id"] = data_source_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def data_source_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the data source.'''
        result = self._values.get("data_source_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_source_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the data source.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_source_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDataSourcePermissionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDataSourceRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_source_id": "dataSourceId",
        "name": "name",
        "credentials": "credentials",
        "data_source_parameters": "dataSourceParameters",
        "ssl_properties": "sslProperties",
        "vpc_connection_properties": "vpcConnectionProperties",
    },
)
class UpdateDataSourceRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_source_id: builtins.str,
        name: builtins.str,
        credentials: typing.Optional[DataSourceCredentials] = None,
        data_source_parameters: typing.Optional[DataSourceParameters] = None,
        ssl_properties: typing.Optional[SslProperties] = None,
        vpc_connection_properties: typing.Optional["VpcConnectionProperties"] = None,
    ) -> None:
        '''
        :param aws_account_id: The AWS account ID.
        :param data_source_id: The ID of the data source. This ID is unique per AWS Region for each AWS account.
        :param name: A display name for the data source.
        :param credentials: The credentials that QuickSight that uses to connect to your underlying source. Currently, only credentials based on user name and password are supported.
        :param data_source_parameters: The parameters that QuickSight uses to connect to your underlying source.
        :param ssl_properties: Secure Socket Layer (SSL) properties that apply when QuickSight connects to your underlying source.
        :param vpc_connection_properties: Use this parameter only when you want QuickSight to use a VPC connection when connecting to your underlying source.
        '''
        if isinstance(credentials, dict):
            credentials = DataSourceCredentials(**credentials)
        if isinstance(data_source_parameters, dict):
            data_source_parameters = DataSourceParameters(**data_source_parameters)
        if isinstance(ssl_properties, dict):
            ssl_properties = SslProperties(**ssl_properties)
        if isinstance(vpc_connection_properties, dict):
            vpc_connection_properties = VpcConnectionProperties(**vpc_connection_properties)
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_source_id": data_source_id,
            "name": name,
        }
        if credentials is not None:
            self._values["credentials"] = credentials
        if data_source_parameters is not None:
            self._values["data_source_parameters"] = data_source_parameters
        if ssl_properties is not None:
            self._values["ssl_properties"] = ssl_properties
        if vpc_connection_properties is not None:
            self._values["vpc_connection_properties"] = vpc_connection_properties

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AWS account ID.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''The ID of the data source.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A display name for the data source.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credentials(self) -> typing.Optional[DataSourceCredentials]:
        '''The credentials that QuickSight that uses to connect to your underlying source.

        Currently, only credentials based on user name and password are supported.
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[DataSourceCredentials], result)

    @builtins.property
    def data_source_parameters(self) -> typing.Optional[DataSourceParameters]:
        '''The parameters that QuickSight uses to connect to your underlying source.'''
        result = self._values.get("data_source_parameters")
        return typing.cast(typing.Optional[DataSourceParameters], result)

    @builtins.property
    def ssl_properties(self) -> typing.Optional[SslProperties]:
        '''Secure Socket Layer (SSL) properties that apply when QuickSight connects to your underlying source.'''
        result = self._values.get("ssl_properties")
        return typing.cast(typing.Optional[SslProperties], result)

    @builtins.property
    def vpc_connection_properties(self) -> typing.Optional["VpcConnectionProperties"]:
        '''Use this parameter only when you want QuickSight to use a VPC connection when connecting to your underlying source.'''
        result = self._values.get("vpc_connection_properties")
        return typing.cast(typing.Optional["VpcConnectionProperties"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDataSourceRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateDataSourceResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "data_source_id": "dataSourceId",
        "request_id": "requestId",
        "status": "status",
        "update_status": "updateStatus",
    },
)
class UpdateDataSourceResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        data_source_id: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        update_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) of the data source.
        :param data_source_id: The ID of the data source. This ID is unique per AWS Region for each AWS account.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param update_status: The update status of the data source's last update.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if data_source_id is not None:
            self._values["data_source_id"] = data_source_id
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if update_status is not None:
            self._values["update_status"] = update_status

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the data source.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_source_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the data source.

        This ID is unique per AWS Region for each AWS account.
        '''
        result = self._values.get("data_source_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def update_status(self) -> typing.Optional[builtins.str]:
        '''The update status of the data source's last update.'''
        result = self._values.get("update_status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateDataSourceResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateGroupRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "group_name": "groupName",
        "namespace": "namespace",
        "description": "description",
    },
)
class UpdateGroupRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        group_name: builtins.str,
        namespace: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param group_name: The name of the group that you want to update.
        :param namespace: The namespace. Currently, you should set this to default.
        :param description: The description for the group that you want to update.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "group_name": group_name,
            "namespace": namespace,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the group is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The name of the group that you want to update.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the group that you want to update.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateGroupRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateGroupResponse",
    jsii_struct_bases=[],
    name_mapping={"group": "group", "request_id": "requestId", "status": "status"},
)
class UpdateGroupResponse:
    def __init__(
        self,
        *,
        group: typing.Optional[Group] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group: The name of the group.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        if isinstance(group, dict):
            group = Group(**group)
        self._values: typing.Dict[str, typing.Any] = {}
        if group is not None:
            self._values["group"] = group
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def group(self) -> typing.Optional[Group]:
        '''The name of the group.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional[Group], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateGroupResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateIAMPolicyAssignmentRequest",
    jsii_struct_bases=[],
    name_mapping={
        "assignment_name": "assignmentName",
        "aws_account_id": "awsAccountId",
        "namespace": "namespace",
        "assignment_status": "assignmentStatus",
        "identities": "identities",
        "policy_arn": "policyArn",
    },
)
class UpdateIAMPolicyAssignmentRequest:
    def __init__(
        self,
        *,
        assignment_name: builtins.str,
        aws_account_id: builtins.str,
        namespace: builtins.str,
        assignment_status: typing.Optional[builtins.str] = None,
        identities: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[builtins.str]]] = None,
        policy_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param assignment_name: The name of the assignment, also called a rule. This name must be unique within an AWS account.
        :param aws_account_id: The ID of the AWS account that contains the IAM policy assignment.
        :param namespace: The namespace of the assignment.
        :param assignment_status: The status of the assignment. Possible values are as follows: ENABLED - Anything specified in this assignment is used when creating the data source. DISABLED - This assignment isn't used when creating the data source. DRAFT - This assignment is an unfinished draft and isn't used when creating the data source.
        :param identities: The QuickSight users, groups, or both that you want to assign the policy to.
        :param policy_arn: The ARN for the IAM policy to apply to the QuickSight users and groups specified in this assignment.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "assignment_name": assignment_name,
            "aws_account_id": aws_account_id,
            "namespace": namespace,
        }
        if assignment_status is not None:
            self._values["assignment_status"] = assignment_status
        if identities is not None:
            self._values["identities"] = identities
        if policy_arn is not None:
            self._values["policy_arn"] = policy_arn

    @builtins.property
    def assignment_name(self) -> builtins.str:
        '''The name of the assignment, also called a rule.

        This name must be unique within an AWS account.
        '''
        result = self._values.get("assignment_name")
        assert result is not None, "Required property 'assignment_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the IAM policy assignment.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace of the assignment.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assignment_status(self) -> typing.Optional[builtins.str]:
        '''The status of the assignment.

        Possible values are as follows:    ENABLED - Anything specified in this assignment is used when creating the data source.    DISABLED - This assignment isn't used when creating the data source.    DRAFT - This assignment is an unfinished draft and isn't used when creating the data source.
        '''
        result = self._values.get("assignment_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identities(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]]:
        '''The QuickSight users, groups, or both that you want to assign the policy to.'''
        result = self._values.get("identities")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]], result)

    @builtins.property
    def policy_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the IAM policy to apply to the QuickSight users and groups specified in this assignment.'''
        result = self._values.get("policy_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateIAMPolicyAssignmentRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateIAMPolicyAssignmentResponse",
    jsii_struct_bases=[],
    name_mapping={
        "assignment_id": "assignmentId",
        "assignment_name": "assignmentName",
        "assignment_status": "assignmentStatus",
        "identities": "identities",
        "policy_arn": "policyArn",
        "request_id": "requestId",
        "status": "status",
    },
)
class UpdateIAMPolicyAssignmentResponse:
    def __init__(
        self,
        *,
        assignment_id: typing.Optional[builtins.str] = None,
        assignment_name: typing.Optional[builtins.str] = None,
        assignment_status: typing.Optional[builtins.str] = None,
        identities: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[builtins.str]]] = None,
        policy_arn: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param assignment_id: The ID of the assignment.
        :param assignment_name: The name of the assignment or rule.
        :param assignment_status: The status of the assignment. Possible values are as follows: ENABLED - Anything specified in this assignment is used when creating the data source. DISABLED - This assignment isn't used when creating the data source. DRAFT - This assignment is an unfinished draft and isn't used when creating the data source.
        :param identities: The QuickSight users, groups, or both that the IAM policy is assigned to.
        :param policy_arn: The ARN for the IAM policy applied to the QuickSight users and groups specified in this assignment.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if assignment_id is not None:
            self._values["assignment_id"] = assignment_id
        if assignment_name is not None:
            self._values["assignment_name"] = assignment_name
        if assignment_status is not None:
            self._values["assignment_status"] = assignment_status
        if identities is not None:
            self._values["identities"] = identities
        if policy_arn is not None:
            self._values["policy_arn"] = policy_arn
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def assignment_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the assignment.'''
        result = self._values.get("assignment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assignment_name(self) -> typing.Optional[builtins.str]:
        '''The name of the assignment or rule.'''
        result = self._values.get("assignment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assignment_status(self) -> typing.Optional[builtins.str]:
        '''The status of the assignment.

        Possible values are as follows:    ENABLED - Anything specified in this assignment is used when creating the data source.    DISABLED - This assignment isn't used when creating the data source.    DRAFT - This assignment is an unfinished draft and isn't used when creating the data source.
        '''
        result = self._values.get("assignment_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identities(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]]:
        '''The QuickSight users, groups, or both that the IAM policy is assigned to.'''
        result = self._values.get("identities")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]], result)

    @builtins.property
    def policy_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the IAM policy applied to the QuickSight users and groups specified in this assignment.'''
        result = self._values.get("policy_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateIAMPolicyAssignmentResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateTemplateAliasRequest",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "aws_account_id": "awsAccountId",
        "template_id": "templateId",
        "template_version_number": "templateVersionNumber",
    },
)
class UpdateTemplateAliasRequest:
    def __init__(
        self,
        *,
        alias_name: builtins.str,
        aws_account_id: builtins.str,
        template_id: builtins.str,
        template_version_number: jsii.Number,
    ) -> None:
        '''
        :param alias_name: The alias of the template that you want to update. If you name a specific alias, you update the version that the alias points to. You can specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter. The keyword $PUBLISHED doesn't apply to templates.
        :param aws_account_id: The ID of the AWS account that contains the template alias that you're updating.
        :param template_id: The ID for the template.
        :param template_version_number: The version number of the template.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alias_name": alias_name,
            "aws_account_id": aws_account_id,
            "template_id": template_id,
            "template_version_number": template_version_number,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''The alias of the template that you want to update.

        If you name a specific alias, you update the version that the alias points to. You can specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter. The keyword $PUBLISHED doesn't apply to templates.
        '''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the template alias that you're updating.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The ID for the template.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_version_number(self) -> jsii.Number:
        '''The version number of the template.'''
        result = self._values.get("template_version_number")
        assert result is not None, "Required property 'template_version_number' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateTemplateAliasRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateTemplateAliasResponse",
    jsii_struct_bases=[],
    name_mapping={
        "request_id": "requestId",
        "status": "status",
        "template_alias": "templateAlias",
    },
)
class UpdateTemplateAliasResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template_alias: typing.Optional[TemplateAlias] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template_alias: The template alias.
        '''
        if isinstance(template_alias, dict):
            template_alias = TemplateAlias(**template_alias)
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template_alias is not None:
            self._values["template_alias"] = template_alias

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template_alias(self) -> typing.Optional[TemplateAlias]:
        '''The template alias.'''
        result = self._values.get("template_alias")
        return typing.cast(typing.Optional[TemplateAlias], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateTemplateAliasResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateTemplatePermissionsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "template_id": "templateId",
        "grant_permissions": "grantPermissions",
        "revoke_permissions": "revokePermissions",
    },
)
class UpdateTemplatePermissionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        template_id: builtins.str,
        grant_permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
        revoke_permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the template.
        :param template_id: The ID for the template.
        :param grant_permissions: A list of resource permissions to be granted on the template.
        :param revoke_permissions: A list of resource permissions to be revoked from the template.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "template_id": template_id,
        }
        if grant_permissions is not None:
            self._values["grant_permissions"] = grant_permissions
        if revoke_permissions is not None:
            self._values["revoke_permissions"] = revoke_permissions

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the template.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The ID for the template.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def grant_permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''A list of resource permissions to be granted on the template.'''
        result = self._values.get("grant_permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    @builtins.property
    def revoke_permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''A list of resource permissions to be revoked from the template.'''
        result = self._values.get("revoke_permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateTemplatePermissionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateTemplatePermissionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "permissions": "permissions",
        "request_id": "requestId",
        "status": "status",
        "template_arn": "templateArn",
        "template_id": "templateId",
    },
)
class UpdateTemplatePermissionsResponse:
    def __init__(
        self,
        *,
        permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template_arn: typing.Optional[builtins.str] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param permissions: A list of resource permissions to be set on the template.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template_arn: The Amazon Resource Name (ARN) of the template.
        :param template_id: The ID for the template.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if permissions is not None:
            self._values["permissions"] = permissions
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template_arn is not None:
            self._values["template_arn"] = template_arn
        if template_id is not None:
            self._values["template_id"] = template_id

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''A list of resource permissions to be set on the template.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the template.'''
        result = self._values.get("template_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the template.'''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateTemplatePermissionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateTemplateRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "source_entity": "sourceEntity",
        "template_id": "templateId",
        "name": "name",
        "version_description": "versionDescription",
    },
)
class UpdateTemplateRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        source_entity: TemplateSourceEntity,
        template_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the template that you're updating.
        :param source_entity: The entity that you are using as a source when you update the template. In SourceEntity, you specify the type of object you're using as source: SourceTemplate for a template or SourceAnalysis for an analysis. Both of these require an Amazon Resource Name (ARN). For SourceTemplate, specify the ARN of the source template. For SourceAnalysis, specify the ARN of the source analysis. The SourceTemplate ARN can contain any AWS Account and any QuickSight-supported AWS Region. Use the DataSetReferences entity within SourceTemplate or SourceAnalysis to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder.
        :param template_id: The ID for the template.
        :param name: The name for the template.
        :param version_description: A description of the current template version that is being updated. Every time you call UpdateTemplate, you create a new version of the template. Each version of the template maintains a description of the version in the VersionDescription field.
        '''
        if isinstance(source_entity, dict):
            source_entity = TemplateSourceEntity(**source_entity)
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "source_entity": source_entity,
            "template_id": template_id,
        }
        if name is not None:
            self._values["name"] = name
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the template that you're updating.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_entity(self) -> TemplateSourceEntity:
        '''The entity that you are using as a source when you update the template.

        In SourceEntity, you specify the type of object you're using as source: SourceTemplate for a template or SourceAnalysis for an analysis. Both of these require an Amazon Resource Name (ARN). For SourceTemplate, specify the ARN of the source template. For SourceAnalysis, specify the ARN of the source analysis. The SourceTemplate ARN can contain any AWS Account and any QuickSight-supported AWS Region.  Use the DataSetReferences entity within SourceTemplate or SourceAnalysis to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder.
        '''
        result = self._values.get("source_entity")
        assert result is not None, "Required property 'source_entity' is missing"
        return typing.cast(TemplateSourceEntity, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The ID for the template.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name for the template.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''A description of the current template version that is being updated.

        Every time you call UpdateTemplate, you create a new version of the template. Each version of the template maintains a description of the version in the VersionDescription field.
        '''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateTemplateRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateTemplateResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "creation_status": "creationStatus",
        "request_id": "requestId",
        "status": "status",
        "template_id": "templateId",
        "version_arn": "versionArn",
    },
)
class UpdateTemplateResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        creation_status: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        template_id: typing.Optional[builtins.str] = None,
        version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) for the template.
        :param creation_status: The creation status of the template.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param template_id: The ID for the template.
        :param version_arn: The ARN for the template, including the version information of the first version.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if creation_status is not None:
            self._values["creation_status"] = creation_status
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if template_id is not None:
            self._values["template_id"] = template_id
        if version_arn is not None:
            self._values["version_arn"] = version_arn

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the template.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_status(self) -> typing.Optional[builtins.str]:
        '''The creation status of the template.'''
        result = self._values.get("creation_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the template.'''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the template, including the version information of the first version.'''
        result = self._values.get("version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateTemplateResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateThemeAliasRequest",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "aws_account_id": "awsAccountId",
        "theme_id": "themeId",
        "theme_version_number": "themeVersionNumber",
    },
)
class UpdateThemeAliasRequest:
    def __init__(
        self,
        *,
        alias_name: builtins.str,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
        theme_version_number: jsii.Number,
    ) -> None:
        '''
        :param alias_name: The name of the theme alias that you want to update.
        :param aws_account_id: The ID of the AWS account that contains the theme alias that you're updating.
        :param theme_id: The ID for the theme.
        :param theme_version_number: The version number of the theme that the alias should reference.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alias_name": alias_name,
            "aws_account_id": aws_account_id,
            "theme_id": theme_id,
            "theme_version_number": theme_version_number,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''The name of the theme alias that you want to update.'''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the theme alias that you're updating.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''The ID for the theme.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_version_number(self) -> jsii.Number:
        '''The version number of the theme that the alias should reference.'''
        result = self._values.get("theme_version_number")
        assert result is not None, "Required property 'theme_version_number' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateThemeAliasRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateThemeAliasResponse",
    jsii_struct_bases=[],
    name_mapping={
        "request_id": "requestId",
        "status": "status",
        "theme_alias": "themeAlias",
    },
)
class UpdateThemeAliasResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme_alias: typing.Optional[ThemeAlias] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme_alias: Information about the theme alias.
        '''
        if isinstance(theme_alias, dict):
            theme_alias = ThemeAlias(**theme_alias)
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme_alias is not None:
            self._values["theme_alias"] = theme_alias

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme_alias(self) -> typing.Optional[ThemeAlias]:
        '''Information about the theme alias.'''
        result = self._values.get("theme_alias")
        return typing.cast(typing.Optional[ThemeAlias], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateThemeAliasResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateThemePermissionsRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "theme_id": "themeId",
        "grant_permissions": "grantPermissions",
        "revoke_permissions": "revokePermissions",
    },
)
class UpdateThemePermissionsRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        theme_id: builtins.str,
        grant_permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
        revoke_permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the theme.
        :param theme_id: The ID for the theme.
        :param grant_permissions: A list of resource permissions to be granted for the theme.
        :param revoke_permissions: A list of resource permissions to be revoked from the theme.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "theme_id": theme_id,
        }
        if grant_permissions is not None:
            self._values["grant_permissions"] = grant_permissions
        if revoke_permissions is not None:
            self._values["revoke_permissions"] = revoke_permissions

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the theme.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''The ID for the theme.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def grant_permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''A list of resource permissions to be granted for the theme.'''
        result = self._values.get("grant_permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    @builtins.property
    def revoke_permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''A list of resource permissions to be revoked from the theme.'''
        result = self._values.get("revoke_permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateThemePermissionsRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateThemePermissionsResponse",
    jsii_struct_bases=[],
    name_mapping={
        "permissions": "permissions",
        "request_id": "requestId",
        "status": "status",
        "theme_arn": "themeArn",
        "theme_id": "themeId",
    },
)
class UpdateThemePermissionsResponse:
    def __init__(
        self,
        *,
        permissions: typing.Optional[typing.Sequence[ResourcePermission]] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme_arn: typing.Optional[builtins.str] = None,
        theme_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param permissions: The resulting list of resource permissions for the theme.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme_arn: The Amazon Resource Name (ARN) of the theme.
        :param theme_id: The ID for the theme.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if permissions is not None:
            self._values["permissions"] = permissions
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme_arn is not None:
            self._values["theme_arn"] = theme_arn
        if theme_id is not None:
            self._values["theme_id"] = theme_id

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List[ResourcePermission]]:
        '''The resulting list of resource permissions for the theme.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List[ResourcePermission]], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the theme.'''
        result = self._values.get("theme_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def theme_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the theme.'''
        result = self._values.get("theme_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateThemePermissionsResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateThemeRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "base_theme_id": "baseThemeId",
        "theme_id": "themeId",
        "configuration": "configuration",
        "name": "name",
        "version_description": "versionDescription",
    },
)
class UpdateThemeRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        base_theme_id: builtins.str,
        theme_id: builtins.str,
        configuration: typing.Optional[ThemeConfiguration] = None,
        name: typing.Optional[builtins.str] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID of the AWS account that contains the theme that you're updating.
        :param base_theme_id: The theme ID, defined by Amazon QuickSight, that a custom theme inherits from. All themes initially inherit from a default QuickSight theme.
        :param theme_id: The ID for the theme.
        :param configuration: The theme configuration, which contains the theme display properties.
        :param name: The name for the theme.
        :param version_description: A description of the theme version that you're updating Every time that you call UpdateTheme, you create a new version of the theme. Each version of the theme maintains a description of the version in VersionDescription.
        '''
        if isinstance(configuration, dict):
            configuration = ThemeConfiguration(**configuration)
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "base_theme_id": base_theme_id,
            "theme_id": theme_id,
        }
        if configuration is not None:
            self._values["configuration"] = configuration
        if name is not None:
            self._values["name"] = name
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account that contains the theme that you're updating.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_theme_id(self) -> builtins.str:
        '''The theme ID, defined by Amazon QuickSight, that a custom theme inherits from.

        All themes initially inherit from a default QuickSight theme.
        '''
        result = self._values.get("base_theme_id")
        assert result is not None, "Required property 'base_theme_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''The ID for the theme.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(self) -> typing.Optional[ThemeConfiguration]:
        '''The theme configuration, which contains the theme display properties.'''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[ThemeConfiguration], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name for the theme.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''A description of the theme version that you're updating Every time that you call UpdateTheme, you create a new version of the theme.

        Each version of the theme maintains a description of the version in VersionDescription.
        '''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateThemeRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateThemeResponse",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "creation_status": "creationStatus",
        "request_id": "requestId",
        "status": "status",
        "theme_id": "themeId",
        "version_arn": "versionArn",
    },
)
class UpdateThemeResponse:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        creation_status: typing.Optional[builtins.str] = None,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        theme_id: typing.Optional[builtins.str] = None,
        version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: The Amazon Resource Name (ARN) for the theme.
        :param creation_status: The creation status of the theme.
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param theme_id: The ID for the theme.
        :param version_arn: The Amazon Resource Name (ARN) for the new version of the theme.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if creation_status is not None:
            self._values["creation_status"] = creation_status
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if theme_id is not None:
            self._values["theme_id"] = theme_id
        if version_arn is not None:
            self._values["version_arn"] = version_arn

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the theme.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_status(self) -> typing.Optional[builtins.str]:
        '''The creation status of the theme.'''
        result = self._values.get("creation_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the theme.'''
        result = self._values.get("theme_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the new version of the theme.'''
        result = self._values.get("version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateThemeResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateUserRequest",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "email": "email",
        "namespace": "namespace",
        "role": "role",
        "user_name": "userName",
        "custom_permissions_name": "customPermissionsName",
        "unapply_custom_permissions": "unapplyCustomPermissions",
    },
)
class UpdateUserRequest:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        email: builtins.str,
        namespace: builtins.str,
        role: builtins.str,
        user_name: builtins.str,
        custom_permissions_name: typing.Optional[builtins.str] = None,
        unapply_custom_permissions: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param aws_account_id: The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :param email: The email address of the user that you want to update.
        :param namespace: The namespace. Currently, you should set this to default.
        :param role: The Amazon QuickSight role of the user. The role can be one of the following default security cohorts: READER: A user who has read-only access to dashboards. AUTHOR: A user who can create data sources, datasets, analyses, and dashboards. ADMIN: A user who is an author, who can also manage Amazon QuickSight settings. The name of the QuickSight role is invisible to the user except for the console screens dealing with permissions.
        :param user_name: The Amazon QuickSight user name that you want to update.
        :param custom_permissions_name: (Enterprise edition only) The name of the custom permissions profile that you want to assign to this user. Customized permissions allows you to control a user's access by restricting access the following operations: Create and update data sources Create and update datasets Create and update email reports Subscribe to email reports A set of custom permissions includes any combination of these restrictions. Currently, you need to create the profile names for custom permission sets by using the QuickSight console. Then, you use the RegisterUser API operation to assign the named set of permissions to a QuickSight user. QuickSight custom permissions are applied through IAM policies. Therefore, they override the permissions typically granted by assigning QuickSight users to one of the default security cohorts in QuickSight (admin, author, reader). This feature is available only to QuickSight Enterprise edition subscriptions that use SAML 2.0-Based Federation for Single Sign-On (SSO).
        :param unapply_custom_permissions: A flag that you use to indicate that you want to remove all custom permissions from this user. Using this parameter resets the user to the state it was in before a custom permissions profile was applied. This parameter defaults to NULL and it doesn't accept any other value.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "email": email,
            "namespace": namespace,
            "role": role,
            "user_name": user_name,
        }
        if custom_permissions_name is not None:
            self._values["custom_permissions_name"] = custom_permissions_name
        if unapply_custom_permissions is not None:
            self._values["unapply_custom_permissions"] = unapply_custom_permissions

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The ID for the AWS account that the user is in.

        Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''The email address of the user that you want to update.'''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace.

        Currently, you should set this to default.
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''The Amazon QuickSight role of the user.

        The role can be one of the following default security cohorts:    READER: A user who has read-only access to dashboards.    AUTHOR: A user who can create data sources, datasets, analyses, and dashboards.    ADMIN: A user who is an author, who can also manage Amazon QuickSight settings.   The name of the QuickSight role is invisible to the user except for the console screens dealing with permissions.
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The Amazon QuickSight user name that you want to update.'''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_permissions_name(self) -> typing.Optional[builtins.str]:
        '''(Enterprise edition only) The name of the custom permissions profile that you want to assign to this user.

        Customized permissions allows you to control a user's access by restricting access the following operations:   Create and update data sources   Create and update datasets   Create and update email reports   Subscribe to email reports   A set of custom permissions includes any combination of these restrictions. Currently, you need to create the profile names for custom permission sets by using the QuickSight console. Then, you use the RegisterUser API operation to assign the named set of permissions to a QuickSight user.  QuickSight custom permissions are applied through IAM policies. Therefore, they override the permissions typically granted by assigning QuickSight users to one of the default security cohorts in QuickSight (admin, author, reader). This feature is available only to QuickSight Enterprise edition subscriptions that use SAML 2.0-Based Federation for Single Sign-On (SSO).
        '''
        result = self._values.get("custom_permissions_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unapply_custom_permissions(self) -> typing.Optional[builtins.bool]:
        '''A flag that you use to indicate that you want to remove all custom permissions from this user.

        Using this parameter resets the user to the state it was in before a custom permissions profile was applied. This parameter defaults to NULL and it doesn't accept any other value.
        '''
        result = self._values.get("unapply_custom_permissions")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateUserRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UpdateUserResponse",
    jsii_struct_bases=[],
    name_mapping={"request_id": "requestId", "status": "status", "user": "user"},
)
class UpdateUserResponse:
    def __init__(
        self,
        *,
        request_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[jsii.Number] = None,
        user: typing.Optional["User"] = None,
    ) -> None:
        '''
        :param request_id: The AWS request ID for this operation.
        :param status: The HTTP status of the request.
        :param user: The Amazon QuickSight user.
        '''
        if isinstance(user, dict):
            user = User(**user)
        self._values: typing.Dict[str, typing.Any] = {}
        if request_id is not None:
            self._values["request_id"] = request_id
        if status is not None:
            self._values["status"] = status
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def request_id(self) -> typing.Optional[builtins.str]:
        '''The AWS request ID for this operation.'''
        result = self._values.get("request_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status of the request.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user(self) -> typing.Optional["User"]:
        '''The Amazon QuickSight user.'''
        result = self._values.get("user")
        return typing.cast(typing.Optional["User"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UpdateUserResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.UploadSettings",
    jsii_struct_bases=[],
    name_mapping={
        "contains_header": "containsHeader",
        "delimiter": "delimiter",
        "format": "format",
        "start_from_row": "startFromRow",
        "text_qualifier": "textQualifier",
    },
)
class UploadSettings:
    def __init__(
        self,
        *,
        contains_header: typing.Optional[builtins.bool] = None,
        delimiter: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        start_from_row: typing.Optional[jsii.Number] = None,
        text_qualifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param contains_header: Whether the file has a header row, or the files each have a header row.
        :param delimiter: The delimiter between values in the file.
        :param format: File format.
        :param start_from_row: A row number to start reading data from.
        :param text_qualifier: Text qualifier.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if contains_header is not None:
            self._values["contains_header"] = contains_header
        if delimiter is not None:
            self._values["delimiter"] = delimiter
        if format is not None:
            self._values["format"] = format
        if start_from_row is not None:
            self._values["start_from_row"] = start_from_row
        if text_qualifier is not None:
            self._values["text_qualifier"] = text_qualifier

    @builtins.property
    def contains_header(self) -> typing.Optional[builtins.bool]:
        '''Whether the file has a header row, or the files each have a header row.'''
        result = self._values.get("contains_header")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def delimiter(self) -> typing.Optional[builtins.str]:
        '''The delimiter between values in the file.'''
        result = self._values.get("delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def format(self) -> typing.Optional[builtins.str]:
        '''File format.'''
        result = self._values.get("format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_from_row(self) -> typing.Optional[jsii.Number]:
        '''A row number to start reading data from.'''
        result = self._values.get("start_from_row")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def text_qualifier(self) -> typing.Optional[builtins.str]:
        '''Text qualifier.'''
        result = self._values.get("text_qualifier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UploadSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.User",
    jsii_struct_bases=[],
    name_mapping={
        "active": "active",
        "arn": "arn",
        "custom_permissions_name": "customPermissionsName",
        "email": "email",
        "identity_type": "identityType",
        "principal_id": "principalId",
        "role": "role",
        "user_name": "userName",
    },
)
class User:
    def __init__(
        self,
        *,
        active: typing.Optional[builtins.bool] = None,
        arn: typing.Optional[builtins.str] = None,
        custom_permissions_name: typing.Optional[builtins.str] = None,
        email: typing.Optional[builtins.str] = None,
        identity_type: typing.Optional[builtins.str] = None,
        principal_id: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param active: The active status of user. When you create an Amazon QuickSight user that’s not an IAM user or an Active Directory user, that user is inactive until they sign in and provide a password.
        :param arn: The Amazon Resource Name (ARN) for the user.
        :param custom_permissions_name: The custom permissions profile associated with this user.
        :param email: The user's email address.
        :param identity_type: The type of identity authentication used by the user.
        :param principal_id: The principal ID of the user.
        :param role: The Amazon QuickSight role for the user. The user role can be one of the following:. READER: A user who has read-only access to dashboards. AUTHOR: A user who can create data sources, datasets, analyses, and dashboards. ADMIN: A user who is an author, who can also manage Amazon QuickSight settings. RESTRICTED_READER: This role isn't currently available for use. RESTRICTED_AUTHOR: This role isn't currently available for use.
        :param user_name: The user's user name.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if active is not None:
            self._values["active"] = active
        if arn is not None:
            self._values["arn"] = arn
        if custom_permissions_name is not None:
            self._values["custom_permissions_name"] = custom_permissions_name
        if email is not None:
            self._values["email"] = email
        if identity_type is not None:
            self._values["identity_type"] = identity_type
        if principal_id is not None:
            self._values["principal_id"] = principal_id
        if role is not None:
            self._values["role"] = role
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def active(self) -> typing.Optional[builtins.bool]:
        '''The active status of user.

        When you create an Amazon QuickSight user that’s not an IAM user or an Active Directory user, that user is inactive until they sign in and provide a password.
        '''
        result = self._values.get("active")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the user.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_permissions_name(self) -> typing.Optional[builtins.str]:
        '''The custom permissions profile associated with this user.'''
        result = self._values.get("custom_permissions_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''The user's email address.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_type(self) -> typing.Optional[builtins.str]:
        '''The type of identity authentication used by the user.'''
        result = self._values.get("identity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def principal_id(self) -> typing.Optional[builtins.str]:
        '''The principal ID of the user.'''
        result = self._values.get("principal_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''The Amazon QuickSight role for the user.

        The user role can be one of the following:.    READER: A user who has read-only access to dashboards.    AUTHOR: A user who can create data sources, datasets, analyses, and dashboards.    ADMIN: A user who is an author, who can also manage Amazon QuickSight settings.    RESTRICTED_READER: This role isn't currently available for use.    RESTRICTED_AUTHOR: This role isn't currently available for use.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''The user's user name.'''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "User(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.VpcConnectionProperties",
    jsii_struct_bases=[],
    name_mapping={"vpc_connection_arn": "vpcConnectionArn"},
)
class VpcConnectionProperties:
    def __init__(self, *, vpc_connection_arn: builtins.str) -> None:
        '''
        :param vpc_connection_arn: The Amazon Resource Name (ARN) for the VPC connection.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "vpc_connection_arn": vpc_connection_arn,
        }

    @builtins.property
    def vpc_connection_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the VPC connection.'''
        result = self._values.get("vpc_connection_arn")
        assert result is not None, "Required property 'vpc_connection_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcConnectionProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DataSetProps",
    jsii_struct_bases=[QSCommonProps],
    name_mapping={
        "name": "name",
        "users": "users",
        "logical_table_map": "logicalTableMap",
        "physical_table_map": "physicalTableMap",
    },
)
class DataSetProps(QSCommonProps):
    def __init__(
        self,
        *,
        name: builtins.str,
        users: typing.Sequence[builtins.str],
        logical_table_map: typing.Mapping[builtins.str, LogicalTable],
        physical_table_map: typing.Mapping[builtins.str, PhysicalTable],
    ) -> None:
        '''
        :param name: 
        :param users: QuickSight Users you want to give access to. In the end the permission arn are looking like arn:aws:quicksight:us-east-1:1234:user/default/martin.mueller@take2.co. If you want to see available users, use aws cli described here https://github.com/Reliantid/cypresspoint-infrastructure/tree/cdk#list-datasets
        :param logical_table_map: 
        :param physical_table_map: 
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "users": users,
            "logical_table_map": logical_table_map,
            "physical_table_map": physical_table_map,
        }

    @builtins.property
    def name(self) -> builtins.str:
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def users(self) -> typing.List[builtins.str]:
        '''QuickSight Users you want to give access to. In the end the permission arn are looking like arn:aws:quicksight:us-east-1:1234:user/default/martin.mueller@take2.co.

        If you want to see available users, use aws cli described here https://github.com/Reliantid/cypresspoint-infrastructure/tree/cdk#list-datasets
        '''
        result = self._values.get("users")
        assert result is not None, "Required property 'users' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def logical_table_map(self) -> typing.Mapping[builtins.str, LogicalTable]:
        result = self._values.get("logical_table_map")
        assert result is not None, "Required property 'logical_table_map' is missing"
        return typing.cast(typing.Mapping[builtins.str, LogicalTable], result)

    @builtins.property
    def physical_table_map(self) -> typing.Mapping[builtins.str, PhysicalTable]:
        result = self._values.get("physical_table_map")
        assert result is not None, "Required property 'physical_table_map' is missing"
        return typing.cast(typing.Mapping[builtins.str, PhysicalTable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-quicksight-constructs.DataSourceProps",
    jsii_struct_bases=[QSCommonProps],
    name_mapping={
        "name": "name",
        "users": "users",
        "data_source_parameters": "dataSourceParameters",
        "type": "type",
    },
)
class DataSourceProps(QSCommonProps):
    def __init__(
        self,
        *,
        name: builtins.str,
        users: typing.Sequence[builtins.str],
        data_source_parameters: DataSourceParameters,
        type: builtins.str,
    ) -> None:
        '''
        :param name: 
        :param users: QuickSight Users you want to give access to. In the end the permission arn are looking like arn:aws:quicksight:us-east-1:1234:user/default/martin.mueller@take2.co. If you want to see available users, use aws cli described here https://github.com/Reliantid/cypresspoint-infrastructure/tree/cdk#list-datasets
        :param data_source_parameters: 
        :param type: 
        '''
        if isinstance(data_source_parameters, dict):
            data_source_parameters = DataSourceParameters(**data_source_parameters)
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "users": users,
            "data_source_parameters": data_source_parameters,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def users(self) -> typing.List[builtins.str]:
        '''QuickSight Users you want to give access to. In the end the permission arn are looking like arn:aws:quicksight:us-east-1:1234:user/default/martin.mueller@take2.co.

        If you want to see available users, use aws cli described here https://github.com/Reliantid/cypresspoint-infrastructure/tree/cdk#list-datasets
        '''
        result = self._values.get("users")
        assert result is not None, "Required property 'users' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def data_source_parameters(self) -> DataSourceParameters:
        result = self._values.get("data_source_parameters")
        assert result is not None, "Required property 'data_source_parameters' is missing"
        return typing.cast(DataSourceParameters, result)

    @builtins.property
    def type(self) -> builtins.str:
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccountCustomization",
    "AccountSettings",
    "ActiveIAMPolicyAssignment",
    "AdHocFilteringOption",
    "AmazonElasticsearchParameters",
    "Analysis",
    "AnalysisError",
    "AnalysisSearchFilter",
    "AnalysisSourceEntity",
    "AnalysisSourceTemplate",
    "AnalysisSummary",
    "AthenaParameters",
    "AuroraParameters",
    "AuroraPostgreSqlParameters",
    "AwsIotAnalyticsParameters",
    "BorderStyle",
    "CalculatedColumn",
    "CancelIngestionRequest",
    "CancelIngestionResponse",
    "CastColumnTypeOperation",
    "ClientApiVersions",
    "ColumnDescription",
    "ColumnGroup",
    "ColumnGroupColumnSchema",
    "ColumnGroupSchema",
    "ColumnLevelPermissionRule",
    "ColumnSchema",
    "ColumnTag",
    "CreateAccountCustomizationRequest",
    "CreateAccountCustomizationResponse",
    "CreateAnalysisRequest",
    "CreateAnalysisResponse",
    "CreateColumnsOperation",
    "CreateDashboardRequest",
    "CreateDashboardResponse",
    "CreateDataSetRequest",
    "CreateDataSetResponse",
    "CreateDataSourceRequest",
    "CreateDataSourceResponse",
    "CreateGroupMembershipRequest",
    "CreateGroupMembershipResponse",
    "CreateGroupRequest",
    "CreateGroupResponse",
    "CreateIAMPolicyAssignmentRequest",
    "CreateIAMPolicyAssignmentResponse",
    "CreateIngestionRequest",
    "CreateIngestionResponse",
    "CreateNamespaceRequest",
    "CreateNamespaceResponse",
    "CreateTemplateAliasRequest",
    "CreateTemplateAliasResponse",
    "CreateTemplateRequest",
    "CreateTemplateResponse",
    "CreateThemeAliasRequest",
    "CreateThemeAliasResponse",
    "CreateThemeRequest",
    "CreateThemeResponse",
    "CredentialPair",
    "CustomSql",
    "Dashboard",
    "DashboardError",
    "DashboardPublishOptions",
    "DashboardSearchFilter",
    "DashboardSourceEntity",
    "DashboardSourceTemplate",
    "DashboardSummary",
    "DashboardVersion",
    "DashboardVersionSummary",
    "DataColorPalette",
    "DataSet",
    "DataSetConfiguration",
    "DataSetConstruct",
    "DataSetProps",
    "DataSetReference",
    "DataSetSchema",
    "DataSetSummary",
    "DataSource",
    "DataSourceConstruct",
    "DataSourceCredentials",
    "DataSourceErrorInfo",
    "DataSourceParameters",
    "DataSourceProps",
    "DateTimeParameter",
    "DecimalParameter",
    "DeleteAccountCustomizationRequest",
    "DeleteAccountCustomizationResponse",
    "DeleteAnalysisRequest",
    "DeleteAnalysisResponse",
    "DeleteDashboardRequest",
    "DeleteDashboardResponse",
    "DeleteDataSetRequest",
    "DeleteDataSetResponse",
    "DeleteDataSourceRequest",
    "DeleteDataSourceResponse",
    "DeleteGroupMembershipRequest",
    "DeleteGroupMembershipResponse",
    "DeleteGroupRequest",
    "DeleteGroupResponse",
    "DeleteIAMPolicyAssignmentRequest",
    "DeleteIAMPolicyAssignmentResponse",
    "DeleteNamespaceRequest",
    "DeleteNamespaceResponse",
    "DeleteTemplateAliasRequest",
    "DeleteTemplateAliasResponse",
    "DeleteTemplateRequest",
    "DeleteTemplateResponse",
    "DeleteThemeAliasRequest",
    "DeleteThemeAliasResponse",
    "DeleteThemeRequest",
    "DeleteThemeResponse",
    "DeleteUserByPrincipalIdRequest",
    "DeleteUserByPrincipalIdResponse",
    "DeleteUserRequest",
    "DeleteUserResponse",
    "DescribeAccountCustomizationRequest",
    "DescribeAccountCustomizationResponse",
    "DescribeAccountSettingsRequest",
    "DescribeAccountSettingsResponse",
    "DescribeAnalysisPermissionsRequest",
    "DescribeAnalysisPermissionsResponse",
    "DescribeAnalysisRequest",
    "DescribeAnalysisResponse",
    "DescribeDashboardPermissionsRequest",
    "DescribeDashboardPermissionsResponse",
    "DescribeDashboardRequest",
    "DescribeDashboardResponse",
    "DescribeDataSetPermissionsRequest",
    "DescribeDataSetPermissionsResponse",
    "DescribeDataSetRequest",
    "DescribeDataSetResponse",
    "DescribeDataSourcePermissionsRequest",
    "DescribeDataSourcePermissionsResponse",
    "DescribeDataSourceRequest",
    "DescribeDataSourceResponse",
    "DescribeGroupRequest",
    "DescribeGroupResponse",
    "DescribeIAMPolicyAssignmentRequest",
    "DescribeIAMPolicyAssignmentResponse",
    "DescribeIngestionRequest",
    "DescribeIngestionResponse",
    "DescribeNamespaceRequest",
    "DescribeNamespaceResponse",
    "DescribeTemplateAliasRequest",
    "DescribeTemplateAliasResponse",
    "DescribeTemplatePermissionsRequest",
    "DescribeTemplatePermissionsResponse",
    "DescribeTemplateRequest",
    "DescribeTemplateResponse",
    "DescribeThemeAliasRequest",
    "DescribeThemeAliasResponse",
    "DescribeThemePermissionsRequest",
    "DescribeThemePermissionsResponse",
    "DescribeThemeRequest",
    "DescribeThemeResponse",
    "DescribeUserRequest",
    "DescribeUserResponse",
    "ErrorInfo",
    "ExportToCSVOption",
    "FieldFolder",
    "FilterOperation",
    "GeoSpatialColumnGroup",
    "GetDashboardEmbedUrlRequest",
    "GetDashboardEmbedUrlResponse",
    "GetSessionEmbedUrlRequest",
    "GetSessionEmbedUrlResponse",
    "Group",
    "GroupMember",
    "GutterStyle",
    "IAMPolicyAssignment",
    "IAMPolicyAssignmentSummary",
    "Ingestion",
    "InputColumn",
    "IntegerParameter",
    "JiraParameters",
    "JoinInstruction",
    "JoinKeyProperties",
    "ListAnalysesRequest",
    "ListAnalysesResponse",
    "ListDashboardVersionsRequest",
    "ListDashboardVersionsResponse",
    "ListDashboardsRequest",
    "ListDashboardsResponse",
    "ListDataSetsRequest",
    "ListDataSetsResponse",
    "ListDataSourcesRequest",
    "ListDataSourcesResponse",
    "ListGroupMembershipsRequest",
    "ListGroupMembershipsResponse",
    "ListGroupsRequest",
    "ListGroupsResponse",
    "ListIAMPolicyAssignmentsForUserRequest",
    "ListIAMPolicyAssignmentsForUserResponse",
    "ListIAMPolicyAssignmentsRequest",
    "ListIAMPolicyAssignmentsResponse",
    "ListIngestionsRequest",
    "ListIngestionsResponse",
    "ListNamespacesRequest",
    "ListNamespacesResponse",
    "ListTagsForResourceRequest",
    "ListTagsForResourceResponse",
    "ListTemplateAliasesRequest",
    "ListTemplateAliasesResponse",
    "ListTemplateVersionsRequest",
    "ListTemplateVersionsResponse",
    "ListTemplatesRequest",
    "ListTemplatesResponse",
    "ListThemeAliasesRequest",
    "ListThemeAliasesResponse",
    "ListThemeVersionsRequest",
    "ListThemeVersionsResponse",
    "ListThemesRequest",
    "ListThemesResponse",
    "ListUserGroupsRequest",
    "ListUserGroupsResponse",
    "ListUsersRequest",
    "ListUsersResponse",
    "LogicalTable",
    "LogicalTableSource",
    "ManifestFileLocation",
    "MarginStyle",
    "MariaDbParameters",
    "MySqlParameters",
    "NamespaceError",
    "NamespaceInfoV2",
    "OracleParameters",
    "OutputColumn",
    "Parameters",
    "PhysicalTable",
    "PostgreSqlParameters",
    "PrestoParameters",
    "ProjectOperation",
    "QSCommonProps",
    "QueueInfo",
    "RdsParameters",
    "RedshiftParameters",
    "RegisterUserRequest",
    "RegisterUserResponse",
    "RelationalTable",
    "RenameColumnOperation",
    "ResourcePermission",
    "RestoreAnalysisRequest",
    "RestoreAnalysisResponse",
    "RowInfo",
    "RowLevelPermissionDataSet",
    "S3Parameters",
    "S3Source",
    "SearchAnalysesRequest",
    "SearchAnalysesResponse",
    "SearchDashboardsRequest",
    "SearchDashboardsResponse",
    "ServiceNowParameters",
    "Sheet",
    "SheetControlsOption",
    "SheetStyle",
    "SnowflakeParameters",
    "SparkParameters",
    "SqlServerParameters",
    "SslProperties",
    "StringParameter",
    "Tag",
    "TagColumnOperation",
    "TagResourceRequest",
    "TagResourceResponse",
    "Template",
    "TemplateAlias",
    "TemplateError",
    "TemplateSourceAnalysis",
    "TemplateSourceEntity",
    "TemplateSourceTemplate",
    "TemplateSummary",
    "TemplateVersion",
    "TemplateVersionSummary",
    "TeradataParameters",
    "Theme",
    "ThemeAlias",
    "ThemeConfiguration",
    "ThemeError",
    "ThemeSummary",
    "ThemeVersion",
    "ThemeVersionSummary",
    "TileLayoutStyle",
    "TileStyle",
    "TransformOperation",
    "TwitterParameters",
    "UIColorPalette",
    "UntagResourceRequest",
    "UntagResourceResponse",
    "UpdateAccountCustomizationRequest",
    "UpdateAccountCustomizationResponse",
    "UpdateAccountSettingsRequest",
    "UpdateAccountSettingsResponse",
    "UpdateAnalysisPermissionsRequest",
    "UpdateAnalysisPermissionsResponse",
    "UpdateAnalysisRequest",
    "UpdateAnalysisResponse",
    "UpdateDashboardPermissionsRequest",
    "UpdateDashboardPermissionsResponse",
    "UpdateDashboardPublishedVersionRequest",
    "UpdateDashboardPublishedVersionResponse",
    "UpdateDashboardRequest",
    "UpdateDashboardResponse",
    "UpdateDataSetPermissionsRequest",
    "UpdateDataSetPermissionsResponse",
    "UpdateDataSetRequest",
    "UpdateDataSetResponse",
    "UpdateDataSourcePermissionsRequest",
    "UpdateDataSourcePermissionsResponse",
    "UpdateDataSourceRequest",
    "UpdateDataSourceResponse",
    "UpdateGroupRequest",
    "UpdateGroupResponse",
    "UpdateIAMPolicyAssignmentRequest",
    "UpdateIAMPolicyAssignmentResponse",
    "UpdateTemplateAliasRequest",
    "UpdateTemplateAliasResponse",
    "UpdateTemplatePermissionsRequest",
    "UpdateTemplatePermissionsResponse",
    "UpdateTemplateRequest",
    "UpdateTemplateResponse",
    "UpdateThemeAliasRequest",
    "UpdateThemeAliasResponse",
    "UpdateThemePermissionsRequest",
    "UpdateThemePermissionsResponse",
    "UpdateThemeRequest",
    "UpdateThemeResponse",
    "UpdateUserRequest",
    "UpdateUserResponse",
    "UploadSettings",
    "User",
    "VpcConnectionProperties",
]

publication.publish()
