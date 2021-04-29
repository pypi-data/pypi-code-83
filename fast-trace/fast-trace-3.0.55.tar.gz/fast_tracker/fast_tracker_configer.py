#!/usr/local/bin python3
# -*- coding: utf-8 -*-

"""
    created by FAST-DEV 2021/4/9
"""
import json

import os

from fast_tracker.loggings import logger
from fast_tracker.utils import exceptions, functions


class FastTrackerConfiger:
    @staticmethod
    def _default_config_keys():
        return [
            "Enable",
            "EnvCode",
            "TenantCode",
            "UserCode",
            "ProductCode",
            "AppCode",
            "ServiceName",
            "SocketPath",
            "BufferSize",
            "SocketTimeout",
            "Event",
            "TenantCodeReader",
            "UserCodeReader",
            "CarrierHeader",
        ]

    @staticmethod
    def load_configuration(config_file=None):
        """
        :param config_file: 配置文件地址
        :param log_level:
        :return:
        """
        if not config_file:
            logger.debug("没有代理配置文件")
            raise exceptions.ConfigurationError("没有发现配置文件")
        logger.debug("代理的配置文件是 %s" % config_file)

        try:
            with open(config_file, "r") as fb:
                config_dict = json.load(fb)
                default_config_keys = FastTrackerConfiger._default_config_keys()
                from fast_tracker import config

                if config_dict:
                    for config_key in config_dict.keys():
                        if config_key in default_config_keys:
                            func_name = "set_" + functions.lower_case_name(config_key)
                            # 如果环境变量已经有值，则不再赋值
                            config_name = func_name if func_name != "socket_path" else "collector_address"
                            is_exist = os.getenv(config_name, "None")
                            if is_exist == "None":
                                getattr(config, func_name)(config_dict.get(config_key))

        except Exception as e:
            raise exceptions.ConfigurationError("json格式配置文件格式不合法(不要有注释),解析失败,文件: %s." % config_file)
