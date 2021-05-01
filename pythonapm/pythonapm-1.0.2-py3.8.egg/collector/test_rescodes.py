import unittest 
from unittest import mock
from .rescodes import is_valid_rescode,get_rescode_message,is_allowed_to_send_request,is_retry_limit_exceeded,get_retry_counter

from pythonapm.util import current_milli_time


class RescodesTest(unittest.TestCase):
    def setUp(self):
        self.rescode_list = [300,400,100,200,0]
    def test_is_valid_rescode(self):
        for code in self.rescode_list :
            self.assertTrue(is_valid_rescode(code))
        self.assertFalse(is_valid_rescode(500))

    def test_get_rescode_message(self):
        self.assertEqual(get_rescode_message(300),'MARKED_FOR_DELETE')
        self.assertEqual(get_rescode_message(500),500)
    
    @mock.patch('pythonapm.collector.rescodes.agentlogger')
    def test_is_allowed_to_send_request(self,mock_logger):
        is_allowed_to_send_request(500,3)
        mock_logger.critical.assert_called_with(f'invalid rescode :500 counter:3')

        is_allowed_to_send_request(100,3)
        mock_logger.info.assert_called_with(f'No time limit restriction for rescode:100')

        self.assertFalse(is_allowed_to_send_request(300,21))
        self.assertFalse(is_allowed_to_send_request(300,31))
    
    def test_is_retry_limit_exceeded(self):
        self.assertTrue(is_retry_limit_exceeded(300,3*24*60))
        self.assertFalse(is_retry_limit_exceeded(300,3*24*60-1))
    
    @mock.patch('pythonapm.collector.rescodes.current_milli_time')
    def test_get_retry_counter(self,mock_time):
        self.assertEqual(get_retry_counter(None,None),1)
        occured_time = current_milli_time()
        cur_time = current_milli_time()
        mock_time.return_value = cur_time
        self.assertEqual(get_retry_counter(300,occured_time),int((cur_time - occured_time)/(60*1000)))

        self.assertEqual(get_retry_counter(0,current_milli_time()),1)


