import unittest
from unittest import mock
from .txn import Transaction
from .metricstore import Metricstore
from pythonapm.agent import Agent

class Resp:
    def __init__(self,status_code):
        self.status_code = status_code

class Err:
    pass

class TxnTest(unittest.TestCase):
    def setUp(self):
        self.txn_instance = Transaction(
            {'PATH_INFO': 'path', 'QUERY_STRING': 'query', 'REQUEST_METHOD': 'req_method'})
    
    @mock.patch('pythonapm.metric.txn.get_agent')
    @mock.patch('pythonapm.metric.test_txn.Agent')
    @mock.patch('pythonapm.metric.test_txn.Metricstore.add_web_txn')
    def test_end_txn(self,mock_add_txn,mock_get_agent,mock_Agent):
        mock_agent_instance = mock_Agent.return_value
        mock_agent_instance.is_data_collection_allowed.return_value = True
        mock_agent_instance.get_metric_store.return_value = Metricstore()
        mock_get_agent.return_value = mock_agent_instance
        self.assertFalse(self.txn_instance.completed)
        self.txn_instance.end_txn(res= Resp(200))
        self.assertTrue(mock_agent_instance.is_data_collection_allowed.called)
        self.assertTrue(mock_add_txn.called)
        self.assertTrue(self.txn_instance.completed)
        self.assertEqual(self.txn_instance.status_code,200)
    
    def test_check_and_add_error(self):
        self.txn_instance.exceptions_info = {}
        self.txn_instance.check_and_add_error(Exception())
        self.txn_instance.check_and_add_error(ArithmeticError())
        self.txn_instance.check_and_add_error(ArithmeticError())
        self.txn_instance.check_and_add_error(Err())
        self.assertEqual(self.txn_instance.exceptions_info['Exception'],1)
        self.assertEqual(self.txn_instance.exceptions_info['ArithmeticError'],2)
        self.assertEqual(self.txn_instance.exceptions_info['Err'],1)
        
    def test_get_url(self):
        self.assertIsInstance(self.txn_instance.get_url(),str)
        self.assertEqual(self.txn_instance.get_url(),'path')
         
    def test_get_method(self):
        self.assertIsInstance(self.txn_instance.get_method(),str)
        self.assertEqual(self.txn_instance.get_method(),'req_method')

    def test_get_query_param(self):
        self.assertIsInstance(self.txn_instance.get_query_param(),str)
        self.assertEqual(self.txn_instance.get_query_param(),'query')
    
    def test_get_status_code(self):
        self.assertIsInstance(self.txn_instance.get_status_code(),object)
    
    def test_is_completed(self):
        self.assertIsInstance(self.txn_instance.is_completed(),bool)
    

    def test_is_error_txn(self):
        self.txn_instance.status_code = 401
        self.assertTrue(self.txn_instance.is_error_txn())
        self.txn_instance.status_code = 200
        self.assertFalse(self.txn_instance.is_error_txn())

    def tearDown(self):
        self.txn_instance = None
