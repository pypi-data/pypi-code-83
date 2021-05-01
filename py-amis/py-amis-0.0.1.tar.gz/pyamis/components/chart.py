
from dataclasses import dataclass
from pyamis.base import PyAmisComponent,Api
from typing import Union


class Chart(PyAmisComponent):
    """
    :param type: 指定为 chart 渲染器
    :param className: 外层 Dom 的类名
    :param body: 内容容器
    :param api: 配置项接口地址
    :param source: 通过数据映射获取数据链中变量值作为配置
    :param initFetch: 组件初始化时，是否请求接口
    :param interval: 刷新时间(最小 1000)
    :param config: 设置 eschars 的配置项,当为string的时候可以设置 function 等配置项
    :param style: 设置根元素的 style
    :param width: 设置根元素的宽度
    :param height: 设置根元素的高度
    :param replaceChartOption: 每次更新是完全覆盖配置项还是追加？
    :param trackExpression: 当这个表达式的值有变化时更新图表
    """
    def __init__(self,
                 type: str = "chart",
                 className: str = None,
                 body: any = None,
                 api: Union[Api,str]= None,
                 source: any = None,
                 initFetch: bool = None,
                 interval: int = None,
                 config: any = None,
                 style: any = None,
                 width: str = None,
                 height: str = None,
                 replaceChartOption: bool = None,
                 trackExpression: str = None,):
        super().__init__(type = type,className = className,body = body,api = api,source = source,initFetch = initFetch,interval = interval,config = config,style = style,width = width,height = height,replaceChartOption = replaceChartOption,trackExpression = trackExpression)
    