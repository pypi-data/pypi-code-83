
from typing import Union
from amispy.base import Api,PyAmisComponent
from .formitem import Formitem


class FormRadios(Formitem):
    def __init__(self,
                 options: any = None,
                 source: any = None,
                 labelField: bool = None,
                 valueField: bool = None,
                 columnsCount: int = None,
                 inline: bool = None,
                 autoFill: any = None,
                 
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/form/radios.md
        :param options: 选项组
        :param source: 动态选项组
        :param labelField: 选项标签字段
        :param valueField: 选项值字段
        :param columnsCount: 选项按几列显示，默认为一列
        :param inline: 是否显示为一行
        :param autoFill: 自动填充
        """
        super(FormRadios,self).__init__(options = options,source = source,labelField = labelField,valueField = valueField,columnsCount = columnsCount,inline = inline,autoFill = autoFill,type="radios",**kwargs)
