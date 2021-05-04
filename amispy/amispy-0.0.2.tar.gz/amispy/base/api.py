from .base import PyAmisComponent


class Api(PyAmisComponent):
    """
    :param method: 请求方式
    :param url: 请求地址
    :param data: 请求数据
    :param dataType: 数据体格式
    :param qsOptions: --
    :param headers: 请求头
    :param sendOn: 请求条件
    :param cache: 接口缓存时间
    :param requestAdaptor: 发送适配器
    :param adaptor: 接收适配器
    :param replaceData: 替换当前数据
    :param responseType: 返回类型
    :param autoRefresh: 是否自动刷新
    :param responseData: 配置返回数据
    :param trackExpression: 跟踪变量
    """
    def __init__(self,
                 method: any = None,
                 url: any = None,
                 data: any = None,
                 dataType: any = None,
                 qsOptions: any = None,
                 headers: any = None,
                 sendOn: any = None,
                 cache: any = None,
                 requestAdaptor: any = None,
                 adaptor: any = None,
                 replaceData: any = None,
                 responseType: any = None,
                 autoRefresh: any = None,
                 responseData: any = None,
                 trackExpression: any = None,):
        super().__init__(method = method,url = url,data = data,dataType = dataType,qsOptions = qsOptions,headers = headers,sendOn = sendOn,cache = cache,requestAdaptor = requestAdaptor,adaptor = adaptor,replaceData = replaceData,responseType = responseType,autoRefresh = autoRefresh,responseData = responseData,trackExpression = trackExpression)
    