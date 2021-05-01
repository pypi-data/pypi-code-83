
import os
from pythonapm.collector.connhandler import init_connection
from pythonapm.instrumentation import init_instrumentation
from pythonapm.metric.txn import Transaction
from pythonapm.metric.metricstore import Metricstore
from pythonapm.config.configuration import Configuration
from pythonapm.collector.insinfo import Instanceinfo
from pythonapm import context
from pythonapm import constants
from pythonapm.logger import agentlogger
from pythonapm.util import is_allowed_url


def initalize():
    agent_instance = Agent()
    if not agent_instance.get_config().is_configured_properly():
        raise RuntimeError('Configure NEXTAPM_LICENSE_KEY and NEXTAPM_PROJECT_ID environment')

    init_instrumentation()
    init_connection()
    return agent_instance


class Agent:
    def __init__(self):
        self.config = Configuration()
        self.insinfo = Instanceinfo()
        self.metricstore = Metricstore()

    def is_data_collection_allowed(self):
        cur_status = self.insinfo.get_status()
        if cur_status is None:
            return True

        if cur_status == constants.manage_agent:
            return True

        return False

    def check_and_create_txn(self, wsgi_environ):
        context.clear_cur_context()
        if not self.is_data_collection_allowed():
            agentlogger.info('data collection stopped')
            return

        if type(wsgi_environ) is not dict:
            return

        url = wsgi_environ.get('PATH_INFO', '')
        if not is_allowed_url(url):
            return
        
        txn = Transaction(wsgi_environ)
        context.ser_cur_context(txn)
        return txn

    def end_txn(self, txn, res=None, err=None):
        if txn is None:
            return

        if isinstance(txn, Transaction):
            txn.end_txn(res, err)

    def track_exception(self, err=None):
        txn = context.get_cur_txn()
        if txn is None:
            return

        if err is None:
            return

        if isinstance(txn, Transaction):
            txn.check_and_add_error(err)

    def get_config(self):
        return self.config

    def get_ins_info(self):
        return self.insinfo

    def get_metric_store(self):
        return self.metricstore
