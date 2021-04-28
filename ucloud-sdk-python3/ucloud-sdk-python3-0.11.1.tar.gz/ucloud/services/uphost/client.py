""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.uphost.schemas import apis


class UPHostClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UPHostClient, self).__init__(
            config, transport, middleware, logger
        )

    def create_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """CreatePHost - 指定数据中心，根据资源使用量创建指定数量的UPHost物理云主机实例。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ImageId** (str) - (Required) 镜像ID。 请通过 [DescribePHostImage]获取
        - **Password** (str) - (Required) 密码（密码需使用base64进行编码）
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ChargeType** (str) - 计费模式，枚举值为：year, 按年付费； month,按月付费；dynamic，按需付费，（需开启权限） trial, 试用（需开启权限）。默认为按月付费
        - **Cluster** (str) - 网络环境，可选千兆：1G ，万兆：10G， 默认1G
        - **Count** (int) - 购买数量，默认为1，（暂不支持）
        - **CouponId** (str) - 代金券
        - **Name** (str) - 物理机名称，默认为phost
        - **Quantity** (str) - 购买时长，默认为1，范围[1-10]
        - **Raid** (str) - Raid配置，默认Raid10  支持:Raid0、Raid1、Raid5、Raid10，NoRaid
        - **Remark** (str) - 物理机备注，默认为空
        - **SecurityGroupId** (str) - 防火墙Id，默认：Web推荐防火墙。如何查询SecurityGroupId请参见  `DescribeSecurityGroup <https://docs.ucloud.cn/api/unet-api/describe_security_group.html>`_
        - **SubnetId** (str) - 子网ID，不填为默认，VPC2.0下需要填写此字段。
        - **Tag** (str) - 业务组，默认为default
        - **Type** (str) - 物理机类型，默认为：db-2(基础型-SAS-V3)
        - **VPCId** (str) - VPC ID，不填为默认，VPC2.0下需要填写此字段。

        **Response**

        - **PHostId** (list) - PHost的资源ID数组

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreatePHostRequestSchema().dumps(d)

        resp = self.invoke("CreatePHost", d, **kwargs)
        return apis.CreatePHostResponseSchema().loads(resp)

    def describe_phost(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribePHost - 获取物理机详细信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Limit** (int) - 返回数据长度，默认为20
        - **Offset** (int) - 数据偏移量，默认为0
        - **PHostId** (list) - PHost资源ID，若为空，则返回当前Region所有PHost。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PHostSet** (list) - 见 **PHostSet** 模型定义
        - **TotalCount** (int) - 满足条件的PHost总数

        **Response Model**

        **PHostCPUSet**

        - **CoreCount** (int) - CPU核数
        - **Count** (int) - CPU个数
        - **Frequence** (float) - CPU主频
        - **Model** (str) - CPU型号

        **PHostDiskSet**

        - **Count** (int) - 磁盘数量
        - **IOCap** (int) - 磁盘IO性能，单位MB/s（待废弃）
        - **Name** (str) - 磁盘名称，sys/data
        - **Space** (int) - 单盘大小，单位GB
        - **Type** (str) - 磁盘属性

        **PHostIPSet**

        - **Bandwidth** (int) - IP对应带宽，单位Mb，内网IP不显示带宽信息
        - **IPAddr** (str) - IP地址，
        - **IPId** (str) - IP资源ID(内网IP无资源ID)（待废弃）
        - **MACAddr** (str) - MAC地址
        - **OperatorName** (str) - 国际: Internation， BGP: BGP， 内网: Private
        - **SubnetId** (str) - 子网ID
        - **VPCId** (str) - VPC ID

        **PHostSet**

        - **AutoRenew** (str) - 自动续费
        - **CPUSet** (dict) - 见 **PHostCPUSet** 模型定义
        - **ChargeType** (str) - 计费模式，枚举值为： Year，按年付费； Month，按月付费； Dynamic，按需付费（需开启权限）； Trial，试用（需开启权限）默认为月付
        - **Cluster** (str) - 网络环境。枚举值：千兆：1G ，万兆：10G
        - **Components** (str) - 组件信息（暂不支持）
        - **CreateTime** (int) - 创建时间
        - **DiskSet** (list) - 见 **PHostDiskSet** 模型定义
        - **ExpireTime** (int) - 到期时间
        - **IPSet** (list) - 见 **PHostIPSet** 模型定义
        - **ImageName** (str) - 镜像名称
        - **IsSupportKVM** (str) - 是否支持紧急登录
        - **Memory** (int) - 内存大小，单位：MB
        - **Name** (str) - 物理机名称
        - **OSType** (str) - 操作系统类型
        - **OSname** (str) - 操作系统名称
        - **PHostId** (str) - PHost资源ID
        - **PHostType** (str) - 物理机类型，参见DescribePHostMachineType返回值
        - **PMStatus** (str) - 物理云主机状态。枚举值：\\ > 初始化:Initializing; \\ > 启动中：Starting； \\ > 运行中：Running；\\ > 关机中：Stopping； \\ > 安装失败：InstallFailed； \\ > 重启中：Rebooting；\\ > 关机：Stopped；
        - **PowerState** (str) - 电源状态，on 或 off
        - **RaidSupported** (str) - 是否支持Raid。枚举值：Yes：支持；No：不支持。
        - **Remark** (str) - 物理机备注
        - **SN** (str) - 物理机序列号
        - **Tag** (str) - 业务组
        - **Zone** (str) - 可用区，参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribePHostRequestSchema().dumps(d)

        resp = self.invoke("DescribePHost", d, **kwargs)
        return apis.DescribePHostResponseSchema().loads(resp)

    def describe_phost_image(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribePHostImage - 获取物理云主机镜像列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ImageId** (list) - 镜像ID
        - **ImageType** (str) - 镜像类别，枚举为：Base,标准镜像；默认为标准镜像。
        - **Limit** (int) - 返回数据长度，默认为20
        - **Offset** (int) - 数据偏移量，默认为0

        **Response**

        - **ImageSet** (list) - 见 **PHostImageSet** 模型定义
        - **TotalCount** (int) - 满足条件的镜像总数

        **Response Model**

        **PHostImageSet**

        - **ImageId** (str) - 镜像ID
        - **ImageName** (str) - 镜像名称
        - **OsName** (str) - 操作系统名称
        - **OsType** (str) - 操作系统类型

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribePHostImageRequestSchema().dumps(d)

        resp = self.invoke("DescribePHostImage", d, **kwargs)
        return apis.DescribePHostImageResponseSchema().loads(resp)

    def describe_phost_tags(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribePHostTags - 获取物理机tag列表（业务组）

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **TagSet** (list) - 见 **PHostTagSet** 模型定义
        - **TotalCount** (int) - Tag的个数

        **Response Model**

        **PHostTagSet**

        - **Tag** (str) - 业务组名称
        - **TotalCount** (int) - 该业务组中包含的主机个数

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribePHostTagsRequestSchema().dumps(d)

        resp = self.invoke("DescribePHostTags", d, **kwargs)
        return apis.DescribePHostTagsResponseSchema().loads(resp)

    def get_phost_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetPHostPrice - 获取物理机价格列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ChargeType** (str) - (Required) 计费模式，枚举值为： Year/Month/Trial/Dynamic
        - **Count** (int) - (Required) 购买数量，范围[1-5]
        - **Quantity** (int) - (Required) 购买时长，1-10个月或1-10年
        - **Cluster** (str) - 网络环境，可选千兆：1G ，万兆：10G
        - **Type** (str) - 默认为：DB(数据库型)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PriceSet** (list) - 见 **PHostPriceSet** 模型定义

        **Response Model**

        **PHostPriceSet**

        - **ChargeType** (str) - Year/Month/Trial/Dynamic
        - **Price** (float) - 价格, 单位:元, 保留小数点后两位有效数字

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetPHostPriceRequestSchema().dumps(d)

        resp = self.invoke("GetPHostPrice", d, **kwargs)
        return apis.GetPHostPriceResponseSchema().loads(resp)

    def modify_phost_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyPHostInfo - 更改物理机信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) 物理机资源ID
        - **Name** (str) - 物理机名称，默认不更改
        - **Remark** (str) - 物理机备注，默认不更改
        - **Tag** (str) - 业务组，默认不更改
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyPHostInfoRequestSchema().dumps(d)

        resp = self.invoke("ModifyPHostInfo", d, **kwargs)
        return apis.ModifyPHostInfoResponseSchema().loads(resp)

    def poweroff_phost(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """PoweroffPHost - 断电物理云主机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) PHost资源ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.PoweroffPHostRequestSchema().dumps(d)

        resp = self.invoke("PoweroffPHost", d, **kwargs)
        return apis.PoweroffPHostResponseSchema().loads(resp)

    def reboot_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """RebootPHost - 重启物理机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) PHost资源ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RebootPHostRequestSchema().dumps(d)

        resp = self.invoke("RebootPHost", d, **kwargs)
        return apis.RebootPHostResponseSchema().loads(resp)

    def reinstall_phost(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ReinstallPHost - 重装物理机操作系统

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) PHost资源ID
        - **Password** (str) - (Required) 密码
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **ImageId** (str) - 镜像Id，参考镜像列表，默认使用原镜像
        - **Name** (str) - 物理机名称，默认不更改
        - **Raid** (str) - 不保留数据盘重装，可选Raid
        - **Remark** (str) - 物理机备注，默认为不更改。
        - **ReserveDisk** (str) - 是否保留数据盘，保留：Yes，不报留：No， 默认：Yes
        - **Tag** (str) - 业务组，默认不更改。

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReinstallPHostRequestSchema().dumps(d)

        resp = self.invoke("ReinstallPHost", d, **kwargs)
        return apis.ReinstallPHostResponseSchema().loads(resp)

    def start_phost(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """StartPHost - 启动物理机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) PHost资源ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.StartPHostRequestSchema().dumps(d)

        resp = self.invoke("StartPHost", d, **kwargs)
        return apis.StartPHostResponseSchema().loads(resp)

    def terminate_phost(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """TerminatePHost - 删除物理云主机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PHostId** (str) - (Required) PHost资源ID
        - **ReleaseEIP** (bool) - 是否释放绑定的EIP。true: 解绑EIP后，并释放；其他值或不填：解绑EIP。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **PHostId** (str) - PHost 的资源ID

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.TerminatePHostRequestSchema().dumps(d)

        resp = self.invoke("TerminatePHost", d, **kwargs)
        return apis.TerminatePHostResponseSchema().loads(resp)
