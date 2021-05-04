
from dataclasses import dataclass
from amispy.base import PyAmisComponent,Api
from typing import Union


class Formitem(PyAmisComponent):

    def __init__(self,
                 type: str = None,
                 className: str = None,
                 inputClassName: str = None,
                 labelClassName: str = None,
                 name: str = None,
                 label: any = None,
                 labelRemark: any = None,
                 description: any = None,
                 placeholder: str = None,
                 inline: bool = None,
                 submitOnChange: bool = None,
                 disabled: bool = None,
                 disabledOn: any = None,
                 visible: any = None,
                 visibleOn: any = None,
                 required: bool = None,
                 requiredOn: any = None,
                 validations: any = None,
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/form/formitem.md
        :param type: 指定表单项类型
        :param className: 表单最外层类名
        :param inputClassName: 表单控制器类名
        :param labelClassName: label 的类名
        :param name: 字段名，指定该表单项提交时的 key
        :param label: 表单项标签
        :param labelRemark: 表单项标签描述
        :param description: 表单项描述
        :param placeholder: 表单项描述
        :param inline: 是否为 内联 模式
        :param submitOnChange: 是否该表单项值发生变化时就提交当前表单。
        :param disabled: 当前表单项是否是禁用状态
        :param disabledOn: 当前表单项是否禁用的条件
        :param visible: 当前表单项是否禁用的条件
        :param visibleOn: 当前表单项是否禁用的条件
        :param required: 是否为必填。
        :param requiredOn: 过表达式来配置当前表单项是否为必填。
        :param validations: 表单项值格式验证，支持设置多个，多个规则用英文逗号隔开。
        """
        super().__init__(type = type,className = className,inputClassName = inputClassName,labelClassName = labelClassName,name = name,label = label,labelRemark = labelRemark,description = description,placeholder = placeholder,inline = inline,submitOnChange = submitOnChange,disabled = disabled,disabledOn = disabledOn,visible = visible,visibleOn = visibleOn,required = required,requiredOn = requiredOn,validations = validations,**kwargs)
