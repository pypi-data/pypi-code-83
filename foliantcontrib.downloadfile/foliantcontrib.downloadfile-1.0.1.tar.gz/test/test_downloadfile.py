import shutil

from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch

from foliant.config.downloadfile import download_file
from foliant.config.downloadfile import get_file_ext_from_url
from foliant.config.downloadfile import get_file_name_from_url


class TestDownloadFile(TestCase):
    def setUp(self):
        self.project_dir = (Path(__file__).parent / 'project_dir').resolve()
        self.project_dir.mkdir(exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.project_dir, ignore_errors=True)

    @patch('foliant.config.downloadfile.urlopen', autospec=True)
    def test_only_url(self, urlopen):
        mock_response = Mock()
        mock_response.read.return_value = b'File content'
        urlopen.return_value = mock_response

        url = 'http://example.com/myfile.txt'

        download_file(root_dir=self.project_dir, url=url)
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

        url = 'http://example.com/myfile.txt'
        save_to = 'subdir1/subdir2/downloaded.txt'

        download_file(root_dir=self.project_dir, url=url, save_to=save_to)
        request = urlopen.call_args.args[0]
        context = urlopen.call_args.kwargs['context']

        self.assertEqual(request.headers, {})
        self.assertIsNone(context)

        with open(self.project_dir / save_to) as f:
            self.assertEqual(f.read(), 'File content')

    @patch('foliant.config.downloadfile.urlopen', autospec=True)
    def test_with_auth(self, urlopen):
        mock_response = Mock()
        mock_response.read.return_value = b'File content'
        urlopen.return_value = mock_response

        url = 'http://example.com/myfile.txt'

        download_file(
            root_dir=self.project_dir,
            url=url,
            login='john',
            password='qwerty1234'
        )
        request = urlopen.call_args.args[0]
        context = urlopen.call_args.kwargs['context']

        self.assertIn('Authorization', request.headers)
        self.assertIsNone(context)

        with open(self.project_dir / 'myfile.txt') as f:
            self.assertEqual(f.read(), 'File content')


class TestGetFileNameFromURL(TestCase):
    def test_with_ext(self):
        url = 'http://example.com/sub/myfile.txt'
        name = get_file_name_from_url(url)
        self.assertEqual(name, 'myfile.txt')

    def test_no_ext(self):
        url = 'http://example.com/sub/myfile'
        name = get_file_name_from_url(url)
        self.assertEqual(name, 'myfile')

    def test_with_clutter(self):
        url = 'http://example.com/sub/myfile.txt?param=val&foo=bar'
        name = get_file_name_from_url(url)
        self.assertEqual(name, 'myfile.txt')


class TestGetFileExtFromURL(TestCase):
    def test_with_ext(self):
        url = 'http://example.com/sub/myfile.txt'
        ext = get_file_ext_from_url(url)
        self.assertEqual(ext, '.txt')

    def test_no_ext(self):
        url = 'http://example.com/sub/myfile'
        ext = get_file_ext_from_url(url)
        self.assertEqual(ext, '')

    def test_with_clutter(self):
        url = 'http://example.com/sub/myfile.txt?param=val&foo=bar'
        ext = get_file_ext_from_url(url)
        self.assertEqual(ext, '.txt')
