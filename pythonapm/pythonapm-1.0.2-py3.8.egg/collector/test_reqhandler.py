import unittest 
import json
import requests
from unittest import mock
from .reqhandler import send_req
from pythonapm.agent import Agent
from pythonapm import constants


class Resp:
    def __init__(self):
        self.data = json.dumps({'txn':'success'})
    def json(self):
        return json.loads(self.data)



class ReqhandlerTest(unittest.TestCase):

    def setUp(self):
        self.agent = Agent()
        self.agent.config.license_key = 'key'
        self.agent.config.project_id  = 'id'
        self.agent.config.print_payload = True

    @mock.patch('pythonapm.collector.reqhandler.get_agent')
    @mock.patch('pythonapm.collector.reqhandler.agentlogger')
    @mock.patch('pythonapm.collector.reqhandler.requests')
    def test_send_req(self,mock_requests,mock_logger,mock_agent):

        mock_agent.return_value = self.agent
        payload = {'txn':'txn_data'}
        payload_str = json.dumps(payload)
        response_data = {'txn':'success'}
        complete_url = f'{constants.collector_domain}/api/agent?licenseKey=key&projectId=id'
        mock_requests.post.return_value = Resp()
        send_req('/api/agent',payload)
        mock_requests.post.assert_called_with(complete_url,data= payload_str,headers = {'content-type':'application/json'})
        mock_logger.info.assert_called_with(f'response for /api/agent request :{json.dumps(response_data)}')
        self.assertEqual(mock_logger.info.call_count,3)
        self.assertListEqual(mock_logger.info.mock_calls,[mock.call(f'sending request to {constants.collector_domain}/api/agent'),mock.call(f'payload :{payload_str}'),mock.call('response for /api/agent request :{"txn": "success"}')])


