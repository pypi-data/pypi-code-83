import os
import unittest
import logging
from logging.handlers import RotatingFileHandler
from unittest import mock

from .logger import initalize,log_to_sysout,check_and_create_dirs

class LoggerTest(unittest.TestCase):
    def create_logger(self):
        self.assertTrue(isinstance(create_logger(RotatingFileHandler()),RotatingFileHandler))

    @mock.patch('pythonapm.logger.os.path.join',autospec=True)
    def test_check_and_create_dirs(self,mock_join):
        mock_join.side_effect = Exception('test logger[test_check_and_create_dirs] Exception')
        with self.assertRaises(Exception) as exp:
            check_and_create_dirs()
        self.assertEqual(str(exp.exception),'test logger[test_check_and_create_dirs] Exception')

    @mock.patch('pythonapm.logger.agentlogger',None)
    @mock.patch('pythonapm.logger.logging.StreamHandler.__init__',return_value=None) 
    @mock.patch('pythonapm.logger.create_logger')  
    def test_log_to_sysout(self,mock_create_logger,mock_StreamHandler):
        mock_StreamHandler.side_effect = Exception('test logger [log_to_sysout] Exception')
        log_to_sysout()
        self.assertFalse(mock_create_logger.called)


    @mock.patch('pythonapm.logger.agentlogger',None)
    @mock.patch('pythonapm.logger.os.path.join')
    @mock.patch('pythonapm.logger.log_to_sysout')
    @mock.patch('pythonapm.logger.create_logger')
    def test_initialize(self,mock_create_logger,mock_log_to_sysout,mock_join):
        mock_join.side_effect = Exception('exception')
        initalize()
        self.assertFalse(mock_create_logger.called)
        self.assertTrue(mock_log_to_sysout.called)



        
