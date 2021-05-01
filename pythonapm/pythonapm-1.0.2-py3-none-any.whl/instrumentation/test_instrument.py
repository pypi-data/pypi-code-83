import unittest
from unittest import mock
from importlib import import_module
from pythonapm.instrumentation import check_and_instrument, instrument_method, init_instrumentation
from .wrapper import wsgi_wrapper
from pythonapm import constants


class MockModule:
    def __call__(self):
        pass

class MockHandler:
    def __call__(self):
        pass


class InstrumentTest(unittest.TestCase):
    def setUp(self):
        self.act_module = MockModule()

    @mock.patch('pythonapm.instrumentation.agentlogger')
    @mock.patch('pythonapm.instrumentation.check_and_instrument')
    def test_init_instrumentation(self, mock_check, mock_logger):
        mock_check.return_value = check_and_instrument

        init_instrumentation()
        # if you have django, or flask installed in local env this would be called
        # self.assertTrue(mock_check.called)
        self.assertTrue(mock_logger.info.called)

    @mock.patch('pythonapm.instrumentation.agentlogger')
    @mock.patch('pythonapm.instrumentation.instrument_method')
    def test_check_and_instrument(self, mock_instrument_method, mock_logger):
        module_name = 'django.core.handlers.wsgi'

        check_and_instrument('django.core.handlers.wsgi', self.act_module)
        self.assertListEqual(mock_instrument_method.mock_calls, [mock.call(module_name,self.act_module, {constants.class_str: 'WSGIHandler',
                                                                                                     constants.method_str: '__call__',
                                                                                                     constants.wrapper_str: wsgi_wrapper, })])
        self.assertTrue(hasattr(self.act_module, 'pythonapm_instrumented'))

    @mock.patch('pythonapm.instrumentation.is_callable')
    @mock.patch('pythonapm.instrumentation.default_wrapper')
    @mock.patch('pythonapm.instrumentation.args_wrapper')
    def test_instrument_method(self,mock_args_wrapper,mock_default_wrapper,mock_callable):
        module_name = 'django.cor.handlers.wsgi'
        mock_callable.return_value = True
        self.mock_handler = MockHandler()
        instrument_method(module_name, self.mock_handler, {constants.class_str: 'WSGIHandler',
                                                         constants.method_str: '__call__',
                                                         }) 
        self.assertTrue(mock_default_wrapper.called)
        
        instrument_method(module_name, self.mock_handler, {constants.class_str: 'WSGIHandler',
                                                         constants.method_str: '__call__',
                                                         constants.wrap_args : 1,
                                                         })
        
        self.assertTrue(mock_args_wrapper.called)


        

        


        
