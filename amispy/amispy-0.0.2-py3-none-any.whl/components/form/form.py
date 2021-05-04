
from dataclasses import dataclass
from amispy.base import PyAmisComponent,Api
from typing import Union


class Form(PyAmisComponent):
    def __init__(self,
                 type: str = "form",
                 name: str = None,
                 mode: str = None,
                 horizontal: any = None,
                 title: str = None,
                 submitText: any = None,
                 className: str = None,
                 controls: any = None,
                 actions: any = None,
                 messages: any = None,
                 wrapWithPanel: bool = None,
                 panelClassName: str = None,
                 api: any = None,
                 initApi: any = None,
                 rules: any = None,
                 interval: int = None,
                 silentPolling: bool = None,
                 stopAutoRefreshWhen: str = None,
                 initAsyncApi: any = None,
                 initFetch: bool = None,
                 initFetchOn: str = None,
                 initFinishedField: str = None,
                 initCheckInterval: int = None,
                 asyncApi: any = None,
                 checkInterval: int = None,
                 finishedField: str = None,
                 submitOnChange: bool = None,
                 submitOnInit: bool = None,
                 resetAfterSubmit: bool = None,
                 primaryField: str = None,
                 target: str = None,
                 redirect: str = None,
                 reload: str = None,
                 autoFocus: bool = None,
                 canAccessSuperData: bool = None,
                 persistData: str = None,
                 clearPersistDataAfterSubmit: bool = None,
                 preventEnterSubmit: bool = None,
                 trimValues: bool = None,
                 promptPageLeave: bool = None,
                 **kwargs):
        """
        :param type: "form" 指定为 Form 渲染器
        :param name: 设置一个名字后，方便其他组件与其通信
        :param mode: 表单展示方式，可以是：normal、horizontal 或者 inline
        :param horizontal: 当 mode 为 horizontal 时有用，用来控制 label
        :param title: Form 的标题
        :param submitText: 默认的提交按钮名称，如果设置成空，则可以把默认按钮去掉。
        :param className: 外层 Dom 的类名
        :param controls: Form 表单项集合
        :param actions: Form 提交按钮，成员为 Action
        :param messages: 消息提示覆写，默认消息读取的是 API 返回的消息，但是在此可以覆写它。
        :param wrapWithPanel: 是否让 Form 用 panel 包起来，设置为 false 后，actions 将无效。
        :param panelClassName: 外层 panel 的类名
        :param api: Form 用来保存数据的 api。
        :param initApi: Form 用来获取初始数据的 api。
        :param rules: 表单组合校验规则
        :param interval: 刷新时间(最低 3000)
        :param silentPolling: 配置刷新时是否显示加载动画
        :param stopAutoRefreshWhen: 通过表达式 来配置停止刷新的条件
        :param initAsyncApi: Form 用来获取初始数据的 api,与 initApi 不同的是，会一直轮询请求该接口，直到返回 finished 属性为 true 才 结束。
        :param initFetch: 设置了 initApi 或者 initAsyncApi 后，默认会开始就发请求，设置为 false 后就不会起始就请求接口
        :param initFetchOn: 用表达式来配置
        :param initFinishedField: 设置了 initAsyncApi 后，默认会从返回数据的 data.finished 来判断是否完成，也可以设置成其他的 xxx，就会从 data.xxx 中获取
        :param initCheckInterval: 设置了 initAsyncApi 以后，默认拉取的时间间隔
        :param asyncApi: 设置此属性后，表单提交发送保存接口后，还会继续轮询请求该接口，直到返回 finished 属性为 true 才 结束。
        :param checkInterval: 轮询请求的时间间隔，默认为 3 秒。设置 asyncApi 才有效
        :param finishedField: 如果决定结束的字段名不是 finished 请设置此属性，比如 is_success
        :param submitOnChange: 表单修改即提交
        :param submitOnInit: 初始就提交一次
        :param resetAfterSubmit: 提交后是否重置表单
        :param primaryField: 设置主键 id, 当设置后，检测表单是否完成时（asyncApi），只会携带此数据。
        :param target: 默认表单提交自己会通过发送 api 保存数据，但是也可以设定另外一个 form 的 name 值，或者另外一个 CRUD 模型的 name 值。 如果 target 目标是一个 Form ，则目标 Form 会重新触发 initApi，api 可以拿到当前 form 数据。如果目标是一个 CRUD 模型，则目标模型会重新触发搜索，参数为当前 Form 数据。当目标是 window 时，会把当前表单的数据附带到页面地址上。
        :param redirect: 设置此属性后，Form 保存成功后，自动跳转到指定页面。支持相对地址，和绝对地址（相对于组内的）。
        :param reload: 操作完后刷新目标对象。请填写目标组件设置的 name 值，如果填写为 window 则让当前页面整体刷新。
        :param autoFocus: 是否自动聚焦。
        :param canAccessSuperData: 指定是否可以自动获取上层的数据并映射到表单项上
        :param persistData: 指定一个唯一的 key，来配置当前表单是否开启本地缓存
        :param clearPersistDataAfterSubmit: 指定表单提交成功后是否清除本地缓存
        :param preventEnterSubmit: 禁用回车提交表单
        :param trimValues: trim 当前表单项的每一个值
        :param promptPageLeave: form 还没保存，即将离开页面前是否弹框确认。
        """
        super().__init__(type = type,name = name,mode = mode,horizontal = horizontal,title = title,submitText = submitText,className = className,controls = controls,actions = actions,messages = messages,wrapWithPanel = wrapWithPanel,panelClassName = panelClassName,api = api,initApi = initApi,rules = rules,interval = interval,silentPolling = silentPolling,stopAutoRefreshWhen = stopAutoRefreshWhen,initAsyncApi = initAsyncApi,initFetch = initFetch,initFetchOn = initFetchOn,initFinishedField = initFinishedField,initCheckInterval = initCheckInterval,asyncApi = asyncApi,checkInterval = checkInterval,finishedField = finishedField,submitOnChange = submitOnChange,submitOnInit = submitOnInit,resetAfterSubmit = resetAfterSubmit,primaryField = primaryField,target = target,redirect = redirect,reload = reload,autoFocus = autoFocus,canAccessSuperData = canAccessSuperData,persistData = persistData,clearPersistDataAfterSubmit = clearPersistDataAfterSubmit,preventEnterSubmit = preventEnterSubmit,trimValues = trimValues,promptPageLeave = promptPageLeave,**kwargs)
    