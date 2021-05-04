import os
import logging

from unittest import main, skip, mock
from unittest import TestCase

from easysettings import EasySettings
from fshare_cli import FshareAPI

class TestConfigs(TestCase):

    CONFIG_DIR = '.fshare-test'

    CONFIG_USERNAME = os.environ.get('FSHARE_TEST_USERNAME')
    CONFIG_PASSWORD = os.environ.get('FSHARE_TEST_PASSWORD')
    CONFIG_APP_NAME = os.environ.get('FSHARE_TEST_APP_NAME')
    CONFIG_APP_KEY  = os.environ.get('FSHARE_TEST_APP_KEY')

    def setUp(self):
        print('Test method %s' % (self._testMethodName))

        self.settings = EasySettings(os.path.expanduser('~/%s/fshare-cli.conf' % (TestConfigs.CONFIG_DIR)))
        self.settings.clear()
        self.settings.save()

        self.fshare_api = FshareAPI(logging.DEBUG)

    @mock.patch('builtins.input', create=True)
    @mock.patch('getpass.getpass')
    def test_empty_configs_and_correct_credentials(self, mocked_getpass, mocked_input):
        mocked_input.side_effect = [
            self.CONFIG_USERNAME,
            self.CONFIG_APP_KEY,
            self.CONFIG_APP_NAME,
        ]
        mocked_getpass.return_value = self.CONFIG_PASSWORD

        self.fshare_api.auto_configure(location=TestConfigs.CONFIG_DIR)

        self.assertIsNotNone(self.settings.get('token'))
        self.assertIsNotNone(self.settings.get('session_id'))

        self.fshare_api.logout()

    @mock.patch('builtins.input', create=True)
    @mock.patch('getpass.getpass')
    def test_empty_configs_and_wrong_app_key(self, mocked_getpass, mocked_input):
        mocked_input.side_effect = [
            self.CONFIG_USERNAME,
            'wrong-app-key',
            self.CONFIG_APP_NAME,
        ]
        mocked_getpass.return_value = self.CONFIG_PASSWORD

        with self.assertRaisesRegex(Exception, 'Invalid app key!') as e:
            self.fshare_api.auto_configure(location=TestConfigs.CONFIG_DIR)

    @mock.patch('builtins.input', create=True)
    @mock.patch('getpass.getpass')
    def test_empty_configs_and_wrong_app_name(self, mocked_getpass, mocked_input):
        mocked_input.side_effect = [
            self.CONFIG_USERNAME,
            self.CONFIG_APP_KEY,
            'wrong-app-name',
        ]
        mocked_getpass.return_value = self.CONFIG_PASSWORD

        with self.assertRaisesRegex(Exception, 'Invalid User Agent!') as e:
            self.fshare_api.auto_configure(location=TestConfigs.CONFIG_DIR)

    @mock.patch('builtins.input', create=True)
    @mock.patch('getpass.getpass')
    def test_empty_configs_and_wrong_app_name_and_wrong_app_key(self, mocked_getpass, mocked_input):
        mocked_input.side_effect = [
            self.CONFIG_USERNAME,
            'wrong-app-key',
            'wrong-app-name',
        ]
        mocked_getpass.return_value = self.CONFIG_PASSWORD

        with self.assertRaisesRegex(Exception, 'Invalid app key!') as e:
            self.fshare_api.auto_configure(location=TestConfigs.CONFIG_DIR)

    @skip('Manual run only due to "wrong password many times"')
    @mock.patch('builtins.input', create=True)
    @mock.patch('getpass.getpass')
    def test_empty_configs_and_wrong_user_pass(self, mocked_getpass, mocked_input):
        mocked_input.side_effect = [
            'wrong-username',
            self.CONFIG_APP_KEY,
            self.CONFIG_APP_NAME,
        ]
        mocked_getpass.return_value = 'wrong-password'

        with self.assertRaisesRegex(Exception, 'Authenticate fail!') as e:
            self.fshare_api.auto_configure(location=TestConfigs.CONFIG_DIR)

    def test_current_configs_and_correct_session(self):
        self.settings.set('username', self.CONFIG_USERNAME)
        self.settings.set('password', self.CONFIG_PASSWORD)
        self.settings.set('app_name', self.CONFIG_APP_NAME)
        self.settings.set('app_key' , self.CONFIG_APP_KEY)
        self.settings.save()

        self.fshare_api.auto_configure(location=TestConfigs.CONFIG_DIR)

        self.fshare_api.info('https://www.fshare.vn/file/WIJUHJ16K28R')

        self.fshare_api.logout()

    def test_current_configs_and_wrong_session_id_or_token(self):
        self.settings.set('username', self.CONFIG_USERNAME)
        self.settings.set('password', self.CONFIG_PASSWORD)
        self.settings.set('app_name', self.CONFIG_APP_NAME)
        self.settings.set('app_key' , self.CONFIG_APP_KEY)
        self.settings.set('token' , 'does-not-matter-if-valid-or-not')
        self.settings.set('session_id' , 'does-not-matter-if-valid-or-not')
        self.settings.save()

        self.fshare_api.auto_configure(location=TestConfigs.CONFIG_DIR)

        self.fshare_api.logout()

    def test_current_configs_and_wrong_app_key_and_wrong_session_id_or_token(self):
        self.settings.set('username', self.CONFIG_USERNAME)
        self.settings.set('password', self.CONFIG_PASSWORD)
        self.settings.set('app_name', self.CONFIG_APP_NAME)
        self.settings.set('app_key' , 'wrong-app-key')
        self.settings.set('token' , 'does-not-matter-if-valid-or-not')
        self.settings.set('session_id' , 'does-not-matter-if-valid-or-not')
        self.settings.save()

        with self.assertRaisesRegex(Exception, 'Invalid app key!') as e:
            self.fshare_api.auto_configure(location=TestConfigs.CONFIG_DIR)

    def test_current_configs_and_wrong_app_name_and_wrong_session_id_or_token(self):
        self.settings.set('username', self.CONFIG_USERNAME)
        self.settings.set('password', self.CONFIG_PASSWORD)
        self.settings.set('app_name', 'wrong-app-name')
        self.settings.set('app_key' , self.CONFIG_APP_KEY)
        self.settings.set('token' , 'does-not-matter-if-valid-or-not')
        self.settings.set('session_id' , 'does-not-matter-if-valid-or-not')
        self.settings.save()

        with self.assertRaisesRegex(Exception, 'Invalid User Agent!') as e:
            self.fshare_api.auto_configure(location=TestConfigs.CONFIG_DIR)

    @skip('Manual run only due to "wrong password many times"')
    def test_current_configs_and_wrong_user_pass_and_wrong_session_id_or_token(self):
        self.settings.set('username', 'wrong-username')
        self.settings.set('password', 'wrong-password')
        self.settings.set('app_name', self.CONFIG_APP_NAME)
        self.settings.set('app_key' , self.CONFIG_APP_KEY)
        self.settings.set('token' , 'does-not-matter-if-valid-or-not')
        self.settings.set('session_id' , 'does-not-matter-if-valid-or-not')
        self.settings.save()

        with self.assertRaisesRegex(Exception, 'Authenticate fail!') as e:
            self.fshare_api.auto_configure(location=TestConfigs.CONFIG_DIR)

if __name__ == '__main__':
    main()
