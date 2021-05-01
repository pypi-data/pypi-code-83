
from dataclasses import dataclass
from pyamis.base import PyAmisComponent,Api
from typing import Union


class Crud(PyAmisComponent):
    """
    :param type: type 指定为 CRUD 渲染器
    :param mode: "table" 、 "cards" 或者 "list"
    :param title: 可设置成空，当设置成空时，没有标题栏
    :param className: 表格外层 Dom 的类名
    :param api: CRUD 用来获取列表数据的 api。
    :param loadDataOnce: 是否一次性加载所有数据（前端分页）
    :param loadDataOnceFetchOnFilter: 在开启 loadDataOnce 时，filter 时是否去重新请求 api
    :param source: 数据映射接口返回某字段的值，不设置会默认把接口返回的items或者rows填充进mode区域
    :param filter: 设置过滤器，当该表单提交后，会把数据带给当前 mode 刷新列表。
    :param filterTogglable: 是否可显隐过滤器
    :param filterDefaultVisible: 设置过滤器默认是否可见。
    :param initFetch: 是否初始化的时候拉取数据, 只针对有 filter 的情况, 没有 filter 初始都会拉取数据
    :param interval: 刷新时间(最低 1000)
    :param silentPolling: 配置刷新时是否隐藏加载动画
    :param stopAutoRefreshWhen: 通过表达式来配置停止刷新的条件
    :param stopAutoRefreshWhenModalIsOpen: 当有弹框时关闭自动刷新，关闭弹框又恢复
    :param syncLocation: 是否将过滤条件的参数同步到地址栏
    :param draggable: 是否可通过拖拽排序
    :param itemDraggableOn: 用表达式来配置是否可拖拽排序
    :param saveOrderApi: 保存排序的 api。
    :param quickSaveApi: 快速编辑后用来批量保存的 API。
    :param quickSaveItemApi: 快速编辑配置成及时保存时使用的 API。
    :param bulkActions: 批量操作列表，配置后，表格可进行选中操作。
    :param defaultChecked: 当可批量操作时，默认是否全部勾选。
    :param messages: 覆盖消息提示，如果不指定，将采用 api 返回的 message
    :param primaryField: 设置 ID 字段名。
    :param perPage: 设置一页显示多少条数据。
    :param defaultParams: 设置默认 filter 默认参数，会在查询的时候一起发给后端
    :param pageField: 设置分页页码字段名。
    :param perPageField: 设置分页一页显示的多少条数据的字段名。注意：最好与 defaultParams 一起使用，请看下面例子。
    :param perPageAvailable: 设置一页显示多少条数据下拉框可选条数。
    :param orderField: 设置用来确定位置的字段名，设置后新的顺序将被赋值到该字段中。
    :param hideQuickSaveBtn: 隐藏顶部快速保存提示
    :param autoJumpToTopOnPagerChange: 当切分页的时候，是否自动跳顶部。
    :param syncResponse2Query: 将返回数据同步到过滤器上。
    :param keepItemSelectionOnPageChange: 保留条目选择，默认分页、搜素后，用户选择条目会被清空，开启此选项后会保留用户选择，可以实现跨页面批量操作。
    :param labelTpl: 单条描述模板，keepItemSelectionOnPageChange设置为true后会把所有已选择条目列出来，此选项可以用来定制条目展示文案。
    :param headerToolbar: 顶部工具栏配置
    :param footerToolbar: 底部工具栏配置
    :param alwaysShowPagination: 是否总是显示分页
    :param affixHeader: 是否固定表头(table 下)
    """
    def __init__(self,
                 type: str = "crud",
                 mode: str = None,
                 title: str = None,
                 className: str = None,
                 api: any = None,
                 loadDataOnce: bool = None,
                 loadDataOnceFetchOnFilter: bool = None,
                 source: str = None,
                 filter: any = None,
                 filterTogglable: bool = None,
                 filterDefaultVisible: bool = None,
                 initFetch: bool = None,
                 interval: int = None,
                 silentPolling: bool = None,
                 stopAutoRefreshWhen: str = None,
                 stopAutoRefreshWhenModalIsOpen: bool = None,
                 syncLocation: bool = None,
                 draggable: bool = None,
                 itemDraggableOn: bool = None,
                 saveOrderApi: any = None,
                 quickSaveApi: any = None,
                 quickSaveItemApi: any = None,
                 bulkActions: any = None,
                 defaultChecked: bool = None,
                 messages: any = None,
                 primaryField: str = None,
                 perPage: int = None,
                 defaultParams: any = None,
                 pageField: str = None,
                 perPageField: str = None,
                 perPageAvailable: any = None,
                 orderField: str = None,
                 hideQuickSaveBtn: bool = None,
                 autoJumpToTopOnPagerChange: bool = None,
                 syncResponse2Query: bool = None,
                 keepItemSelectionOnPageChange: bool = None,
                 labelTpl: str = None,
                 headerToolbar: any = None,
                 footerToolbar: any = None,
                 alwaysShowPagination: bool = None,
                 affixHeader: bool = None,
                 **kwargs):
        super().__init__(type = type,mode = mode,title = title,className = className,api = api,loadDataOnce = loadDataOnce,loadDataOnceFetchOnFilter = loadDataOnceFetchOnFilter,source = source,filter = filter,filterTogglable = filterTogglable,filterDefaultVisible = filterDefaultVisible,initFetch = initFetch,interval = interval,silentPolling = silentPolling,stopAutoRefreshWhen = stopAutoRefreshWhen,stopAutoRefreshWhenModalIsOpen = stopAutoRefreshWhenModalIsOpen,syncLocation = syncLocation,draggable = draggable,itemDraggableOn = itemDraggableOn,saveOrderApi = saveOrderApi,quickSaveApi = quickSaveApi,quickSaveItemApi = quickSaveItemApi,bulkActions = bulkActions,defaultChecked = defaultChecked,messages = messages,primaryField = primaryField,perPage = perPage,defaultParams = defaultParams,pageField = pageField,perPageField = perPageField,perPageAvailable = perPageAvailable,orderField = orderField,hideQuickSaveBtn = hideQuickSaveBtn,autoJumpToTopOnPagerChange = autoJumpToTopOnPagerChange,syncResponse2Query = syncResponse2Query,keepItemSelectionOnPageChange = keepItemSelectionOnPageChange,labelTpl = labelTpl,headerToolbar = headerToolbar,footerToolbar = footerToolbar,alwaysShowPagination = alwaysShowPagination,affixHeader = affixHeader,**kwargs)
    