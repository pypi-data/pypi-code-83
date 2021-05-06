"""
Type annotations for opsworks service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/literals.html)

Usage::

    ```python
    from mypy_boto3_opsworks.literals import AppAttributesKeys

    data: AppAttributesKeys = "AutoBundleOnDeploy"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AppAttributesKeys",
    "AppExistsWaiterName",
    "AppType",
    "Architecture",
    "AutoScalingType",
    "CloudWatchLogsEncoding",
    "CloudWatchLogsInitialPosition",
    "CloudWatchLogsTimeZone",
    "DeploymentCommandName",
    "DeploymentSuccessfulWaiterName",
    "DescribeEcsClustersPaginatorName",
    "InstanceOnlineWaiterName",
    "InstanceRegisteredWaiterName",
    "InstanceStoppedWaiterName",
    "InstanceTerminatedWaiterName",
    "LayerAttributesKeys",
    "LayerType",
    "RootDeviceType",
    "SourceType",
    "StackAttributesKeys",
    "VirtualizationType",
    "VolumeType",
)


AppAttributesKeys = Literal["AutoBundleOnDeploy", "AwsFlowRubySettings", "DocumentRoot", "RailsEnv"]
AppExistsWaiterName = Literal["app_exists"]
AppType = Literal["aws-flow-ruby", "java", "nodejs", "other", "php", "rails", "static"]
Architecture = Literal["i386", "x86_64"]
AutoScalingType = Literal["load", "timer"]
CloudWatchLogsEncoding = Literal[
    "ascii",
    "big5",
    "big5hkscs",
    "cp037",
    "cp1006",
    "cp1026",
    "cp1140",
    "cp1250",
    "cp1251",
    "cp1252",
    "cp1253",
    "cp1254",
    "cp1255",
    "cp1256",
    "cp1257",
    "cp1258",
    "cp424",
    "cp437",
    "cp500",
    "cp720",
    "cp737",
    "cp775",
    "cp850",
    "cp852",
    "cp855",
    "cp856",
    "cp857",
    "cp858",
    "cp860",
    "cp861",
    "cp862",
    "cp863",
    "cp864",
    "cp865",
    "cp866",
    "cp869",
    "cp874",
    "cp875",
    "cp932",
    "cp949",
    "cp950",
    "euc_jis_2004",
    "euc_jisx0213",
    "euc_jp",
    "euc_kr",
    "gb18030",
    "gb2312",
    "gbk",
    "hz",
    "iso2022_jp",
    "iso2022_jp_1",
    "iso2022_jp_2",
    "iso2022_jp_2004",
    "iso2022_jp_3",
    "iso2022_jp_ext",
    "iso2022_kr",
    "iso8859_10",
    "iso8859_13",
    "iso8859_14",
    "iso8859_15",
    "iso8859_16",
    "iso8859_2",
    "iso8859_3",
    "iso8859_4",
    "iso8859_5",
    "iso8859_6",
    "iso8859_7",
    "iso8859_8",
    "iso8859_9",
    "johab",
    "koi8_r",
    "koi8_u",
    "latin_1",
    "mac_cyrillic",
    "mac_greek",
    "mac_iceland",
    "mac_latin2",
    "mac_roman",
    "mac_turkish",
    "ptcp154",
    "shift_jis",
    "shift_jis_2004",
    "shift_jisx0213",
    "utf_16",
    "utf_16_be",
    "utf_16_le",
    "utf_32",
    "utf_32_be",
    "utf_32_le",
    "utf_7",
    "utf_8",
    "utf_8_sig",
]
CloudWatchLogsInitialPosition = Literal["end_of_file", "start_of_file"]
CloudWatchLogsTimeZone = Literal["LOCAL", "UTC"]
DeploymentCommandName = Literal[
    "configure",
    "deploy",
    "execute_recipes",
    "install_dependencies",
    "restart",
    "rollback",
    "setup",
    "start",
    "stop",
    "undeploy",
    "update_custom_cookbooks",
    "update_dependencies",
]
DeploymentSuccessfulWaiterName = Literal["deployment_successful"]
DescribeEcsClustersPaginatorName = Literal["describe_ecs_clusters"]
InstanceOnlineWaiterName = Literal["instance_online"]
InstanceRegisteredWaiterName = Literal["instance_registered"]
InstanceStoppedWaiterName = Literal["instance_stopped"]
InstanceTerminatedWaiterName = Literal["instance_terminated"]
LayerAttributesKeys = Literal[
    "BundlerVersion",
    "EcsClusterArn",
    "EnableHaproxyStats",
    "GangliaPassword",
    "GangliaUrl",
    "GangliaUser",
    "HaproxyHealthCheckMethod",
    "HaproxyHealthCheckUrl",
    "HaproxyStatsPassword",
    "HaproxyStatsUrl",
    "HaproxyStatsUser",
    "JavaAppServer",
    "JavaAppServerVersion",
    "Jvm",
    "JvmOptions",
    "JvmVersion",
    "ManageBundler",
    "MemcachedMemory",
    "MysqlRootPassword",
    "MysqlRootPasswordUbiquitous",
    "NodejsVersion",
    "PassengerVersion",
    "RailsStack",
    "RubyVersion",
    "RubygemsVersion",
]
LayerType = Literal[
    "aws-flow-ruby",
    "custom",
    "db-master",
    "ecs-cluster",
    "java-app",
    "lb",
    "memcached",
    "monitoring-master",
    "nodejs-app",
    "php-app",
    "rails-app",
    "web",
]
RootDeviceType = Literal["ebs", "instance-store"]
SourceType = Literal["archive", "git", "s3", "svn"]
StackAttributesKeys = Literal["Color"]
VirtualizationType = Literal["hvm", "paravirtual"]
VolumeType = Literal["gp2", "io1", "standard"]
