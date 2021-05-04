
from dataclasses import dataclass
from amispy.base import PyAmisComponent,Api
from typing import Union
from .formitem import Formitem

class FormDatetimeRange(Formitem):

    def __init__(self,
                 format: str = None,
                 inputFormat: str = None,
                 placeholder: str = None,
                 ranges: any = None,
                 minDate: str = None,
                 maxDate: str = None,
                 utc: bool = None,
                 clearable: bool = None,
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/form/datetime-range.md
        :param format: 日期时间选择器值格式
        :param inputFormat: 日期时间选择器显示格式
        :param placeholder: 占位文本
        :param ranges: 日期范围快捷键，可选：today, yesterday, 1dayago, 7daysago, 30daysago, 90daysago, prevweek, thismonth, thisquarter, prevmonth, prevquarter
        :param minDate: 限制最小日期时间，用法同 限制范围
        :param maxDate: 限制最大日期时间，用法同 限制范围
        :param utc: 保存 UTC 值
        :param clearable: 是否可清除
        """
        super(FormDatetimeRange,self).__init__(format = format,inputFormat = inputFormat,placeholder = placeholder,ranges = ranges,minDate = minDate,maxDate = maxDate,utc = utc,clearable = clearable,type = "datetime-range",**kwargs)
    