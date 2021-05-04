
from typing import Union
from amispy.base import Api,PyAmisComponent
from .formitem import Formitem


class FormSelect(Formitem):
    def __init__(self,
                 options: any = None,
                 source: any = None,
                 autoComplete: any = None,
                 delimeter: str = None,
                 labelField: str = None,
                 valueField: str = None,
                 joinValues: bool = None,
                 extractValue: bool = None,
                 checkAll: bool = None,
                 checkAllLabel: str = None,
                 defaultCheckAll: bool = None,
                 creatable: bool = None,
                 multiple: bool = None,
                 searchable: bool = None,
                 createBtnLabel: str = None,
                 addControls: any = None,
                 addApi: any = None,
                 editable: bool = None,
                 editControls: any = None,
                 editApi: any = None,
                 removable: bool = None,
                 deleteApi: any = None,
                 autoFill: any = None,
                 menuTpl: str = None,
                 
                 **kwargs):
        """
        https://github.com/baidu/amis/blob/master/docs/zh-CN/components/form/select.md
        :param options: 选项组
        :param source: 动态选项组
        :param autoComplete: 自动提示补全
        :param delimeter: 拼接符
        :param labelField: 选项标签字段
        :param valueField: 选项值字段
        :param joinValues: 拼接值
        :param extractValue: 提取值
        :param checkAll: 是否支持全选
        :param checkAllLabel: 全选的文字
        :param defaultCheckAll: 默认是否全选
        :param creatable: 新增选项
        :param multiple: 多选
        :param searchable: 检索
        :param createBtnLabel: 新增选项
        :param addControls: 自定义新增表单项
        :param addApi: 配置新增选项接口
        :param editable: 编辑选项
        :param editControls: 自定义编辑表单项
        :param editApi: 配置编辑选项接口
        :param removable: 删除选项
        :param deleteApi: 配置删除选项接口
        :param autoFill: 自动填充
        :param menuTpl: 支持配置自定义菜单
        """
        super(FormSelect,self).__init__(options = options,source = source,autoComplete = autoComplete,delimeter = delimeter,labelField = labelField,valueField = valueField,joinValues = joinValues,extractValue = extractValue,checkAll = checkAll,checkAllLabel = checkAllLabel,defaultCheckAll = defaultCheckAll,creatable = creatable,multiple = multiple,searchable = searchable,createBtnLabel = createBtnLabel,addControls = addControls,addApi = addApi,editable = editable,editControls = editControls,editApi = editApi,removable = removable,deleteApi = deleteApi,autoFill = autoFill,menuTpl = menuTpl,type="select",**kwargs)
