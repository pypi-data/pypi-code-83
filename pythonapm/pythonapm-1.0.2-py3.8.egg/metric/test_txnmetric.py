import unittest
from unittest import mock
from .txnmetric import TxnMetric
from .txn import Transaction


class TxnmetricTest(unittest.TestCase):

    def setUp(self):
        self.txnmetric = TxnMetric()
        self.txn_instance = Transaction(
            {'PATH_INFO': 'path', 'QUERY_STRING': 'query', 'REQUEST_METHOD': 'req_method'})

    def test_update_req_count(self):
        self.txnmetric.err_count = 0
        self.txnmetric.count = 0
        self.txn_instance.status_code = 400
        self.txnmetric.update_req_count(self.txn_instance)
        self.assertEqual(self.txnmetric.err_count, 1)
        self.txn_instance.status_code = 200
        self.txnmetric.update_req_count(self.txn_instance)
        self.assertEqual(self.txnmetric.count, 1)

    def test_aggregate(self):
        self.txn_instance.status_code = 400
        self.txnmetric.error_codes = {}
        self.txn_instance.rt = 10
        self.txn_instance.exceptions_info = {
            'Exception': 1
        }
        self.txnmetric.exceptions_info = {
            'Exception': 1,
            'ArithmeticError': 1,
        }
        self.txnmetric.err_count = 10
        self.txnmetric.err_rt = 10
        self.txnmetric.aggregate(self.txn_instance)
        self.assertEqual(self.txnmetric.err_count, 11)
        self.assertEqual(self.txnmetric.err_rt, 20)
        self.assertDictEqual(self.txnmetric.exceptions_info, {
            'Exception': 2,
            'ArithmeticError': 1,
        })
        self.assertEqual(self.txnmetric.error_codes[400], 1)

    def test_aggregate_non_error_txn(self):
        self.txn_instance.status_code = 200
        self.txn_instance.rt = 10
        self.txnmetric.rt = 10
        self.txnmetric.count = 1
        self.txn_instance.exceptions_info = {
            'Exception': 1
        }
        self.txnmetric.exceptions_info = {
            'Exception': 1,
            'ArithmeticError': 1,
        }
        self.txnmetric.aggregate_non_error_txn(self.txn_instance)
        self.assertEqual(self.txnmetric.count, 2)
        self.assertEqual(self.txnmetric.rt, 20)
        self.assertFalse(hasattr(self.txnmetric.error_codes, '200'))
        self.assertDictEqual(self.txnmetric.exceptions_info, {
            'Exception': 2,
            'ArithmeticError': 1,
        })

    def test_aggregate_errorcode(self):
        self.txn_instance.status_code = 400
        self.txnmetric.error_codes = {}
        self.txnmetric.aggregate_errorcode(self.txn_instance)
        self.assertEqual(self.txnmetric.error_codes[400], 1)

    def test_aggregate_exceptions(self):
        self.txnmetric.exceptions_info = {
            'Exception': 1,
            'ArithmeticError': 1,
        }
        self.txnmetric.aggregate_exceptions(cur_exc_info={
            'Exception': 2,
            'NameError': 1
        })

        self.assertDictEqual(self.txnmetric.exceptions_info, {
                             'Exception': 3, 'NameError': 1, 'ArithmeticError': 1})

    def test_get_formatted_data(self):
        self.txnmetric = TxnMetric()
        self.txnmetric.exceptions_info = {
            'Exception': 1
        }
        self.assertDictEqual(self.txnmetric.get_formatted_data(), {
            'url': '',
            'method': '',
            'rt': 0,
            'minrt': 0,
            'maxrt': 0,
            'errorrt': 0,
            'count': 0,
            'errcount': 0,
            'errors': {},
            'exceptions': {'Exception': 1},
        })
    
    def test_get_count(self):
        self.assertIsInstance(self.txnmetric.get_count(),int)
    
    def test_get_error_count(self):
        self.assertIsInstance(self.txnmetric.get_error_count(),int)
    
    def test_get_rt(self):
        self.assertIsInstance(self.txnmetric.get_rt(),int)
    
    def test_get_error_rt(self):
        self.assertIsInstance(self.txnmetric.get_error_rt(),int)
    
    def test_get_min_rt(self):
        self.assertIsInstance(self.txnmetric.get_min_rt(),int)

    def test_get_max_rt(self):
        self.assertIsInstance(self.txnmetric.get_max_rt(),int)

    def test_get_exceptions_info(self):
        self.assertIsInstance(self.txnmetric.get_exceptions_info(),dict)
    

    def tearDown(self):
        self.txnmetric = None
        self.txn_instance = None
