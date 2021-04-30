#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals


from namekox_jsonrpc.constants import (
    DEFAULT_JSONRPC_CALL_MODE_ID,
    DEFAULT_JSONRPC_TB_CALL_MODE,
    DEFAULT_JSONRPC_YB_CALL_MODE
)
from namekox_jsonrpc.core.client import ServerProxy
from namekox_jsonrpc.core.messaging import gen_message_headers
from namekox_zookeeper_jsonrpc.constants import DEFAULT_PROXY_TIMEOUT


class Proxy(object):
    def __init__(self, service, protocol='http', timeout=None):
        self.service = service
        self.protocol = protocol
        self.timeout = timeout or DEFAULT_PROXY_TIMEOUT

    def __call__(self, protocol='http', timeout=None):
        self.protocol = protocol
        self.timeout = timeout or DEFAULT_PROXY_TIMEOUT

    def __getattr__(self, target_service):
        return Service(self, target_service)


class Service(object):
    def __init__(self, proxy, target_service):
        self.proxy = proxy
        self.target_service = target_service

    def __getattr__(self, target_method):
        return Method(self.proxy, self.target_service, target_method)


class Method(object):
    def __init__(self, proxy, target_service, target_method):
        self.target_method = target_method
        server = proxy.service.zk.allotter.get(target_service)
        uri = '{}://{}:{}'.format(proxy.protocol, server['address'], server['port'])
        timeout = proxy.timeout
        headers = gen_message_headers(proxy.service.ctx.data)
        self.target_service = ServerProxy(uri, headers=headers, timeout=timeout)

    def call_async(self, *args, **kwargs):
        kwargs.setdefault(DEFAULT_JSONRPC_CALL_MODE_ID, DEFAULT_JSONRPC_YB_CALL_MODE)
        return self.target_service.__getattr__(self.target_method)(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        kwargs.setdefault(DEFAULT_JSONRPC_CALL_MODE_ID, DEFAULT_JSONRPC_TB_CALL_MODE)
        return self.target_service.__getattr__(self.target_method)(*args, **kwargs)
