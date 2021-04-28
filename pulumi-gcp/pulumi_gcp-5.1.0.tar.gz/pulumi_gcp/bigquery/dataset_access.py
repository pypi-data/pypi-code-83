# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DatasetAccessArgs', 'DatasetAccess']

@pulumi.input_type
class DatasetAccessArgs:
    def __init__(__self__, *,
                 dataset_id: pulumi.Input[str],
                 domain: Optional[pulumi.Input[str]] = None,
                 group_by_email: Optional[pulumi.Input[str]] = None,
                 iam_member: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 special_group: Optional[pulumi.Input[str]] = None,
                 user_by_email: Optional[pulumi.Input[str]] = None,
                 view: Optional[pulumi.Input['DatasetAccessViewArgs']] = None):
        """
        The set of arguments for constructing a DatasetAccess resource.
        :param pulumi.Input[str] dataset_id: The ID of the dataset containing this table.
        :param pulumi.Input[str] domain: A domain to grant access to. Any users signed in with the
               domain specified will be granted the specified access
        :param pulumi.Input[str] group_by_email: An email address of a Google Group to grant access to.
        :param pulumi.Input[str] iam_member: Some other type of member that appears in the IAM Policy but isn't a user,
               group, domain, or special group. For example: `allUsers`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] role: Describes the rights granted to the user specified by the other
               member of the access object. Basic, predefined, and custom roles are
               supported. Predefined roles that have equivalent basic roles are
               swapped by the API to their basic counterparts, and will show a diff
               post-create. See
               [official docs](https://cloud.google.com/bigquery/docs/access-control).
        :param pulumi.Input[str] special_group: A special group to grant access to. Possible values include:
        :param pulumi.Input[str] user_by_email: An email address of a user to grant access to. For example:
               fred@example.com
        :param pulumi.Input['DatasetAccessViewArgs'] view: A view from a different dataset to grant access to. Queries
               executed against that view will have read access to tables in
               this dataset. The role field is not required when this field is
               set. If that view is updated by any user, access to the view
               needs to be granted again via an update operation.
               Structure is documented below.
        """
        pulumi.set(__self__, "dataset_id", dataset_id)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if group_by_email is not None:
            pulumi.set(__self__, "group_by_email", group_by_email)
        if iam_member is not None:
            pulumi.set(__self__, "iam_member", iam_member)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if special_group is not None:
            pulumi.set(__self__, "special_group", special_group)
        if user_by_email is not None:
            pulumi.set(__self__, "user_by_email", user_by_email)
        if view is not None:
            pulumi.set(__self__, "view", view)

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[str]:
        """
        The ID of the dataset containing this table.
        """
        return pulumi.get(self, "dataset_id")

    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataset_id", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        A domain to grant access to. Any users signed in with the
        domain specified will be granted the specified access
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="groupByEmail")
    def group_by_email(self) -> Optional[pulumi.Input[str]]:
        """
        An email address of a Google Group to grant access to.
        """
        return pulumi.get(self, "group_by_email")

    @group_by_email.setter
    def group_by_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_by_email", value)

    @property
    @pulumi.getter(name="iamMember")
    def iam_member(self) -> Optional[pulumi.Input[str]]:
        """
        Some other type of member that appears in the IAM Policy but isn't a user,
        group, domain, or special group. For example: `allUsers`
        """
        return pulumi.get(self, "iam_member")

    @iam_member.setter
    def iam_member(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iam_member", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        Describes the rights granted to the user specified by the other
        member of the access object. Basic, predefined, and custom roles are
        supported. Predefined roles that have equivalent basic roles are
        swapped by the API to their basic counterparts, and will show a diff
        post-create. See
        [official docs](https://cloud.google.com/bigquery/docs/access-control).
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="specialGroup")
    def special_group(self) -> Optional[pulumi.Input[str]]:
        """
        A special group to grant access to. Possible values include:
        """
        return pulumi.get(self, "special_group")

    @special_group.setter
    def special_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "special_group", value)

    @property
    @pulumi.getter(name="userByEmail")
    def user_by_email(self) -> Optional[pulumi.Input[str]]:
        """
        An email address of a user to grant access to. For example:
        fred@example.com
        """
        return pulumi.get(self, "user_by_email")

    @user_by_email.setter
    def user_by_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_by_email", value)

    @property
    @pulumi.getter
    def view(self) -> Optional[pulumi.Input['DatasetAccessViewArgs']]:
        """
        A view from a different dataset to grant access to. Queries
        executed against that view will have read access to tables in
        this dataset. The role field is not required when this field is
        set. If that view is updated by any user, access to the view
        needs to be granted again via an update operation.
        Structure is documented below.
        """
        return pulumi.get(self, "view")

    @view.setter
    def view(self, value: Optional[pulumi.Input['DatasetAccessViewArgs']]):
        pulumi.set(self, "view", value)


@pulumi.input_type
class _DatasetAccessState:
    def __init__(__self__, *,
                 api_updated_member: Optional[pulumi.Input[bool]] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 group_by_email: Optional[pulumi.Input[str]] = None,
                 iam_member: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 special_group: Optional[pulumi.Input[str]] = None,
                 user_by_email: Optional[pulumi.Input[str]] = None,
                 view: Optional[pulumi.Input['DatasetAccessViewArgs']] = None):
        """
        Input properties used for looking up and filtering DatasetAccess resources.
        :param pulumi.Input[bool] api_updated_member: If true, represents that that the iam_member in the config was translated to a different member type by the API, and is
               stored in state as a different member type
        :param pulumi.Input[str] dataset_id: The ID of the dataset containing this table.
        :param pulumi.Input[str] domain: A domain to grant access to. Any users signed in with the
               domain specified will be granted the specified access
        :param pulumi.Input[str] group_by_email: An email address of a Google Group to grant access to.
        :param pulumi.Input[str] iam_member: Some other type of member that appears in the IAM Policy but isn't a user,
               group, domain, or special group. For example: `allUsers`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] role: Describes the rights granted to the user specified by the other
               member of the access object. Basic, predefined, and custom roles are
               supported. Predefined roles that have equivalent basic roles are
               swapped by the API to their basic counterparts, and will show a diff
               post-create. See
               [official docs](https://cloud.google.com/bigquery/docs/access-control).
        :param pulumi.Input[str] special_group: A special group to grant access to. Possible values include:
        :param pulumi.Input[str] user_by_email: An email address of a user to grant access to. For example:
               fred@example.com
        :param pulumi.Input['DatasetAccessViewArgs'] view: A view from a different dataset to grant access to. Queries
               executed against that view will have read access to tables in
               this dataset. The role field is not required when this field is
               set. If that view is updated by any user, access to the view
               needs to be granted again via an update operation.
               Structure is documented below.
        """
        if api_updated_member is not None:
            pulumi.set(__self__, "api_updated_member", api_updated_member)
        if dataset_id is not None:
            pulumi.set(__self__, "dataset_id", dataset_id)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if group_by_email is not None:
            pulumi.set(__self__, "group_by_email", group_by_email)
        if iam_member is not None:
            pulumi.set(__self__, "iam_member", iam_member)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if special_group is not None:
            pulumi.set(__self__, "special_group", special_group)
        if user_by_email is not None:
            pulumi.set(__self__, "user_by_email", user_by_email)
        if view is not None:
            pulumi.set(__self__, "view", view)

    @property
    @pulumi.getter(name="apiUpdatedMember")
    def api_updated_member(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, represents that that the iam_member in the config was translated to a different member type by the API, and is
        stored in state as a different member type
        """
        return pulumi.get(self, "api_updated_member")

    @api_updated_member.setter
    def api_updated_member(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "api_updated_member", value)

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the dataset containing this table.
        """
        return pulumi.get(self, "dataset_id")

    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dataset_id", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        A domain to grant access to. Any users signed in with the
        domain specified will be granted the specified access
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="groupByEmail")
    def group_by_email(self) -> Optional[pulumi.Input[str]]:
        """
        An email address of a Google Group to grant access to.
        """
        return pulumi.get(self, "group_by_email")

    @group_by_email.setter
    def group_by_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_by_email", value)

    @property
    @pulumi.getter(name="iamMember")
    def iam_member(self) -> Optional[pulumi.Input[str]]:
        """
        Some other type of member that appears in the IAM Policy but isn't a user,
        group, domain, or special group. For example: `allUsers`
        """
        return pulumi.get(self, "iam_member")

    @iam_member.setter
    def iam_member(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iam_member", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        Describes the rights granted to the user specified by the other
        member of the access object. Basic, predefined, and custom roles are
        supported. Predefined roles that have equivalent basic roles are
        swapped by the API to their basic counterparts, and will show a diff
        post-create. See
        [official docs](https://cloud.google.com/bigquery/docs/access-control).
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="specialGroup")
    def special_group(self) -> Optional[pulumi.Input[str]]:
        """
        A special group to grant access to. Possible values include:
        """
        return pulumi.get(self, "special_group")

    @special_group.setter
    def special_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "special_group", value)

    @property
    @pulumi.getter(name="userByEmail")
    def user_by_email(self) -> Optional[pulumi.Input[str]]:
        """
        An email address of a user to grant access to. For example:
        fred@example.com
        """
        return pulumi.get(self, "user_by_email")

    @user_by_email.setter
    def user_by_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_by_email", value)

    @property
    @pulumi.getter
    def view(self) -> Optional[pulumi.Input['DatasetAccessViewArgs']]:
        """
        A view from a different dataset to grant access to. Queries
        executed against that view will have read access to tables in
        this dataset. The role field is not required when this field is
        set. If that view is updated by any user, access to the view
        needs to be granted again via an update operation.
        Structure is documented below.
        """
        return pulumi.get(self, "view")

    @view.setter
    def view(self, value: Optional[pulumi.Input['DatasetAccessViewArgs']]):
        pulumi.set(self, "view", value)


class DatasetAccess(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 group_by_email: Optional[pulumi.Input[str]] = None,
                 iam_member: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 special_group: Optional[pulumi.Input[str]] = None,
                 user_by_email: Optional[pulumi.Input[str]] = None,
                 view: Optional[pulumi.Input[pulumi.InputType['DatasetAccessViewArgs']]] = None,
                 __props__=None):
        """
        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dataset_id: The ID of the dataset containing this table.
        :param pulumi.Input[str] domain: A domain to grant access to. Any users signed in with the
               domain specified will be granted the specified access
        :param pulumi.Input[str] group_by_email: An email address of a Google Group to grant access to.
        :param pulumi.Input[str] iam_member: Some other type of member that appears in the IAM Policy but isn't a user,
               group, domain, or special group. For example: `allUsers`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] role: Describes the rights granted to the user specified by the other
               member of the access object. Basic, predefined, and custom roles are
               supported. Predefined roles that have equivalent basic roles are
               swapped by the API to their basic counterparts, and will show a diff
               post-create. See
               [official docs](https://cloud.google.com/bigquery/docs/access-control).
        :param pulumi.Input[str] special_group: A special group to grant access to. Possible values include:
        :param pulumi.Input[str] user_by_email: An email address of a user to grant access to. For example:
               fred@example.com
        :param pulumi.Input[pulumi.InputType['DatasetAccessViewArgs']] view: A view from a different dataset to grant access to. Queries
               executed against that view will have read access to tables in
               this dataset. The role field is not required when this field is
               set. If that view is updated by any user, access to the view
               needs to be granted again via an update operation.
               Structure is documented below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatasetAccessArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param DatasetAccessArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatasetAccessArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 group_by_email: Optional[pulumi.Input[str]] = None,
                 iam_member: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 special_group: Optional[pulumi.Input[str]] = None,
                 user_by_email: Optional[pulumi.Input[str]] = None,
                 view: Optional[pulumi.Input[pulumi.InputType['DatasetAccessViewArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatasetAccessArgs.__new__(DatasetAccessArgs)

            if dataset_id is None and not opts.urn:
                raise TypeError("Missing required property 'dataset_id'")
            __props__.__dict__["dataset_id"] = dataset_id
            __props__.__dict__["domain"] = domain
            __props__.__dict__["group_by_email"] = group_by_email
            __props__.__dict__["iam_member"] = iam_member
            __props__.__dict__["project"] = project
            __props__.__dict__["role"] = role
            __props__.__dict__["special_group"] = special_group
            __props__.__dict__["user_by_email"] = user_by_email
            __props__.__dict__["view"] = view
            __props__.__dict__["api_updated_member"] = None
        super(DatasetAccess, __self__).__init__(
            'gcp:bigquery/datasetAccess:DatasetAccess',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_updated_member: Optional[pulumi.Input[bool]] = None,
            dataset_id: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            group_by_email: Optional[pulumi.Input[str]] = None,
            iam_member: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None,
            special_group: Optional[pulumi.Input[str]] = None,
            user_by_email: Optional[pulumi.Input[str]] = None,
            view: Optional[pulumi.Input[pulumi.InputType['DatasetAccessViewArgs']]] = None) -> 'DatasetAccess':
        """
        Get an existing DatasetAccess resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] api_updated_member: If true, represents that that the iam_member in the config was translated to a different member type by the API, and is
               stored in state as a different member type
        :param pulumi.Input[str] dataset_id: The ID of the dataset containing this table.
        :param pulumi.Input[str] domain: A domain to grant access to. Any users signed in with the
               domain specified will be granted the specified access
        :param pulumi.Input[str] group_by_email: An email address of a Google Group to grant access to.
        :param pulumi.Input[str] iam_member: Some other type of member that appears in the IAM Policy but isn't a user,
               group, domain, or special group. For example: `allUsers`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] role: Describes the rights granted to the user specified by the other
               member of the access object. Basic, predefined, and custom roles are
               supported. Predefined roles that have equivalent basic roles are
               swapped by the API to their basic counterparts, and will show a diff
               post-create. See
               [official docs](https://cloud.google.com/bigquery/docs/access-control).
        :param pulumi.Input[str] special_group: A special group to grant access to. Possible values include:
        :param pulumi.Input[str] user_by_email: An email address of a user to grant access to. For example:
               fred@example.com
        :param pulumi.Input[pulumi.InputType['DatasetAccessViewArgs']] view: A view from a different dataset to grant access to. Queries
               executed against that view will have read access to tables in
               this dataset. The role field is not required when this field is
               set. If that view is updated by any user, access to the view
               needs to be granted again via an update operation.
               Structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatasetAccessState.__new__(_DatasetAccessState)

        __props__.__dict__["api_updated_member"] = api_updated_member
        __props__.__dict__["dataset_id"] = dataset_id
        __props__.__dict__["domain"] = domain
        __props__.__dict__["group_by_email"] = group_by_email
        __props__.__dict__["iam_member"] = iam_member
        __props__.__dict__["project"] = project
        __props__.__dict__["role"] = role
        __props__.__dict__["special_group"] = special_group
        __props__.__dict__["user_by_email"] = user_by_email
        __props__.__dict__["view"] = view
        return DatasetAccess(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiUpdatedMember")
    def api_updated_member(self) -> pulumi.Output[bool]:
        """
        If true, represents that that the iam_member in the config was translated to a different member type by the API, and is
        stored in state as a different member type
        """
        return pulumi.get(self, "api_updated_member")

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Output[str]:
        """
        The ID of the dataset containing this table.
        """
        return pulumi.get(self, "dataset_id")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[str]]:
        """
        A domain to grant access to. Any users signed in with the
        domain specified will be granted the specified access
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="groupByEmail")
    def group_by_email(self) -> pulumi.Output[Optional[str]]:
        """
        An email address of a Google Group to grant access to.
        """
        return pulumi.get(self, "group_by_email")

    @property
    @pulumi.getter(name="iamMember")
    def iam_member(self) -> pulumi.Output[Optional[str]]:
        """
        Some other type of member that appears in the IAM Policy but isn't a user,
        group, domain, or special group. For example: `allUsers`
        """
        return pulumi.get(self, "iam_member")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[Optional[str]]:
        """
        Describes the rights granted to the user specified by the other
        member of the access object. Basic, predefined, and custom roles are
        supported. Predefined roles that have equivalent basic roles are
        swapped by the API to their basic counterparts, and will show a diff
        post-create. See
        [official docs](https://cloud.google.com/bigquery/docs/access-control).
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="specialGroup")
    def special_group(self) -> pulumi.Output[Optional[str]]:
        """
        A special group to grant access to. Possible values include:
        """
        return pulumi.get(self, "special_group")

    @property
    @pulumi.getter(name="userByEmail")
    def user_by_email(self) -> pulumi.Output[Optional[str]]:
        """
        An email address of a user to grant access to. For example:
        fred@example.com
        """
        return pulumi.get(self, "user_by_email")

    @property
    @pulumi.getter
    def view(self) -> pulumi.Output[Optional['outputs.DatasetAccessView']]:
        """
        A view from a different dataset to grant access to. Queries
        executed against that view will have read access to tables in
        this dataset. The role field is not required when this field is
        set. If that view is updated by any user, access to the view
        needs to be granted again via an update operation.
        Structure is documented below.
        """
        return pulumi.get(self, "view")

