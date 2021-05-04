
from dataclasses import dataclass
from amispy.base import PyAmisComponent,Api
from typing import Union
from .formitem import Formitem

class FormMonth(Formitem):

    def __init__(self,
                 value: str = None,
                 format: str = None,
                 inputFormat: str = None,
                 placeholder: str = None,
                 clearable: bool = None,
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/form/month.md
        :param value: 默认值
        :param format: 月份选择器值格式，更多格式类型请参考 moment
        :param inputFormat: 月份选择器显示格式，即时间戳格式，更多格式类型请参考 moment
        :param placeholder: 占位文本
        :param clearable: 是否可清除
        """
        super(FormMonth,self).__init__(value = value,format = format,inputFormat = inputFormat,placeholder = placeholder,clearable = clearable,type = "month",**kwargs)
    