
from typing import Union
from amispy.base import Api,PyAmisComponent
from .formitem import Formitem


class FormArray(Formitem):
    def __init__(self,
                 items: any = None,
                 addable: bool = None,
                 removable: bool = None,
                 draggable: bool = None,
                 draggableTip: str = None,
                 addButtonText: str = None,
                 minLength: int = None,
                 maxLength: int = None,
                 
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/form/array.md
        :param type: 指明为array组件
        :param items: 配置单项表单类型
        :param addable: 是否可新增。
        :param removable: 是否可删除
        :param draggable: 是否可以拖动排序, 需要注意的是当启用拖动排序的时候，会多一个$id 字段
        :param draggableTip: 可拖拽的提示文字，默认为："可通过拖动每行中的【交换】按钮进行顺序调整"
        :param addButtonText: 新增按钮文字
        :param minLength: 限制最小长度
        :param maxLength: 限制最大长度
        """
        super(FormArray,self).__init__(items = items,addable = addable,removable = removable,draggable = draggable,draggableTip = draggableTip,addButtonText = addButtonText,minLength = minLength,maxLength = maxLength,type="array",**kwargs)
