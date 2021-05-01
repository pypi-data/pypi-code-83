import unittest 
from unittest import mock

from .datahandler import get_data_with_time,process_collected_data
from ..util import current_milli_time
from ..agent import Agent
from ..metric.metricstore import TxnMetric
from pythonapm import constants

class DatahandlerTest(unittest.TestCase):

    def setUp(self):
        self.agent = Agent()
        self.agent.metricstore.web_txn_metric = {
            'get - /api/data': TxnMetric()
        }
        
    
    @mock.patch('pythonapm.collector.datahandler.current_milli_time')
    def test_get_data_with_time(self,mock_time):
        time = current_milli_time()
        mock_time.return_value = time
        
        self.assertDictEqual(get_data_with_time({'txn':'success'}),{
            'info':{
                'time': time,
            },
            'data':{
                'txn':'success'
            }
        })

    @mock.patch('pythonapm.collector.datahandler.get_agent')
    @mock.patch('pythonapm.collector.datahandler.send_req')
    @mock.patch('pythonapm.collector.datahandler.handle_data_response')
    @mock.patch('pythonapm.collector.datahandler.current_milli_time')
    def test_process_collected_data(self,mock_time,mock_handle_response,mock_send_req,mock_agent):
        mock_agent.return_value = self.agent
        time = current_milli_time()
        mock_time.return_value = time
        self.agent.insinfo.status = 100
        mock_send_req.return_value = {}
        process_collected_data()
        mock_send_req.assert_called_with(constants.api_data,get_data_with_time([{
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
        }]))
        mock_handle_response.assert_called_with({})

        self.agent.insinfo.status = 200
        mock_send_req.return_value = {'not-data':''}
        process_collected_data()
        mock_send_req.assert_called_with(constants.api_data,get_data_with_time([]))
        mock_handle_response.called_with({'not-data':''})

        self.agent.insinfo.status = 300
        process_collected_data()
        mock_send_req.assert_called_with(constants.api_data,get_data_with_time([]))
        mock_handle_response({'not-data':''})








