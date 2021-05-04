
from dataclasses import dataclass
from amispy.base import PyAmisComponent,Api
from typing import Union


class Service(PyAmisComponent):

    def __init__(self,
                 type: str = "service",
                 className: str = None,
                 body: any = None,
                 api: Api = None,
                 ws: str = None,
                 initFetch: bool = None,
                 schemaApi: Api = None,
                 initFetchSchema: bool = None,
                 messages: any = None,
                 interval: int = None,
                 silentPolling: bool = None,
                 stopAutoRefreshWhen: any = None,
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/service.md
        :param type: 指定为 service 渲染器
        :param className: 外层 Dom 的类名
        :param body: 内容容器
        :param api: 初始化数据域接口地址
        :param ws: WebScocket 地址
        :param initFetch: 是否默认拉取
        :param schemaApi: 用来获取远程 Schema 接口地址
        :param initFetchSchema: 是否默认拉取 Schema
        :param messages: 消息提示覆写，默认消息读取的是接口返回的 toast 提示文字，但是在此可以覆写它。
        :param interval: 轮询时间间隔(最低 3000)
        :param silentPolling: 配置轮询时是否显示加载动画
        :param stopAutoRefreshWhen: 配置停止轮询的条件
        """
        super(Service,self).__init__(type = type,className = className,body = body,api = api,ws = ws,initFetch = initFetch,schemaApi = schemaApi,initFetchSchema = initFetchSchema,messages = messages,interval = interval,silentPolling = silentPolling,stopAutoRefreshWhen = stopAutoRefreshWhen,**kwargs)
    