import unittest
from pythonapm.config.configuration import Configuration
from .agent import Agent,initalize
from pythonapm.metric.txn import Transaction
from pythonapm.metric.metricstore import Metricstore
from pythonapm.collector.insinfo import Instanceinfo
from pythonapm import context
from unittest import mock 

class AgentTest(unittest.TestCase):
    def setUp(self):
        self.agent = Agent()
    def test_is_data_collection_allowed(self):
        self.assertIsInstance(self.agent.is_data_collection_allowed(),bool)
    
    def test_check_and_create_txn(self):
        self.assertIsInstance(self.agent.check_and_create_txn({'PATH_INFO':'/txn'}),Transaction)
    
    @mock.patch('pythonapm.test_agent.Transaction.end_txn')
    def test_end_txn(self,mock_obj):
        self.agent.end_txn(Transaction())
        self.assertTrue(mock_obj.called)
    
    @mock.patch('pythonapm.test_agent.context.get_cur_txn')
    @mock.patch('pythonapm.test_agent.Transaction.check_and_add_error')
    def test_track_execption(self,mock_context,mock_error):
        mock_context.return_value = Transaction({})
        self.agent.track_exception()
        self.assertTrue(mock_error.called)

    def test_get_config(self):
        self.assertTrue(isinstance(self.agent.get_config(),Configuration))

    def test_get_metric_store(self):
        self.assertIsInstance(self.agent.get_metric_store(),Metricstore)
    
    def test_get_ins_info(self):
        self.assertIsInstance(self.agent.get_ins_info(),Instanceinfo)


    @mock.patch('pythonapm.test_agent.Configuration.is_configured_properly')
    def test_initalize(self,mock_config):
        mock_config.return_value = True
        self.assertTrue(isinstance(initalize(),Agent))