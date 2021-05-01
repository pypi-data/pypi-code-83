import sys
import unittest
from unittest import mock
from importlib import import_module
from pythonapm import  constants
from pythonapm.contrib.django.wrapper import instrument_middlewares
from . import tests
from .wrapper import methods


class MockDjangoMiddlewareHandler:
    pass


class InstrumentMiddlewaresTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        sys.modules['django.conf'] = tests

    @mock.patch('pythonapm.contrib.django.wrapper.agentlogger')
    @mock.patch('pythonapm.contrib.django.wrapper.instrument_method')
    def test_instrument_middlewares(self, mock_instrument_method, mock_logger):
        instrument_middlewares()
        
        self.assertTrue(mock_instrument_method.called)
        imported_module = import_module('pythonapm.contrib.django.test_wrapper')
        calls = [('pythonapm.contrib.django.test_wrapper',imported_module,{
            constants.class_str : 'MockDjangoMiddlewareHandler',
            constants.method_str : method
        }) for method in methods ]
        self.assertListEqual(mock_instrument_method.mock_calls,[mock.call(call[0],call[1],call[2]) for call in calls])
    
