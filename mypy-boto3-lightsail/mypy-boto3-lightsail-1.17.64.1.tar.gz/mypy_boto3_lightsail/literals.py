"""
Type annotations for lightsail service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/literals.html)

Usage::

    ```python
    from mypy_boto3_lightsail.literals import AccessDirection

    data: AccessDirection = "inbound"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccessDirection",
    "AddOnType",
    "AlarmState",
    "AutoSnapshotStatus",
    "BehaviorEnum",
    "BlueprintType",
    "CertificateStatus",
    "CloudFormationStackRecordSourceType",
    "ComparisonOperator",
    "ContactMethodStatus",
    "ContactMethodVerificationProtocol",
    "ContactProtocol",
    "ContainerServiceDeploymentState",
    "ContainerServiceMetricName",
    "ContainerServicePowerName",
    "ContainerServiceProtocol",
    "ContainerServiceState",
    "ContainerServiceStateDetailCode",
    "DiskSnapshotState",
    "DiskState",
    "DistributionMetricName",
    "ExportSnapshotRecordSourceType",
    "ForwardValues",
    "GetActiveNamesPaginatorName",
    "GetBlueprintsPaginatorName",
    "GetBundlesPaginatorName",
    "GetCloudFormationStackRecordsPaginatorName",
    "GetDiskSnapshotsPaginatorName",
    "GetDisksPaginatorName",
    "GetDomainsPaginatorName",
    "GetExportSnapshotRecordsPaginatorName",
    "GetInstanceSnapshotsPaginatorName",
    "GetInstancesPaginatorName",
    "GetKeyPairsPaginatorName",
    "GetLoadBalancersPaginatorName",
    "GetOperationsPaginatorName",
    "GetRelationalDatabaseBlueprintsPaginatorName",
    "GetRelationalDatabaseBundlesPaginatorName",
    "GetRelationalDatabaseEventsPaginatorName",
    "GetRelationalDatabaseParametersPaginatorName",
    "GetRelationalDatabaseSnapshotsPaginatorName",
    "GetRelationalDatabasesPaginatorName",
    "GetStaticIpsPaginatorName",
    "HeaderEnum",
    "InstanceAccessProtocol",
    "InstanceHealthReason",
    "InstanceHealthState",
    "InstanceMetricName",
    "InstancePlatform",
    "InstanceSnapshotState",
    "IpAddressType",
    "LoadBalancerAttributeName",
    "LoadBalancerMetricName",
    "LoadBalancerProtocol",
    "LoadBalancerState",
    "LoadBalancerTlsCertificateDomainStatus",
    "LoadBalancerTlsCertificateFailureReason",
    "LoadBalancerTlsCertificateRenewalStatus",
    "LoadBalancerTlsCertificateRevocationReason",
    "LoadBalancerTlsCertificateStatus",
    "MetricName",
    "MetricStatistic",
    "MetricUnit",
    "NetworkProtocol",
    "OperationStatus",
    "OperationType",
    "OriginProtocolPolicyEnum",
    "PortAccessType",
    "PortInfoSourceType",
    "PortState",
    "RecordState",
    "RegionName",
    "RelationalDatabaseEngine",
    "RelationalDatabaseMetricName",
    "RelationalDatabasePasswordVersion",
    "RenewalStatus",
    "ResourceType",
    "TreatMissingData",
)


AccessDirection = Literal["inbound", "outbound"]
AddOnType = Literal["AutoSnapshot"]
AlarmState = Literal["ALARM", "INSUFFICIENT_DATA", "OK"]
AutoSnapshotStatus = Literal["Failed", "InProgress", "NotFound", "Success"]
BehaviorEnum = Literal["cache", "dont-cache"]
BlueprintType = Literal["app", "os"]
CertificateStatus = Literal[
    "EXPIRED",
    "FAILED",
    "INACTIVE",
    "ISSUED",
    "PENDING_VALIDATION",
    "REVOKED",
    "VALIDATION_TIMED_OUT",
]
CloudFormationStackRecordSourceType = Literal["ExportSnapshotRecord"]
ComparisonOperator = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanOrEqualToThreshold",
    "LessThanThreshold",
]
ContactMethodStatus = Literal["Invalid", "PendingVerification", "Valid"]
ContactMethodVerificationProtocol = Literal["Email"]
ContactProtocol = Literal["Email", "SMS"]
ContainerServiceDeploymentState = Literal["ACTIVATING", "ACTIVE", "FAILED", "INACTIVE"]
ContainerServiceMetricName = Literal["CPUUtilization", "MemoryUtilization"]
ContainerServicePowerName = Literal["large", "medium", "micro", "nano", "small", "xlarge"]
ContainerServiceProtocol = Literal["HTTP", "HTTPS", "TCP", "UDP"]
ContainerServiceState = Literal[
    "DELETING", "DEPLOYING", "DISABLED", "PENDING", "READY", "RUNNING", "UPDATING"
]
ContainerServiceStateDetailCode = Literal[
    "ACTIVATING_DEPLOYMENT",
    "CERTIFICATE_LIMIT_EXCEEDED",
    "CREATING_DEPLOYMENT",
    "CREATING_NETWORK_INFRASTRUCTURE",
    "CREATING_SYSTEM_RESOURCES",
    "EVALUATING_HEALTH_CHECK",
    "PROVISIONING_CERTIFICATE",
    "PROVISIONING_SERVICE",
    "UNKNOWN_ERROR",
]
DiskSnapshotState = Literal["completed", "error", "pending", "unknown"]
DiskState = Literal["available", "error", "in-use", "pending", "unknown"]
DistributionMetricName = Literal[
    "BytesDownloaded",
    "BytesUploaded",
    "Http4xxErrorRate",
    "Http5xxErrorRate",
    "Requests",
    "TotalErrorRate",
]
ExportSnapshotRecordSourceType = Literal["DiskSnapshot", "InstanceSnapshot"]
ForwardValues = Literal["all", "allow-list", "none"]
GetActiveNamesPaginatorName = Literal["get_active_names"]
GetBlueprintsPaginatorName = Literal["get_blueprints"]
GetBundlesPaginatorName = Literal["get_bundles"]
GetCloudFormationStackRecordsPaginatorName = Literal["get_cloud_formation_stack_records"]
GetDiskSnapshotsPaginatorName = Literal["get_disk_snapshots"]
GetDisksPaginatorName = Literal["get_disks"]
GetDomainsPaginatorName = Literal["get_domains"]
GetExportSnapshotRecordsPaginatorName = Literal["get_export_snapshot_records"]
GetInstanceSnapshotsPaginatorName = Literal["get_instance_snapshots"]
GetInstancesPaginatorName = Literal["get_instances"]
GetKeyPairsPaginatorName = Literal["get_key_pairs"]
GetLoadBalancersPaginatorName = Literal["get_load_balancers"]
GetOperationsPaginatorName = Literal["get_operations"]
GetRelationalDatabaseBlueprintsPaginatorName = Literal["get_relational_database_blueprints"]
GetRelationalDatabaseBundlesPaginatorName = Literal["get_relational_database_bundles"]
GetRelationalDatabaseEventsPaginatorName = Literal["get_relational_database_events"]
GetRelationalDatabaseParametersPaginatorName = Literal["get_relational_database_parameters"]
GetRelationalDatabaseSnapshotsPaginatorName = Literal["get_relational_database_snapshots"]
GetRelationalDatabasesPaginatorName = Literal["get_relational_databases"]
GetStaticIpsPaginatorName = Literal["get_static_ips"]
HeaderEnum = Literal[
    "Accept",
    "Accept-Charset",
    "Accept-Datetime",
    "Accept-Encoding",
    "Accept-Language",
    "Authorization",
    "CloudFront-Forwarded-Proto",
    "CloudFront-Is-Desktop-Viewer",
    "CloudFront-Is-Mobile-Viewer",
    "CloudFront-Is-SmartTV-Viewer",
    "CloudFront-Is-Tablet-Viewer",
    "CloudFront-Viewer-Country",
    "Host",
    "Origin",
    "Referer",
]
InstanceAccessProtocol = Literal["rdp", "ssh"]
InstanceHealthReason = Literal[
    "Instance.DeregistrationInProgress",
    "Instance.FailedHealthChecks",
    "Instance.InvalidState",
    "Instance.IpUnusable",
    "Instance.NotInUse",
    "Instance.NotRegistered",
    "Instance.ResponseCodeMismatch",
    "Instance.Timeout",
    "Lb.InitialHealthChecking",
    "Lb.InternalError",
    "Lb.RegistrationInProgress",
]
InstanceHealthState = Literal[
    "draining", "healthy", "initial", "unavailable", "unhealthy", "unused"
]
InstanceMetricName = Literal[
    "BurstCapacityPercentage",
    "BurstCapacityTime",
    "CPUUtilization",
    "NetworkIn",
    "NetworkOut",
    "StatusCheckFailed",
    "StatusCheckFailed_Instance",
    "StatusCheckFailed_System",
]
InstancePlatform = Literal["LINUX_UNIX", "WINDOWS"]
InstanceSnapshotState = Literal["available", "error", "pending"]
IpAddressType = Literal["dualstack", "ipv4"]
LoadBalancerAttributeName = Literal[
    "HealthCheckPath", "SessionStickinessEnabled", "SessionStickiness_LB_CookieDurationSeconds"
]
LoadBalancerMetricName = Literal[
    "ClientTLSNegotiationErrorCount",
    "HTTPCode_Instance_2XX_Count",
    "HTTPCode_Instance_3XX_Count",
    "HTTPCode_Instance_4XX_Count",
    "HTTPCode_Instance_5XX_Count",
    "HTTPCode_LB_4XX_Count",
    "HTTPCode_LB_5XX_Count",
    "HealthyHostCount",
    "InstanceResponseTime",
    "RejectedConnectionCount",
    "RequestCount",
    "UnhealthyHostCount",
]
LoadBalancerProtocol = Literal["HTTP", "HTTP_HTTPS"]
LoadBalancerState = Literal["active", "active_impaired", "failed", "provisioning", "unknown"]
LoadBalancerTlsCertificateDomainStatus = Literal["FAILED", "PENDING_VALIDATION", "SUCCESS"]
LoadBalancerTlsCertificateFailureReason = Literal[
    "ADDITIONAL_VERIFICATION_REQUIRED",
    "DOMAIN_NOT_ALLOWED",
    "INVALID_PUBLIC_DOMAIN",
    "NO_AVAILABLE_CONTACTS",
    "OTHER",
]
LoadBalancerTlsCertificateRenewalStatus = Literal[
    "FAILED", "PENDING_AUTO_RENEWAL", "PENDING_VALIDATION", "SUCCESS"
]
LoadBalancerTlsCertificateRevocationReason = Literal[
    "AFFILIATION_CHANGED",
    "A_A_COMPROMISE",
    "CA_COMPROMISE",
    "CERTIFICATE_HOLD",
    "CESSATION_OF_OPERATION",
    "KEY_COMPROMISE",
    "PRIVILEGE_WITHDRAWN",
    "REMOVE_FROM_CRL",
    "SUPERCEDED",
    "UNSPECIFIED",
]
LoadBalancerTlsCertificateStatus = Literal[
    "EXPIRED",
    "FAILED",
    "INACTIVE",
    "ISSUED",
    "PENDING_VALIDATION",
    "REVOKED",
    "UNKNOWN",
    "VALIDATION_TIMED_OUT",
]
MetricName = Literal[
    "BurstCapacityPercentage",
    "BurstCapacityTime",
    "CPUUtilization",
    "ClientTLSNegotiationErrorCount",
    "DatabaseConnections",
    "DiskQueueDepth",
    "FreeStorageSpace",
    "HTTPCode_Instance_2XX_Count",
    "HTTPCode_Instance_3XX_Count",
    "HTTPCode_Instance_4XX_Count",
    "HTTPCode_Instance_5XX_Count",
    "HTTPCode_LB_4XX_Count",
    "HTTPCode_LB_5XX_Count",
    "HealthyHostCount",
    "InstanceResponseTime",
    "NetworkIn",
    "NetworkOut",
    "NetworkReceiveThroughput",
    "NetworkTransmitThroughput",
    "RejectedConnectionCount",
    "RequestCount",
    "StatusCheckFailed",
    "StatusCheckFailed_Instance",
    "StatusCheckFailed_System",
    "UnhealthyHostCount",
]
MetricStatistic = Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
MetricUnit = Literal[
    "Bits",
    "Bits/Second",
    "Bytes",
    "Bytes/Second",
    "Count",
    "Count/Second",
    "Gigabits",
    "Gigabits/Second",
    "Gigabytes",
    "Gigabytes/Second",
    "Kilobits",
    "Kilobits/Second",
    "Kilobytes",
    "Kilobytes/Second",
    "Megabits",
    "Megabits/Second",
    "Megabytes",
    "Megabytes/Second",
    "Microseconds",
    "Milliseconds",
    "None",
    "Percent",
    "Seconds",
    "Terabits",
    "Terabits/Second",
    "Terabytes",
    "Terabytes/Second",
]
NetworkProtocol = Literal["all", "icmp", "tcp", "udp"]
OperationStatus = Literal["Completed", "Failed", "NotStarted", "Started", "Succeeded"]
OperationType = Literal[
    "AllocateStaticIp",
    "AttachCertificateToDistribution",
    "AttachDisk",
    "AttachInstancesToLoadBalancer",
    "AttachLoadBalancerTlsCertificate",
    "AttachStaticIp",
    "CloseInstancePublicPorts",
    "CreateCertificate",
    "CreateContactMethod",
    "CreateContainerService",
    "CreateContainerServiceDeployment",
    "CreateContainerServiceRegistryLogin",
    "CreateDisk",
    "CreateDiskFromSnapshot",
    "CreateDiskSnapshot",
    "CreateDistribution",
    "CreateDomain",
    "CreateInstance",
    "CreateInstanceSnapshot",
    "CreateInstancesFromSnapshot",
    "CreateLoadBalancer",
    "CreateLoadBalancerTlsCertificate",
    "CreateRelationalDatabase",
    "CreateRelationalDatabaseFromSnapshot",
    "CreateRelationalDatabaseSnapshot",
    "DeleteAlarm",
    "DeleteCertificate",
    "DeleteContactMethod",
    "DeleteContainerImage",
    "DeleteContainerService",
    "DeleteDisk",
    "DeleteDiskSnapshot",
    "DeleteDistribution",
    "DeleteDomain",
    "DeleteDomainEntry",
    "DeleteInstance",
    "DeleteInstanceSnapshot",
    "DeleteKnownHostKeys",
    "DeleteLoadBalancer",
    "DeleteLoadBalancerTlsCertificate",
    "DeleteRelationalDatabase",
    "DeleteRelationalDatabaseSnapshot",
    "DetachCertificateFromDistribution",
    "DetachDisk",
    "DetachInstancesFromLoadBalancer",
    "DetachStaticIp",
    "DisableAddOn",
    "EnableAddOn",
    "GetAlarms",
    "GetContactMethods",
    "OpenInstancePublicPorts",
    "PutAlarm",
    "PutInstancePublicPorts",
    "RebootInstance",
    "RebootRelationalDatabase",
    "RegisterContainerImage",
    "ReleaseStaticIp",
    "ResetDistributionCache",
    "SendContactMethodVerification",
    "SetIpAddressType",
    "StartInstance",
    "StartRelationalDatabase",
    "StopInstance",
    "StopRelationalDatabase",
    "TestAlarm",
    "UpdateContainerService",
    "UpdateDistribution",
    "UpdateDistributionBundle",
    "UpdateDomainEntry",
    "UpdateLoadBalancerAttribute",
    "UpdateRelationalDatabase",
    "UpdateRelationalDatabaseParameters",
]
OriginProtocolPolicyEnum = Literal["http-only", "https-only"]
PortAccessType = Literal["Private", "Public"]
PortInfoSourceType = Literal["CLOSED", "DEFAULT", "INSTANCE", "NONE"]
PortState = Literal["closed", "open"]
RecordState = Literal["Failed", "Started", "Succeeded"]
RegionName = Literal[
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
RelationalDatabaseEngine = Literal["mysql"]
RelationalDatabaseMetricName = Literal[
    "CPUUtilization",
    "DatabaseConnections",
    "DiskQueueDepth",
    "FreeStorageSpace",
    "NetworkReceiveThroughput",
    "NetworkTransmitThroughput",
]
RelationalDatabasePasswordVersion = Literal["CURRENT", "PENDING", "PREVIOUS"]
RenewalStatus = Literal["Failed", "PendingAutoRenewal", "PendingValidation", "Success"]
ResourceType = Literal[
    "Alarm",
    "Certificate",
    "CloudFormationStackRecord",
    "ContactMethod",
    "ContainerService",
    "Disk",
    "DiskSnapshot",
    "Distribution",
    "Domain",
    "ExportSnapshotRecord",
    "Instance",
    "InstanceSnapshot",
    "KeyPair",
    "LoadBalancer",
    "LoadBalancerTlsCertificate",
    "PeeredVpc",
    "RelationalDatabase",
    "RelationalDatabaseSnapshot",
    "StaticIp",
]
TreatMissingData = Literal["breaching", "ignore", "missing", "notBreaching"]
