""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.pathx.schemas import apis


class PathXClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(PathXClient, self).__init__(config, transport, middleware, logger)

    def bind_path_xssl(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """BindPathXSSL - 绑定PathX SSL证书

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Port** (list) - (Required) 绑定SSL证书的HTTPS端口。Port.0 Port.1对应多个Port。如果Port不存在则不会绑定
        - **SSLId** (str) - (Required) 证书ID，如果没有指定证书ID也没有申请免费证书，HTTPS接入无法正常工作
        - **UGAId** (str) - (Required) UGA实例ID

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.BindPathXSSLRequestSchema().dumps(d)

        resp = self.invoke("BindPathXSSL", d, **kwargs)
        return apis.BindPathXSSLResponseSchema().loads(resp)

    def create_global_ssh_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateGlobalSSHInstance - 创建GlobalSSH实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID,如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Area** (str) - (Required) 填写支持SSH访问IP的地区名称，如“洛杉矶”，“新加坡”，“香港”，“东京”，“华盛顿”，“法兰克福”。Area和AreaCode两者必填一个
        - **AreaCode** (str) - (Required) AreaCode, 区域航空港国际通用代码。Area和AreaCode两者必填一个
        - **Port** (int) - (Required) 源站服务器监听的SSH端口，可取范围[1-65535]，不能使用80，443,  65123端口。如果InstanceType=Free，取值范围缩小为[22,3389],linux系统选择22，windows系统自动选3389。
        - **TargetIP** (str) - (Required) 被SSH访问的源站IP，仅支持IPv4地址。
        - **BandwidthPackage** (int) - Ultimate版本带宽包大小,枚举值：[0,20,40]。单位MB
        - **ChargeType** (str) - 支付方式，如按月、按年、按时
        - **CouponId** (str) - 使用代金券可冲抵部分费用
        - **ForwardRegion** (str) - InstanceType等于Basic时可以在["cn-bj2","cn-sh2","cn-gd"]中选择1个作为转发机房，Free版本固定为cn-bj2,其他付费版默认配置三个转发机房
        - **InstanceType** (str) - 枚举值：["Enterprise","Basic","Free"], 分别代表企业版，基础版，免费版
        - **Quantity** (int) - 购买数量
        - **Remark** (str) - 备注信息

        **Response**

        - **AcceleratingDomain** (str) - 加速域名，访问该域名可就近接入
        - **InstanceId** (str) - 实例ID，资源唯一标识
        - **Message** (str) - 提示信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.CreateGlobalSSHInstanceRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateGlobalSSHInstance", d, **kwargs)
        return apis.CreateGlobalSSHInstanceResponseSchema().loads(resp)

    def create_path_xssl(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreatePathXSSL - 创建SSL证书，可以把整个 Pem 证书内容传到SSLContent，或者把证书、私钥、CA证书分别传过来

        **Request**

        - **ProjectId** (str) - (Config) 项目ID org-xxx格式。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **SSLName** (str) - (Required) SSL证书的名字
        - **CACert** (str) - CA颁发证书内容
        - **PrivateKey** (str) - 加密证书的私钥，不可使用密码保护，开启密码保护后，重启服务需要输入密码
        - **SSLContent** (str) - SSL证书的完整内容，私钥不可使用密码，包括加密证书的私钥、用户证书或CA证书等
        - **SSLType** (str) - 所添加的SSL证书类型，目前只支持Pem格式
        - **UserCert** (str) - 用户自签证书内容

        **Response**

        - **SSLId** (str) - SSL证书的Id

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.CreatePathXSSLRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreatePathXSSL", d, **kwargs)
        return apis.CreatePathXSSLResponseSchema().loads(resp)

    def create_uga_forwarder(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateUGAForwarder - 创建加速实例转发器，支持HTTPS接入HTTPS回源、HTTPS接入HTTP回源、HTTP接入HTTP回源、TCP接入TCP回源、UDP接入UDP回源、 支持WSS接入WSS回源、WSS接入WS回源、WS接入WS回源

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **UGAId** (str) - (Required) 加速配置实例ID
        - **HTTPHTTP** (list) - HTTP接入HTTP回源转发，接入端口。禁用65123端口
        - **HTTPHTTPRS** (list) - HTTP接入HTTP回源转发，源站监听端口
        - **HTTPSHTTP** (list) - HTTPS接入HTTP回源转发，接入端口。禁用65123端口
        - **HTTPSHTTPRS** (list) - HTTPS接入HTTP回源转发，回源端口
        - **HTTPSHTTPS** (list) - HTTPS接入HTTPS回源转发，接入端口。禁用65123端口
        - **HTTPSHTTPSRS** (list) - HTTPS接入HTTPS回源转发，源站监听端口
        - **TCP** (list) - TCP接入端口
        - **TCPRS** (list) - TCP回源端口
        - **UDP** (list) - UDP接入端口
        - **UDPRS** (list) - UDP回源端口

        **Response**

        - **Message** (str) - 返回信息 说明

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.CreateUGAForwarderRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUGAForwarder", d, **kwargs)
        return apis.CreateUGAForwarderResponseSchema().loads(resp)

    def create_uga_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateUGAInstance - 创建全球加速配置项

        **Request**

        - **ProjectId** (str) - (Config) 项目ID,如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Name** (str) - (Required) 加速配置实例名称
        - **Domain** (str) - 加速源域名，IPList和Domain二选一必填
        - **IPList** (str) - 加速源IP，多个IP用英文半角逗号(,)隔开；IPList和Domain二选一必填
        - **TCP** (list) - TCP端口号，已废弃。请使用 CreateUGAForwarder API 创建端口
        - **UDP** (list) - UDP端口号，已废弃。请使用 CreateUGAForwarder API 创建端口

        **Response**

        - **CName** (str) - 加速域名 用户可把业务域名CName到此域名上。注意：未绑定线路情况时 加速域名解析不出IP。
        - **Message** (str) - 返回信息
        - **UGAId** (str) - 加速配置ID

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.CreateUGAInstanceRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUGAInstance", d, **kwargs)
        return apis.CreateUGAInstanceResponseSchema().loads(resp)

    def create_upath(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """CreateUPath - 创建UPath

        **Request**

        - **ProjectId** (str) - (Config) 项目ID,如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Bandwidth** (int) - (Required) 线路带宽，最小1Mbps,最大带宽由 DescribePathXLineConfig 接口获得。如需更大带宽，请联系产品团队。
        - **LineId** (str) - (Required) 选择的线路
        - **Name** (str) - (Required) UPath名字
        - **ChargeType** (str) - 计费模式，默认为Month 按月收费,可选范围['Month','Year','Dynamic']
        - **CouponId** (str) - 代金券Id
        - **PostPaid** (bool) - 是否开启后付费, 默认为false
        - **Quantity** (int) - 购买周期，ChargeType为Month时，Quantity默认为0代表购买到月底，按时和按年付费该参数必须大于0

        **Response**

        - **UPathId** (str) - 加速线路实例Id

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.CreateUPathRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUPath", d, **kwargs)
        return apis.CreateUPathResponseSchema().loads(resp)

    def delete_global_ssh_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteGlobalSSHInstance -

        **Request**

        - **ProjectId** (str) - (Config)
        - **InstanceId** (str) - (Required)

        **Response**

        - **Message** (str) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DeleteGlobalSSHInstanceRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("DeleteGlobalSSHInstance", d, **kwargs)
        return apis.DeleteGlobalSSHInstanceResponseSchema().loads(resp)

    def delete_path_xssl(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeletePathXSSL - 删除PathX SSL证书

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **SSLId** (str) - (Required) SSL证书的ID

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DeletePathXSSLRequestSchema().dumps(d)

        resp = self.invoke("DeletePathXSSL", d, **kwargs)
        return apis.DeletePathXSSLResponseSchema().loads(resp)

    def delete_uga_forwarder(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteUGAForwarder - 删除加速实例转发器 按接入端口删除

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **UGAId** (str) - (Required) 加速配置实例ID
        - **HTTPHTTP** (list) - HTTP接入HTTP回源，接入端口。禁用65123端口
        - **HTTPSHTTP** (list) - HTTPS接入HTTP回源， 接入端口。禁用65123端口
        - **HTTPSHTTPS** (list) - HTTPS接入HTTPS回源， 接入端口。禁用65123端口
        - **TCP** (list) - TCP接入端口
        - **UDP** (list) - UDP接入端口

        **Response**

        - **Message** (str) - 返回信息 说明

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DeleteUGAForwarderRequestSchema().dumps(d)

        resp = self.invoke("DeleteUGAForwarder", d, **kwargs)
        return apis.DeleteUGAForwarderResponseSchema().loads(resp)

    def delete_uga_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteUGAInstance - 删除全球加速服务加速配置

        **Request**

        - **ProjectId** (str) - (Config) 项目ID,如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **UGAId** (str) - (Required) 加速配置实例ID

        **Response**

        - **Message** (str) - 消息提示

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DeleteUGAInstanceRequestSchema().dumps(d)

        resp = self.invoke("DeleteUGAInstance", d, **kwargs)
        return apis.DeleteUGAInstanceResponseSchema().loads(resp)

    def delete_upath(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """DeleteUPath - 删除UPath

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **UPathId** (str) - (Required) 加速线路实例ID

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DeleteUPathRequestSchema().dumps(d)

        resp = self.invoke("DeleteUPath", d, **kwargs)
        return apis.DeleteUPathResponseSchema().loads(resp)

    def describe_global_ssh_area(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeGlobalSSHArea -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)

        **Response**

        - **AreaSet** (list) - 见 **GlobalSSHArea** 模型定义
        - **Message** (str) -

        **Response Model**

        **GlobalSSHArea**
        - **Area** (str) -
        - **AreaCode** (str) -
        - **RegionSet** (list) -


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DescribeGlobalSSHAreaRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("DescribeGlobalSSHArea", d, **kwargs)
        return apis.DescribeGlobalSSHAreaResponseSchema().loads(resp)

    def describe_global_ssh_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeGlobalSSHInstance - 获取GlobalSSH实例列表（传实例ID获取单个实例信息，不传获取项目下全部实例）

        **Request**

        - **ProjectId** (str) - (Config) 项目ID，如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **InstanceId** (str) - 实例ID，资源唯一标识

        **Response**

        - **InstanceSet** (list) - 见 **GlobalSSHInfo** 模型定义

        **Response Model**

        **GlobalSSHInfo**
        - **AcceleratingDomain** (str) - GlobalSSH分配的加速域名。
        - **Area** (str) - 被SSH访问的IP所在地区
        - **BandwidthPackage** (int) - globalssh Ultimate带宽包大小
        - **ChargeType** (str) - 支付周期，如Month,Year,Dynamic等
        - **CreateTime** (int) - 资源创建时间戳
        - **Expire** (bool) - 是否过期
        - **ExpireTime** (int) - 资源过期时间戳
        - **ForwardRegion** (str) - InstanceType为Basic版本时，需要展示具体分配的转发机房
        - **GlobalSSHPort** (int) - InstanceType等于Free时，由系统自动分配，不等于源站Port值。InstanceType不等于Free时，与源站Port值相同。
        - **InstanceId** (str) - 实例ID，资源唯一标识
        - **InstanceType** (str) - 枚举值：["Enterprise","Basic","Free","Welfare"], 分别代表企业版，基础版本，免费版本，较早的公测免费版
        - **Port** (int) - 源站服务器监听的SSH端口，windows系统为RDP端口
        - **Remark** (str) - 备注信息
        - **TargetIP** (str) - 被SSH访问的源站 IPv4地址。


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DescribeGlobalSSHInstanceRequestSchema().dumps(d)

        resp = self.invoke("DescribeGlobalSSHInstance", d, **kwargs)
        return apis.DescribeGlobalSSHInstanceResponseSchema().loads(resp)

    def describe_path_x_line_config(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribePathXLineConfig - 获取全球加速线路信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID,如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_

        **Response**

        - **LineSet** (list) - 见 **UGAALine** 模型定义

        **Response Model**

        **LineDetail**
        - **LineFrom** (str) - 线路源
        - **LineFromName** (str) - 线路源中文名称
        - **LineId** (str) - 线路计费Id
        - **LineTo** (str) - 线路目的
        - **LineToName** (str) - 线路目的中文名称


        **UGAALine**
        - **LineDetail** (list) - 见 **LineDetail** 模型定义
        - **LineFrom** (str) - 线路源
        - **LineFromName** (str) - 线路源中文名称
        - **LineId** (str) - 线路计费Id
        - **LineTo** (str) - 线路目的
        - **LineToName** (str) - 线路目的中文名称
        - **MaxBandwidth** (int) - 线路可售最大带宽


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DescribePathXLineConfigRequestSchema().dumps(d)

        resp = self.invoke("DescribePathXLineConfig", d, **kwargs)
        return apis.DescribePathXLineConfigResponseSchema().loads(resp)

    def describe_path_xssl(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribePathXSSL - 获取SSL证书信息,支持分页，支持按证书名称 证书域名模糊搜索

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Limit** (int) - 最大返回条数，默认100，最大400
        - **Offset** (int) - 偏移值 默认为0
        - **SSLId** (str) - SSL证书的Id，不传分页获取证书列表
        - **SearchValue** (str) - 不为空则按证书名称、证书域名模糊搜索 分页返回结果

        **Response**

        - **DataSet** (list) - 见 **PathXSSLSet** 模型定义
        - **TotalCount** (int) - 符合条件的证书总数

        **Response Model**

        **SSLBindedTargetSet**
        - **ResourceId** (str) - SSL证书绑定到的实例ID
        - **ResourceName** (str) - SSL证书绑定到的实例名称


        **PathXSSLSet**
        - **CreateTime** (int) - SSL证书的创建时间 时间戳
        - **ExpireTime** (int) - 证书过期时间 时间戳
        - **SSLBindedTargetSet** (list) - 见 **SSLBindedTargetSet** 模型定义
        - **SSLContent** (str) - SSL证书内容
        - **SSLId** (str) - SSL证书的Id
        - **SSLMD5** (str) - SSL证书（用户证书、私钥、ca证书合并）内容md5值
        - **SSLName** (str) - SSL证书的名字
        - **SourceType** (int) - 证书来源，0：用户上传 1: 免费颁发
        - **SubjectName** (str) - 证书域名


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DescribePathXSSLRequestSchema().dumps(d)

        resp = self.invoke("DescribePathXSSL", d, **kwargs)
        return apis.DescribePathXSSLResponseSchema().loads(resp)

    def describe_uga_instance(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeUGAInstance - 获取全球加速服务加速配置信息，指定实例ID返回单个实例。未指定实例ID时 指定分页参数 则按创建时间降序 返回记录

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Limit** (int) - 返回的最大条数，默认为100，最大值400
        - **Offset** (int) - 偏移量，默认为0
        - **UGAId** (str) - 加速配置实例ID，如果传了实例ID 则返回匹配实例ID的记录；如果没传则返回 ProjectId 下全部实例且符合分页要求

        **Response**

        - **TotalCount** (int) - 符合条件的总数
        - **UGAList** (list) - 见 **UGAAInfo** 模型定义

        **Response Model**

        **UGAL7Forwarder**
        - **Port** (int) - 接入端口
        - **Protocol** (str) - 转发协议，枚举值["TCP"，"UDP"，"HTTPHTTP"，"HTTPSHTTP"，"HTTPSHTTPS"]。TCP和UDP代表四层转发，其余为七层转发
        - **RSPort** (int) - RSPort，源站监听端口
        - **SSLId** (str) - 证书ID
        - **SSLName** (str) - 证书名称


        **UGAATask**
        - **Port** (int) - 接入端口
        - **Protocol** (str) - 转发协议，枚举值["TCP"，"UDP"，"HTTPHTTP"，"HTTPSHTTP"，"HTTPSHTTPS"]。TCP和UDP代表四层转发，其余为七层转发


        **OutPublicIpInfo**
        - **Area** (str) - 线路出口机房代号
        - **IP** (str) - 线路出口EIP


        **UGAL4Forwarder**
        - **Port** (int) - 接入端口
        - **Protocol** (str) - 转发协议，枚举值["TCP"，"UDP"，"HTTPHTTP"，"HTTPSHTTP"，"HTTPSHTTPS"]。TCP和UDP代表四层转发，其余为七层转发
        - **RSPort** (int) - RSPort，源站监听端口


        **UPathSet**
        - **Bandwidth** (int) - 带宽 Mbps, 1~800Mbps
        - **LineFrom** (str) - 线路起点英文代号，加速区域
        - **LineFromName** (str) - 线路起点中文名字，加速区域
        - **LineId** (str) - 线路ID
        - **LineTo** (str) - 线路对端英文代号，源站区域
        - **LineToName** (str) - 线路对端中文名字，源站区域
        - **UPathId** (str) - UPath 实例ID
        - **UPathName** (str) - UPath名字


        **UGAAInfo**
        - **CName** (str) - 加速域名，请在加速区域配置您的业务域名的CName记录值为加速域名
        - **Domain** (str) - 源站域名
        - **IPList** (list) - 源站IP列表，多个值由半角英文逗号相隔
        - **L4ForwarderSet** (list) - 见 **UGAL4Forwarder** 模型定义
        - **L7ForwarderSet** (list) - 见 **UGAL7Forwarder** 模型定义
        - **Location** (str) - 源站所在区域，加速实例在绑定线路后会自动设置该值。console页面上通过该值过滤加速实例可以绑定的upath实例。注意：缺少该值会导致在console上无法修改线路
        - **OutPublicIpList** (list) - 见 **OutPublicIpInfo** 模型定义
        - **TaskSet** (list) - 见 **UGAATask** 模型定义
        - **UGAId** (str) - 加速配置实例ID
        - **UGAName** (str) - 加速配置名称
        - **UPathSet** (list) - 见 **UPathSet** 模型定义


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DescribeUGAInstanceRequestSchema().dumps(d)

        resp = self.invoke("DescribeUGAInstance", d, **kwargs)
        return apis.DescribeUGAInstanceResponseSchema().loads(resp)

    def describe_upath(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeUPath - 获取加速线路信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **UPathId** (str) - 如果不填参数 返回 ProjectId 下所有的线路资源，填此参数则返回upath实例ID匹配的线路

        **Response**

        - **UPathSet** (list) - 见 **UPathInfo** 模型定义

        **Response Model**

        **OutPublicIpInfo**
        - **Area** (str) - 线路出口机房代号
        - **IP** (str) - 线路出口EIP


        **PathXUGAInfo**
        - **Domain** (str) - 源站域名
        - **IPList** (list) - 源站IP列表，多个值由半角英文逗号相隔
        - **UGAId** (str) - 加速配置ID


        **UPathInfo**
        - **Bandwidth** (int) - 带宽，单位Mbps
        - **ChargeType** (str) - 计费模式，默认为Month 按月收费,可选范围['Month','Year','Dynamic']
        - **CreateTime** (int) - UPath创建的时间，10位时间戳
        - **ExpireTime** (int) - UPath的过期时间，10位时间戳
        - **LineFromName** (str) - 线路入口名称
        - **LineId** (str) - 选择的线路
        - **LineToName** (str) - 线路出口名称
        - **Name** (str) - UPath实例名字
        - **OutPublicIpList** (list) - 见 **OutPublicIpInfo** 模型定义
        - **PostPaid** (bool) - 是否为后付费实例
        - **UGAList** (list) - 见 **PathXUGAInfo** 模型定义
        - **UPathId** (str) - UPath加速线路实例ID


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DescribeUPathRequestSchema().dumps(d)

        resp = self.invoke("DescribeUPath", d, **kwargs)
        return apis.DescribeUPathResponseSchema().loads(resp)

    def describe_upath_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DescribeUPathTemplate - 查询UPath的监控模板

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **UPathId** (str) - (Required) 加速线路实例ID,格式 upath-xxxx

        **Response**

        - **DataSet** (list) - 见 **AlarmRuler** 模型定义

        **Response Model**

        **AlarmRuler**
        - **AlarmFrequency** (int) - 告警探测周期，单位秒
        - **AlarmStrategy** (str) - 收敛策略，可选范围 ['Exponential','Continuous','Once']，分别对应指数递增、连续告警、单次告警
        - **AlarmTemplateRuleId** (int) - 告警模板策略ID
        - **Compare** (str) - 比较策略，可选 ['GE','LE']  分别代表不小于和不大于
        - **ContactGroupId** (int) - 联系组ID
        - **MetricName** (str) - 告警指标名称, 所有n的个数必须一致。目前仅允许以下四项：UpathNetworkOut:出向带宽，UpathNetworkIn:入向带宽，UpathNetworkOutUsage:出向带宽使用率，UpathNetworkInUsage:入向带宽使用率
        - **ResourceType** (str) - 资源类型
        - **Threshold** (int) - 告警阈值，带宽使用率的阈值范围是[50,100]的正整数，带宽告警阈值为1000000的倍数, 如大于2Mbps则告警 阈值应该传 2000000
        - **TriggerCount** (int) - 告警触发周期（次数）


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.DescribeUPathTemplateRequestSchema().dumps(d)

        resp = self.invoke("DescribeUPathTemplate", d, **kwargs)
        return apis.DescribeUPathTemplateResponseSchema().loads(resp)

    def get_global_ssh_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetGlobalSSHPrice - 获取GlobalSSH价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID,如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **ChargeType** (str) - 计费类型：Dynamic，Month，Year
        - **InstanceType** (str) - 版本类型。枚举值，Enterprise:企业版；Basic:基础版。可不填，默认为Basic。
        - **Quantity** (int) - 购买周期，如果ChargeType为Month，Quantity默认为0；其他情况必须为大于0的整数

        **Response**

        - **Price** (float) - 价格,返回单位为元

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.GetGlobalSSHPriceRequestSchema().dumps(d)

        resp = self.invoke("GetGlobalSSHPrice", d, **kwargs)
        return apis.GetGlobalSSHPriceResponseSchema().loads(resp)

    def get_global_ssh_update_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetGlobalSSHUpdatePrice - 获取GlobalSSH升级价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID,如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **InstanceType** (str) - (Required) 升级后的实例类型。枚举值，Enterprise:企业版；Basic:基础版。
        - **ChargeType** (str) - 计费类型：Dynamic，Month，Year。从免费版升级到付费版必须传，其他情况不需要传
        - **InstanceId** (str) - 实例ID，唯一资源标识。从免费版升级到付费版可不填，其他情况必填。
        - **Quantity** (int) - 购买周期，如果ChargeType为Month，Quantity可以不填默认为0；其他情况必须为正整数。

        **Response**

        - **Price** (float) - 价格,返回单位为元。正数表示付费升级，负数表示降级退费。

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.GetGlobalSSHUpdatePriceRequestSchema().dumps(d)

        resp = self.invoke("GetGlobalSSHUpdatePrice", d, **kwargs)
        return apis.GetGlobalSSHUpdatePriceResponseSchema().loads(resp)

    def get_path_x_metric(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetPathXMetric - 获取全球加速监控信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list>`_
        - **BeginTime** (int) - (Required) 查询起始时间，10位长度时间戳
        - **EndTime** (int) - (Required) 查询结束时间，10位长度时间戳
        - **LineId** (str) - (Required) 具体线路id，调用DescribePathXLineConfig接口获取线路列表
        - **MetricName** (list) - (Required) 查询监控的指标项。目前仅允许以下四项：NetworkOut:出向带宽，NetworkIn:入向带宽，NetworkOutUsage:出向带宽使用率，NetworkInUsage:入向带宽使用率
        - **ResourceId** (str) - (Required) ResourceId，如upath ID  和 uga ID
        - **ResourceType** (str) - (Required) upath:加速线路,uga:加速实例

        **Response**

        - **DataSet** (dict) - 见 **MetricPeriod** 模型定义

        **Response Model**

        **MatricPoint**
        - **Timestamp** (int) - 时间戳
        - **Value** (int) - 监控点数值


        **MetricPeriod**
        - **NetworkIn** (list) - 见 **MatricPoint** 模型定义
        - **NetworkInUsage** (list) - 见 **MatricPoint** 模型定义
        - **NetworkOut** (list) - 见 **MatricPoint** 模型定义
        - **NetworkOutUsage** (list) - 见 **MatricPoint** 模型定义


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.GetPathXMetricRequestSchema().dumps(d)

        resp = self.invoke("GetPathXMetric", d, **kwargs)
        return apis.GetPathXMetricResponseSchema().loads(resp)

    def modify_global_ssh_port(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyGlobalSSHPort -

        **Request**

        - **ProjectId** (str) - (Config)
        - **InstanceId** (str) - (Required)
        - **Port** (int) - (Required)

        **Response**

        - **Message** (str) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.ModifyGlobalSSHPortRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("ModifyGlobalSSHPort", d, **kwargs)
        return apis.ModifyGlobalSSHPortResponseSchema().loads(resp)

    def modify_global_ssh_remark(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyGlobalSSHRemark -

        **Request**

        - **ProjectId** (str) - (Config)
        - **InstanceId** (str) - (Required)
        - **Remark** (str) -

        **Response**

        - **Message** (str) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.ModifyGlobalSSHRemarkRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("ModifyGlobalSSHRemark", d, **kwargs)
        return apis.ModifyGlobalSSHRemarkResponseSchema().loads(resp)

    def modify_global_ssh_type(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyGlobalSSHType - 修改GlobalSSH实例类型，仅支持低版本升级到高版本，不支持高版本降级到低版本

        **Request**

        - **ProjectId** (str) - (Config) 项目ID，如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **InstanceId** (str) - (Required) 实例ID,资源唯一标识
        - **InstanceType** (str) - (Required) 取值范围["Enterprise","Basic"]，分别对应企业版和基础版，表示升级后的实例类型。比如从Free版本升级为Basic版或Enterprise版，不可从收费版降级为免费版，或从企业版降级为基础版
        - **ChargeType** (str) - 支付方式，如按月、按年、按时
        - **CouponId** (str) - 可抵扣费用的券，通常不使用
        - **Quantity** (str) - 购买时间，当ChargeType为Month，Quantity为0代表购买到月底

        **Response**

        - **Message** (str) - 提示信息

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.ModifyGlobalSSHTypeRequestSchema().dumps(d)

        resp = self.invoke("ModifyGlobalSSHType", d, **kwargs)
        return apis.ModifyGlobalSSHTypeResponseSchema().loads(resp)

    def modify_upath_bandwidth(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyUPathBandwidth - 修改加速线路带宽

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Bandwidth** (int) - (Required) 线路带宽，单位Mbps。最小1Mbps,最大带宽由 DescribePathXLineConfig 接口获得。如需更大带宽，请联系产品团队。
        - **UPathId** (str) - (Required) UPath 加速线路实例Id

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.ModifyUPathBandwidthRequestSchema().dumps(d)

        resp = self.invoke("ModifyUPathBandwidth", d, **kwargs)
        return apis.ModifyUPathBandwidthResponseSchema().loads(resp)

    def modify_upath_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyUPathTemplate - 修改UPath监控告警项

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **UPathId** (str) - (Required) 加速线路实例ID
        - **AlarmFrequency** (list) - 告警探测周期，单位：秒
        - **AlarmStrategy** (list) - 收敛策略，可选范围 ['Exponential','Continuous','Once']，分别对应指数递增、连续告警、单次告警
        - **Compare** (list) - 比较策略，可选 ['GE','LE']  分别代表不小于和不大于
        - **ContactGroupId** (list) - 告警组id
        - **MetricName** (list) - 告警指标名称, 所有n的个数必须一致。目前仅允许以下四项：UpathNetworkOut:出向带宽，UpathNetworkIn:入向带宽，UpathNetworkOutUsage:出向带宽使用率，UpathNetworkInUsage:入向带宽使用率
        - **Threshold** (list) - 告警阈值，带宽使用率的阈值范围是[50,100]的正整数，带宽告警阈值为1000000的倍数, 如大于2Mbps则告警 阈值应该传 2000000
        - **TriggerCount** (list) - 告警触发周期（次数）

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.ModifyUPathTemplateRequestSchema().dumps(d)

        resp = self.invoke("ModifyUPathTemplate", d, **kwargs)
        return apis.ModifyUPathTemplateResponseSchema().loads(resp)

    def uga_bind_upath(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UGABindUPath - UGA绑定UPath

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **UGAId** (str) - (Required) 加速配置实例ID，格式uga-xxxx
        - **UPathId** (str) - (Required) 加速线路实例ID，格式upath-xxx
        - **CouponId** (str) - 代金券

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.UGABindUPathRequestSchema().dumps(d)

        resp = self.invoke("UGABindUPath", d, **kwargs)
        return apis.UGABindUPathResponseSchema().loads(resp)

    def uga_un_bind_upath(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UGAUnBindUPath - UGA与UPath解绑

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **UGAId** (str) - (Required) 加速配置实例ID 格式uga-xxx
        - **UPathId** (str) - (Required) 加速线路实例ID 格式upath-xxx

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.UGAUnBindUPathRequestSchema().dumps(d)

        resp = self.invoke("UGAUnBindUPath", d, **kwargs)
        return apis.UGAUnBindUPathResponseSchema().loads(resp)

    def un_bind_path_xssl(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UnBindPathXSSL - 解绑PathX SSL 证书

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Port** (list) - (Required) 解绑SSL证书的HTTPS端口。Port.0 Port.1格式 端口错误则解绑失败。
        - **SSLId** (str) - (Required) SSL证书ID。
        - **UGAId** (str) - (Required) UGA实例ID。

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
        }
        req and d.update(req)
        d = apis.UnBindPathXSSLRequestSchema().dumps(d)

        resp = self.invoke("UnBindPathXSSL", d, **kwargs)
        return apis.UnBindPathXSSLResponseSchema().loads(resp)
