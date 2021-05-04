"""
Type annotations for elbv2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/literals.html)

Usage::

    ```python
    from mypy_boto3_elbv2.literals import ActionTypeEnum

    data: ActionTypeEnum = "authenticate-cognito"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionTypeEnum",
    "AuthenticateCognitoActionConditionalBehaviorEnum",
    "AuthenticateOidcActionConditionalBehaviorEnum",
    "DescribeAccountLimitsPaginatorName",
    "DescribeListenerCertificatesPaginatorName",
    "DescribeListenersPaginatorName",
    "DescribeLoadBalancersPaginatorName",
    "DescribeRulesPaginatorName",
    "DescribeSSLPoliciesPaginatorName",
    "DescribeTargetGroupsPaginatorName",
    "IpAddressType",
    "LoadBalancerAvailableWaiterName",
    "LoadBalancerExistsWaiterName",
    "LoadBalancerSchemeEnum",
    "LoadBalancerStateEnum",
    "LoadBalancerTypeEnum",
    "LoadBalancersDeletedWaiterName",
    "ProtocolEnum",
    "RedirectActionStatusCodeEnum",
    "TargetDeregisteredWaiterName",
    "TargetHealthReasonEnum",
    "TargetHealthStateEnum",
    "TargetInServiceWaiterName",
    "TargetTypeEnum",
)


ActionTypeEnum = Literal[
    "authenticate-cognito", "authenticate-oidc", "fixed-response", "forward", "redirect"
]
AuthenticateCognitoActionConditionalBehaviorEnum = Literal["allow", "authenticate", "deny"]
AuthenticateOidcActionConditionalBehaviorEnum = Literal["allow", "authenticate", "deny"]
DescribeAccountLimitsPaginatorName = Literal["describe_account_limits"]
DescribeListenerCertificatesPaginatorName = Literal["describe_listener_certificates"]
DescribeListenersPaginatorName = Literal["describe_listeners"]
DescribeLoadBalancersPaginatorName = Literal["describe_load_balancers"]
DescribeRulesPaginatorName = Literal["describe_rules"]
DescribeSSLPoliciesPaginatorName = Literal["describe_ssl_policies"]
DescribeTargetGroupsPaginatorName = Literal["describe_target_groups"]
IpAddressType = Literal["dualstack", "ipv4"]
LoadBalancerAvailableWaiterName = Literal["load_balancer_available"]
LoadBalancerExistsWaiterName = Literal["load_balancer_exists"]
LoadBalancerSchemeEnum = Literal["internal", "internet-facing"]
LoadBalancerStateEnum = Literal["active", "active_impaired", "failed", "provisioning"]
LoadBalancerTypeEnum = Literal["application", "gateway", "network"]
LoadBalancersDeletedWaiterName = Literal["load_balancers_deleted"]
ProtocolEnum = Literal["GENEVE", "HTTP", "HTTPS", "TCP", "TCP_UDP", "TLS", "UDP"]
RedirectActionStatusCodeEnum = Literal["HTTP_301", "HTTP_302"]
TargetDeregisteredWaiterName = Literal["target_deregistered"]
TargetHealthReasonEnum = Literal[
    "Elb.InitialHealthChecking",
    "Elb.InternalError",
    "Elb.RegistrationInProgress",
    "Target.DeregistrationInProgress",
    "Target.FailedHealthChecks",
    "Target.HealthCheckDisabled",
    "Target.InvalidState",
    "Target.IpUnusable",
    "Target.NotInUse",
    "Target.NotRegistered",
    "Target.ResponseCodeMismatch",
    "Target.Timeout",
]
TargetHealthStateEnum = Literal[
    "draining", "healthy", "initial", "unavailable", "unhealthy", "unused"
]
TargetInServiceWaiterName = Literal["target_in_service"]
TargetTypeEnum = Literal["instance", "ip", "lambda"]
