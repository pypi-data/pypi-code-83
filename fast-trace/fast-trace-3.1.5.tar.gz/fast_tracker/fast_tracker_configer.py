#!/usr/local/bin python3
# -*- coding: utf-8 -*-

"""
    created by FAST-DEV 2021/4/9
"""
import json

import os
from fast_tracker import config
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
            "EnvCodeReader",
        ]

    @staticmethod
    def load_configuration(config_file=None):
        """
        :param config_file: 配置文件地址
        :param log_level:
        :return:
        """
        if not config_file:
            logger.debug("没有探针配置文件")
            raise exceptions.ConfigurationError("没有发现配置文件")
        logger.debug("探针的配置文件是 %s" % config_file)

        try:
            with open(config_file, "r") as fb:

                config_dict = json.load(fb)
                default_config_keys = FastTrackerConfiger._default_config_keys()

                if config_dict:
                    for config_key in config_dict.keys():
                        if config_key in default_config_keys:
                            func_name = "set_" + functions.lower_case_name(config_key)
                            if config_key == "TenantCodeReader":
                                config.set_tenant_code_reader(**config_dict.get(config_key))
                            elif config_key == "UserCodeReader":
                                config.set_user_code_reader(**config_dict.get(config_key))
                            elif config_key == "EnvCodeReader":
                                config.set_env_code_reader(**config_dict.get(config_key))
                            elif config_key == "CarrierHeader":
                                config.set_carrier_header(**config_dict.get(config_key))
                            else:
                                getattr(config, func_name)(config_dict.get(config_key))

        except Exception as e:
            raise exceptions.ConfigurationError("json格式配置文件格式不合法(不要有注释),解析失败,文件: %s, 错误信息：%s" % (config_file, str(e)))

    @staticmethod
    def set_config_by_env():
        """
        通过环境变量设置配置值
        :return:
        """
        env_dict = os.environ
        for key, val in env_dict.items():
            if key.startswith("FastTracker_"):
                if key.startswith("FastTracker_TenantCodeReader_"):
                    args = {functions.lower_case_name(key[29:]): val}
                    config.set_tenant_code_reader(**args)
                elif key.startswith("FastTracker_UserCodeReader_"):
                    args = {functions.lower_case_name(key[27:]): val}
                    config.set_user_code_reader(**args)
                elif key.startswith("FastTracker_EnvCodeReader_"):
                    args = {functions.lower_case_name(key[26:]): val}
                    config.set_env_code_reader(**args)
                elif key.startswith("FastTracker_CarrierHeader_"):
                    args = {functions.lower_case_name(key[26:]): val}
                    config.set_carrier_header(**args)
                else:
                    config_name = functions.lower_case_name(key[12:])
                    setattr(config, config_name, val)
