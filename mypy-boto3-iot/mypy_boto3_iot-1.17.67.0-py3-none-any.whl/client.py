"""
Type annotations for iot service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iot import IoTClient

    client: IoTClient = boto3.client("iot")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_iot.literals import (
    AuditFrequency,
    AuditMitigationActionsExecutionStatus,
    AuditMitigationActionsTaskStatus,
    AuditTaskStatus,
    AuditTaskType,
    AuthorizerStatus,
    AutoRegistrationStatus,
    BehaviorCriteriaType,
    CACertificateStatus,
    CertificateStatus,
    CustomMetricType,
    DayOfWeek,
    DomainConfigurationStatus,
    EventType,
    JobExecutionStatus,
    JobStatus,
    LogLevel,
    LogTargetType,
    MitigationActionType,
    OTAUpdateStatus,
    ProtocolType,
    ReportType,
    ServiceType,
    Status,
    TargetSelection,
    TopicRuleDestinationStatus,
)
from mypy_boto3_iot.paginator import (
    GetBehaviorModelTrainingSummariesPaginator,
    ListActiveViolationsPaginator,
    ListAttachedPoliciesPaginator,
    ListAuditFindingsPaginator,
    ListAuditMitigationActionsExecutionsPaginator,
    ListAuditMitigationActionsTasksPaginator,
    ListAuditSuppressionsPaginator,
    ListAuditTasksPaginator,
    ListAuthorizersPaginator,
    ListBillingGroupsPaginator,
    ListCACertificatesPaginator,
    ListCertificatesByCAPaginator,
    ListCertificatesPaginator,
    ListCustomMetricsPaginator,
    ListDetectMitigationActionsExecutionsPaginator,
    ListDetectMitigationActionsTasksPaginator,
    ListDimensionsPaginator,
    ListDomainConfigurationsPaginator,
    ListIndicesPaginator,
    ListJobExecutionsForJobPaginator,
    ListJobExecutionsForThingPaginator,
    ListJobsPaginator,
    ListMitigationActionsPaginator,
    ListOTAUpdatesPaginator,
    ListOutgoingCertificatesPaginator,
    ListPoliciesPaginator,
    ListPolicyPrincipalsPaginator,
    ListPrincipalPoliciesPaginator,
    ListPrincipalThingsPaginator,
    ListProvisioningTemplatesPaginator,
    ListProvisioningTemplateVersionsPaginator,
    ListRoleAliasesPaginator,
    ListScheduledAuditsPaginator,
    ListSecurityProfilesForTargetPaginator,
    ListSecurityProfilesPaginator,
    ListStreamsPaginator,
    ListTagsForResourcePaginator,
    ListTargetsForPolicyPaginator,
    ListTargetsForSecurityProfilePaginator,
    ListThingGroupsForThingPaginator,
    ListThingGroupsPaginator,
    ListThingPrincipalsPaginator,
    ListThingRegistrationTaskReportsPaginator,
    ListThingRegistrationTasksPaginator,
    ListThingsInBillingGroupPaginator,
    ListThingsInThingGroupPaginator,
    ListThingsPaginator,
    ListThingTypesPaginator,
    ListTopicRuleDestinationsPaginator,
    ListTopicRulesPaginator,
    ListV2LoggingLevelsPaginator,
    ListViolationEventsPaginator,
)
from mypy_boto3_iot.type_defs import (
    AbortConfigTypeDef,
    AlertTargetTypeDef,
    AssociateTargetsWithJobResponseTypeDef,
    AttributePayloadTypeDef,
    AuditCheckConfigurationTypeDef,
    AuditMitigationActionsTaskTargetTypeDef,
    AuditNotificationTargetTypeDef,
    AuthInfoTypeDef,
    AuthorizerConfigTypeDef,
    AwsJobAbortConfigTypeDef,
    AwsJobExecutionsRolloutConfigTypeDef,
    AwsJobPresignedUrlConfigTypeDef,
    AwsJobTimeoutConfigTypeDef,
    BehaviorTypeDef,
    BillingGroupPropertiesTypeDef,
    CancelJobResponseTypeDef,
    ConfigurationTypeDef,
    CreateAuthorizerResponseTypeDef,
    CreateBillingGroupResponseTypeDef,
    CreateCertificateFromCsrResponseTypeDef,
    CreateCustomMetricResponseTypeDef,
    CreateDimensionResponseTypeDef,
    CreateDomainConfigurationResponseTypeDef,
    CreateDynamicThingGroupResponseTypeDef,
    CreateJobResponseTypeDef,
    CreateKeysAndCertificateResponseTypeDef,
    CreateMitigationActionResponseTypeDef,
    CreateOTAUpdateResponseTypeDef,
    CreatePolicyResponseTypeDef,
    CreatePolicyVersionResponseTypeDef,
    CreateProvisioningClaimResponseTypeDef,
    CreateProvisioningTemplateResponseTypeDef,
    CreateProvisioningTemplateVersionResponseTypeDef,
    CreateRoleAliasResponseTypeDef,
    CreateScheduledAuditResponseTypeDef,
    CreateSecurityProfileResponseTypeDef,
    CreateStreamResponseTypeDef,
    CreateThingGroupResponseTypeDef,
    CreateThingResponseTypeDef,
    CreateThingTypeResponseTypeDef,
    CreateTopicRuleDestinationResponseTypeDef,
    DescribeAccountAuditConfigurationResponseTypeDef,
    DescribeAuditFindingResponseTypeDef,
    DescribeAuditMitigationActionsTaskResponseTypeDef,
    DescribeAuditSuppressionResponseTypeDef,
    DescribeAuditTaskResponseTypeDef,
    DescribeAuthorizerResponseTypeDef,
    DescribeBillingGroupResponseTypeDef,
    DescribeCACertificateResponseTypeDef,
    DescribeCertificateResponseTypeDef,
    DescribeCustomMetricResponseTypeDef,
    DescribeDefaultAuthorizerResponseTypeDef,
    DescribeDetectMitigationActionsTaskResponseTypeDef,
    DescribeDimensionResponseTypeDef,
    DescribeDomainConfigurationResponseTypeDef,
    DescribeEndpointResponseTypeDef,
    DescribeEventConfigurationsResponseTypeDef,
    DescribeIndexResponseTypeDef,
    DescribeJobExecutionResponseTypeDef,
    DescribeJobResponseTypeDef,
    DescribeMitigationActionResponseTypeDef,
    DescribeProvisioningTemplateResponseTypeDef,
    DescribeProvisioningTemplateVersionResponseTypeDef,
    DescribeRoleAliasResponseTypeDef,
    DescribeScheduledAuditResponseTypeDef,
    DescribeSecurityProfileResponseTypeDef,
    DescribeStreamResponseTypeDef,
    DescribeThingGroupResponseTypeDef,
    DescribeThingRegistrationTaskResponseTypeDef,
    DescribeThingResponseTypeDef,
    DescribeThingTypeResponseTypeDef,
    DetectMitigationActionsTaskTargetTypeDef,
    GetBehaviorModelTrainingSummariesResponseTypeDef,
    GetCardinalityResponseTypeDef,
    GetEffectivePoliciesResponseTypeDef,
    GetIndexingConfigurationResponseTypeDef,
    GetJobDocumentResponseTypeDef,
    GetLoggingOptionsResponseTypeDef,
    GetOTAUpdateResponseTypeDef,
    GetPercentilesResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetPolicyVersionResponseTypeDef,
    GetRegistrationCodeResponseTypeDef,
    GetStatisticsResponseTypeDef,
    GetTopicRuleDestinationResponseTypeDef,
    GetTopicRuleResponseTypeDef,
    GetV2LoggingOptionsResponseTypeDef,
    HttpContextTypeDef,
    JobExecutionsRolloutConfigTypeDef,
    ListActiveViolationsResponseTypeDef,
    ListAttachedPoliciesResponseTypeDef,
    ListAuditFindingsResponseTypeDef,
    ListAuditMitigationActionsExecutionsResponseTypeDef,
    ListAuditMitigationActionsTasksResponseTypeDef,
    ListAuditSuppressionsResponseTypeDef,
    ListAuditTasksResponseTypeDef,
    ListAuthorizersResponseTypeDef,
    ListBillingGroupsResponseTypeDef,
    ListCACertificatesResponseTypeDef,
    ListCertificatesByCAResponseTypeDef,
    ListCertificatesResponseTypeDef,
    ListCustomMetricsResponseTypeDef,
    ListDetectMitigationActionsExecutionsResponseTypeDef,
    ListDetectMitigationActionsTasksResponseTypeDef,
    ListDimensionsResponseTypeDef,
    ListDomainConfigurationsResponseTypeDef,
    ListIndicesResponseTypeDef,
    ListJobExecutionsForJobResponseTypeDef,
    ListJobExecutionsForThingResponseTypeDef,
    ListJobsResponseTypeDef,
    ListMitigationActionsResponseTypeDef,
    ListOTAUpdatesResponseTypeDef,
    ListOutgoingCertificatesResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyPrincipalsResponseTypeDef,
    ListPolicyVersionsResponseTypeDef,
    ListPrincipalPoliciesResponseTypeDef,
    ListPrincipalThingsResponseTypeDef,
    ListProvisioningTemplatesResponseTypeDef,
    ListProvisioningTemplateVersionsResponseTypeDef,
    ListRoleAliasesResponseTypeDef,
    ListScheduledAuditsResponseTypeDef,
    ListSecurityProfilesForTargetResponseTypeDef,
    ListSecurityProfilesResponseTypeDef,
    ListStreamsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsForPolicyResponseTypeDef,
    ListTargetsForSecurityProfileResponseTypeDef,
    ListThingGroupsForThingResponseTypeDef,
    ListThingGroupsResponseTypeDef,
    ListThingPrincipalsResponseTypeDef,
    ListThingRegistrationTaskReportsResponseTypeDef,
    ListThingRegistrationTasksResponseTypeDef,
    ListThingsInBillingGroupResponseTypeDef,
    ListThingsInThingGroupResponseTypeDef,
    ListThingsResponseTypeDef,
    ListThingTypesResponseTypeDef,
    ListTopicRuleDestinationsResponseTypeDef,
    ListTopicRulesResponseTypeDef,
    ListV2LoggingLevelsResponseTypeDef,
    ListViolationEventsResponseTypeDef,
    LoggingOptionsPayloadTypeDef,
    LogTargetTypeDef,
    MetricToRetainTypeDef,
    MitigationActionParamsTypeDef,
    MqttContextTypeDef,
    OTAUpdateFileTypeDef,
    PresignedUrlConfigTypeDef,
    ProvisioningHookTypeDef,
    RegisterCACertificateResponseTypeDef,
    RegisterCertificateResponseTypeDef,
    RegisterCertificateWithoutCAResponseTypeDef,
    RegisterThingResponseTypeDef,
    RegistrationConfigTypeDef,
    ResourceIdentifierTypeDef,
    SearchIndexResponseTypeDef,
    SetDefaultAuthorizerResponseTypeDef,
    StartAuditMitigationActionsTaskResponseTypeDef,
    StartDetectMitigationActionsTaskResponseTypeDef,
    StartOnDemandAuditTaskResponseTypeDef,
    StartThingRegistrationTaskResponseTypeDef,
    StreamFileTypeDef,
    TagTypeDef,
    TestAuthorizationResponseTypeDef,
    TestInvokeAuthorizerResponseTypeDef,
    ThingGroupIndexingConfigurationTypeDef,
    ThingGroupPropertiesTypeDef,
    ThingIndexingConfigurationTypeDef,
    ThingTypePropertiesTypeDef,
    TimeoutConfigTypeDef,
    TlsContextTypeDef,
    TopicRuleDestinationConfigurationTypeDef,
    TopicRulePayloadTypeDef,
    TransferCertificateResponseTypeDef,
    UpdateAuthorizerResponseTypeDef,
    UpdateBillingGroupResponseTypeDef,
    UpdateCustomMetricResponseTypeDef,
    UpdateDimensionResponseTypeDef,
    UpdateDomainConfigurationResponseTypeDef,
    UpdateDynamicThingGroupResponseTypeDef,
    UpdateMitigationActionResponseTypeDef,
    UpdateRoleAliasResponseTypeDef,
    UpdateScheduledAuditResponseTypeDef,
    UpdateSecurityProfileResponseTypeDef,
    UpdateStreamResponseTypeDef,
    UpdateThingGroupResponseTypeDef,
    ValidateSecurityProfileBehaviorsResponseTypeDef,
    ViolationEventOccurrenceRangeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    CertificateConflictException: Type[BotocoreClientError]
    CertificateStateException: Type[BotocoreClientError]
    CertificateValidationException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictingResourceUpdateException: Type[BotocoreClientError]
    DeleteConflictException: Type[BotocoreClientError]
    IndexNotReadyException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidAggregationException: Type[BotocoreClientError]
    InvalidQueryException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidResponseException: Type[BotocoreClientError]
    InvalidStateTransitionException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedPolicyException: Type[BotocoreClientError]
    NotConfiguredException: Type[BotocoreClientError]
    RegistrationCodeValidationException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceRegistrationFailureException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    SqlParseException: Type[BotocoreClientError]
    TaskAlreadyExistsException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TransferAlreadyCompletedException: Type[BotocoreClientError]
    TransferConflictException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    VersionConflictException: Type[BotocoreClientError]
    VersionsLimitExceededException: Type[BotocoreClientError]


class IoTClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_certificate_transfer(self, certificateId: str, setAsActive: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.accept_certificate_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#accept-certificate-transfer)
        """

    def add_thing_to_billing_group(
        self,
        billingGroupName: str = None,
        billingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.add_thing_to_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#add-thing-to-billing-group)
        """

    def add_thing_to_thing_group(
        self,
        thingGroupName: str = None,
        thingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
        overrideDynamicGroups: bool = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.add_thing_to_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#add-thing-to-thing-group)
        """

    def associate_targets_with_job(
        self, targets: List[str], jobId: str, comment: str = None, namespaceId: str = None
    ) -> AssociateTargetsWithJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.associate_targets_with_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#associate-targets-with-job)
        """

    def attach_policy(self, policyName: str, target: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.attach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#attach-policy)
        """

    def attach_principal_policy(self, policyName: str, principal: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.attach_principal_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#attach-principal-policy)
        """

    def attach_security_profile(
        self, securityProfileName: str, securityProfileTargetArn: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.attach_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#attach-security-profile)
        """

    def attach_thing_principal(self, thingName: str, principal: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.attach_thing_principal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#attach-thing-principal)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#can-paginate)
        """

    def cancel_audit_mitigation_actions_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.cancel_audit_mitigation_actions_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#cancel-audit-mitigation-actions-task)
        """

    def cancel_audit_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.cancel_audit_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#cancel-audit-task)
        """

    def cancel_certificate_transfer(self, certificateId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.cancel_certificate_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#cancel-certificate-transfer)
        """

    def cancel_detect_mitigation_actions_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.cancel_detect_mitigation_actions_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#cancel-detect-mitigation-actions-task)
        """

    def cancel_job(
        self, jobId: str, reasonCode: str = None, comment: str = None, force: bool = None
    ) -> CancelJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.cancel_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#cancel-job)
        """

    def cancel_job_execution(
        self,
        jobId: str,
        thingName: str,
        force: bool = None,
        expectedVersion: int = None,
        statusDetails: Dict[str, str] = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.cancel_job_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#cancel-job-execution)
        """

    def clear_default_authorizer(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.clear_default_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#clear-default-authorizer)
        """

    def confirm_topic_rule_destination(self, confirmationToken: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.confirm_topic_rule_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#confirm-topic-rule-destination)
        """

    def create_audit_suppression(
        self,
        checkName: str,
        resourceIdentifier: "ResourceIdentifierTypeDef",
        clientRequestToken: str,
        expirationDate: datetime = None,
        suppressIndefinitely: bool = None,
        description: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_audit_suppression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-audit-suppression)
        """

    def create_authorizer(
        self,
        authorizerName: str,
        authorizerFunctionArn: str,
        tokenKeyName: str = None,
        tokenSigningPublicKeys: Dict[str, str] = None,
        status: AuthorizerStatus = None,
        tags: List["TagTypeDef"] = None,
        signingDisabled: bool = None,
    ) -> CreateAuthorizerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-authorizer)
        """

    def create_billing_group(
        self,
        billingGroupName: str,
        billingGroupProperties: "BillingGroupPropertiesTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateBillingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-billing-group)
        """

    def create_certificate_from_csr(
        self, certificateSigningRequest: str, setAsActive: bool = None
    ) -> CreateCertificateFromCsrResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_certificate_from_csr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-certificate-from-csr)
        """

    def create_custom_metric(
        self,
        metricName: str,
        metricType: CustomMetricType,
        clientRequestToken: str,
        displayName: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateCustomMetricResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_custom_metric)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-custom-metric)
        """

    def create_dimension(
        self,
        name: str,
        type: Literal["TOPIC_FILTER"],
        stringValues: List[str],
        clientRequestToken: str,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDimensionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_dimension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-dimension)
        """

    def create_domain_configuration(
        self,
        domainConfigurationName: str,
        domainName: str = None,
        serverCertificateArns: List[str] = None,
        validationCertificateArn: str = None,
        authorizerConfig: "AuthorizerConfigTypeDef" = None,
        serviceType: ServiceType = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDomainConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_domain_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-domain-configuration)
        """

    def create_dynamic_thing_group(
        self,
        thingGroupName: str,
        queryString: str,
        thingGroupProperties: "ThingGroupPropertiesTypeDef" = None,
        indexName: str = None,
        queryVersion: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDynamicThingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_dynamic_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-dynamic-thing-group)
        """

    def create_job(
        self,
        jobId: str,
        targets: List[str],
        documentSource: str = None,
        document: str = None,
        description: str = None,
        presignedUrlConfig: "PresignedUrlConfigTypeDef" = None,
        targetSelection: TargetSelection = None,
        jobExecutionsRolloutConfig: "JobExecutionsRolloutConfigTypeDef" = None,
        abortConfig: "AbortConfigTypeDef" = None,
        timeoutConfig: "TimeoutConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        namespaceId: str = None,
    ) -> CreateJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-job)
        """

    def create_keys_and_certificate(
        self, setAsActive: bool = None
    ) -> CreateKeysAndCertificateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_keys_and_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-keys-and-certificate)
        """

    def create_mitigation_action(
        self,
        actionName: str,
        roleArn: str,
        actionParams: "MitigationActionParamsTypeDef",
        tags: List["TagTypeDef"] = None,
    ) -> CreateMitigationActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_mitigation_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-mitigation-action)
        """

    def create_ota_update(
        self,
        otaUpdateId: str,
        targets: List[str],
        files: List["OTAUpdateFileTypeDef"],
        roleArn: str,
        description: str = None,
        protocols: List[ProtocolType] = None,
        targetSelection: TargetSelection = None,
        awsJobExecutionsRolloutConfig: "AwsJobExecutionsRolloutConfigTypeDef" = None,
        awsJobPresignedUrlConfig: "AwsJobPresignedUrlConfigTypeDef" = None,
        awsJobAbortConfig: AwsJobAbortConfigTypeDef = None,
        awsJobTimeoutConfig: AwsJobTimeoutConfigTypeDef = None,
        additionalParameters: Dict[str, str] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateOTAUpdateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_ota_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-ota-update)
        """

    def create_policy(
        self, policyName: str, policyDocument: str, tags: List["TagTypeDef"] = None
    ) -> CreatePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-policy)
        """

    def create_policy_version(
        self, policyName: str, policyDocument: str, setAsDefault: bool = None
    ) -> CreatePolicyVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-policy-version)
        """

    def create_provisioning_claim(
        self, templateName: str
    ) -> CreateProvisioningClaimResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_provisioning_claim)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-provisioning-claim)
        """

    def create_provisioning_template(
        self,
        templateName: str,
        templateBody: str,
        provisioningRoleArn: str,
        description: str = None,
        enabled: bool = None,
        preProvisioningHook: "ProvisioningHookTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateProvisioningTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_provisioning_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-provisioning-template)
        """

    def create_provisioning_template_version(
        self, templateName: str, templateBody: str, setAsDefault: bool = None
    ) -> CreateProvisioningTemplateVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_provisioning_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-provisioning-template-version)
        """

    def create_role_alias(
        self,
        roleAlias: str,
        roleArn: str,
        credentialDurationSeconds: int = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateRoleAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_role_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-role-alias)
        """

    def create_scheduled_audit(
        self,
        frequency: AuditFrequency,
        targetCheckNames: List[str],
        scheduledAuditName: str,
        dayOfMonth: str = None,
        dayOfWeek: DayOfWeek = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateScheduledAuditResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_scheduled_audit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-scheduled-audit)
        """

    def create_security_profile(
        self,
        securityProfileName: str,
        securityProfileDescription: str = None,
        behaviors: List["BehaviorTypeDef"] = None,
        alertTargets: Dict[Literal["SNS"], "AlertTargetTypeDef"] = None,
        additionalMetricsToRetain: List[str] = None,
        additionalMetricsToRetainV2: List["MetricToRetainTypeDef"] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateSecurityProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-security-profile)
        """

    def create_stream(
        self,
        streamId: str,
        files: List["StreamFileTypeDef"],
        roleArn: str,
        description: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateStreamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-stream)
        """

    def create_thing(
        self,
        thingName: str,
        thingTypeName: str = None,
        attributePayload: "AttributePayloadTypeDef" = None,
        billingGroupName: str = None,
    ) -> CreateThingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-thing)
        """

    def create_thing_group(
        self,
        thingGroupName: str,
        parentGroupName: str = None,
        thingGroupProperties: "ThingGroupPropertiesTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateThingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-thing-group)
        """

    def create_thing_type(
        self,
        thingTypeName: str,
        thingTypeProperties: "ThingTypePropertiesTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateThingTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_thing_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-thing-type)
        """

    def create_topic_rule(
        self, ruleName: str, topicRulePayload: TopicRulePayloadTypeDef, tags: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_topic_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-topic-rule)
        """

    def create_topic_rule_destination(
        self, destinationConfiguration: TopicRuleDestinationConfigurationTypeDef
    ) -> CreateTopicRuleDestinationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.create_topic_rule_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create-topic-rule-destination)
        """

    def delete_account_audit_configuration(
        self, deleteScheduledAudits: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_account_audit_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-account-audit-configuration)
        """

    def delete_audit_suppression(
        self, checkName: str, resourceIdentifier: "ResourceIdentifierTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_audit_suppression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-audit-suppression)
        """

    def delete_authorizer(self, authorizerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-authorizer)
        """

    def delete_billing_group(
        self, billingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-billing-group)
        """

    def delete_ca_certificate(self, certificateId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_ca_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-ca-certificate)
        """

    def delete_certificate(self, certificateId: str, forceDelete: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-certificate)
        """

    def delete_custom_metric(self, metricName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_custom_metric)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-custom-metric)
        """

    def delete_dimension(self, name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_dimension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-dimension)
        """

    def delete_domain_configuration(self, domainConfigurationName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_domain_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-domain-configuration)
        """

    def delete_dynamic_thing_group(
        self, thingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_dynamic_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-dynamic-thing-group)
        """

    def delete_job(self, jobId: str, force: bool = None, namespaceId: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-job)
        """

    def delete_job_execution(
        self,
        jobId: str,
        thingName: str,
        executionNumber: int,
        force: bool = None,
        namespaceId: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_job_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-job-execution)
        """

    def delete_mitigation_action(self, actionName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_mitigation_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-mitigation-action)
        """

    def delete_ota_update(
        self, otaUpdateId: str, deleteStream: bool = None, forceDeleteAWSJob: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_ota_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-ota-update)
        """

    def delete_policy(self, policyName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-policy)
        """

    def delete_policy_version(self, policyName: str, policyVersionId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-policy-version)
        """

    def delete_provisioning_template(self, templateName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_provisioning_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-provisioning-template)
        """

    def delete_provisioning_template_version(
        self, templateName: str, versionId: int
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_provisioning_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-provisioning-template-version)
        """

    def delete_registration_code(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_registration_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-registration-code)
        """

    def delete_role_alias(self, roleAlias: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_role_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-role-alias)
        """

    def delete_scheduled_audit(self, scheduledAuditName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_scheduled_audit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-scheduled-audit)
        """

    def delete_security_profile(
        self, securityProfileName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-security-profile)
        """

    def delete_stream(self, streamId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-stream)
        """

    def delete_thing(self, thingName: str, expectedVersion: int = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-thing)
        """

    def delete_thing_group(
        self, thingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-thing-group)
        """

    def delete_thing_type(self, thingTypeName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_thing_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-thing-type)
        """

    def delete_topic_rule(self, ruleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_topic_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-topic-rule)
        """

    def delete_topic_rule_destination(self, arn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_topic_rule_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-topic-rule-destination)
        """

    def delete_v2_logging_level(self, targetType: LogTargetType, targetName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.delete_v2_logging_level)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete-v2-logging-level)
        """

    def deprecate_thing_type(
        self, thingTypeName: str, undoDeprecate: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.deprecate_thing_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#deprecate-thing-type)
        """

    def describe_account_audit_configuration(
        self,
    ) -> DescribeAccountAuditConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_account_audit_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-account-audit-configuration)
        """

    def describe_audit_finding(self, findingId: str) -> DescribeAuditFindingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_audit_finding)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-audit-finding)
        """

    def describe_audit_mitigation_actions_task(
        self, taskId: str
    ) -> DescribeAuditMitigationActionsTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_audit_mitigation_actions_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-audit-mitigation-actions-task)
        """

    def describe_audit_suppression(
        self, checkName: str, resourceIdentifier: "ResourceIdentifierTypeDef"
    ) -> DescribeAuditSuppressionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_audit_suppression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-audit-suppression)
        """

    def describe_audit_task(self, taskId: str) -> DescribeAuditTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_audit_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-audit-task)
        """

    def describe_authorizer(self, authorizerName: str) -> DescribeAuthorizerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-authorizer)
        """

    def describe_billing_group(self, billingGroupName: str) -> DescribeBillingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-billing-group)
        """

    def describe_ca_certificate(self, certificateId: str) -> DescribeCACertificateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_ca_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-ca-certificate)
        """

    def describe_certificate(self, certificateId: str) -> DescribeCertificateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-certificate)
        """

    def describe_custom_metric(self, metricName: str) -> DescribeCustomMetricResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_custom_metric)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-custom-metric)
        """

    def describe_default_authorizer(self) -> DescribeDefaultAuthorizerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_default_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-default-authorizer)
        """

    def describe_detect_mitigation_actions_task(
        self, taskId: str
    ) -> DescribeDetectMitigationActionsTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_detect_mitigation_actions_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-detect-mitigation-actions-task)
        """

    def describe_dimension(self, name: str) -> DescribeDimensionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_dimension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-dimension)
        """

    def describe_domain_configuration(
        self, domainConfigurationName: str
    ) -> DescribeDomainConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_domain_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-domain-configuration)
        """

    def describe_endpoint(self, endpointType: str = None) -> DescribeEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-endpoint)
        """

    def describe_event_configurations(self) -> DescribeEventConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_event_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-event-configurations)
        """

    def describe_index(self, indexName: str) -> DescribeIndexResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-index)
        """

    def describe_job(self, jobId: str) -> DescribeJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-job)
        """

    def describe_job_execution(
        self, jobId: str, thingName: str, executionNumber: int = None
    ) -> DescribeJobExecutionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_job_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-job-execution)
        """

    def describe_mitigation_action(
        self, actionName: str
    ) -> DescribeMitigationActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_mitigation_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-mitigation-action)
        """

    def describe_provisioning_template(
        self, templateName: str
    ) -> DescribeProvisioningTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_provisioning_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-provisioning-template)
        """

    def describe_provisioning_template_version(
        self, templateName: str, versionId: int
    ) -> DescribeProvisioningTemplateVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_provisioning_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-provisioning-template-version)
        """

    def describe_role_alias(self, roleAlias: str) -> DescribeRoleAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_role_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-role-alias)
        """

    def describe_scheduled_audit(
        self, scheduledAuditName: str
    ) -> DescribeScheduledAuditResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_scheduled_audit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-scheduled-audit)
        """

    def describe_security_profile(
        self, securityProfileName: str
    ) -> DescribeSecurityProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-security-profile)
        """

    def describe_stream(self, streamId: str) -> DescribeStreamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-stream)
        """

    def describe_thing(self, thingName: str) -> DescribeThingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-thing)
        """

    def describe_thing_group(self, thingGroupName: str) -> DescribeThingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-thing-group)
        """

    def describe_thing_registration_task(
        self, taskId: str
    ) -> DescribeThingRegistrationTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_thing_registration_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-thing-registration-task)
        """

    def describe_thing_type(self, thingTypeName: str) -> DescribeThingTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.describe_thing_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe-thing-type)
        """

    def detach_policy(self, policyName: str, target: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.detach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#detach-policy)
        """

    def detach_principal_policy(self, policyName: str, principal: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.detach_principal_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#detach-principal-policy)
        """

    def detach_security_profile(
        self, securityProfileName: str, securityProfileTargetArn: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.detach_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#detach-security-profile)
        """

    def detach_thing_principal(self, thingName: str, principal: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.detach_thing_principal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#detach-thing-principal)
        """

    def disable_topic_rule(self, ruleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.disable_topic_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#disable-topic-rule)
        """

    def enable_topic_rule(self, ruleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.enable_topic_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#enable-topic-rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#generate-presigned-url)
        """

    def get_behavior_model_training_summaries(
        self, securityProfileName: str = None, maxResults: int = None, nextToken: str = None
    ) -> GetBehaviorModelTrainingSummariesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_behavior_model_training_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-behavior-model-training-summaries)
        """

    def get_cardinality(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
    ) -> GetCardinalityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_cardinality)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-cardinality)
        """

    def get_effective_policies(
        self, principal: str = None, cognitoIdentityPoolId: str = None, thingName: str = None
    ) -> GetEffectivePoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_effective_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-effective-policies)
        """

    def get_indexing_configuration(self) -> GetIndexingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_indexing_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-indexing-configuration)
        """

    def get_job_document(self, jobId: str) -> GetJobDocumentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_job_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-job-document)
        """

    def get_logging_options(self) -> GetLoggingOptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-logging-options)
        """

    def get_ota_update(self, otaUpdateId: str) -> GetOTAUpdateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_ota_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-ota-update)
        """

    def get_percentiles(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
        percents: List[float] = None,
    ) -> GetPercentilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_percentiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-percentiles)
        """

    def get_policy(self, policyName: str) -> GetPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-policy)
        """

    def get_policy_version(
        self, policyName: str, policyVersionId: str
    ) -> GetPolicyVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-policy-version)
        """

    def get_registration_code(self) -> GetRegistrationCodeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_registration_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-registration-code)
        """

    def get_statistics(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
    ) -> GetStatisticsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-statistics)
        """

    def get_topic_rule(self, ruleName: str) -> GetTopicRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_topic_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-topic-rule)
        """

    def get_topic_rule_destination(self, arn: str) -> GetTopicRuleDestinationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_topic_rule_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-topic-rule-destination)
        """

    def get_v2_logging_options(self) -> GetV2LoggingOptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.get_v2_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get-v2-logging-options)
        """

    def list_active_violations(
        self,
        thingName: str = None,
        securityProfileName: str = None,
        behaviorCriteriaType: BehaviorCriteriaType = None,
        listSuppressedAlerts: bool = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListActiveViolationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_active_violations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-active-violations)
        """

    def list_attached_policies(
        self, target: str, recursive: bool = None, marker: str = None, pageSize: int = None
    ) -> ListAttachedPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_attached_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-attached-policies)
        """

    def list_audit_findings(
        self,
        taskId: str = None,
        checkName: str = None,
        resourceIdentifier: "ResourceIdentifierTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        listSuppressedFindings: bool = None,
    ) -> ListAuditFindingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_audit_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-audit-findings)
        """

    def list_audit_mitigation_actions_executions(
        self,
        taskId: str,
        findingId: str,
        actionStatus: AuditMitigationActionsExecutionStatus = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListAuditMitigationActionsExecutionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_audit_mitigation_actions_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-audit-mitigation-actions-executions)
        """

    def list_audit_mitigation_actions_tasks(
        self,
        startTime: datetime,
        endTime: datetime,
        auditTaskId: str = None,
        findingId: str = None,
        taskStatus: AuditMitigationActionsTaskStatus = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListAuditMitigationActionsTasksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_audit_mitigation_actions_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-audit-mitigation-actions-tasks)
        """

    def list_audit_suppressions(
        self,
        checkName: str = None,
        resourceIdentifier: "ResourceIdentifierTypeDef" = None,
        ascendingOrder: bool = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAuditSuppressionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_audit_suppressions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-audit-suppressions)
        """

    def list_audit_tasks(
        self,
        startTime: datetime,
        endTime: datetime,
        taskType: AuditTaskType = None,
        taskStatus: AuditTaskStatus = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAuditTasksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_audit_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-audit-tasks)
        """

    def list_authorizers(
        self,
        pageSize: int = None,
        marker: str = None,
        ascendingOrder: bool = None,
        status: AuthorizerStatus = None,
    ) -> ListAuthorizersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_authorizers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-authorizers)
        """

    def list_billing_groups(
        self, nextToken: str = None, maxResults: int = None, namePrefixFilter: str = None
    ) -> ListBillingGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_billing_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-billing-groups)
        """

    def list_ca_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListCACertificatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_ca_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-ca-certificates)
        """

    def list_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListCertificatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-certificates)
        """

    def list_certificates_by_ca(
        self,
        caCertificateId: str,
        pageSize: int = None,
        marker: str = None,
        ascendingOrder: bool = None,
    ) -> ListCertificatesByCAResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_certificates_by_ca)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-certificates-by-ca)
        """

    def list_custom_metrics(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListCustomMetricsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_custom_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-custom-metrics)
        """

    def list_detect_mitigation_actions_executions(
        self,
        taskId: str = None,
        violationId: str = None,
        thingName: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListDetectMitigationActionsExecutionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_detect_mitigation_actions_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-detect-mitigation-actions-executions)
        """

    def list_detect_mitigation_actions_tasks(
        self, startTime: datetime, endTime: datetime, maxResults: int = None, nextToken: str = None
    ) -> ListDetectMitigationActionsTasksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_detect_mitigation_actions_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-detect-mitigation-actions-tasks)
        """

    def list_dimensions(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListDimensionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_dimensions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-dimensions)
        """

    def list_domain_configurations(
        self, marker: str = None, pageSize: int = None, serviceType: ServiceType = None
    ) -> ListDomainConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_domain_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-domain-configurations)
        """

    def list_indices(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListIndicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_indices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-indices)
        """

    def list_job_executions_for_job(
        self,
        jobId: str,
        status: JobExecutionStatus = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListJobExecutionsForJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_job_executions_for_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-job-executions-for-job)
        """

    def list_job_executions_for_thing(
        self,
        thingName: str,
        status: JobExecutionStatus = None,
        namespaceId: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListJobExecutionsForThingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_job_executions_for_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-job-executions-for-thing)
        """

    def list_jobs(
        self,
        status: JobStatus = None,
        targetSelection: TargetSelection = None,
        maxResults: int = None,
        nextToken: str = None,
        thingGroupName: str = None,
        thingGroupId: str = None,
        namespaceId: str = None,
    ) -> ListJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-jobs)
        """

    def list_mitigation_actions(
        self, actionType: MitigationActionType = None, maxResults: int = None, nextToken: str = None
    ) -> ListMitigationActionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_mitigation_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-mitigation-actions)
        """

    def list_ota_updates(
        self, maxResults: int = None, nextToken: str = None, otaUpdateStatus: OTAUpdateStatus = None
    ) -> ListOTAUpdatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_ota_updates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-ota-updates)
        """

    def list_outgoing_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListOutgoingCertificatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_outgoing_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-outgoing-certificates)
        """

    def list_policies(
        self, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ListPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-policies)
        """

    def list_policy_principals(
        self, policyName: str, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ListPolicyPrincipalsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_policy_principals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-policy-principals)
        """

    def list_policy_versions(self, policyName: str) -> ListPolicyVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_policy_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-policy-versions)
        """

    def list_principal_policies(
        self, principal: str, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ListPrincipalPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_principal_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-principal-policies)
        """

    def list_principal_things(
        self, principal: str, nextToken: str = None, maxResults: int = None
    ) -> ListPrincipalThingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_principal_things)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-principal-things)
        """

    def list_provisioning_template_versions(
        self, templateName: str, maxResults: int = None, nextToken: str = None
    ) -> ListProvisioningTemplateVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_provisioning_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-provisioning-template-versions)
        """

    def list_provisioning_templates(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListProvisioningTemplatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_provisioning_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-provisioning-templates)
        """

    def list_role_aliases(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListRoleAliasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_role_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-role-aliases)
        """

    def list_scheduled_audits(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListScheduledAuditsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_scheduled_audits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-scheduled-audits)
        """

    def list_security_profiles(
        self,
        nextToken: str = None,
        maxResults: int = None,
        dimensionName: str = None,
        metricName: str = None,
    ) -> ListSecurityProfilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_security_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-security-profiles)
        """

    def list_security_profiles_for_target(
        self,
        securityProfileTargetArn: str,
        nextToken: str = None,
        maxResults: int = None,
        recursive: bool = None,
    ) -> ListSecurityProfilesForTargetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_security_profiles_for_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-security-profiles-for-target)
        """

    def list_streams(
        self, maxResults: int = None, nextToken: str = None, ascendingOrder: bool = None
    ) -> ListStreamsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-streams)
        """

    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-tags-for-resource)
        """

    def list_targets_for_policy(
        self, policyName: str, marker: str = None, pageSize: int = None
    ) -> ListTargetsForPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_targets_for_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-targets-for-policy)
        """

    def list_targets_for_security_profile(
        self, securityProfileName: str, nextToken: str = None, maxResults: int = None
    ) -> ListTargetsForSecurityProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_targets_for_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-targets-for-security-profile)
        """

    def list_thing_groups(
        self,
        nextToken: str = None,
        maxResults: int = None,
        parentGroup: str = None,
        namePrefixFilter: str = None,
        recursive: bool = None,
    ) -> ListThingGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_thing_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-thing-groups)
        """

    def list_thing_groups_for_thing(
        self, thingName: str, nextToken: str = None, maxResults: int = None
    ) -> ListThingGroupsForThingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_thing_groups_for_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-thing-groups-for-thing)
        """

    def list_thing_principals(
        self, thingName: str, nextToken: str = None, maxResults: int = None
    ) -> ListThingPrincipalsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_thing_principals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-thing-principals)
        """

    def list_thing_registration_task_reports(
        self, taskId: str, reportType: ReportType, nextToken: str = None, maxResults: int = None
    ) -> ListThingRegistrationTaskReportsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_thing_registration_task_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-thing-registration-task-reports)
        """

    def list_thing_registration_tasks(
        self, nextToken: str = None, maxResults: int = None, status: Status = None
    ) -> ListThingRegistrationTasksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_thing_registration_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-thing-registration-tasks)
        """

    def list_thing_types(
        self, nextToken: str = None, maxResults: int = None, thingTypeName: str = None
    ) -> ListThingTypesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_thing_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-thing-types)
        """

    def list_things(
        self,
        nextToken: str = None,
        maxResults: int = None,
        attributeName: str = None,
        attributeValue: str = None,
        thingTypeName: str = None,
        usePrefixAttributeValue: bool = None,
    ) -> ListThingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_things)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-things)
        """

    def list_things_in_billing_group(
        self, billingGroupName: str, nextToken: str = None, maxResults: int = None
    ) -> ListThingsInBillingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_things_in_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-things-in-billing-group)
        """

    def list_things_in_thing_group(
        self,
        thingGroupName: str,
        recursive: bool = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListThingsInThingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_things_in_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-things-in-thing-group)
        """

    def list_topic_rule_destinations(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListTopicRuleDestinationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_topic_rule_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-topic-rule-destinations)
        """

    def list_topic_rules(
        self,
        topic: str = None,
        maxResults: int = None,
        nextToken: str = None,
        ruleDisabled: bool = None,
    ) -> ListTopicRulesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_topic_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-topic-rules)
        """

    def list_v2_logging_levels(
        self, targetType: LogTargetType = None, nextToken: str = None, maxResults: int = None
    ) -> ListV2LoggingLevelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_v2_logging_levels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-v2-logging-levels)
        """

    def list_violation_events(
        self,
        startTime: datetime,
        endTime: datetime,
        thingName: str = None,
        securityProfileName: str = None,
        behaviorCriteriaType: BehaviorCriteriaType = None,
        listSuppressedAlerts: bool = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListViolationEventsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.list_violation_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list-violation-events)
        """

    def register_ca_certificate(
        self,
        caCertificate: str,
        verificationCertificate: str,
        setAsActive: bool = None,
        allowAutoRegistration: bool = None,
        registrationConfig: "RegistrationConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> RegisterCACertificateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.register_ca_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#register-ca-certificate)
        """

    def register_certificate(
        self,
        certificatePem: str,
        caCertificatePem: str = None,
        setAsActive: bool = None,
        status: CertificateStatus = None,
    ) -> RegisterCertificateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.register_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#register-certificate)
        """

    def register_certificate_without_ca(
        self, certificatePem: str, status: CertificateStatus = None
    ) -> RegisterCertificateWithoutCAResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.register_certificate_without_ca)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#register-certificate-without-ca)
        """

    def register_thing(
        self, templateBody: str, parameters: Dict[str, str] = None
    ) -> RegisterThingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.register_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#register-thing)
        """

    def reject_certificate_transfer(self, certificateId: str, rejectReason: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.reject_certificate_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#reject-certificate-transfer)
        """

    def remove_thing_from_billing_group(
        self,
        billingGroupName: str = None,
        billingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.remove_thing_from_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#remove-thing-from-billing-group)
        """

    def remove_thing_from_thing_group(
        self,
        thingGroupName: str = None,
        thingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.remove_thing_from_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#remove-thing-from-thing-group)
        """

    def replace_topic_rule(self, ruleName: str, topicRulePayload: TopicRulePayloadTypeDef) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.replace_topic_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#replace-topic-rule)
        """

    def search_index(
        self,
        queryString: str,
        indexName: str = None,
        nextToken: str = None,
        maxResults: int = None,
        queryVersion: str = None,
    ) -> SearchIndexResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.search_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#search-index)
        """

    def set_default_authorizer(self, authorizerName: str) -> SetDefaultAuthorizerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.set_default_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#set-default-authorizer)
        """

    def set_default_policy_version(self, policyName: str, policyVersionId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.set_default_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#set-default-policy-version)
        """

    def set_logging_options(self, loggingOptionsPayload: LoggingOptionsPayloadTypeDef) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.set_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#set-logging-options)
        """

    def set_v2_logging_level(self, logTarget: "LogTargetTypeDef", logLevel: LogLevel) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.set_v2_logging_level)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#set-v2-logging-level)
        """

    def set_v2_logging_options(
        self, roleArn: str = None, defaultLogLevel: LogLevel = None, disableAllLogs: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.set_v2_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#set-v2-logging-options)
        """

    def start_audit_mitigation_actions_task(
        self,
        taskId: str,
        target: "AuditMitigationActionsTaskTargetTypeDef",
        auditCheckToActionsMapping: Dict[str, List[str]],
        clientRequestToken: str,
    ) -> StartAuditMitigationActionsTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.start_audit_mitigation_actions_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#start-audit-mitigation-actions-task)
        """

    def start_detect_mitigation_actions_task(
        self,
        taskId: str,
        target: "DetectMitigationActionsTaskTargetTypeDef",
        actions: List[str],
        clientRequestToken: str,
        violationEventOccurrenceRange: "ViolationEventOccurrenceRangeTypeDef" = None,
        includeOnlyActiveViolations: bool = None,
        includeSuppressedAlerts: bool = None,
    ) -> StartDetectMitigationActionsTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.start_detect_mitigation_actions_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#start-detect-mitigation-actions-task)
        """

    def start_on_demand_audit_task(
        self, targetCheckNames: List[str]
    ) -> StartOnDemandAuditTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.start_on_demand_audit_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#start-on-demand-audit-task)
        """

    def start_thing_registration_task(
        self, templateBody: str, inputFileBucket: str, inputFileKey: str, roleArn: str
    ) -> StartThingRegistrationTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.start_thing_registration_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#start-thing-registration-task)
        """

    def stop_thing_registration_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.stop_thing_registration_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#stop-thing-registration-task)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#tag-resource)
        """

    def test_authorization(
        self,
        authInfos: List["AuthInfoTypeDef"],
        principal: str = None,
        cognitoIdentityPoolId: str = None,
        clientId: str = None,
        policyNamesToAdd: List[str] = None,
        policyNamesToSkip: List[str] = None,
    ) -> TestAuthorizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.test_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#test-authorization)
        """

    def test_invoke_authorizer(
        self,
        authorizerName: str,
        token: str = None,
        tokenSignature: str = None,
        httpContext: HttpContextTypeDef = None,
        mqttContext: MqttContextTypeDef = None,
        tlsContext: TlsContextTypeDef = None,
    ) -> TestInvokeAuthorizerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.test_invoke_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#test-invoke-authorizer)
        """

    def transfer_certificate(
        self, certificateId: str, targetAwsAccount: str, transferMessage: str = None
    ) -> TransferCertificateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.transfer_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#transfer-certificate)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#untag-resource)
        """

    def update_account_audit_configuration(
        self,
        roleArn: str = None,
        auditNotificationTargetConfigurations: Dict[
            Literal["SNS"], "AuditNotificationTargetTypeDef"
        ] = None,
        auditCheckConfigurations: Dict[str, "AuditCheckConfigurationTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_account_audit_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-account-audit-configuration)
        """

    def update_audit_suppression(
        self,
        checkName: str,
        resourceIdentifier: "ResourceIdentifierTypeDef",
        expirationDate: datetime = None,
        suppressIndefinitely: bool = None,
        description: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_audit_suppression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-audit-suppression)
        """

    def update_authorizer(
        self,
        authorizerName: str,
        authorizerFunctionArn: str = None,
        tokenKeyName: str = None,
        tokenSigningPublicKeys: Dict[str, str] = None,
        status: AuthorizerStatus = None,
    ) -> UpdateAuthorizerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-authorizer)
        """

    def update_billing_group(
        self,
        billingGroupName: str,
        billingGroupProperties: "BillingGroupPropertiesTypeDef",
        expectedVersion: int = None,
    ) -> UpdateBillingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-billing-group)
        """

    def update_ca_certificate(
        self,
        certificateId: str,
        newStatus: CACertificateStatus = None,
        newAutoRegistrationStatus: AutoRegistrationStatus = None,
        registrationConfig: "RegistrationConfigTypeDef" = None,
        removeAutoRegistration: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_ca_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-ca-certificate)
        """

    def update_certificate(self, certificateId: str, newStatus: CertificateStatus) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-certificate)
        """

    def update_custom_metric(
        self, metricName: str, displayName: str
    ) -> UpdateCustomMetricResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_custom_metric)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-custom-metric)
        """

    def update_dimension(
        self, name: str, stringValues: List[str]
    ) -> UpdateDimensionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_dimension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-dimension)
        """

    def update_domain_configuration(
        self,
        domainConfigurationName: str,
        authorizerConfig: "AuthorizerConfigTypeDef" = None,
        domainConfigurationStatus: DomainConfigurationStatus = None,
        removeAuthorizerConfig: bool = None,
    ) -> UpdateDomainConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_domain_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-domain-configuration)
        """

    def update_dynamic_thing_group(
        self,
        thingGroupName: str,
        thingGroupProperties: "ThingGroupPropertiesTypeDef",
        expectedVersion: int = None,
        indexName: str = None,
        queryString: str = None,
        queryVersion: str = None,
    ) -> UpdateDynamicThingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_dynamic_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-dynamic-thing-group)
        """

    def update_event_configurations(
        self, eventConfigurations: Dict[EventType, "ConfigurationTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_event_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-event-configurations)
        """

    def update_indexing_configuration(
        self,
        thingIndexingConfiguration: "ThingIndexingConfigurationTypeDef" = None,
        thingGroupIndexingConfiguration: "ThingGroupIndexingConfigurationTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_indexing_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-indexing-configuration)
        """

    def update_job(
        self,
        jobId: str,
        description: str = None,
        presignedUrlConfig: "PresignedUrlConfigTypeDef" = None,
        jobExecutionsRolloutConfig: "JobExecutionsRolloutConfigTypeDef" = None,
        abortConfig: "AbortConfigTypeDef" = None,
        timeoutConfig: "TimeoutConfigTypeDef" = None,
        namespaceId: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-job)
        """

    def update_mitigation_action(
        self,
        actionName: str,
        roleArn: str = None,
        actionParams: "MitigationActionParamsTypeDef" = None,
    ) -> UpdateMitigationActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_mitigation_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-mitigation-action)
        """

    def update_provisioning_template(
        self,
        templateName: str,
        description: str = None,
        enabled: bool = None,
        defaultVersionId: int = None,
        provisioningRoleArn: str = None,
        preProvisioningHook: "ProvisioningHookTypeDef" = None,
        removePreProvisioningHook: bool = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_provisioning_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-provisioning-template)
        """

    def update_role_alias(
        self, roleAlias: str, roleArn: str = None, credentialDurationSeconds: int = None
    ) -> UpdateRoleAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_role_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-role-alias)
        """

    def update_scheduled_audit(
        self,
        scheduledAuditName: str,
        frequency: AuditFrequency = None,
        dayOfMonth: str = None,
        dayOfWeek: DayOfWeek = None,
        targetCheckNames: List[str] = None,
    ) -> UpdateScheduledAuditResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_scheduled_audit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-scheduled-audit)
        """

    def update_security_profile(
        self,
        securityProfileName: str,
        securityProfileDescription: str = None,
        behaviors: List["BehaviorTypeDef"] = None,
        alertTargets: Dict[Literal["SNS"], "AlertTargetTypeDef"] = None,
        additionalMetricsToRetain: List[str] = None,
        additionalMetricsToRetainV2: List["MetricToRetainTypeDef"] = None,
        deleteBehaviors: bool = None,
        deleteAlertTargets: bool = None,
        deleteAdditionalMetricsToRetain: bool = None,
        expectedVersion: int = None,
    ) -> UpdateSecurityProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-security-profile)
        """

    def update_stream(
        self,
        streamId: str,
        description: str = None,
        files: List["StreamFileTypeDef"] = None,
        roleArn: str = None,
    ) -> UpdateStreamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-stream)
        """

    def update_thing(
        self,
        thingName: str,
        thingTypeName: str = None,
        attributePayload: "AttributePayloadTypeDef" = None,
        expectedVersion: int = None,
        removeThingType: bool = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-thing)
        """

    def update_thing_group(
        self,
        thingGroupName: str,
        thingGroupProperties: "ThingGroupPropertiesTypeDef",
        expectedVersion: int = None,
    ) -> UpdateThingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-thing-group)
        """

    def update_thing_groups_for_thing(
        self,
        thingName: str = None,
        thingGroupsToAdd: List[str] = None,
        thingGroupsToRemove: List[str] = None,
        overrideDynamicGroups: bool = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_thing_groups_for_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-thing-groups-for-thing)
        """

    def update_topic_rule_destination(
        self, arn: str, status: TopicRuleDestinationStatus
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.update_topic_rule_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update-topic-rule-destination)
        """

    def validate_security_profile_behaviors(
        self, behaviors: List["BehaviorTypeDef"]
    ) -> ValidateSecurityProfileBehaviorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Client.validate_security_profile_behaviors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#validate-security-profile-behaviors)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_behavior_model_training_summaries"]
    ) -> GetBehaviorModelTrainingSummariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.GetBehaviorModelTrainingSummaries)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#getbehaviormodeltrainingsummariespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_active_violations"]
    ) -> ListActiveViolationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListActiveViolations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listactiveviolationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_policies"]
    ) -> ListAttachedPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listattachedpoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_findings"]
    ) -> ListAuditFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListAuditFindings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditfindingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_mitigation_actions_executions"]
    ) -> ListAuditMitigationActionsExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsExecutions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditmitigationactionsexecutionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_mitigation_actions_tasks"]
    ) -> ListAuditMitigationActionsTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsTasks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditmitigationactionstaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_suppressions"]
    ) -> ListAuditSuppressionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListAuditSuppressions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditsuppressionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_audit_tasks"]) -> ListAuditTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListAuditTasks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listaudittaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_authorizers"]
    ) -> ListAuthorizersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListAuthorizers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauthorizerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_billing_groups"]
    ) -> ListBillingGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListBillingGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listbillinggroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ca_certificates"]
    ) -> ListCACertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListCACertificates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcacertificatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> ListCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListCertificates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcertificatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificates_by_ca"]
    ) -> ListCertificatesByCAPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcertificatesbycapaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_metrics"]
    ) -> ListCustomMetricsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListCustomMetrics)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcustommetricspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_detect_mitigation_actions_executions"]
    ) -> ListDetectMitigationActionsExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListDetectMitigationActionsExecutions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdetectmitigationactionsexecutionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_detect_mitigation_actions_tasks"]
    ) -> ListDetectMitigationActionsTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListDetectMitigationActionsTasks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdetectmitigationactionstaskspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_dimensions"]) -> ListDimensionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListDimensions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdimensionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_domain_configurations"]
    ) -> ListDomainConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListDomainConfigurations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdomainconfigurationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_indices"]) -> ListIndicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListIndices)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listindicespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_job_executions_for_job"]
    ) -> ListJobExecutionsForJobPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobexecutionsforjobpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_job_executions_for_thing"]
    ) -> ListJobExecutionsForThingPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobexecutionsforthingpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_mitigation_actions"]
    ) -> ListMitigationActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListMitigationActions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listmitigationactionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ota_updates"]) -> ListOTAUpdatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListOTAUpdates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listotaupdatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_outgoing_certificates"]
    ) -> ListOutgoingCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listoutgoingcertificatespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listpoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_principals"]
    ) -> ListPolicyPrincipalsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listpolicyprincipalspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_principal_policies"]
    ) -> ListPrincipalPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprincipalpoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_principal_things"]
    ) -> ListPrincipalThingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListPrincipalThings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprincipalthingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioning_template_versions"]
    ) -> ListProvisioningTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplateVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprovisioningtemplateversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioning_templates"]
    ) -> ListProvisioningTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprovisioningtemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_role_aliases"]
    ) -> ListRoleAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListRoleAliases)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listrolealiasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_scheduled_audits"]
    ) -> ListScheduledAuditsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListScheduledAudits)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listscheduledauditspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles"]
    ) -> ListSecurityProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listsecurityprofilespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles_for_target"]
    ) -> ListSecurityProfilesForTargetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listsecurityprofilesfortargetpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_streams"]) -> ListStreamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListStreams)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#liststreamspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListTagsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtagsforresourcepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_policy"]
    ) -> ListTargetsForPolicyPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtargetsforpolicypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_security_profile"]
    ) -> ListTargetsForSecurityProfilePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtargetsforsecurityprofilepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_groups"]
    ) -> ListThingGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListThingGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthinggroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_groups_for_thing"]
    ) -> ListThingGroupsForThingPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthinggroupsforthingpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_principals"]
    ) -> ListThingPrincipalsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListThingPrincipals)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingprincipalspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_registration_task_reports"]
    ) -> ListThingRegistrationTaskReportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTaskReports)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingregistrationtaskreportspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_registration_tasks"]
    ) -> ListThingRegistrationTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingregistrationtaskspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_thing_types"]) -> ListThingTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListThingTypes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingtypespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_things"]) -> ListThingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListThings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_things_in_billing_group"]
    ) -> ListThingsInBillingGroupPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingsinbillinggrouppaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_things_in_thing_group"]
    ) -> ListThingsInThingGroupPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingsinthinggrouppaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_topic_rule_destinations"]
    ) -> ListTopicRuleDestinationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListTopicRuleDestinations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtopicruledestinationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_topic_rules"]) -> ListTopicRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListTopicRules)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtopicrulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_v2_logging_levels"]
    ) -> ListV2LoggingLevelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listv2logginglevelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_violation_events"]
    ) -> ListViolationEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/iot.html#IoT.Paginator.ListViolationEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listviolationeventspaginator)
        """
