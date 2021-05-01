import unittest
import platform
from unittest import mock
import pythonapm
import threading
from pythonapm import constants
from ..util import current_milli_time
from .connhandler import init_connection, background_task, send_connect, getconn_payload
from ..agent import Agent

class MockThread:
    def __init__(self):
        pass 
    def setDaemon(self,value):
        pass
    def start(self):
        pass


class ConnhandlerTest(unittest.TestCase):

    def setUp(self):
        self.agent = Agent()
        self.payload = {
            "agent_info": {
                "agent_version": pythonapm.version,
                "host_type": platform.system(),
                "hostname": platform.node()
            }, "environment": {
                "os_version": platform.release(),
                "machine_name": platform.node(),
                'AgentInstallPath': pythonapm.installed_path,
                "python_version": platform.python_version(),
                "osarch": platform.machine(),
                "os": platform.system(),
            }
        }

    @mock.patch('pythonapm.collector.connhandler.conn_payload', None)
    @mock.patch('pythonapm.collector.connhandler.get_agent')
    def test_getconn_payload(self, mock_agent):
        mock_agent.return_value = self.agent

        self.assertDictEqual(getconn_payload(), self.payload)

    @mock.patch('pythonapm.collector.connhandler.send_req')
    @mock.patch('pythonapm.collector.connhandler.get_agent')
    def test_send_connect(self, mock_agent,mock_req):
        mock_agent.return_value = self.agent
        mock_req.return_value = {}
        self.assertFalse(send_connect())
        mock_req.assert_called_with(constants.api_connect,self.payload)

   

      
    @mock.patch('pythonapm.collector.connhandler.task_spawned',False)
    @mock.patch('pythonapm.collector.test_connhandler.threading.Thread')
    @mock.patch('pythonapm.collector.connhandler.agentlogger')
    def test_init_connection(self,mock_logger,mock_thread):
        mock_thread.retun_value = MockThread()
        init_connection()
        mock_thread.assert_called_with(target= background_task, args=(),kwargs={})


    @mock.patch('pythonapm.collector.connhandler.task_spawned',True)
    @mock.patch('pythonapm.collector.test_connhandler.threading.Thread')
    @mock.patch('pythonapm.collector.connhandler.agentlogger')
    def test_init_connection_with_true(self,mock_logger,mock_thread):
        self.assertIsNone(init_connection())

    @mock.patch('pythonapm.collector.connhandler.task_spawned',False)
    @mock.patch('pythonapm.collector.test_connhandler.threading.Thread')
    @mock.patch('pythonapm.collector.connhandler.agentlogger')
    def test_init_connection_exception(self,mock_logger,mock_thread):
        mock_thread.return_value = Exception('exp')
        init_connection()
        mock_logger.exception.assert_called_with('Error while spawning thread')



        






        




