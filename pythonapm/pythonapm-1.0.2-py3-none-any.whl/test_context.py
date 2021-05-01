import os
import unittest
from unittest import mock 
from .context import set_cur_txn,ser_cur_context,clear_cur_context,get_cur_txn,is_txn_active,is_no_active_txn
class AgentContextTest(unittest.TestCase):

    def test_set_cur_txn(self):
        set_cur_txn({'a':'b'})
        self.assertDictEqual(get_cur_txn(),{'a':'b'})
        
    def test_ser_cur_context(self):
        ser_cur_context({'a':'b'})
        self.assertDictEqual(get_cur_txn(),{'a':'b'})

    def test_clear_cur_context(self):
        clear_cur_context()
        self.assertIsNone(get_cur_txn())

    def test_get_cur_txn(self):
        clear_cur_context()
        self.assertIsNone(get_cur_txn())
        
    def test_is_txn_active(self):
        set_cur_txn({'a':'b'})
        self.assertTrue(is_txn_active())
        clear_cur_context()
        self.assertFalse(is_txn_active())
        