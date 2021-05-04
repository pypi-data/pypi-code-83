import os
import logging

from unittest import main, skip, mock
from unittest import TestCase

from easysettings import EasySettings
from fshare_cli import FshareAPI

class TestApis(TestCase):

    CONFIG_DIR = '.fshare-test'

    CONFIG_USERNAME = os.environ.get('FSHARE_TEST_USERNAME')
    CONFIG_PASSWORD = os.environ.get('FSHARE_TEST_PASSWORD')
    CONFIG_APP_NAME = os.environ.get('FSHARE_TEST_APP_NAME')
    CONFIG_APP_KEY  = os.environ.get('FSHARE_TEST_APP_KEY')

    def setUp(self):
        print('Test method', self._testMethodName)

        self.settings = EasySettings(os.path.expanduser('~/%s/fshare-cli.conf' % (TestApis.CONFIG_DIR)))
        self.settings.set('username', self.CONFIG_USERNAME)
        self.settings.set('password', self.CONFIG_PASSWORD)
        self.settings.set('app_name', self.CONFIG_APP_NAME)
        self.settings.set('app_key' , self.CONFIG_APP_KEY)
        self.settings.save()

        self.fshare_api = FshareAPI(logging.DEBUG)
        self.fshare_api.auto_configure(location=TestApis.CONFIG_DIR)

    # def test_api_me(self):
    #     me = self.fshare_api.me()
    #
    #     self.assertEqual(me['name'], self.CONFIG_USERNAME)
    #     self.assertEqual(me['email'], self.CONFIG_USERNAME)
    #     self.assertEqual(me['account_type'], 'VipPoint')

    # def test_api_upload(self):
    #     link = self.fshare_api.upload('dummy.txt', '10', '/')
    #
    #     self.assertIsNotNone(link['location'])

    # def test_api_download_no_password(self):
    #     link = self.fshare_api.download('https://www.fshare.vn/file/WIJUHJ16K28R')
    #
    #     self.assertIsNotNone(link['location'])

    # def test_api_download_with_password(self):
    #     link = self.fshare_api.download('https://www.fshare.vn/file/2P6FDB4EB6NH', 'pass')
    #
    #     self.assertIsNotNone(link['location'])

if __name__ == '__main__':
    main()
