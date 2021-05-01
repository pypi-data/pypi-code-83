import unittest 
from unittest import mock 
from .reshandler import handle_connect_response,handle_data_response

from ..agent import Agent

class ReshandlerTest(unittest.TestCase):

    def setUp(self):
        self.agent  = Agent()
        self.res_data =  {'data':{'code':300}}
        

    @mock.patch('pythonapm.collector.reshandler.get_agent')
    @mock.patch('pythonapm.collector.reshandler.agentlogger')
    def test_handle_connect_response(self,mock_logger,mock_agent):
        mock_agent.return_value = self.agent
        self.assertFalse(handle_connect_response({}))
        self.assertFalse(handle_connect_response(None))
        self.assertTrue(handle_connect_response(res_data=self.res_data))
        mock_logger.critical.assert_called_with(f'received response code :300')

        mock_agent.side_effect = Exception('[response handler connect_response]')
        self.assertFalse(handle_connect_response(self.res_data))
        mock_logger.exception.assert_called_with(f'connect response handler')

    @mock.patch('pythonapm.collector.reshandler.get_agent')
    @mock.patch('pythonapm.collector.reshandler.agentlogger')
    def test_handle_data_response(self,mock_logger,mock_agent):
        mock_agent.return_value = self.agent
        self.assertFalse(handle_data_response({}))
        self.assertFalse(handle_data_response(None))
        self.assertTrue(handle_data_response({'data':{}}))
        self.assertTrue(handle_data_response(self.res_data))
        mock_logger.critical.assert_called_with(f'received response code :MARKED_FOR_DELETE')

        mock_agent.side_effect = Exception('[response handler data_response]')
        self.assertFalse(handle_data_response(self.res_data))
        mock_logger.exception.assert_called_with(f'data response handler')

        

