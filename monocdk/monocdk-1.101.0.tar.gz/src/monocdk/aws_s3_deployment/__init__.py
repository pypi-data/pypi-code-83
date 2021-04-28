'''
# AWS S3 Deployment Construct Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

> **Status: Experimental**

This library allows populating an S3 bucket with the contents of .zip files
from other S3 buckets or from local disk.

The following example defines a publicly accessible S3 bucket with web hosting
enabled and populates it from a local directory on disk.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
website_bucket = s3.Bucket(self, "WebsiteBucket",
    website_index_document="index.html",
    public_read_access=True
)

s3deploy.BucketDeployment(self, "DeployWebsite",
    sources=[s3deploy.Source.asset("./website-dist")],
    destination_bucket=website_bucket,
    destination_key_prefix="web/static"
)
```

This is what happens under the hood:

1. When this stack is deployed (either via `cdk deploy` or via CI/CD), the
   contents of the local `website-dist` directory will be archived and uploaded
   to an intermediary assets bucket. If there is more than one source, they will
   be individually uploaded.
2. The `BucketDeployment` construct synthesizes a custom CloudFormation resource
   of type `Custom::CDKBucketDeployment` into the template. The source bucket/key
   is set to point to the assets bucket.
3. The custom resource downloads the .zip archive, extracts it and issues `aws s3 sync --delete` against the destination bucket (in this case
   `websiteBucket`). If there is more than one source, the sources will be
   downloaded and merged pre-deployment at this step.

## Supported sources

The following source types are supported for bucket deployments:

* Local .zip file: `s3deploy.Source.asset('/path/to/local/file.zip')`
* Local directory: `s3deploy.Source.asset('/path/to/local/directory')`
* Another bucket: `s3deploy.Source.bucket(bucket, zipObjectKey)`

To create a source from a single file, you can pass `AssetOptions` to exclude
all but a single file:

* Single file: `s3deploy.Source.asset('/path/to/local/directory', { exclude: ['**', '!onlyThisFile.txt'] })`

## Retain on Delete

By default, the contents of the destination bucket will **not** be deleted when the
`BucketDeployment` resource is removed from the stack or when the destination is
changed. You can use the option `retainOnDelete: false` to disable this behavior,
in which case the contents will be deleted.

Configuring this has a few implications you should be aware of:

* **Logical ID Changes**

  Changing the logical ID of the `BucketDeployment` construct, without changing the destination
  (for example due to refactoring, or intentional ID change) **will result in the deletion of the objects**.
  This is because CloudFormation will first create the new resource, which will have no affect,
  followed by a deletion of the old resource, which will cause a deletion of the objects,
  since the destination hasn't changed, and `retainOnDelete` is `false`.
* **Destination Changes**

  When the destination bucket or prefix is changed, all files in the previous destination will **first** be
  deleted and then uploaded to the new destination location. This could have availablity implications
  on your users.

### General Recommendations

#### Shared Bucket

If the destination bucket **is not** dedicated to the specific `BucketDeployment` construct (i.e shared by other entities),
we recommend to always configure the `destinationKeyPrefix` property. This will prevent the deployment from
accidentally deleting data that wasn't uploaded by it.

#### Dedicated Bucket

If the destination bucket **is** dedicated, it might be reasonable to skip the prefix configuration,
in which case, we recommend to remove `retainOnDelete: false`, and instead, configure the
[`autoDeleteObjects`](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-s3-readme.html#bucket-deletion)
property on the destination bucket. This will avoid the logical ID problem mentioned above.

## Prune

By default, files in the destination bucket that don't exist in the source will be deleted
when the `BucketDeployment` resource is created or updated. You can use the option `prune: false` to disable
this behavior, in which case the files will not be deleted.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
s3deploy.BucketDeployment(self, "DeployMeWithoutDeletingFilesOnDestination",
    sources=[s3deploy.Source.asset(path.join(__dirname, "my-website"))],
    destination_bucket=destination_bucket,
    prune=False
)
```

This option also enables you to specify multiple bucket deployments for the same destination bucket & prefix,
each with its own characteristics. For example, you can set different cache-control headers
based on file extensions:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
BucketDeployment(self, "BucketDeployment",
    sources=[Source.asset("./website", exclude=["index.html"])],
    destination_bucket=bucket,
    cache_control=[CacheControl.from_string("max-age=31536000,public,immutable")],
    prune=False
)

BucketDeployment(self, "HTMLBucketDeployment",
    sources=[Source.asset("./website", exclude=["*", "!index.html"])],
    destination_bucket=bucket,
    cache_control=[CacheControl.from_string("max-age=0,no-cache,no-store,must-revalidate")],
    prune=False
)
```

## Objects metadata

You can specify metadata to be set on all the objects in your deployment.
There are 2 types of metadata in S3: system-defined metadata and user-defined metadata.
System-defined metadata have a special purpose, for example cache-control defines how long to keep an object cached.
User-defined metadata are not used by S3 and keys always begin with `x-amz-meta-` (this prefix is added automatically).

System defined metadata keys include the following:

* cache-control
* content-disposition
* content-encoding
* content-language
* content-type
* expires
* server-side-encryption
* storage-class
* website-redirect-location
* ssekms-key-id
* sse-customer-algorithm

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
website_bucket = s3.Bucket(self, "WebsiteBucket",
    website_index_document="index.html",
    public_read_access=True
)

s3deploy.BucketDeployment(self, "DeployWebsite",
    sources=[s3deploy.Source.asset("./website-dist")],
    destination_bucket=website_bucket,
    destination_key_prefix="web/static", # optional prefix in destination bucket
    metadata={"A": "1", "b": "2"}, # user-defined metadata

    # system-defined metadata
    content_type="text/html",
    content_language="en",
    storage_class=StorageClass.INTELLIGENT_TIERING,
    server_side_encryption=ServerSideEncryption.AES_256,
    cache_control=[CacheControl.set_public(), CacheControl.max_age(cdk.Duration.hours(1))]
)
```

## CloudFront Invalidation

You can provide a CloudFront distribution and optional paths to invalidate after the bucket deployment finishes.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins


bucket = s3.Bucket(self, "Destination")

# Handles buckets whether or not they are configured for website hosting.
distribution = cloudfront.Distribution(self, "Distribution",
    default_behavior=BehaviorOptions(origin=origins.S3Origin(bucket))
)

s3deploy.BucketDeployment(self, "DeployWithInvalidation",
    sources=[s3deploy.Source.asset("./website-dist")],
    destination_bucket=bucket,
    distribution=distribution,
    distribution_paths=["/images/*.png"]
)
```

## Memory Limit

The default memory limit for the deployment resource is 128MiB. If you need to
copy larger files, you can use the `memoryLimit` configuration to specify the
size of the AWS Lambda resource handler.

> NOTE: a new AWS Lambda handler will be created in your stack for each memory
> limit configuration.

## Notes

* This library uses an AWS CloudFormation custom resource which about 10MiB in
  size. The code of this resource is bundled with this library.
* AWS Lambda execution time is limited to 15min. This limits the amount of data
  which can be deployed into the bucket by this timeout.
* When the `BucketDeployment` is removed from the stack, the contents are retained
  in the destination bucket ([#952](https://github.com/aws/aws-cdk/issues/952)).
* Bucket deployment *only happens* during stack create/update. This means that
  if you wish to update the contents of the destination, you will need to
  change the source s3 key (or bucket), so that the resource will be updated.
  This is inline with best practices. If you use local disk assets, this will
  happen automatically whenever you modify the asset, since the S3 key is based
  on a hash of the asset contents.

## Development

The custom resource is implemented in Python 3.6 in order to be able to leverage
the AWS CLI for "aws sync". The code is under [`lib/lambda`](https://github.com/aws/aws-cdk/tree/master/packages/%40aws-cdk/aws-s3-deployment/lib/lambda) and
unit tests are under [`test/lambda`](https://github.com/aws/aws-cdk/tree/master/packages/%40aws-cdk/aws-s3-deployment/test/lambda).

This package requires Python 3.6 during build time in order to create the custom
resource Lambda bundle and test it. It also relies on a few bash scripts, so
might be tricky to build on Windows.

## Roadmap

* [ ] Support "blue/green" deployments ([#954](https://github.com/aws/aws-cdk/issues/954))
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
    AssetHashType as _AssetHashType_49193809,
    BundlingOptions as _BundlingOptions_ab115a99,
    Construct as _Construct_e78e779f,
    Duration as _Duration_070aa057,
    Expiration as _Expiration_505df041,
    IgnoreMode as _IgnoreMode_31d8bf46,
    SymlinkFollowMode as _SymlinkFollowMode_abf4527a,
)
from ..assets import FollowMode as _FollowMode_98b05cc5
from ..aws_cloudfront import IDistribution as _IDistribution_685deca5
from ..aws_ec2 import (
    IVpc as _IVpc_6d1f76c4, SubnetSelection as _SubnetSelection_1284e62c
)
from ..aws_iam import IGrantable as _IGrantable_4c5a91d1, IRole as _IRole_59af6f50
from ..aws_s3 import IBucket as _IBucket_73486e29
from ..aws_s3_assets import AssetOptions as _AssetOptions_bd2996da


class BucketDeployment(
    _Construct_e78e779f,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_s3_deployment.BucketDeployment",
):
    '''(experimental) ``BucketDeployment`` populates an S3 bucket with the contents of .zip files from other S3 buckets or from local disk.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        destination_bucket: _IBucket_73486e29,
        sources: typing.Sequence["ISource"],
        cache_control: typing.Optional[typing.Sequence["CacheControl"]] = None,
        content_disposition: typing.Optional[builtins.str] = None,
        content_encoding: typing.Optional[builtins.str] = None,
        content_language: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        destination_key_prefix: typing.Optional[builtins.str] = None,
        distribution: typing.Optional[_IDistribution_685deca5] = None,
        distribution_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        expires: typing.Optional[_Expiration_505df041] = None,
        memory_limit: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional["UserDefinedObjectMetadata"] = None,
        prune: typing.Optional[builtins.bool] = None,
        retain_on_delete: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_59af6f50] = None,
        server_side_encryption: typing.Optional["ServerSideEncryption"] = None,
        server_side_encryption_aws_kms_key_id: typing.Optional[builtins.str] = None,
        server_side_encryption_customer_algorithm: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional["StorageClass"] = None,
        vpc: typing.Optional[_IVpc_6d1f76c4] = None,
        vpc_subnets: typing.Optional[_SubnetSelection_1284e62c] = None,
        website_redirect_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param destination_bucket: (experimental) The S3 bucket to sync the contents of the zip file to.
        :param sources: (experimental) The sources from which to deploy the contents of this bucket.
        :param cache_control: (experimental) System-defined cache-control metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_disposition: (experimental) System-defined cache-disposition metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_encoding: (experimental) System-defined content-encoding metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_language: (experimental) System-defined content-language metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_type: (experimental) System-defined content-type metadata to be set on all objects in the deployment. Default: - Not set.
        :param destination_key_prefix: (experimental) Key prefix in the destination bucket. Default: "/" (unzip to root of the destination bucket)
        :param distribution: (experimental) The CloudFront distribution using the destination bucket as an origin. Files in the distribution's edge caches will be invalidated after files are uploaded to the destination bucket. Default: - No invalidation occurs
        :param distribution_paths: (experimental) The file paths to invalidate in the CloudFront distribution. Default: - All files under the destination bucket key prefix will be invalidated.
        :param expires: (experimental) System-defined expires metadata to be set on all objects in the deployment. Default: - The objects in the distribution will not expire.
        :param memory_limit: (experimental) The amount of memory (in MiB) to allocate to the AWS Lambda function which replicates the files from the CDK bucket to the destination bucket. If you are deploying large files, you will need to increase this number accordingly. Default: 128
        :param metadata: (experimental) User-defined object metadata to be set on all objects in the deployment. Default: - No user metadata is set
        :param prune: (experimental) If this is set to false, files in the destination bucket that do not exist in the asset, will NOT be deleted during deployment (create/update). Default: true
        :param retain_on_delete: (experimental) If this is set to "false", the destination files will be deleted when the resource is deleted or the destination is updated. NOTICE: Configuring this to "false" might have operational implications. Please visit to the package documentation referred below to make sure you fully understand those implications. Default: true - when resource is deleted/updated, files are retained
        :param role: (experimental) Execution role associated with this function. Default: - A role is automatically created
        :param server_side_encryption: (experimental) System-defined x-amz-server-side-encryption metadata to be set on all objects in the deployment. Default: - Server side encryption is not used.
        :param server_side_encryption_aws_kms_key_id: (experimental) System-defined x-amz-server-side-encryption-aws-kms-key-id metadata to be set on all objects in the deployment. Default: - Not set.
        :param server_side_encryption_customer_algorithm: (experimental) System-defined x-amz-server-side-encryption-customer-algorithm metadata to be set on all objects in the deployment. Warning: This is not a useful parameter until this bug is fixed: https://github.com/aws/aws-cdk/issues/6080 Default: - Not set.
        :param storage_class: (experimental) System-defined x-amz-storage-class metadata to be set on all objects in the deployment. Default: - Default storage-class for the bucket is used.
        :param vpc: (experimental) The VPC network to place the deployment lambda handler in. Default: None
        :param vpc_subnets: (experimental) Where in the VPC to place the deployment lambda handler. Only used if 'vpc' is supplied. Default: - the Vpc default strategy if not specified
        :param website_redirect_location: (experimental) System-defined x-amz-website-redirect-location metadata to be set on all objects in the deployment. Default: - No website redirection.

        :stability: experimental
        '''
        props = BucketDeploymentProps(
            destination_bucket=destination_bucket,
            sources=sources,
            cache_control=cache_control,
            content_disposition=content_disposition,
            content_encoding=content_encoding,
            content_language=content_language,
            content_type=content_type,
            destination_key_prefix=destination_key_prefix,
            distribution=distribution,
            distribution_paths=distribution_paths,
            expires=expires,
            memory_limit=memory_limit,
            metadata=metadata,
            prune=prune,
            retain_on_delete=retain_on_delete,
            role=role,
            server_side_encryption=server_side_encryption,
            server_side_encryption_aws_kms_key_id=server_side_encryption_aws_kms_key_id,
            server_side_encryption_customer_algorithm=server_side_encryption_customer_algorithm,
            storage_class=storage_class,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            website_redirect_location=website_redirect_location,
        )

        jsii.create(BucketDeployment, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_s3_deployment.BucketDeploymentProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_bucket": "destinationBucket",
        "sources": "sources",
        "cache_control": "cacheControl",
        "content_disposition": "contentDisposition",
        "content_encoding": "contentEncoding",
        "content_language": "contentLanguage",
        "content_type": "contentType",
        "destination_key_prefix": "destinationKeyPrefix",
        "distribution": "distribution",
        "distribution_paths": "distributionPaths",
        "expires": "expires",
        "memory_limit": "memoryLimit",
        "metadata": "metadata",
        "prune": "prune",
        "retain_on_delete": "retainOnDelete",
        "role": "role",
        "server_side_encryption": "serverSideEncryption",
        "server_side_encryption_aws_kms_key_id": "serverSideEncryptionAwsKmsKeyId",
        "server_side_encryption_customer_algorithm": "serverSideEncryptionCustomerAlgorithm",
        "storage_class": "storageClass",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "website_redirect_location": "websiteRedirectLocation",
    },
)
class BucketDeploymentProps:
    def __init__(
        self,
        *,
        destination_bucket: _IBucket_73486e29,
        sources: typing.Sequence["ISource"],
        cache_control: typing.Optional[typing.Sequence["CacheControl"]] = None,
        content_disposition: typing.Optional[builtins.str] = None,
        content_encoding: typing.Optional[builtins.str] = None,
        content_language: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        destination_key_prefix: typing.Optional[builtins.str] = None,
        distribution: typing.Optional[_IDistribution_685deca5] = None,
        distribution_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        expires: typing.Optional[_Expiration_505df041] = None,
        memory_limit: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional["UserDefinedObjectMetadata"] = None,
        prune: typing.Optional[builtins.bool] = None,
        retain_on_delete: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_59af6f50] = None,
        server_side_encryption: typing.Optional["ServerSideEncryption"] = None,
        server_side_encryption_aws_kms_key_id: typing.Optional[builtins.str] = None,
        server_side_encryption_customer_algorithm: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional["StorageClass"] = None,
        vpc: typing.Optional[_IVpc_6d1f76c4] = None,
        vpc_subnets: typing.Optional[_SubnetSelection_1284e62c] = None,
        website_redirect_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties for ``BucketDeployment``.

        :param destination_bucket: (experimental) The S3 bucket to sync the contents of the zip file to.
        :param sources: (experimental) The sources from which to deploy the contents of this bucket.
        :param cache_control: (experimental) System-defined cache-control metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_disposition: (experimental) System-defined cache-disposition metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_encoding: (experimental) System-defined content-encoding metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_language: (experimental) System-defined content-language metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_type: (experimental) System-defined content-type metadata to be set on all objects in the deployment. Default: - Not set.
        :param destination_key_prefix: (experimental) Key prefix in the destination bucket. Default: "/" (unzip to root of the destination bucket)
        :param distribution: (experimental) The CloudFront distribution using the destination bucket as an origin. Files in the distribution's edge caches will be invalidated after files are uploaded to the destination bucket. Default: - No invalidation occurs
        :param distribution_paths: (experimental) The file paths to invalidate in the CloudFront distribution. Default: - All files under the destination bucket key prefix will be invalidated.
        :param expires: (experimental) System-defined expires metadata to be set on all objects in the deployment. Default: - The objects in the distribution will not expire.
        :param memory_limit: (experimental) The amount of memory (in MiB) to allocate to the AWS Lambda function which replicates the files from the CDK bucket to the destination bucket. If you are deploying large files, you will need to increase this number accordingly. Default: 128
        :param metadata: (experimental) User-defined object metadata to be set on all objects in the deployment. Default: - No user metadata is set
        :param prune: (experimental) If this is set to false, files in the destination bucket that do not exist in the asset, will NOT be deleted during deployment (create/update). Default: true
        :param retain_on_delete: (experimental) If this is set to "false", the destination files will be deleted when the resource is deleted or the destination is updated. NOTICE: Configuring this to "false" might have operational implications. Please visit to the package documentation referred below to make sure you fully understand those implications. Default: true - when resource is deleted/updated, files are retained
        :param role: (experimental) Execution role associated with this function. Default: - A role is automatically created
        :param server_side_encryption: (experimental) System-defined x-amz-server-side-encryption metadata to be set on all objects in the deployment. Default: - Server side encryption is not used.
        :param server_side_encryption_aws_kms_key_id: (experimental) System-defined x-amz-server-side-encryption-aws-kms-key-id metadata to be set on all objects in the deployment. Default: - Not set.
        :param server_side_encryption_customer_algorithm: (experimental) System-defined x-amz-server-side-encryption-customer-algorithm metadata to be set on all objects in the deployment. Warning: This is not a useful parameter until this bug is fixed: https://github.com/aws/aws-cdk/issues/6080 Default: - Not set.
        :param storage_class: (experimental) System-defined x-amz-storage-class metadata to be set on all objects in the deployment. Default: - Default storage-class for the bucket is used.
        :param vpc: (experimental) The VPC network to place the deployment lambda handler in. Default: None
        :param vpc_subnets: (experimental) Where in the VPC to place the deployment lambda handler. Only used if 'vpc' is supplied. Default: - the Vpc default strategy if not specified
        :param website_redirect_location: (experimental) System-defined x-amz-website-redirect-location metadata to be set on all objects in the deployment. Default: - No website redirection.

        :stability: experimental
        '''
        if isinstance(metadata, dict):
            metadata = UserDefinedObjectMetadata(**metadata)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_1284e62c(**vpc_subnets)
        self._values: typing.Dict[str, typing.Any] = {
            "destination_bucket": destination_bucket,
            "sources": sources,
        }
        if cache_control is not None:
            self._values["cache_control"] = cache_control
        if content_disposition is not None:
            self._values["content_disposition"] = content_disposition
        if content_encoding is not None:
            self._values["content_encoding"] = content_encoding
        if content_language is not None:
            self._values["content_language"] = content_language
        if content_type is not None:
            self._values["content_type"] = content_type
        if destination_key_prefix is not None:
            self._values["destination_key_prefix"] = destination_key_prefix
        if distribution is not None:
            self._values["distribution"] = distribution
        if distribution_paths is not None:
            self._values["distribution_paths"] = distribution_paths
        if expires is not None:
            self._values["expires"] = expires
        if memory_limit is not None:
            self._values["memory_limit"] = memory_limit
        if metadata is not None:
            self._values["metadata"] = metadata
        if prune is not None:
            self._values["prune"] = prune
        if retain_on_delete is not None:
            self._values["retain_on_delete"] = retain_on_delete
        if role is not None:
            self._values["role"] = role
        if server_side_encryption is not None:
            self._values["server_side_encryption"] = server_side_encryption
        if server_side_encryption_aws_kms_key_id is not None:
            self._values["server_side_encryption_aws_kms_key_id"] = server_side_encryption_aws_kms_key_id
        if server_side_encryption_customer_algorithm is not None:
            self._values["server_side_encryption_customer_algorithm"] = server_side_encryption_customer_algorithm
        if storage_class is not None:
            self._values["storage_class"] = storage_class
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if website_redirect_location is not None:
            self._values["website_redirect_location"] = website_redirect_location

    @builtins.property
    def destination_bucket(self) -> _IBucket_73486e29:
        '''(experimental) The S3 bucket to sync the contents of the zip file to.

        :stability: experimental
        '''
        result = self._values.get("destination_bucket")
        assert result is not None, "Required property 'destination_bucket' is missing"
        return typing.cast(_IBucket_73486e29, result)

    @builtins.property
    def sources(self) -> typing.List["ISource"]:
        '''(experimental) The sources from which to deploy the contents of this bucket.

        :stability: experimental
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List["ISource"], result)

    @builtins.property
    def cache_control(self) -> typing.Optional[typing.List["CacheControl"]]:
        '''(experimental) System-defined cache-control metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        :stability: experimental
        '''
        result = self._values.get("cache_control")
        return typing.cast(typing.Optional[typing.List["CacheControl"]], result)

    @builtins.property
    def content_disposition(self) -> typing.Optional[builtins.str]:
        '''(experimental) System-defined cache-disposition metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        :stability: experimental
        '''
        result = self._values.get("content_disposition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_encoding(self) -> typing.Optional[builtins.str]:
        '''(experimental) System-defined content-encoding metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        :stability: experimental
        '''
        result = self._values.get("content_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_language(self) -> typing.Optional[builtins.str]:
        '''(experimental) System-defined content-language metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        :stability: experimental
        '''
        result = self._values.get("content_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) System-defined content-type metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        :stability: experimental
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_key_prefix(self) -> typing.Optional[builtins.str]:
        '''(experimental) Key prefix in the destination bucket.

        :default: "/" (unzip to root of the destination bucket)

        :stability: experimental
        '''
        result = self._values.get("destination_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distribution(self) -> typing.Optional[_IDistribution_685deca5]:
        '''(experimental) The CloudFront distribution using the destination bucket as an origin.

        Files in the distribution's edge caches will be invalidated after
        files are uploaded to the destination bucket.

        :default: - No invalidation occurs

        :stability: experimental
        '''
        result = self._values.get("distribution")
        return typing.cast(typing.Optional[_IDistribution_685deca5], result)

    @builtins.property
    def distribution_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) The file paths to invalidate in the CloudFront distribution.

        :default: - All files under the destination bucket key prefix will be invalidated.

        :stability: experimental
        '''
        result = self._values.get("distribution_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def expires(self) -> typing.Optional[_Expiration_505df041]:
        '''(experimental) System-defined expires metadata to be set on all objects in the deployment.

        :default: - The objects in the distribution will not expire.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        :stability: experimental
        '''
        result = self._values.get("expires")
        return typing.cast(typing.Optional[_Expiration_505df041], result)

    @builtins.property
    def memory_limit(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The amount of memory (in MiB) to allocate to the AWS Lambda function which replicates the files from the CDK bucket to the destination bucket.

        If you are deploying large files, you will need to increase this number
        accordingly.

        :default: 128

        :stability: experimental
        '''
        result = self._values.get("memory_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metadata(self) -> typing.Optional["UserDefinedObjectMetadata"]:
        '''(experimental) User-defined object metadata to be set on all objects in the deployment.

        :default: - No user metadata is set

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#UserMetadata
        :stability: experimental
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional["UserDefinedObjectMetadata"], result)

    @builtins.property
    def prune(self) -> typing.Optional[builtins.bool]:
        '''(experimental) If this is set to false, files in the destination bucket that do not exist in the asset, will NOT be deleted during deployment (create/update).

        :default: true

        :see: https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html
        :stability: experimental
        '''
        result = self._values.get("prune")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def retain_on_delete(self) -> typing.Optional[builtins.bool]:
        '''(experimental) If this is set to "false", the destination files will be deleted when the resource is deleted or the destination is updated.

        NOTICE: Configuring this to "false" might have operational implications. Please
        visit to the package documentation referred below to make sure you fully understand those implications.

        :default: true - when resource is deleted/updated, files are retained

        :see: https://github.com/aws/aws-cdk/tree/master/packages/%40aws-cdk/aws-s3-deployment#retain-on-delete
        :stability: experimental
        '''
        result = self._values.get("retain_on_delete")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        '''(experimental) Execution role associated with this function.

        :default: - A role is automatically created

        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_59af6f50], result)

    @builtins.property
    def server_side_encryption(self) -> typing.Optional["ServerSideEncryption"]:
        '''(experimental) System-defined x-amz-server-side-encryption metadata to be set on all objects in the deployment.

        :default: - Server side encryption is not used.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        :stability: experimental
        '''
        result = self._values.get("server_side_encryption")
        return typing.cast(typing.Optional["ServerSideEncryption"], result)

    @builtins.property
    def server_side_encryption_aws_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) System-defined x-amz-server-side-encryption-aws-kms-key-id metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        :stability: experimental
        '''
        result = self._values.get("server_side_encryption_aws_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_encryption_customer_algorithm(
        self,
    ) -> typing.Optional[builtins.str]:
        '''(experimental) System-defined x-amz-server-side-encryption-customer-algorithm metadata to be set on all objects in the deployment.

        Warning: This is not a useful parameter until this bug is fixed: https://github.com/aws/aws-cdk/issues/6080

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html#sse-c-how-to-programmatically-intro
        :stability: experimental
        '''
        result = self._values.get("server_side_encryption_customer_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class(self) -> typing.Optional["StorageClass"]:
        '''(experimental) System-defined x-amz-storage-class metadata to be set on all objects in the deployment.

        :default: - Default storage-class for the bucket is used.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        :stability: experimental
        '''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional["StorageClass"], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_6d1f76c4]:
        '''(experimental) The VPC network to place the deployment lambda handler in.

        :default: None

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_IVpc_6d1f76c4], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_1284e62c]:
        '''(experimental) Where in the VPC to place the deployment lambda handler.

        Only used if 'vpc' is supplied.

        :default: - the Vpc default strategy if not specified

        :stability: experimental
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_1284e62c], result)

    @builtins.property
    def website_redirect_location(self) -> typing.Optional[builtins.str]:
        '''(experimental) System-defined x-amz-website-redirect-location metadata to be set on all objects in the deployment.

        :default: - No website redirection.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        :stability: experimental
        '''
        result = self._values.get("website_redirect_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BucketDeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CacheControl(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_s3_deployment.CacheControl",
):
    '''(experimental) Used for HTTP cache-control header, which influences downstream caches.

    :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
    :stability: experimental
    '''

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(cls, s: builtins.str) -> "CacheControl":
        '''(experimental) Constructs a custom cache control key from the literal value.

        :param s: -

        :stability: experimental
        '''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "fromString", [s]))

    @jsii.member(jsii_name="maxAge") # type: ignore[misc]
    @builtins.classmethod
    def max_age(cls, t: _Duration_070aa057) -> "CacheControl":
        '''(experimental) Sets 'max-age='.

        :param t: -

        :stability: experimental
        '''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "maxAge", [t]))

    @jsii.member(jsii_name="mustRevalidate") # type: ignore[misc]
    @builtins.classmethod
    def must_revalidate(cls) -> "CacheControl":
        '''(experimental) Sets 'must-revalidate'.

        :stability: experimental
        '''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "mustRevalidate", []))

    @jsii.member(jsii_name="noCache") # type: ignore[misc]
    @builtins.classmethod
    def no_cache(cls) -> "CacheControl":
        '''(experimental) Sets 'no-cache'.

        :stability: experimental
        '''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "noCache", []))

    @jsii.member(jsii_name="noTransform") # type: ignore[misc]
    @builtins.classmethod
    def no_transform(cls) -> "CacheControl":
        '''(experimental) Sets 'no-transform'.

        :stability: experimental
        '''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "noTransform", []))

    @jsii.member(jsii_name="proxyRevalidate") # type: ignore[misc]
    @builtins.classmethod
    def proxy_revalidate(cls) -> "CacheControl":
        '''(experimental) Sets 'proxy-revalidate'.

        :stability: experimental
        '''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "proxyRevalidate", []))

    @jsii.member(jsii_name="setPrivate") # type: ignore[misc]
    @builtins.classmethod
    def set_private(cls) -> "CacheControl":
        '''(experimental) Sets 'private'.

        :stability: experimental
        '''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "setPrivate", []))

    @jsii.member(jsii_name="setPublic") # type: ignore[misc]
    @builtins.classmethod
    def set_public(cls) -> "CacheControl":
        '''(experimental) Sets 'public'.

        :stability: experimental
        '''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "setPublic", []))

    @jsii.member(jsii_name="sMaxAge") # type: ignore[misc]
    @builtins.classmethod
    def s_max_age(cls, t: _Duration_070aa057) -> "CacheControl":
        '''(experimental) Sets 's-maxage='.

        :param t: -

        :stability: experimental
        '''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "sMaxAge", [t]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''(experimental) The raw cache control setting.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="monocdk.aws_s3_deployment.DeploymentSourceContext",
    jsii_struct_bases=[],
    name_mapping={"handler_role": "handlerRole"},
)
class DeploymentSourceContext:
    def __init__(self, *, handler_role: _IRole_59af6f50) -> None:
        '''(experimental) Bind context for ISources.

        :param handler_role: (experimental) The role for the handler.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "handler_role": handler_role,
        }

    @builtins.property
    def handler_role(self) -> _IRole_59af6f50:
        '''(experimental) The role for the handler.

        :stability: experimental
        '''
        result = self._values.get("handler_role")
        assert result is not None, "Required property 'handler_role' is missing"
        return typing.cast(_IRole_59af6f50, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentSourceContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Expires(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_s3_deployment.Expires"):
    '''(deprecated) Used for HTTP expires header, which influences downstream caches.

    Does NOT influence deletion of the object.

    :deprecated: use core.Expiration

    :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
    :stability: deprecated
    '''

    @jsii.member(jsii_name="after") # type: ignore[misc]
    @builtins.classmethod
    def after(cls, t: _Duration_070aa057) -> "Expires":
        '''(deprecated) Expire once the specified duration has passed since deployment time.

        :param t: the duration to wait before expiring.

        :stability: deprecated
        '''
        return typing.cast("Expires", jsii.sinvoke(cls, "after", [t]))

    @jsii.member(jsii_name="atDate") # type: ignore[misc]
    @builtins.classmethod
    def at_date(cls, d: datetime.datetime) -> "Expires":
        '''(deprecated) Expire at the specified date.

        :param d: date to expire at.

        :stability: deprecated
        '''
        return typing.cast("Expires", jsii.sinvoke(cls, "atDate", [d]))

    @jsii.member(jsii_name="atTimestamp") # type: ignore[misc]
    @builtins.classmethod
    def at_timestamp(cls, t: jsii.Number) -> "Expires":
        '''(deprecated) Expire at the specified timestamp.

        :param t: timestamp in unix milliseconds.

        :stability: deprecated
        '''
        return typing.cast("Expires", jsii.sinvoke(cls, "atTimestamp", [t]))

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(cls, s: builtins.str) -> "Expires":
        '''(deprecated) Create an expiration date from a raw date string.

        :param s: -

        :stability: deprecated
        '''
        return typing.cast("Expires", jsii.sinvoke(cls, "fromString", [s]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''(deprecated) The raw expiration date expression.

        :stability: deprecated
        '''
        return typing.cast(typing.Any, jsii.get(self, "value"))


@jsii.interface(jsii_type="monocdk.aws_s3_deployment.ISource")
class ISource(typing_extensions.Protocol):
    '''(experimental) Represents a source for bucket deployments.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_ISourceProxy"]:
        return _ISourceProxy

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _Construct_e78e779f,
        *,
        handler_role: _IRole_59af6f50,
    ) -> "SourceConfig":
        '''(experimental) Binds the source to a bucket deployment.

        :param scope: The construct tree context.
        :param handler_role: (experimental) The role for the handler.

        :stability: experimental
        '''
        ...


class _ISourceProxy:
    '''(experimental) Represents a source for bucket deployments.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_s3_deployment.ISource"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _Construct_e78e779f,
        *,
        handler_role: _IRole_59af6f50,
    ) -> "SourceConfig":
        '''(experimental) Binds the source to a bucket deployment.

        :param scope: The construct tree context.
        :param handler_role: (experimental) The role for the handler.

        :stability: experimental
        '''
        context = DeploymentSourceContext(handler_role=handler_role)

        return typing.cast("SourceConfig", jsii.invoke(self, "bind", [scope, context]))


@jsii.enum(jsii_type="monocdk.aws_s3_deployment.ServerSideEncryption")
class ServerSideEncryption(enum.Enum):
    '''(experimental) Indicates whether server-side encryption is enabled for the object, and whether that encryption is from the AWS Key Management Service (AWS KMS) or from Amazon S3 managed encryption (SSE-S3).

    :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
    :stability: experimental
    '''

    AES_256 = "AES_256"
    '''(experimental) 'AES256'.

    :stability: experimental
    '''
    AWS_KMS = "AWS_KMS"
    '''(experimental) 'aws:kms'.

    :stability: experimental
    '''


class Source(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_s3_deployment.Source"):
    '''(experimental) Specifies bucket deployment source.

    Usage::

        Source.bucket(bucket, key)
        Source.asset('/local/path/to/directory')
        Source.asset('/local/path/to/a/file.zip')

    :stability: experimental
    '''

    @jsii.member(jsii_name="asset") # type: ignore[misc]
    @builtins.classmethod
    def asset(
        cls,
        path: builtins.str,
        *,
        readers: typing.Optional[typing.Sequence[_IGrantable_4c5a91d1]] = None,
        source_hash: typing.Optional[builtins.str] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow: typing.Optional[_FollowMode_98b05cc5] = None,
        ignore_mode: typing.Optional[_IgnoreMode_31d8bf46] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_abf4527a] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_AssetHashType_49193809] = None,
        bundling: typing.Optional[_BundlingOptions_ab115a99] = None,
    ) -> ISource:
        '''(experimental) Uses a local asset as the deployment source.

        :param path: The path to a local .zip file or a directory.
        :param readers: (experimental) A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param source_hash: (deprecated) Custom hash to use when identifying the specific version of the asset. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the source hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the source hash, you will need to make sure it is updated every time the source changes, or otherwise it is possible that some deployments will not be invalidated. Default: - automatically calculate source hash based on the contents of the source file or directory.
        :param exclude: (deprecated) Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: (deprecated) A strategy for how to handle symlinks. Default: Never
        :param ignore_mode: (deprecated) The ignore behavior to use for exclude patterns. Default: - GLOB for file assets, DOCKER or GLOB for docker assets depending on whether the '
        :param follow_symlinks: (experimental) A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param asset_hash: (experimental) Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: (experimental) Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: (experimental) Bundle the asset by executing a command in a Docker container. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise

        :stability: experimental
        '''
        options = _AssetOptions_bd2996da(
            readers=readers,
            source_hash=source_hash,
            exclude=exclude,
            follow=follow,
            ignore_mode=ignore_mode,
            follow_symlinks=follow_symlinks,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
        )

        return typing.cast(ISource, jsii.sinvoke(cls, "asset", [path, options]))

    @jsii.member(jsii_name="bucket") # type: ignore[misc]
    @builtins.classmethod
    def bucket(cls, bucket: _IBucket_73486e29, zip_object_key: builtins.str) -> ISource:
        '''(experimental) Uses a .zip file stored in an S3 bucket as the source for the destination bucket contents.

        :param bucket: The S3 Bucket.
        :param zip_object_key: The S3 object key of the zip file with contents.

        :stability: experimental
        '''
        return typing.cast(ISource, jsii.sinvoke(cls, "bucket", [bucket, zip_object_key]))


@jsii.data_type(
    jsii_type="monocdk.aws_s3_deployment.SourceConfig",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "zip_object_key": "zipObjectKey"},
)
class SourceConfig:
    def __init__(
        self,
        *,
        bucket: _IBucket_73486e29,
        zip_object_key: builtins.str,
    ) -> None:
        '''(experimental) Source information.

        :param bucket: (experimental) The source bucket to deploy from.
        :param zip_object_key: (experimental) An S3 object key in the source bucket that points to a zip file.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "zip_object_key": zip_object_key,
        }

    @builtins.property
    def bucket(self) -> _IBucket_73486e29:
        '''(experimental) The source bucket to deploy from.

        :stability: experimental
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_IBucket_73486e29, result)

    @builtins.property
    def zip_object_key(self) -> builtins.str:
        '''(experimental) An S3 object key in the source bucket that points to a zip file.

        :stability: experimental
        '''
        result = self._values.get("zip_object_key")
        assert result is not None, "Required property 'zip_object_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_s3_deployment.StorageClass")
class StorageClass(enum.Enum):
    '''(experimental) Storage class used for storing the object.

    :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
    :stability: experimental
    '''

    STANDARD = "STANDARD"
    '''(experimental) 'STANDARD'.

    :stability: experimental
    '''
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    '''(experimental) 'REDUCED_REDUNDANCY'.

    :stability: experimental
    '''
    STANDARD_IA = "STANDARD_IA"
    '''(experimental) 'STANDARD_IA'.

    :stability: experimental
    '''
    ONEZONE_IA = "ONEZONE_IA"
    '''(experimental) 'ONEZONE_IA'.

    :stability: experimental
    '''
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    '''(experimental) 'INTELLIGENT_TIERING'.

    :stability: experimental
    '''
    GLACIER = "GLACIER"
    '''(experimental) 'GLACIER'.

    :stability: experimental
    '''
    DEEP_ARCHIVE = "DEEP_ARCHIVE"
    '''(experimental) 'DEEP_ARCHIVE'.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="monocdk.aws_s3_deployment.UserDefinedObjectMetadata",
    jsii_struct_bases=[],
    name_mapping={},
)
class UserDefinedObjectMetadata:
    def __init__(self) -> None:
        '''(experimental) Custom user defined metadata.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserDefinedObjectMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BucketDeployment",
    "BucketDeploymentProps",
    "CacheControl",
    "DeploymentSourceContext",
    "Expires",
    "ISource",
    "ServerSideEncryption",
    "Source",
    "SourceConfig",
    "StorageClass",
    "UserDefinedObjectMetadata",
]

publication.publish()
