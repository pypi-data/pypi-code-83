from pyamis.base.base import PyAmisComponent


class Action(PyAmisComponent):
    """
    :param type: 指定为 Page 渲染器。
    :param actionType: 【必填】这是 action 最核心的配置，来指定该 action 的作用类型，支持：ajax、link、url、drawer、dialog、confirm、cancel、prev、next、copy、close。
    :param label: 按钮文本。可用 ${xxx} 取值。
    :param level: 按钮样式，支持：link、primary、secondary、info、success、warning、danger、light、dark、default。
    :param size: 按钮大小，支持：xs、sm、md、lg。
    :param icon: 设置图标，例如fa fa-plus。
    :param iconClassName: 给图标上添加类名。
    :param active: 按钮是否高亮。
    :param activeLevel: 按钮高亮时的样式，配置支持同level。
    :param activeClassName: 给按钮高亮添加类名。
    :param block: 用display:"block"来显示按钮。
    :param confirmText: 当设置后，操作在开始前会询问用户。可用 ${xxx} 取值。
    :param reload: 指定此次操作完后，需要刷新的目标组件名字（组件的name值，自己配置的），多个请用 , 号隔开。
    :param tooltip: 鼠标停留时弹出该段文字，也可以配置对象类型：字段为title和content。可用 ${xxx} 取值。
    :param disabledTip: 被禁用后鼠标停留时弹出该段文字，也可以配置对象类型：字段为title和content。可用 ${xxx} 取值。
    :param tooltipPlacement: 如果配置了tooltip或者disabledTip，指定提示信息位置，可配置top、bottom、left、right。
    :param close: 当action配置在dialog或drawer的actions中时，配置为true指定此次操作完后关闭当前dialog或drawer。当值为字符串，并且是祖先层弹框的名字的时候，会把祖先弹框关闭掉。
    :param required: 配置字符串数组，指定在form中进行操作之前，需要指定的字段名的表单项通过验证
    """
    def __init__(self,
                 type: str = "action",
                 actionType: str = None,
                 label: str = None,
                 level: str = None,
                 size: str = None,
                 icon: str = None,
                 iconClassName: str = None,
                 active: bool = None,
                 activeLevel: str = None,
                 activeClassName: str = None,
                 block: bool = None,
                 confirmText: any = None,
                 reload: str = None,
                 tooltip: str = None,
                 disabledTip: str = None,
                 tooltipPlacement: str = None,
                 close: any = None,
                 required: any = None,
                 ):
        super().__init__(type = type,actionType = actionType,label = label,level = level,size = size,icon = icon,iconClassName = iconClassName,active = active,activeLevel = activeLevel,activeClassName = activeClassName,block = block,confirmText = confirmText,reload = reload,tooltip = tooltip,disabledTip = disabledTip,tooltipPlacement = tooltipPlacement,close = close,required = required)


action = Action(actionType='bbb')
action['aaa'] = 'bbb'
action['acc'] = Action(required=1)
# print(action.to_json())
import json

print(json.dumps(action))
