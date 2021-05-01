import unittest
from unittest import mock
import os
from .configuration import Configuration,get_collector_domain
import pythonapm
from pythonapm import constants


class ConfigurationTest(unittest.TestCase):

    @mock.patch.dict('os.environ', {'NEXTAPM_LICENSE_KEY': 'key', 'NEXTAPM_PROJECT_ID': 'id', 'NEXTAPM_PRINT_PAYLOAD': 'payload', 'NEXTAPM_COLLECTOR_HOST': 'host'})
    def setUp(self):
        self.config = Configuration()

    def test_is_configured_properly(self):
        self.assertTrue(self.config.is_configured_properly())

    def test_get_license_key(self):
        self.assertEqual(self.config.get_license_key(),'key')
    
    def test_get_project_id(self):
        self.assertEqual(self.config.get_project_id(),'id')
    
    def test_get_collector_domain(self):
        self.assertEqual(self.config.get_collector_domain(),'host')
    
    def test_get_agent_version(self):
        self.assertEqual(self.config.get_agent_version(),pythonapm.version)
    
    def test_get_installed_dir(self):
        self.assertEqual(self.config.get_installed_dir(),pythonapm.installed_path)
    
    def test_is_payload_print_enabled(self):
        self.assertTrue(self.config.is_payload_print_enabled())

    @mock.patch('os.environ',{'NEXTAPM_COLLECTOR_HOST':''})
    def test_get_collector_domain_util(self):
        self.assertEqual(get_collector_domain(),'https://data.nextapm.dev')

    def tearDown(self):
        self.config = None
