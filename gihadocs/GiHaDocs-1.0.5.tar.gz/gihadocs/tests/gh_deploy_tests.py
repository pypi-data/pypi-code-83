import unittest
from unittest import mock

from gihadocs.tests.base import load_config
from gihadocs.commands import gh_deploy
from gihadocs import __version__


class TestGitHubDeploy(unittest.TestCase):

    def assert_mock_called_once(self, mock):
        """assert that the mock was called only once.

        The `mock.assert_called_once()` method was added in PY36.
        TODO: Remove this when PY35 support is dropped.
        """
        try:
            mock.assert_called_once()
        except AttributeError:
            if not mock.call_count == 1:
                msg = ("Expected '%s' to have been called once. Called %s times." %
                       (mock._mock_name or 'mock', self.call_count))
                raise AssertionError(msg)

    @mock.patch('subprocess.Popen')
    def test_is_cwd_git_repo(self, mock_popeno):

        mock_popeno().wait.return_value = 0

        self.assertTrue(gh_deploy._is_cwd_git_repo())

    @mock.patch('subprocess.Popen')
    def test_is_cwd_not_git_repo(self, mock_popeno):

        mock_popeno().wait.return_value = 1

        self.assertFalse(gh_deploy._is_cwd_git_repo())

    @mock.patch('subprocess.Popen')
    def test_get_current_sha(self, mock_popeno):

        mock_popeno().communicate.return_value = (b'6d98394\n', b'')

        self.assertEqual(gh_deploy._get_current_sha('.'), '6d98394')

    @mock.patch('subprocess.Popen')
    def test_get_remote_url_ssh(self, mock_popeno):

        mock_popeno().communicate.return_value = (
            b'git@github.com:gihadocs/gihadocs.git\n',
            b''
        )

        expected = ('git@', 'gihadocs/gihadocs.git')
        self.assertEqual(expected, gh_deploy._get_remote_url('origin'))

    @mock.patch('subprocess.Popen')
    def test_get_remote_url_http(self, mock_popeno):

        mock_popeno().communicate.return_value = (
            b'https://github.com/gihadocs/gihadocs.git\n',
            b''
        )

        expected = ('https://', 'gihadocs/gihadocs.git')
        self.assertEqual(expected, gh_deploy._get_remote_url('origin'))

    @mock.patch('subprocess.Popen')
    def test_get_remote_url_enterprise(self, mock_popeno):

        mock_popeno().communicate.return_value = (
            b'https://notgh.com/gihadocs/gihadocs.git\n',
            b''
        )

        expected = (None, None)
        self.assertEqual(expected, gh_deploy._get_remote_url('origin'))

    @mock.patch('gihadocs.commands.gh_deploy._is_cwd_git_repo', return_value=True)
    @mock.patch('gihadocs.commands.gh_deploy._get_current_sha', return_value='shashas')
    @mock.patch('gihadocs.commands.gh_deploy._get_remote_url', return_value=(None, None))
    @mock.patch('gihadocs.commands.gh_deploy._check_version')
    @mock.patch('gihadocs.commands.gh_deploy.ghp_import.ghp_import', return_value=(True, ''))
    def test_deploy(self, mock_import, check_version, get_remote, get_sha, is_repo):

        config = load_config(
            remote_branch='test',
        )
        gh_deploy.gh_deploy(config)

    @mock.patch('gihadocs.commands.gh_deploy._is_cwd_git_repo', return_value=True)
    @mock.patch('gihadocs.commands.gh_deploy._get_current_sha', return_value='shashas')
    @mock.patch('gihadocs.commands.gh_deploy._get_remote_url', return_value=(None, None))
    @mock.patch('gihadocs.commands.gh_deploy._check_version')
    @mock.patch('gihadocs.commands.gh_deploy.ghp_import.ghp_import', return_value=(True, ''))
    @mock.patch('os.path.isfile', return_value=False)
    def test_deploy_no_cname(self, mock_isfile, mock_import, check_version, get_remote,
                             get_sha, is_repo):

        config = load_config(
            remote_branch='test',
        )
        gh_deploy.gh_deploy(config)

    @mock.patch('gihadocs.commands.gh_deploy._is_cwd_git_repo', return_value=True)
    @mock.patch('gihadocs.commands.gh_deploy._get_current_sha', return_value='shashas')
    @mock.patch('gihadocs.commands.gh_deploy._get_remote_url', return_value=(
        'git@', 'gihadocs/gihadocs.git'))
    @mock.patch('gihadocs.commands.gh_deploy._check_version')
    @mock.patch('gihadocs.commands.gh_deploy.ghp_import.ghp_import', return_value=(True, ''))
    def test_deploy_hostname(self, mock_import, check_version, get_remote, get_sha, is_repo):

        config = load_config(
            remote_branch='test',
        )
        gh_deploy.gh_deploy(config)

    @mock.patch('gihadocs.commands.gh_deploy._is_cwd_git_repo', return_value=True)
    @mock.patch('gihadocs.commands.gh_deploy._get_current_sha', return_value='shashas')
    @mock.patch('gihadocs.commands.gh_deploy._get_remote_url', return_value=(None, None))
    @mock.patch('gihadocs.commands.gh_deploy._check_version')
    @mock.patch('gihadocs.commands.gh_deploy.ghp_import.ghp_import', return_value=(True, ''))
    def test_deploy_ignore_version_default(self, mock_import, check_version, get_remote, get_sha, is_repo):

        config = load_config(
            remote_branch='test',
        )
        gh_deploy.gh_deploy(config)
        self.assert_mock_called_once(check_version)

    @mock.patch('gihadocs.commands.gh_deploy._is_cwd_git_repo', return_value=True)
    @mock.patch('gihadocs.commands.gh_deploy._get_current_sha', return_value='shashas')
    @mock.patch('gihadocs.commands.gh_deploy._get_remote_url', return_value=(None, None))
    @mock.patch('gihadocs.commands.gh_deploy._check_version')
    @mock.patch('gihadocs.commands.gh_deploy.ghp_import.ghp_import', return_value=(True, ''))
    def test_deploy_ignore_version(self, mock_import, check_version, get_remote, get_sha, is_repo):

        config = load_config(
            remote_branch='test',
        )
        gh_deploy.gh_deploy(config, ignore_version=True)
        check_version.assert_not_called()

    @mock.patch('gihadocs.commands.gh_deploy._is_cwd_git_repo', return_value=True)
    @mock.patch('gihadocs.commands.gh_deploy._get_current_sha', return_value='shashas')
    @mock.patch('gihadocs.commands.gh_deploy._check_version')
    @mock.patch('gihadocs.utils.ghp_import.ghp_import')
    @mock.patch('gihadocs.commands.gh_deploy.log')
    def test_deploy_error(self, mock_log, mock_import, check_version, get_sha, is_repo):
        error_string = 'TestError123'
        mock_import.return_value = (False, error_string)

        config = load_config(
            remote_branch='test',
        )

        self.assertRaises(SystemExit, gh_deploy.gh_deploy, config)
        mock_log.error.assert_called_once_with('Failed to deploy to GitHub with error: \n%s',
                                               error_string)


class TestGitHubDeployLogs(unittest.TestCase):

    @mock.patch('subprocess.Popen')
    def test_gihadocs_newer(self, mock_popeno):

        mock_popeno().communicate.return_value = (b'Deployed 12345678 with GiHaDocs version: 0.1.2\n', b'')

        with self.assertLogs('gihadocs', level='INFO') as cm:
            gh_deploy._check_version('gh-pages')
        self.assertEqual(
            cm.output, ['INFO:gihadocs.commands.gh_deploy:Previous deployment was done with GiHaDocs '
                        'version 0.1.2; you are deploying with a newer version ({})'.format(__version__)]
        )

    @mock.patch('subprocess.Popen')
    def test_gihadocs_older(self, mock_popeno):

        mock_popeno().communicate.return_value = (b'Deployed 12345678 with GiHaDocs version: 10.1.2\n', b'')

        with self.assertLogs('gihadocs', level='ERROR') as cm:
            self.assertRaises(SystemExit, gh_deploy._check_version, 'gh-pages')
        self.assertEqual(
            cm.output, ['ERROR:gihadocs.commands.gh_deploy:Deployment terminated: Previous deployment was made with '
                        'GiHaDocs version 10.1.2; you are attempting to deploy with an older version ({}). Use '
                        '--ignore-version to deploy anyway.'.format(__version__)]
        )

    @mock.patch('subprocess.Popen')
    def test_version_unknown(self, mock_popeno):

        mock_popeno().communicate.return_value = (b'No version specified\n', b'')

        with self.assertLogs('gihadocs', level='WARNING') as cm:
            gh_deploy._check_version('gh-pages')
        self.assertEqual(
            cm.output,
            ['WARNING:gihadocs.commands.gh_deploy:Version check skipped: No version specified in previous deployment.']
        )
