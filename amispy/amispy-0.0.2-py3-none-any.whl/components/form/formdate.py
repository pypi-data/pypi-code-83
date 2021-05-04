
from dataclasses import dataclass
from amispy.base import PyAmisComponent,Api
from typing import Union
from .formitem import Formitem

class FormDate(Formitem):

    def __init__(self,
                 value: str = None,
                 format: str = None,
                 inputFormat: str = None,
                 closeOnSelect: bool = None,
                 placeholder: str = None,
                 shortcuts: str = None,
                 minDate: str = None,
                 maxDate: str = None,
                 utc: bool = None,
                 clearable: bool = None,
                 embed: bool = None,
                 timeConstraints: any = None,
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/form/date.md
        :param value: 默认值
        :param format: 日期选择器值格式，更多格式类型请参考 文档
        :param inputFormat: 日期选择器显示格式，即时间戳格式，更多格式类型请参考 文档
        :param closeOnSelect: 点选日期后，是否马上关闭选择框
        :param placeholder: 占位文本
        :param shortcuts: 日期快捷键
        :param minDate: 限制最小日期
        :param maxDate: 限制最大日期
        :param utc: 保存 utc 值
        :param clearable: 是否可清除
        :param embed: 是否内联模式
        :param timeConstraints: 请参考： react-datetime
        """
        super(FormDate,self).__init__(value = value,format = format,inputFormat = inputFormat,closeOnSelect = closeOnSelect,placeholder = placeholder,shortcuts = shortcuts,minDate = minDate,maxDate = maxDate,utc = utc,clearable = clearable,embed = embed,timeConstraints = timeConstraints,type = "date",**kwargs)
    