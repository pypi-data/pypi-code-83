
from dataclasses import dataclass
from pyamis.base import PyAmisComponent,Api
from typing import Union


class Page(PyAmisComponent):
    """
    :param type: 指定为 Page 组件
    :param title: 页面标题
    :param subTitle: 页面副标题
    :param remark: 标题附近会出现一个提示图标，鼠标放上去会提示该内容。
    :param aside: 往页面的边栏区域加内容
    :param toolbar: 往页面的右上角加内容，需要注意的是，当有 title 时，该区域在右上角，没有时该区域在顶部
    :param body: 往页面的内容区域加内容
    :param className: 外层 dom 类名
    :param cssVars: 自定义 CSS 变量，请参考样式
    :param toolbarClassName: Toolbar dom 类名
    :param bodyClassName: Body dom 类名
    :param asideClassName: Aside dom 类名
    :param headerClassName: Header 区域 dom 类名
    :param initApi: Page 用来获取初始数据的 api。返回的数据可以整个 page 级别使用。
    :param initFetch: 是否起始拉取 initApi
    :param initFetchOn: 是否起始拉取 initApi, 通过表达式配置
    :param interval: 刷新时间(最小 1000)
    :param silentPolling: 配置刷新时是否显示加载动画
    :param stopAutoRefreshWhen: 通过表达式来配置停止刷新的条件
    """
    def __init__(self,
                 type: str = "page",
                 title: any = None,
                 subTitle: any = None,
                 remark: any = None,
                 aside: any = None,
                 toolbar: any = None,
                 body: any = None,
                 className: str = None,
                 cssVars: any = None,
                 toolbarClassName: str = None,
                 bodyClassName: str = None,
                 asideClassName: str = None,
                 headerClassName: str = None,
                 initApi: any = None,
                 initFetch: bool = None,
                 initFetchOn: any = None,
                 interval: int = None,
                 silentPolling: bool = None,
                 stopAutoRefreshWhen: any = None,
                 **kwargs):
        super().__init__(type = type,title = title,subTitle = subTitle,remark = remark,aside = aside,toolbar = toolbar,body = body,className = className,cssVars = cssVars,toolbarClassName = toolbarClassName,bodyClassName = bodyClassName,asideClassName = asideClassName,headerClassName = headerClassName,initApi = initApi,initFetch = initFetch,initFetchOn = initFetchOn,interval = interval,silentPolling = silentPolling,stopAutoRefreshWhen = stopAutoRefreshWhen,**kwargs)

