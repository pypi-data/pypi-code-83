'''
# Construct Hub

This project maintains a [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) construct library
that can be used to deploy instances of the Construct Hub in any AWS Account.

## Development

The `test/devapp` directory includes an AWS CDK app designed for deploying the
construct hub into a development account. This app is also used as a golden
snapshot, so every time the construct changes, you'll see its snapshot updated.

To bootstrap your developer account, use the following command:

```shell
CDK_NEW_BOOTSTRAP=1 npx cdk bootstrap aws://ACCOUNT/REGION
```

Use the following tasks to work with the dev app. It will always work with the
currently configured CLI account/region:

* `yarn dev:synth` - synthesize into `test/devapp/cdk.out`
* `yarn dev:deploy` - deploy to the current environment
* `yarn dev:diff` - diff against the current environment

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more
information.

## License

This project is licensed under the Apache-2.0 License.
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

import aws_cdk.aws_certificatemanager
import aws_cdk.aws_route53
import aws_cdk.aws_sns
import aws_cdk.core
import constructs


class ConstructHub(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="construct-hub.ConstructHub",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        contact_urls: typing.Optional["ContactURLs"] = None,
        dashboard_name: typing.Optional[builtins.str] = None,
        domain: typing.Optional["WebAppDomain"] = None,
        enable_npm_feed: typing.Optional[builtins.bool] = None,
        updates_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param contact_urls: (experimental) Contact URLs to be used for contacting this Construct Hub operators. Default: - none
        :param dashboard_name: (experimental) The name of the CloudWatch Dashboard created to observe this application. Default: - the path to this construct is used as the dashboard name.
        :param domain: (experimental) Connect the hub to a domain (requires a hosted zone and a certificate).
        :param enable_npm_feed: (experimental) Whether the package feed from the npmjs.com registry should be enabled. Default: true
        :param updates_topic: (experimental) An optional topic to be notified whenever a new package is indexed into this Construct Hub instance. Default: - none

        :stability: experimental
        '''
        props = ConstructHubProps(
            contact_urls=contact_urls,
            dashboard_name=dashboard_name,
            domain=domain,
            enable_npm_feed=enable_npm_feed,
            updates_topic=updates_topic,
        )

        jsii.create(ConstructHub, self, [scope, id, props])


@jsii.data_type(
    jsii_type="construct-hub.ConstructHubProps",
    jsii_struct_bases=[],
    name_mapping={
        "contact_urls": "contactUrls",
        "dashboard_name": "dashboardName",
        "domain": "domain",
        "enable_npm_feed": "enableNpmFeed",
        "updates_topic": "updatesTopic",
    },
)
class ConstructHubProps:
    def __init__(
        self,
        *,
        contact_urls: typing.Optional["ContactURLs"] = None,
        dashboard_name: typing.Optional[builtins.str] = None,
        domain: typing.Optional["WebAppDomain"] = None,
        enable_npm_feed: typing.Optional[builtins.bool] = None,
        updates_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
    ) -> None:
        '''
        :param contact_urls: (experimental) Contact URLs to be used for contacting this Construct Hub operators. Default: - none
        :param dashboard_name: (experimental) The name of the CloudWatch Dashboard created to observe this application. Default: - the path to this construct is used as the dashboard name.
        :param domain: (experimental) Connect the hub to a domain (requires a hosted zone and a certificate).
        :param enable_npm_feed: (experimental) Whether the package feed from the npmjs.com registry should be enabled. Default: true
        :param updates_topic: (experimental) An optional topic to be notified whenever a new package is indexed into this Construct Hub instance. Default: - none

        :stability: experimental
        '''
        if isinstance(contact_urls, dict):
            contact_urls = ContactURLs(**contact_urls)
        if isinstance(domain, dict):
            domain = WebAppDomain(**domain)
        self._values: typing.Dict[str, typing.Any] = {}
        if contact_urls is not None:
            self._values["contact_urls"] = contact_urls
        if dashboard_name is not None:
            self._values["dashboard_name"] = dashboard_name
        if domain is not None:
            self._values["domain"] = domain
        if enable_npm_feed is not None:
            self._values["enable_npm_feed"] = enable_npm_feed
        if updates_topic is not None:
            self._values["updates_topic"] = updates_topic

    @builtins.property
    def contact_urls(self) -> typing.Optional["ContactURLs"]:
        '''(experimental) Contact URLs to be used for contacting this Construct Hub operators.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("contact_urls")
        return typing.cast(typing.Optional["ContactURLs"], result)

    @builtins.property
    def dashboard_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the CloudWatch Dashboard created to observe this application.

        :default: - the path to this construct is used as the dashboard name.

        :stability: experimental
        '''
        result = self._values.get("dashboard_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional["WebAppDomain"]:
        '''(experimental) Connect the hub to a domain (requires a hosted zone and a certificate).

        :stability: experimental
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional["WebAppDomain"], result)

    @builtins.property
    def enable_npm_feed(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the package feed from the npmjs.com registry should be enabled.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("enable_npm_feed")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def updates_topic(self) -> typing.Optional[aws_cdk.aws_sns.ITopic]:
        '''(experimental) An optional topic to be notified whenever a new package is indexed into this Construct Hub instance.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("updates_topic")
        return typing.cast(typing.Optional[aws_cdk.aws_sns.ITopic], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConstructHubProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="construct-hub.ContactURLs",
    jsii_struct_bases=[],
    name_mapping={
        "other": "other",
        "security_issue": "securityIssue",
        "unlist_package": "unlistPackage",
    },
)
class ContactURLs:
    def __init__(
        self,
        *,
        other: typing.Optional[builtins.str] = None,
        security_issue: typing.Optional[builtins.str] = None,
        unlist_package: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param other: (experimental) The URL to the issue tracker or documentation for reporting other issues. Default: - none
        :param security_issue: (experimental) The URL to the issue tracker or documentation for reporting security issues. Default: - none
        :param unlist_package: (experimental) The URL to the issue tracker or documentation for requesting a package be un-listed from this Construct Hub instance. Default: - none

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if other is not None:
            self._values["other"] = other
        if security_issue is not None:
            self._values["security_issue"] = security_issue
        if unlist_package is not None:
            self._values["unlist_package"] = unlist_package

    @builtins.property
    def other(self) -> typing.Optional[builtins.str]:
        '''(experimental) The URL to the issue tracker or documentation for reporting other issues.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("other")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_issue(self) -> typing.Optional[builtins.str]:
        '''(experimental) The URL to the issue tracker or documentation for reporting security issues.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("security_issue")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unlist_package(self) -> typing.Optional[builtins.str]:
        '''(experimental) The URL to the issue tracker or documentation for requesting a package be un-listed from this Construct Hub instance.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("unlist_package")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactURLs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="construct-hub.WebAppDomain",
    jsii_struct_bases=[],
    name_mapping={"cert": "cert", "zone": "zone"},
)
class WebAppDomain:
    def __init__(
        self,
        *,
        cert: aws_cdk.aws_certificatemanager.ICertificate,
        zone: aws_cdk.aws_route53.IHostedZone,
    ) -> None:
        '''
        :param cert: (experimental) The certificate to use for serving the Construct Hub over a custom domain. Default: - a DNS-Validated certificate will be provisioned using the provided ``hostedZone``.
        :param zone: (experimental) The root domain name where this instance of Construct Hub will be served.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cert": cert,
            "zone": zone,
        }

    @builtins.property
    def cert(self) -> aws_cdk.aws_certificatemanager.ICertificate:
        '''(experimental) The certificate to use for serving the Construct Hub over a custom domain.

        :default:

        - a DNS-Validated certificate will be provisioned using the
        provided ``hostedZone``.

        :stability: experimental
        '''
        result = self._values.get("cert")
        assert result is not None, "Required property 'cert' is missing"
        return typing.cast(aws_cdk.aws_certificatemanager.ICertificate, result)

    @builtins.property
    def zone(self) -> aws_cdk.aws_route53.IHostedZone:
        '''(experimental) The root domain name where this instance of Construct Hub will be served.

        :stability: experimental
        '''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(aws_cdk.aws_route53.IHostedZone, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebAppDomain(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConstructHub",
    "ConstructHubProps",
    "ContactURLs",
    "WebAppDomain",
]

publication.publish()
