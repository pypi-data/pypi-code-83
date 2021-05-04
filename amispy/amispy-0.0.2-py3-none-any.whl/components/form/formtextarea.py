
from dataclasses import dataclass
from amispy.base import PyAmisComponent,Api
from typing import Union
from .formitem import Formitem

class FormTextarea(Formitem):

    def __init__(self,
                 minRows: int = None,
                 maxRows: int = None,
                 trimContents: bool = None,
                 readOnly: bool = None,
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/form/textarea.md
        :param minRows: 最小行数
        :param maxRows: 最大行数
        :param trimContents: 是否去除首尾空白文本
        :param readOnly: 是否只读
        """
        super(FormTextarea,self).__init__(minRows = minRows,maxRows = maxRows,trimContents = trimContents,readOnly = readOnly,type = "textarea",**kwargs)
    