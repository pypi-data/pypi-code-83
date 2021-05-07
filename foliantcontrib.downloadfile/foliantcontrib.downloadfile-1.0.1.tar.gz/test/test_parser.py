import logging
import shutil

from hashlib import md5
from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch
from urllib.error import HTTPError

from foliant_test.config_extension import ConfigExtensionTestFramework

from foliant.config.downloadfile import BadConfigException
from foliant.config.downloadfile import DownloadError


logging.disable(logging.CRITICAL)


class TestParser(TestCase):
    def setUp(self):
        self.ctf = ConfigExtensionTestFramework('downloadfile')
        self.project_dir = (Path(__file__).parent / 'project_dir').resolve()
        self.project_dir.mkdir(exist_ok=True)
        self.ctf.project_path = self.project_dir
        self.ctf.config_path = self.project_dir / self.ctf.config_file_name

    def tearDown(self):
        shutil.rmtree(self.project_dir, ignore_errors=True)
        # pass

    @patch('foliant.config.downloadfile.urlopen', autospec=True)
    def test_one_url(self, urlopen):
        mock_response = Mock()
        mock_response.read.return_value = b'File content'
        urlopen.return_value = mock_response

        source = '''
downloadfile:
    queue:
        - url: http://example.com/myfile.txt
        '''

        expected = {
            'downloadfile': {
                'queue': [{'url': 'http://example.com/myfile.txt'}]
            }
        }

        self.ctf.test_extension(input_config=source, expected_config=expected)
        request = urlopen.call_args.args[0]
        context = urlopen.call_args.kwargs['context']

        self.assertEqual(request.headers, {})
        self.assertIsNone(context)

        with open(self.project_dir / 'myfile.txt') as f:
            self.assertEqual(f.read(), 'File content')

    @patch('foliant.config.downloadfile.urlopen', autospec=True)
    def test_save_to(self, urlopen):
        mock_response = Mock()
        mock_response.read.return_value = b'File content'
        urlopen.return_value = mock_response

        source = '''
downloadfile:
    queue:
        - url: http://example.com/myfile.txt
          save_to: sub1/sub2/downloaded.txt
        '''

        expected = {
            'downloadfile': {
                'queue': [
                    {
                        'url': 'http://example.com/myfile.txt',
                        'save_to': 'sub1/sub2/downloaded.txt'
                    }
                ]
            }
        }

        self.ctf.test_extension(input_config=source, expected_config=expected)
        request = urlopen.call_args.args[0]
        context = urlopen.call_args.kwargs['context']

        self.assertEqual(request.headers, {})
        self.assertIsNone(context)

        with open(self.project_dir / 'sub1/sub2/downloaded.txt') as f:
            self.assertEqual(f.read(), 'File content')

    @patch('foliant.config.downloadfile.urlopen', autospec=True)
    def test_three_files(self, urlopen):
        files = [
            b'First file content',
            b'Second file content',
            b'Third file content',
        ]
        mock_response = Mock()
        mock_response.read.side_effect = files
        urlopen.return_value = mock_response

        source = '''
downloadfile:
    queue:
        - url: http://example.com/myfile.txt
          save_to: file1.txt
        - url: http://example.com/file2.txt
        - url: http://example.com/home/random.txt
          login: login
          password: password
          save_to: file3.txt
        '''

        expected = {
            'downloadfile': {
                'queue': [
                    {
                        'url': 'http://example.com/myfile.txt',
                        'save_to': 'file1.txt'
                    },
                    {
                        'url': 'http://example.com/file2.txt',
                    },
                    {
                        'url': 'http://example.com/home/random.txt',
                        'login': 'login',
                        'password': 'password',
                        'save_to': 'file3.txt'
                    }

                ]
            }
        }

        self.ctf.test_extension(input_config=source, expected_config=expected)
        with open(self.project_dir / 'file1.txt') as f:
            self.assertEqual(f.read(), files[0].decode())
        with open(self.project_dir / 'file2.txt') as f:
            self.assertEqual(f.read(), files[1].decode())
        with open(self.project_dir / 'file3.txt') as f:
            self.assertEqual(f.read(), files[2].decode())

    @patch('foliant.config.downloadfile.urlopen', autospec=True)
    def test_http_error(self, urlopen):
        urlopen.side_effect = HTTPError(url='http://example.com/myfile.txt', code=404, msg='Not Found', hdrs={}, fp=None)

        source = '''
downloadfile:
    queue:
        - url: http://example.com/myfile.txt
          save_to: file1.txt
        - url: http://example.com/file2.txt
        - url: http://example.com/home/random.txt
          login: login
          password: password
          save_to: file3.txt
        '''

        expected = {
            'downloadfile': {
                'queue': [
                    {
                        'url': 'http://example.com/myfile.txt',
                        'save_to': 'file1.txt'
                    },
                    {
                        'url': 'http://example.com/file2.txt',
                    },
                    {
                        'url': 'http://example.com/home/random.txt',
                        'login': 'login',
                        'password': 'password',
                        'save_to': 'file3.txt'
                    }

                ]
            }
        }

        with self.assertRaises(DownloadError):
            self.ctf.test_extension(input_config=source, expected_config=expected)

        self.assertEqual(list(self.project_dir.iterdir()), [])

    @patch('foliant.config.downloadfile.urlopen', autospec=True)
    def test_config_error(self, urlopen):
        source = '''
downloadfile:
    queue:
        - save_to: file1.txt
        - url: http://example.com/file2.txt
        - url: http://example.com/home/random.txt
          login: login
          password: password
          save_to: file3.txt
        '''

        expected = {
            'downloadfile': {
                'queue': [
                    {
                        'url': 'http://example.com/myfile.txt',
                        'save_to': 'file1.txt'
                    },
                    {
                        'url': 'http://example.com/file2.txt',
                    },
                    {
                        'url': 'http://example.com/home/random.txt',
                        'login': 'login',
                        'password': 'password',
                        'save_to': 'file3.txt'
                    }

                ]
            }
        }

        with self.assertRaises(BadConfigException):
            self.ctf.test_extension(input_config=source, expected_config=expected)

        self.assertEqual(list(self.project_dir.iterdir()), [])

    @patch('foliant.config.downloadfile.urlopen', autospec=True)
    def test_fail_fast_false(self, urlopen):
        mock_response = Mock()
        mock_response.read.return_value = b'File content'
        urlopen.side_effect = [
            HTTPError(url='http://example.com/file2.txt', code=404, msg='Not Found', hdrs={}, fp=None),
            mock_response
        ]

        source = '''
downloadfile:
    fail_fast: false
    queue:
        - save_to: file1.txt
        - url: http://example.com/file2.txt
        - url: http://example.com/home/random.txt
          login: login
          password: password
          save_to: file3.txt
        '''

        expected = {
            'downloadfile': {
                'fail_fast': False,
                'queue': [
                    {
                        'save_to': 'file1.txt'
                    },
                    {
                        'url': 'http://example.com/file2.txt',
                    },
                    {
                        'url': 'http://example.com/home/random.txt',
                        'login': 'login',
                        'password': 'password',
                        'save_to': 'file3.txt'
                    }

                ]
            }
        }

        self.ctf.test_extension(input_config=source, expected_config=expected)

        self.assertEqual(list(self.project_dir.iterdir()), [self.project_dir / 'file3.txt'])
        with open(self.project_dir / 'file3.txt') as f:
            self.assertEqual(f.read(), 'File content')

    @patch('foliant.config.downloadfile.urlopen', autospec=True)
    def test_download_tag(self, urlopen):
        mock_response = Mock()
        mock_response.read.return_value = b'File content'
        urlopen.return_value = mock_response

        url = 'http://example.com/myfile.txt'
        filename = f'{md5(url.encode()).hexdigest()}.txt'
        filepath = self.project_dir / '.downloadfilecache' / filename

        source = f'test: !download {url}'
        expected = {'test': str(filepath.resolve())}

        self.ctf.test_extension(input_config=source, expected_config=expected)

        with open(filepath) as f:
            self.assertEqual(f.read(), 'File content')
