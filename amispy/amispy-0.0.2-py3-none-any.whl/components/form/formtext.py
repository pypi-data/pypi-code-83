
from .formitem import Formitem

class FormText(Formitem):
    def __init__(self,
                 options: any = None,
                 source: any = None,
                 autoComplete: any = None,
                 multiple: bool = None,
                 delimeter: str = None,
                 labelField: str = None,
                 valueField: str = None,
                 joinValues: bool = None,
                 extractValue: bool = None,
                 addOn: any = None,
                 trimContents: bool = None,
                 clearable: bool = None,
                 resetValue: str = None,
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/form/text.md
        :param options: 选项组
        :param source: 动态选项组
        :param autoComplete: 自动补全
        :param multiple: 是否多选
        :param delimeter: 拼接符
        :param labelField: 选项标签字段
        :param valueField: 选项值字段
        :param joinValues: 拼接值
        :param extractValue: 提取值
        :param addOn: 输入框附加组件，比如附带一个提示文字，或者附带一个提交按钮。
        :param trimContents: 是否去除首尾空白文本。
        :param clearable: 是否可清除
        :param resetValue: 清除后设置此配置项给定的值。
        """

        super(FormText,self).__init__(options = options,source = source,autoComplete = autoComplete,multiple = multiple,delimeter = delimeter,labelField = labelField,valueField = valueField,joinValues = joinValues,extractValue = extractValue,addOn = addOn,trimContents = trimContents,clearable = clearable,resetValue = resetValue,type = "text",**kwargs)
    