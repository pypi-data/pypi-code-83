import unittest
from unittest import mock
from .metricstore import Metricstore
from .txn import Transaction
from .txnmetric import TxnMetric


class MetricstoreTest(unittest.TestCase):
    def setUp(self):
        self.metricstore_instance = Metricstore()
        self.txn_instance = Transaction(
            {'PATH_INFO': '/api/data', 'QUERY_STRING': 'query', 'REQUEST_METHOD': 'GET'})

    def test_add_web_txn(self):
        self.txn_instance.completed = True
        self.txn_instance.status_code = 400
        self.txn_instance.exceptions_info = {
            'Exception': 1,
            'NameError': 1
        }
        self.assertTrue(
            self.metricstore_instance.add_web_txn(self.txn_instance))
        self.assertEqual(
            self.metricstore_instance.web_txn_metric['GET - /api/data'].error_codes[400], 1)
        self.txn_instance.status_code = 401
        self.assertTrue(
            self.metricstore_instance.add_web_txn(self.txn_instance))
        self.assertEqual(
            self.metricstore_instance.web_txn_metric['GET - /api/data'].error_codes[401], 1)

        self.assertDictEqual(self.metricstore_instance.web_txn_metric['GET - /api/data'].exceptions_info, {'Exception': 2,
                                                                                                           'NameError': 2})

    def test_get_formatted_data(self):
        self.metricstore_instance.web_txn_metric = {
            'get-/api/data': TxnMetric()}
        self.assertListEqual(self.metricstore_instance.get_formatted_data(), [{
            'url': '',
            'method': '',
            'rt': 0,
            'minrt': 0,
            'maxrt': 0,
            'errorrt': 0,
            'count': 0,
            'errcount': 0,
            'errors': {},
            'exceptions': {},
        }])

    def test_cleanup(self):
        self.metricstore_instance.cleanup()
        self.assertDictEqual(self.metricstore_instance.get_webtxn_metric(), {})

    def tearDown(self):
        self.metricstore_instance = None
