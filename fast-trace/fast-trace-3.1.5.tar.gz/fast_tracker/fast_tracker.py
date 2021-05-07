#!/usr/local/bin python3
# -*- coding: utf-8 -*-

"""
    created by FAST-DEV 2021/4/12
"""

from fast_tracker import config, Layer, ComponentType, Log, LogItem
from fast_tracker.trace.context import get_context
from fast_tracker.trace.tags import Tag

custom_user_code = ""
custom_tenant_code = ""
custom_env_code = ""


class FastTracker:
    def __init__(self):
        self.span = None

    @property
    def product_code(self):
        """
        获取 product_code 值
        :return:
        """
        return config.product_code

    @product_code.setter
    def product_code(self, product_code: str = ""):
        """
        设置 product_code 值
        :param product_code:
        :return:
        """
        config.set_product_code(product_code)

    @property
    def app_code(self):
        """
        获取 app_code 值
        :return:
        """
        return config.app_code

    @app_code.setter
    def app_code(self, app_code: str = ""):
        """
        设置 app_code 值
        :param app_code:
        :return:
        """
        config.set_app_code(app_code)

    @property
    def env_code(self):
        """
        获取 env_code 值
        :return:
        """
        global custom_env_code
        return custom_env_code if custom_env_code else config.env_code

    @env_code.setter
    def env_code(self, env_code: str = ""):
        """
        设置 env_code 值
        :param env_code:
        :return:
        """
        if env_code:
            global custom_env_code
            custom_env_code = env_code
        config.set_env_code(env_code)

    @property
    def tenant_code(self):
        """
        获取 tenant_code 值
        :return:
        """
        global custom_tenant_code
        return custom_tenant_code if custom_tenant_code else config.tenant_code

    @tenant_code.setter
    def tenant_code(self, tenant_code: str = ""):
        """
        设置 tenant_code 值
        :param tenant_code:
        :return:
        """
        if tenant_code:
            global custom_tenant_code
            custom_tenant_code = tenant_code
        config.set_tenant_code(tenant_code)

    @property
    def user_code(self):
        """
        获取 user_code 值
        :return:
        """
        global custom_user_code
        return custom_user_code if custom_user_code else config.user_code

    @user_code.setter
    def user_code(self, user_code: str = ""):
        """
        设置 user_code 值
        :param user_code:
        :return:
        """
        if user_code:
            global custom_user_code
            custom_user_code = user_code
        config.set_user_code(user_code)

    @property
    def service_name(self):
        """
        获取 service_name 值
        :return:
        """
        return config.service_name

    @service_name.setter
    def service_name(self, service_name: str = ""):
        """
        设置 service_name 值
        :param service_name:
        :return:
        """
        config.set_service_name(service_name)

    @property
    def socket_path(self):
        """
        获取 socket_path 值
        :return:
        """
        return config.collector_address

    @socket_path.setter
    def socket_path(self, socket_path: str = ""):
        """
        设置 socket_path 值
        :param socket_path:
        :return:
        """
        config.set_socket_path(socket_path)

    @property
    def buffer_size(self):
        """
        获取 buffer_size 值
        :return:
        """
        return config.buffer_size

    @buffer_size.setter
    def buffer_size(self, buffer_size: int = 1):
        """
        设置 buffer_size 值
        :param buffer_size:
        :return:
        """
        config.set_buffer_size(buffer_size)

    @property
    def socket_timeout(self):
        """
        获取 socket_timeout 值
        :return:
        """
        return config.socket_timeout

    @socket_timeout.setter
    def socket_timeout(self, socket_timeout: int = 1):
        """
        设置 socket_timeout 值
        :param socket_timeout:
        :return:
        """
        config.set_socket_timeout(socket_timeout)

    @property
    def event(self):
        """
        获取 event 值
        :return:
        """
        return config.event

    @event.setter
    def event(self, event: dict):
        """
        设置 event 值
        :param event:
        :return:
        """
        config.set_event(event)

    @staticmethod
    def get_config():
        return {
            "ServiceName": config.service_name,
            "ServiceInstance": config.service_instance,
            "Protocol": config.protocol,
            "LogLevel": config.log_level,
            "IgnoreSuffix": config.ignore_suffix,
            "CorrelationElementMaxNumber": config.correlation_element_max_number,
            "CorrelationValueMaxLength": config.correlation_value_max_length,
            "TraceIgnorePath": config.trace_ignore_path,
            "Enable": config.enable,
            "EnvCode": config.env_code,
            "TenantCode": config.tenant_code,
            "UserCode": config.user_code,
            "SocketPath": config.collector_address,
            "BufferSize": config.buffer_size,
            "SocketTimeout": config.socket_timeout,
            "Event": config.event,
            "TenantCodeReader": config.tenant_code_reader,
            "UserCodeReader": config.user_code_reader,
            "CarrierHeader": config.carrier_header,
        }

    def begin_event(self, op: str = ""):
        """
        log模块开始 类似数据库事务的begin_trasaction
        :param op:
        :return:
        """
        try:
            context = get_context()
            span = context.active_span()
            self.span = context.new_local_span(op="execute")
            self.span.layer = Layer.Local
            self.span.component = ComponentType.CustomEvent
            self.span.op = op
            self.span.pid = span.sid
            self.span.start()
            return self
        except Exception as e:
            raise e

    def tag(self, tag_name: str = ""):
        if not self.span:
            raise RuntimeError("请先调用begin_event进行实例化")
        self.span.tag(Tag(key=ComponentType.CustomEvent, val=tag_name))

    def log(self, log: str = ""):
        if not self.span:
            raise RuntimeError("请先调用begin_event进行实例化")
        self.span.logs.append(Log(items=[LogItem(key=ComponentType.CustomEvent, val=self.log_covert(log))]))

    def log_covert(self, msg: str = ""):
        return {"err_msg": msg, "err_type": "", "err_trace": ""}

    def end_event(self):
        """
        log模块结束
        :return:
        """
        if not self.span:
            raise RuntimeError("请先调用begin_event进行实例化")
        self.span.stop()
