# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SecretCiphertextArgs', 'SecretCiphertext']

@pulumi.input_type
class SecretCiphertextArgs:
    def __init__(__self__, *,
                 crypto_key: pulumi.Input[str],
                 plaintext: pulumi.Input[str],
                 additional_authenticated_data: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecretCiphertext resource.
        :param pulumi.Input[str] crypto_key: The full name of the CryptoKey that will be used to encrypt the provided plaintext.
               Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'`
        :param pulumi.Input[str] plaintext: The plaintext to be encrypted.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] additional_authenticated_data: The additional authenticated data used for integrity checks during encryption and decryption.
               **Note**: This property is sensitive and will not be displayed in the plan.
        """
        pulumi.set(__self__, "crypto_key", crypto_key)
        pulumi.set(__self__, "plaintext", plaintext)
        if additional_authenticated_data is not None:
            pulumi.set(__self__, "additional_authenticated_data", additional_authenticated_data)

    @property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> pulumi.Input[str]:
        """
        The full name of the CryptoKey that will be used to encrypt the provided plaintext.
        Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'`
        """
        return pulumi.get(self, "crypto_key")

    @crypto_key.setter
    def crypto_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "crypto_key", value)

    @property
    @pulumi.getter
    def plaintext(self) -> pulumi.Input[str]:
        """
        The plaintext to be encrypted.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "plaintext")

    @plaintext.setter
    def plaintext(self, value: pulumi.Input[str]):
        pulumi.set(self, "plaintext", value)

    @property
    @pulumi.getter(name="additionalAuthenticatedData")
    def additional_authenticated_data(self) -> Optional[pulumi.Input[str]]:
        """
        The additional authenticated data used for integrity checks during encryption and decryption.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "additional_authenticated_data")

    @additional_authenticated_data.setter
    def additional_authenticated_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "additional_authenticated_data", value)


@pulumi.input_type
class _SecretCiphertextState:
    def __init__(__self__, *,
                 additional_authenticated_data: Optional[pulumi.Input[str]] = None,
                 ciphertext: Optional[pulumi.Input[str]] = None,
                 crypto_key: Optional[pulumi.Input[str]] = None,
                 plaintext: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SecretCiphertext resources.
        :param pulumi.Input[str] additional_authenticated_data: The additional authenticated data used for integrity checks during encryption and decryption.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] ciphertext: Contains the result of encrypting the provided plaintext, encoded in base64.
        :param pulumi.Input[str] crypto_key: The full name of the CryptoKey that will be used to encrypt the provided plaintext.
               Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'`
        :param pulumi.Input[str] plaintext: The plaintext to be encrypted.
               **Note**: This property is sensitive and will not be displayed in the plan.
        """
        if additional_authenticated_data is not None:
            pulumi.set(__self__, "additional_authenticated_data", additional_authenticated_data)
        if ciphertext is not None:
            pulumi.set(__self__, "ciphertext", ciphertext)
        if crypto_key is not None:
            pulumi.set(__self__, "crypto_key", crypto_key)
        if plaintext is not None:
            pulumi.set(__self__, "plaintext", plaintext)

    @property
    @pulumi.getter(name="additionalAuthenticatedData")
    def additional_authenticated_data(self) -> Optional[pulumi.Input[str]]:
        """
        The additional authenticated data used for integrity checks during encryption and decryption.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "additional_authenticated_data")

    @additional_authenticated_data.setter
    def additional_authenticated_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "additional_authenticated_data", value)

    @property
    @pulumi.getter
    def ciphertext(self) -> Optional[pulumi.Input[str]]:
        """
        Contains the result of encrypting the provided plaintext, encoded in base64.
        """
        return pulumi.get(self, "ciphertext")

    @ciphertext.setter
    def ciphertext(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ciphertext", value)

    @property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> Optional[pulumi.Input[str]]:
        """
        The full name of the CryptoKey that will be used to encrypt the provided plaintext.
        Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'`
        """
        return pulumi.get(self, "crypto_key")

    @crypto_key.setter
    def crypto_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "crypto_key", value)

    @property
    @pulumi.getter
    def plaintext(self) -> Optional[pulumi.Input[str]]:
        """
        The plaintext to be encrypted.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "plaintext")

    @plaintext.setter
    def plaintext(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plaintext", value)


class SecretCiphertext(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_authenticated_data: Optional[pulumi.Input[str]] = None,
                 crypto_key: Optional[pulumi.Input[str]] = None,
                 plaintext: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Encrypts secret data with Google Cloud KMS and provides access to the ciphertext.

        > **NOTE:** Using this resource will allow you to conceal secret data within your
        resource definitions, but it does not take care of protecting that data in the
        logging output, plan output, or state output.  Please take care to secure your secret
        data outside of resource definitions.

        To get more information about SecretCiphertext, see:

        * [API documentation](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt)
        * How-to Guides
            * [Encrypting and decrypting data with a symmetric key](https://cloud.google.com/kms/docs/encrypt-decrypt)

        > **Warning:** All arguments including `plaintext` and `additional_authenticated_data` will be stored in the raw
        state as plain-text. [Read more about secrets in state](https://www.pulumi.com/docs/intro/concepts/programming-model/#secrets).

        ## Example Usage
        ### Kms Secret Ciphertext Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        keyring = gcp.kms.KeyRing("keyring", location="global")
        cryptokey = gcp.kms.CryptoKey("cryptokey",
            key_ring=keyring.id,
            rotation_period="100000s")
        my_password = gcp.kms.SecretCiphertext("myPassword",
            crypto_key=cryptokey.id,
            plaintext="my-secret-password")
        instance = gcp.compute.Instance("instance",
            machine_type="e2-medium",
            zone="us-central1-a",
            boot_disk=gcp.compute.InstanceBootDiskArgs(
                initialize_params=gcp.compute.InstanceBootDiskInitializeParamsArgs(
                    image="debian-cloud/debian-9",
                ),
            ),
            network_interfaces=[gcp.compute.InstanceNetworkInterfaceArgs(
                network="default",
                access_configs=[gcp.compute.InstanceNetworkInterfaceAccessConfigArgs()],
            )],
            metadata={
                "password": my_password.ciphertext,
            })
        ```

        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] additional_authenticated_data: The additional authenticated data used for integrity checks during encryption and decryption.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] crypto_key: The full name of the CryptoKey that will be used to encrypt the provided plaintext.
               Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'`
        :param pulumi.Input[str] plaintext: The plaintext to be encrypted.
               **Note**: This property is sensitive and will not be displayed in the plan.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecretCiphertextArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Encrypts secret data with Google Cloud KMS and provides access to the ciphertext.

        > **NOTE:** Using this resource will allow you to conceal secret data within your
        resource definitions, but it does not take care of protecting that data in the
        logging output, plan output, or state output.  Please take care to secure your secret
        data outside of resource definitions.

        To get more information about SecretCiphertext, see:

        * [API documentation](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt)
        * How-to Guides
            * [Encrypting and decrypting data with a symmetric key](https://cloud.google.com/kms/docs/encrypt-decrypt)

        > **Warning:** All arguments including `plaintext` and `additional_authenticated_data` will be stored in the raw
        state as plain-text. [Read more about secrets in state](https://www.pulumi.com/docs/intro/concepts/programming-model/#secrets).

        ## Example Usage
        ### Kms Secret Ciphertext Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        keyring = gcp.kms.KeyRing("keyring", location="global")
        cryptokey = gcp.kms.CryptoKey("cryptokey",
            key_ring=keyring.id,
            rotation_period="100000s")
        my_password = gcp.kms.SecretCiphertext("myPassword",
            crypto_key=cryptokey.id,
            plaintext="my-secret-password")
        instance = gcp.compute.Instance("instance",
            machine_type="e2-medium",
            zone="us-central1-a",
            boot_disk=gcp.compute.InstanceBootDiskArgs(
                initialize_params=gcp.compute.InstanceBootDiskInitializeParamsArgs(
                    image="debian-cloud/debian-9",
                ),
            ),
            network_interfaces=[gcp.compute.InstanceNetworkInterfaceArgs(
                network="default",
                access_configs=[gcp.compute.InstanceNetworkInterfaceAccessConfigArgs()],
            )],
            metadata={
                "password": my_password.ciphertext,
            })
        ```

        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param SecretCiphertextArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecretCiphertextArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_authenticated_data: Optional[pulumi.Input[str]] = None,
                 crypto_key: Optional[pulumi.Input[str]] = None,
                 plaintext: Optional[pulumi.Input[str]] = None,
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
            __props__ = SecretCiphertextArgs.__new__(SecretCiphertextArgs)

            __props__.__dict__["additional_authenticated_data"] = additional_authenticated_data
            if crypto_key is None and not opts.urn:
                raise TypeError("Missing required property 'crypto_key'")
            __props__.__dict__["crypto_key"] = crypto_key
            if plaintext is None and not opts.urn:
                raise TypeError("Missing required property 'plaintext'")
            __props__.__dict__["plaintext"] = plaintext
            __props__.__dict__["ciphertext"] = None
        super(SecretCiphertext, __self__).__init__(
            'gcp:kms/secretCiphertext:SecretCiphertext',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            additional_authenticated_data: Optional[pulumi.Input[str]] = None,
            ciphertext: Optional[pulumi.Input[str]] = None,
            crypto_key: Optional[pulumi.Input[str]] = None,
            plaintext: Optional[pulumi.Input[str]] = None) -> 'SecretCiphertext':
        """
        Get an existing SecretCiphertext resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] additional_authenticated_data: The additional authenticated data used for integrity checks during encryption and decryption.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] ciphertext: Contains the result of encrypting the provided plaintext, encoded in base64.
        :param pulumi.Input[str] crypto_key: The full name of the CryptoKey that will be used to encrypt the provided plaintext.
               Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'`
        :param pulumi.Input[str] plaintext: The plaintext to be encrypted.
               **Note**: This property is sensitive and will not be displayed in the plan.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecretCiphertextState.__new__(_SecretCiphertextState)

        __props__.__dict__["additional_authenticated_data"] = additional_authenticated_data
        __props__.__dict__["ciphertext"] = ciphertext
        __props__.__dict__["crypto_key"] = crypto_key
        __props__.__dict__["plaintext"] = plaintext
        return SecretCiphertext(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalAuthenticatedData")
    def additional_authenticated_data(self) -> pulumi.Output[Optional[str]]:
        """
        The additional authenticated data used for integrity checks during encryption and decryption.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "additional_authenticated_data")

    @property
    @pulumi.getter
    def ciphertext(self) -> pulumi.Output[str]:
        """
        Contains the result of encrypting the provided plaintext, encoded in base64.
        """
        return pulumi.get(self, "ciphertext")

    @property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> pulumi.Output[str]:
        """
        The full name of the CryptoKey that will be used to encrypt the provided plaintext.
        Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'`
        """
        return pulumi.get(self, "crypto_key")

    @property
    @pulumi.getter
    def plaintext(self) -> pulumi.Output[str]:
        """
        The plaintext to be encrypted.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "plaintext")

