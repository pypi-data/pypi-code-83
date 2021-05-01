import threading

from pyamis.base import PyAmisComponent
from .page import Page

default_page = threading.Lock()


class AppPage(PyAmisComponent):
    """
    https://baidu.gitee.io/amis/zh-CN/components/app
    生成分页中的`pages`现
    """
    def __init__(self,
                 url: str = None,
                 label: str = None,
                 schema: any = default_page,
                 schema_body: any = None,
                 children: list = None,
                 **kwargs):
        if schema is default_page:
            schema = Page()
        if schema_body:
            schema['body'] = schema_body

        super(AppPage, self).__init__(url=url, label=label, schema=schema, children=children, **kwargs)
