
from dataclasses import dataclass
from amispy.base import PyAmisComponent,Api
from typing import Union
from .formitem import Formitem

class FormLocation(Formitem):

    def __init__(self,
                 vendor: any = None,
                 ak: str = None,
                 clearable: bool = None,
                 placeholder: str = None,
                 coordinatesType: str = None,
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/form/location.md
        :param vendor: 地图厂商，目前只实现了百度地图
        :param ak: 百度地图的 ak
        :param clearable: 输入框是否可清空
        :param placeholder: 默认提示
        :param coordinatesType: 默为百度坐标，可设置为'gcj02'
        """
        super(FormLocation,self).__init__(vendor = vendor,ak = ak,clearable = clearable,placeholder = placeholder,coordinatesType = coordinatesType,type = "location",**kwargs)
    