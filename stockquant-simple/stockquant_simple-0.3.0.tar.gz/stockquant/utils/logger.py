# -*- coding:utf-8 -*-

"""
日志输出
Author: Gary-Hertel
Date:   2020/07/09
"""

import logging
from logging import handlers
from stockquant.config import config
import os
import traceback


class __LOGGER:

    def __init__(self):
        if not os.path.exists("./logs"):    # 如果logs文件夹不存在就自动创建
            os.makedirs("./logs")
        self.__path = './logs/error.log'
        self.__logger = logging.getLogger("stockquant")

    def __initialize(self):
        if config.log["level"] == "debug":
            level = logging.DEBUG
        elif config.log["level"] == "info":
            level = logging.INFO
        elif config.log["level"] == "warning":
            level = logging.WARNING
        elif config.log["level"] == "error":
            level = logging.ERROR
        elif config.log["level"] == "critical":
            level = logging.CRITICAL
        else:
            level = logging.DEBUG
        self.__logger.setLevel(level=level)
        formatter = logging.Formatter(fmt='[%(asctime)s] -> [%(levelname)s] : %(message)s')
        # 文件输出按照时间分割
        time_rotating_file_handler = handlers.TimedRotatingFileHandler(filename=self.__path, when='MIDNIGHT',
                                                                       interval=1, backupCount=1000)
        time_rotating_file_handler.setFormatter(formatter)
        time_rotating_file_handler.suffix = "%Y%m%d-%H%M%S.log"

        # 控制台输出
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        if config.log["handler"] == "time":
            if not self.__logger.handlers:
                self.__logger.addHandler(time_rotating_file_handler)
        else:
            if not self.__logger.handlers:
                self.__logger.addHandler(stream_handler)

    def debug(self, *args):
        self.__initialize()
        self.__logger.debug(args) if args is not None else self.__logger.debug(traceback.format_exc(limit=1))

    def info(self, *args):
        self.__initialize()
        self.__logger.info(args) if args is not None else self.__logger.info(traceback.format_exc(limit=1))

    def warning(self, *args):
        self.__initialize()
        self.__logger.warning(args) if args is not None else self.__logger.warning(traceback.format_exc(limit=1))

    def error(self, *args):
        self.__initialize()
        self.__logger.error(args) if args is not None else self.__logger.error(traceback.format_exc(limit=1))

    def critical(self, *args):
        self.__initialize()
        self.__logger.critical(args) if args is not None else self.__logger.critical(traceback.format_exc(limit=1))


logger = __LOGGER()