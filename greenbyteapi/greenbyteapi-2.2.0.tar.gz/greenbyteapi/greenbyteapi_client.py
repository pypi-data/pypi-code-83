# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from greenbyteapi.decorators import lazy_property
from greenbyteapi.configuration import Configuration
from greenbyteapi.controllers.data_controller import DataController
from greenbyteapi.controllers.statuses_controller import StatusesController
from greenbyteapi.controllers.configuration_data_controller import ConfigurationDataController
from greenbyteapi.controllers.assets_controller import AssetsController
from greenbyteapi.controllers.alerts_controller import AlertsController
from greenbyteapi.controllers.plan_controller import PlanController


class GreenbyteapiClient(object):

    config = Configuration

    @lazy_property
    def data(self):
        return DataController()

    @lazy_property
    def statuses(self):
        return StatusesController()

    @lazy_property
    def configuration_data(self):
        return ConfigurationDataController()

    @lazy_property
    def assets(self):
        return AssetsController()

    @lazy_property
    def alerts(self):
        return AlertsController()

    @lazy_property
    def plan(self):
        return PlanController()


    def __init__(self,
                 x_api_key=None):
        if x_api_key is not None:
            Configuration.x_api_key = x_api_key

