"""
Type annotations for network-firewall service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/literals.html)

Usage::

    ```python
    from mypy_boto3_network_firewall.literals import AttachmentStatus

    data: AttachmentStatus = "CREATING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AttachmentStatus",
    "ConfigurationSyncState",
    "FirewallStatusValue",
    "GeneratedRulesType",
    "ListFirewallPoliciesPaginatorName",
    "ListFirewallsPaginatorName",
    "ListRuleGroupsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "LogDestinationType",
    "LogType",
    "PerObjectSyncStatus",
    "ResourceStatus",
    "RuleGroupType",
    "StatefulAction",
    "StatefulRuleDirection",
    "StatefulRuleProtocol",
    "TCPFlag",
    "TargetType",
)


AttachmentStatus = Literal["CREATING", "DELETING", "READY", "SCALING"]
ConfigurationSyncState = Literal["IN_SYNC", "PENDING"]
FirewallStatusValue = Literal["DELETING", "PROVISIONING", "READY"]
GeneratedRulesType = Literal["ALLOWLIST", "DENYLIST"]
ListFirewallPoliciesPaginatorName = Literal["list_firewall_policies"]
ListFirewallsPaginatorName = Literal["list_firewalls"]
ListRuleGroupsPaginatorName = Literal["list_rule_groups"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
LogDestinationType = Literal["CloudWatchLogs", "KinesisDataFirehose", "S3"]
LogType = Literal["ALERT", "FLOW"]
PerObjectSyncStatus = Literal["IN_SYNC", "PENDING"]
ResourceStatus = Literal["ACTIVE", "DELETING"]
RuleGroupType = Literal["STATEFUL", "STATELESS"]
StatefulAction = Literal["ALERT", "DROP", "PASS"]
StatefulRuleDirection = Literal["ANY", "FORWARD"]
StatefulRuleProtocol = Literal[
    "DCERPC",
    "DHCP",
    "DNS",
    "FTP",
    "HTTP",
    "ICMP",
    "IKEV2",
    "IMAP",
    "IP",
    "KRB5",
    "MSN",
    "NTP",
    "SMB",
    "SMTP",
    "SSH",
    "TCP",
    "TFTP",
    "TLS",
    "UDP",
]
TCPFlag = Literal["ACK", "CWR", "ECE", "FIN", "PSH", "RST", "SYN", "URG"]
TargetType = Literal["HTTP_HOST", "TLS_SNI"]
