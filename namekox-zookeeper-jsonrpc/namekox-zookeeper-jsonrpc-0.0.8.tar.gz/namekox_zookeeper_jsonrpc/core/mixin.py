#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals


from namekox_zookeeper.core.allotter import Allotter
from namekox_config.core.dependencies import ConfigHelper
from namekox_jsonrpc.constants import DEFAULT_JSONRPC_PORT
from namekox_context.core.dependencies import ContextHelper
from namekox_zookeeper.core.dependencies import ZooKeeperHelper
from namekox_zookeeper.constants import DEFAULT_ZOOKEEPER_SERVICE_ROOT_PATH


def Registry(**options):
    class Mixin(object):
        name = options['name']

        cfg = ConfigHelper()
        ctx = ContextHelper()
        zk = ZooKeeperHelper(
            name,
            serverid=options.pop('serverid', None),
            coptions=options.pop('coptions', None),
            allotter=options.pop('allotter', Allotter()),
            roptions=options.pop('roptions', {'port': DEFAULT_JSONRPC_PORT}),
            watching=options.pop('watching', DEFAULT_ZOOKEEPER_SERVICE_ROOT_PATH)
        )
    return Mixin
