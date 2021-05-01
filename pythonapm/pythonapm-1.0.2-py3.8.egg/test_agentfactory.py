import os
import unittest
from unittest import mock 
from .agentfactory import agent_instance,get_agent

class AgentFactoryTest(unittest.TestCase):
    
    @mock.patch('pythonapm.agentfactory.agent_instance',None) 
    @mock.patch('pythonapm.agentfactory.agentlogger')
    def test_get_agent(self,mock_logger):
       get_agent()
       self.assertTrue(mock_logger.exception.called)
       #TODO check when intalize() doesn't throw Exception
       #somehow we have to mock intalize() 

