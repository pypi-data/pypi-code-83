"""
Type annotations for sns service ServiceResource

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_sns import SNSServiceResource
    import mypy_boto3_sns.service_resource as sns_resources

    resource: SNSServiceResource = boto3.resource("sns")

    my_platform_application: sns_resources.PlatformApplication = resource.PlatformApplication(...)
    my_platform_endpoint: sns_resources.PlatformEndpoint = resource.PlatformEndpoint(...)
    my_subscription: sns_resources.Subscription = resource.Subscription(...)
    my_topic: sns_resources.Topic = resource.Topic(...)
```
"""
from typing import Any, Dict, Iterator, List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from mypy_boto3_sns.type_defs import (
    MessageAttributeValueTypeDef,
    PublishResponseTypeDef,
    TagTypeDef,
)

__all__ = (
    "SNSServiceResource",
    "PlatformApplication",
    "PlatformEndpoint",
    "Subscription",
    "Topic",
    "ServiceResourcePlatformApplicationsCollection",
    "ServiceResourceSubscriptionsCollection",
    "ServiceResourceTopicsCollection",
    "PlatformApplicationEndpointsCollection",
    "TopicSubscriptionsCollection",
)


class ServiceResourcePlatformApplicationsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.platform_applications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#serviceresourceplatformapplicationscollection)
    """

    def all(self) -> "ServiceResourcePlatformApplicationsCollection":
        pass

    def filter(  # type: ignore
        self, NextToken: str = None
    ) -> "ServiceResourcePlatformApplicationsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourcePlatformApplicationsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourcePlatformApplicationsCollection":
        pass

    def pages(self) -> Iterator[List["PlatformApplication"]]:
        pass

    def __iter__(self) -> Iterator["PlatformApplication"]:
        pass


class ServiceResourceSubscriptionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.subscriptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#serviceresourcesubscriptionscollection)
    """

    def all(self) -> "ServiceResourceSubscriptionsCollection":
        pass

    def filter(  # type: ignore
        self, NextToken: str = None
    ) -> "ServiceResourceSubscriptionsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceSubscriptionsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceSubscriptionsCollection":
        pass

    def pages(self) -> Iterator[List["Subscription"]]:
        pass

    def __iter__(self) -> Iterator["Subscription"]:
        pass


class ServiceResourceTopicsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.topics)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#serviceresourcetopicscollection)
    """

    def all(self) -> "ServiceResourceTopicsCollection":
        pass

    def filter(self, NextToken: str = None) -> "ServiceResourceTopicsCollection":  # type: ignore
        pass

    def limit(self, count: int) -> "ServiceResourceTopicsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceTopicsCollection":
        pass

    def pages(self) -> Iterator[List["Topic"]]:
        pass

    def __iter__(self) -> Iterator["Topic"]:
        pass


class PlatformApplicationEndpointsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformApplication.endpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformapplicationendpointscollection)
    """

    def all(self) -> "PlatformApplicationEndpointsCollection":
        pass

    def filter(  # type: ignore
        self, NextToken: str = None
    ) -> "PlatformApplicationEndpointsCollection":
        pass

    def limit(self, count: int) -> "PlatformApplicationEndpointsCollection":
        pass

    def page_size(self, count: int) -> "PlatformApplicationEndpointsCollection":
        pass

    def pages(self) -> Iterator[List["PlatformEndpoint"]]:
        pass

    def __iter__(self) -> Iterator["PlatformEndpoint"]:
        pass


class TopicSubscriptionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Topic.subscriptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#topicsubscriptionscollection)
    """

    def all(self) -> "TopicSubscriptionsCollection":
        pass

    def filter(self, NextToken: str = None) -> "TopicSubscriptionsCollection":  # type: ignore
        pass

    def limit(self, count: int) -> "TopicSubscriptionsCollection":
        pass

    def page_size(self, count: int) -> "TopicSubscriptionsCollection":
        pass

    def pages(self) -> Iterator[List["Subscription"]]:
        pass

    def __iter__(self) -> Iterator["Subscription"]:
        pass


class PlatformEndpoint(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformendpoint)
    """

    attributes: Dict[str, Any]
    arn: str

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformEndpoint.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformendpointdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformEndpoint.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformendpointget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformEndpoint.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformendpointloadmethod)
        """

    def publish(
        self,
        Message: str,
        TopicArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None,
    ) -> PublishResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformEndpoint.publish)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformendpointpublishmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformEndpoint.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformendpointreloadmethod)
        """

    def set_attributes(self, Attributes: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformEndpoint.set_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformendpointset-attributesmethod)
        """


_PlatformEndpoint = PlatformEndpoint


class Subscription(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.Subscription)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#subscription)
    """

    attributes: Dict[str, Any]
    arn: str

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Subscription.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#subscriptiondeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Subscription.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#subscriptionget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Subscription.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#subscriptionloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Subscription.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#subscriptionreloadmethod)
        """

    def set_attributes(self, AttributeName: str, AttributeValue: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Subscription.set_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#subscriptionset-attributesmethod)
        """


_Subscription = Subscription


class PlatformApplication(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformapplication)
    """

    attributes: Dict[str, Any]
    arn: str
    endpoints: PlatformApplicationEndpointsCollection

    def create_platform_endpoint(
        self, Token: str, CustomUserData: str = None, Attributes: Dict[str, str] = None
    ) -> _PlatformEndpoint:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformApplication.create_platform_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformapplicationcreate-platform-endpointmethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformApplication.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformapplicationdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformApplication.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformapplicationget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformApplication.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformapplicationloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformApplication.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformapplicationreloadmethod)
        """

    def set_attributes(self, Attributes: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.PlatformApplication.set_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#platformapplicationset-attributesmethod)
        """


_PlatformApplication = PlatformApplication


class Topic(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.Topic)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#topic)
    """

    attributes: Dict[str, Any]
    arn: str
    subscriptions: TopicSubscriptionsCollection

    def add_permission(self, Label: str, AWSAccountId: List[str], ActionName: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Topic.add_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#topicadd-permissionmethod)
        """

    def confirm_subscription(
        self, Token: str, AuthenticateOnUnsubscribe: str = None
    ) -> _Subscription:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Topic.confirm_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#topicconfirm-subscriptionmethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Topic.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#topicdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Topic.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#topicget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Topic.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#topicloadmethod)
        """

    def publish(
        self,
        Message: str,
        TargetArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None,
    ) -> PublishResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Topic.publish)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#topicpublishmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Topic.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#topicreloadmethod)
        """

    def remove_permission(self, Label: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Topic.remove_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#topicremove-permissionmethod)
        """

    def set_attributes(self, AttributeName: str, AttributeValue: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Topic.set_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#topicset-attributesmethod)
        """

    def subscribe(
        self,
        Protocol: str,
        Endpoint: str = None,
        Attributes: Dict[str, str] = None,
        ReturnSubscriptionArn: bool = None,
    ) -> _Subscription:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.Topic.subscribe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#topicsubscribemethod)
        """


_Topic = Topic


class SNSServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html)
    """

    platform_applications: ServiceResourcePlatformApplicationsCollection
    subscriptions: ServiceResourceSubscriptionsCollection
    topics: ServiceResourceTopicsCollection

    def PlatformApplication(self, arn: str) -> _PlatformApplication:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#snsserviceresourceplatformapplicationmethod)
        """

    def PlatformEndpoint(self, arn: str) -> _PlatformEndpoint:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#snsserviceresourceplatformendpointmethod)
        """

    def Subscription(self, arn: str) -> _Subscription:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.Subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#snsserviceresourcesubscriptionmethod)
        """

    def Topic(self, arn: str) -> _Topic:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.Topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#snsserviceresourcetopicmethod)
        """

    def create_platform_application(
        self, Name: str, Platform: str, Attributes: Dict[str, str]
    ) -> _PlatformApplication:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.create_platform_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#snsserviceresourcecreate-platform-applicationmethod)
        """

    def create_topic(
        self, Name: str, Attributes: Dict[str, str] = None, Tags: List["TagTypeDef"] = None
    ) -> _Topic:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.create_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#snsserviceresourcecreate-topicmethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sns.html#SNS.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource.html#snsserviceresourceget-available-subresourcesmethod)
        """
