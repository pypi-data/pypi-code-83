
from dataclasses import dataclass
from amispy.base import PyAmisComponent,Api
from typing import Union
from .formitem import Formitem

class FormDateRange(Formitem):
    def __init__(self,
                 format: str = None,
                 inputFormat: str = None,
                 placeholder: str = None,
                 ranges: any = None,
                 minDate: str = None,
                 maxDate: str = None,
                 minDuration: str = None,
                 maxDuration: str = None,
                 utc: bool = None,
                 clearable: bool = None,
                 embed: bool = None,
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/form/date-range.md
        :param format: 日期选择器值格式
        :param inputFormat: 日期选择器显示格式
        :param placeholder: 占位文本
        :param ranges: 日期范围快捷键，可选：today, yesterday, 1dayago, 7daysago, 30daysago, 90daysago, prevweek, thismonth, thisquarter, prevmonth, prevquarter
        :param minDate: 限制最小日期，用法同 限制范围
        :param maxDate: 限制最大日期，用法同 限制范围
        :param minDuration: 限制最小跨度，如： 2days
        :param maxDuration: 限制最大跨度，如：1year
        :param utc: 保存 UTC 值
        :param clearable: 是否可清除
        :param embed: 是否内联模式
        """
        super(FormDateRange,self).__init__(format = format,inputFormat = inputFormat,placeholder = placeholder,ranges = ranges,minDate = minDate,maxDate = maxDate,minDuration = minDuration,maxDuration = maxDuration,utc = utc,clearable = clearable,embed = embed,type = "date-range",**kwargs)
    