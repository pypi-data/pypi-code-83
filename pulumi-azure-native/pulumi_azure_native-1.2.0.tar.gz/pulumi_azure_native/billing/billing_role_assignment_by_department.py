# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BillingRoleAssignmentByDepartmentArgs', 'BillingRoleAssignmentByDepartment']

@pulumi.input_type
class BillingRoleAssignmentByDepartmentArgs:
    def __init__(__self__, *,
                 billing_account_name: pulumi.Input[str],
                 department_name: pulumi.Input[str],
                 billing_role_assignment_name: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 principal_tenant_id: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 user_authentication_type: Optional[pulumi.Input[str]] = None,
                 user_email_address: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BillingRoleAssignmentByDepartment resource.
        :param pulumi.Input[str] billing_account_name: The ID that uniquely identifies a billing account.
        :param pulumi.Input[str] department_name: The ID that uniquely identifies a department.
        :param pulumi.Input[str] billing_role_assignment_name: The ID that uniquely identifies a role assignment.
        :param pulumi.Input[str] principal_id: The principal id of the user to whom the role was assigned.
        :param pulumi.Input[str] principal_tenant_id: The principal tenant id of the user to whom the role was assigned.
        :param pulumi.Input[str] role_definition_id: The ID of the role definition.
        :param pulumi.Input[str] user_authentication_type: The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.
        :param pulumi.Input[str] user_email_address: The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.
        """
        pulumi.set(__self__, "billing_account_name", billing_account_name)
        pulumi.set(__self__, "department_name", department_name)
        if billing_role_assignment_name is not None:
            pulumi.set(__self__, "billing_role_assignment_name", billing_role_assignment_name)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if principal_tenant_id is not None:
            pulumi.set(__self__, "principal_tenant_id", principal_tenant_id)
        if role_definition_id is not None:
            pulumi.set(__self__, "role_definition_id", role_definition_id)
        if user_authentication_type is not None:
            pulumi.set(__self__, "user_authentication_type", user_authentication_type)
        if user_email_address is not None:
            pulumi.set(__self__, "user_email_address", user_email_address)

    @property
    @pulumi.getter(name="billingAccountName")
    def billing_account_name(self) -> pulumi.Input[str]:
        """
        The ID that uniquely identifies a billing account.
        """
        return pulumi.get(self, "billing_account_name")

    @billing_account_name.setter
    def billing_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "billing_account_name", value)

    @property
    @pulumi.getter(name="departmentName")
    def department_name(self) -> pulumi.Input[str]:
        """
        The ID that uniquely identifies a department.
        """
        return pulumi.get(self, "department_name")

    @department_name.setter
    def department_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "department_name", value)

    @property
    @pulumi.getter(name="billingRoleAssignmentName")
    def billing_role_assignment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The ID that uniquely identifies a role assignment.
        """
        return pulumi.get(self, "billing_role_assignment_name")

    @billing_role_assignment_name.setter
    def billing_role_assignment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_role_assignment_name", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The principal id of the user to whom the role was assigned.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="principalTenantId")
    def principal_tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The principal tenant id of the user to whom the role was assigned.
        """
        return pulumi.get(self, "principal_tenant_id")

    @principal_tenant_id.setter
    def principal_tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_tenant_id", value)

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the role definition.
        """
        return pulumi.get(self, "role_definition_id")

    @role_definition_id.setter
    def role_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_definition_id", value)

    @property
    @pulumi.getter(name="userAuthenticationType")
    def user_authentication_type(self) -> Optional[pulumi.Input[str]]:
        """
        The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.
        """
        return pulumi.get(self, "user_authentication_type")

    @user_authentication_type.setter
    def user_authentication_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_authentication_type", value)

    @property
    @pulumi.getter(name="userEmailAddress")
    def user_email_address(self) -> Optional[pulumi.Input[str]]:
        """
        The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.
        """
        return pulumi.get(self, "user_email_address")

    @user_email_address.setter
    def user_email_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_email_address", value)


class BillingRoleAssignmentByDepartment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_account_name: Optional[pulumi.Input[str]] = None,
                 billing_role_assignment_name: Optional[pulumi.Input[str]] = None,
                 department_name: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 principal_tenant_id: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 user_authentication_type: Optional[pulumi.Input[str]] = None,
                 user_email_address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The role assignment
        API Version: 2019-10-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] billing_account_name: The ID that uniquely identifies a billing account.
        :param pulumi.Input[str] billing_role_assignment_name: The ID that uniquely identifies a role assignment.
        :param pulumi.Input[str] department_name: The ID that uniquely identifies a department.
        :param pulumi.Input[str] principal_id: The principal id of the user to whom the role was assigned.
        :param pulumi.Input[str] principal_tenant_id: The principal tenant id of the user to whom the role was assigned.
        :param pulumi.Input[str] role_definition_id: The ID of the role definition.
        :param pulumi.Input[str] user_authentication_type: The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.
        :param pulumi.Input[str] user_email_address: The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BillingRoleAssignmentByDepartmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The role assignment
        API Version: 2019-10-01-preview.

        :param str resource_name: The name of the resource.
        :param BillingRoleAssignmentByDepartmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BillingRoleAssignmentByDepartmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_account_name: Optional[pulumi.Input[str]] = None,
                 billing_role_assignment_name: Optional[pulumi.Input[str]] = None,
                 department_name: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 principal_tenant_id: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 user_authentication_type: Optional[pulumi.Input[str]] = None,
                 user_email_address: Optional[pulumi.Input[str]] = None,
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
            __props__ = BillingRoleAssignmentByDepartmentArgs.__new__(BillingRoleAssignmentByDepartmentArgs)

            if billing_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'billing_account_name'")
            __props__.__dict__["billing_account_name"] = billing_account_name
            __props__.__dict__["billing_role_assignment_name"] = billing_role_assignment_name
            if department_name is None and not opts.urn:
                raise TypeError("Missing required property 'department_name'")
            __props__.__dict__["department_name"] = department_name
            __props__.__dict__["principal_id"] = principal_id
            __props__.__dict__["principal_tenant_id"] = principal_tenant_id
            __props__.__dict__["role_definition_id"] = role_definition_id
            __props__.__dict__["user_authentication_type"] = user_authentication_type
            __props__.__dict__["user_email_address"] = user_email_address
            __props__.__dict__["created_by_principal_id"] = None
            __props__.__dict__["created_by_principal_tenant_id"] = None
            __props__.__dict__["created_by_user_email_address"] = None
            __props__.__dict__["created_on"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["scope"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:billing:BillingRoleAssignmentByDepartment"), pulumi.Alias(type_="azure-native:billing/v20191001preview:BillingRoleAssignmentByDepartment"), pulumi.Alias(type_="azure-nextgen:billing/v20191001preview:BillingRoleAssignmentByDepartment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BillingRoleAssignmentByDepartment, __self__).__init__(
            'azure-native:billing:BillingRoleAssignmentByDepartment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BillingRoleAssignmentByDepartment':
        """
        Get an existing BillingRoleAssignmentByDepartment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BillingRoleAssignmentByDepartmentArgs.__new__(BillingRoleAssignmentByDepartmentArgs)

        __props__.__dict__["created_by_principal_id"] = None
        __props__.__dict__["created_by_principal_tenant_id"] = None
        __props__.__dict__["created_by_user_email_address"] = None
        __props__.__dict__["created_on"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["principal_id"] = None
        __props__.__dict__["principal_tenant_id"] = None
        __props__.__dict__["role_definition_id"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_authentication_type"] = None
        __props__.__dict__["user_email_address"] = None
        return BillingRoleAssignmentByDepartment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdByPrincipalId")
    def created_by_principal_id(self) -> pulumi.Output[str]:
        """
        The principal Id of the user who created the role assignment.
        """
        return pulumi.get(self, "created_by_principal_id")

    @property
    @pulumi.getter(name="createdByPrincipalTenantId")
    def created_by_principal_tenant_id(self) -> pulumi.Output[str]:
        """
        The tenant Id of the user who created the role assignment.
        """
        return pulumi.get(self, "created_by_principal_tenant_id")

    @property
    @pulumi.getter(name="createdByUserEmailAddress")
    def created_by_user_email_address(self) -> pulumi.Output[str]:
        """
        The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.
        """
        return pulumi.get(self, "created_by_user_email_address")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        """
        The date the role assignment was created.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[Optional[str]]:
        """
        The principal id of the user to whom the role was assigned.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="principalTenantId")
    def principal_tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        The principal tenant id of the user to whom the role was assigned.
        """
        return pulumi.get(self, "principal_tenant_id")

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the role definition.
        """
        return pulumi.get(self, "role_definition_id")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        The scope at which the role was assigned.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAuthenticationType")
    def user_authentication_type(self) -> pulumi.Output[Optional[str]]:
        """
        The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.
        """
        return pulumi.get(self, "user_authentication_type")

    @property
    @pulumi.getter(name="userEmailAddress")
    def user_email_address(self) -> pulumi.Output[Optional[str]]:
        """
        The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.
        """
        return pulumi.get(self, "user_email_address")

