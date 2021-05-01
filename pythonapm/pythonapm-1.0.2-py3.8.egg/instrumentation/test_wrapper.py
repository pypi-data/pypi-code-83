import unittest
from unittest import mock
from unittest.mock import patch
from pythonapm import constants

from pythonapm.instrumentation import wrapper
from ..agent import Agent


class MockWSGIHandler:
    def __call__(self, a, b):
        return (a, b['hello'])


def mock_func(a,b):
    return (a, b['hello'])



class MockFlaskHandler:
    def add_url_rule(self, a, b, c, call):
        x,y = call(a,b)
        return (x,y)


class WrapperTest(unittest.TestCase):
    def setUp(self):
        self.mockhandler = MockWSGIHandler()
        self.flaskhandler = MockFlaskHandler()
        self.agent = Agent()

    @mock.patch.dict('os.environ', {'NEXTAPM_LICENSE_KEY': 'key', 'NEXTAPM_PROJECT_ID': 'id', 'NEXTAPM_PRINT_PAYLOAD': 'payload', 'NEXTAPM_COLLECTOR_HOST': 'host'})
    def test_wsgi_wrapper(self):
        mock_wrapper = wrapper.wsgi_wrapper(self.mockhandler.__call__, module='django.core.handlers.wsgi.WSGIHandler', method_info={constants.class_str: 'WSGIHandler',
                                                                                                                                    constants.method_str: '__call__',
                                                                                                                                    })
        self.assertTupleEqual(mock_wrapper(
            1, {'hello': 'world'}), (1, 'world'))

    @mock.patch.dict('os.environ', {'NEXTAPM_LICENSE_KEY': 'key', 'NEXTAPM_PROJECT_ID': 'id', 'NEXTAPM_PRINT_PAYLOAD': 'payload', 'NEXTAPM_COLLECTOR_HOST': 'host'})
    def test_default_wrapper(self):
        mock_wrapper = wrapper.default_wrapper(self.mockhandler.__call__, module='django.core.handlers.wsgi.WSGIHandler', method_info={constants.class_str: 'WSGIHandler',
                                                                                                                                       constants.method_str: '__call__',
                                                                                                                                       })
        self.assertTupleEqual(mock_wrapper(
            1, {'hello': 'world'}), (1, 'world'))

    @mock.patch.dict('os.environ', {'NEXTAPM_LICENSE_KEY': 'key', 'NEXTAPM_PROJECT_ID': 'id', 'NEXTAPM_PRINT_PAYLOAD': 'payload', 'NEXTAPM_COLLECTOR_HOST': 'host'})
    def test_args_wrapper(self):
        mock_wrapper = wrapper.args_wrapper(self.flaskhandler.add_url_rule, module='flask', method_info={constants.class_str: 'Flask',
                                                                                                         constants.method_str: 'add_url_rule',
                                                                                                         constants.wrap_args: 3
                                                                                                         })
        self.assertTupleEqual(mock_wrapper(
            1, {'hello': 'world'},1,mock_func), (1, 'world'))
        

