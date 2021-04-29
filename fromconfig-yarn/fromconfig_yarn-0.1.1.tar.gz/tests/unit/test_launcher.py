"""Test launcher."""

from collections import namedtuple

from cluster_pack.skein import skein_launcher
import cluster_pack
import pytest
import skein
import fromconfig

import fromconfig_yarn


def test_launcher_is_discovered():
    """Test that the Launcher is discovered as fromconfig extension."""
    fromconfig.utils.testing.assert_launcher_is_discovered("yarn", fromconfig_yarn.YarnLauncher)


@pytest.mark.parametrize(
    "yarn",
    [
        pytest.param({}, id="default"),
        pytest.param({"zip_file": "viewfs://root/user/fromconfig_yarn/envs/test.pex"}, id="existing-hdfs"),
        pytest.param({"zip_file": "test.pex"}, id="existing-local"),
    ],
)
def test_launcher(yarn, monkeypatch):
    """Test launcher."""
    # pylint: disable=missing-class-docstring

    got = {}

    class _MonkeyClient:
        # pylint: disable=unused-argument

        def __enter__(self, *args, **kwargs):
            return self

        def __exit__(self, *args, **kwargs):
            return self

        def application_report(self, app_id):
            Report = namedtuple("Report", "tracking_uri")
            return Report("127.0.0.1")

    def _monkey_submit_func(func, args, **kwargs):
        # pylint: disable=unused-argument
        func(*args)
        got.update({"ran": True})

    monkeypatch.setattr(cluster_pack, "upload_env", lambda *_, **__: None)
    monkeypatch.setattr(cluster_pack, "upload_zip", lambda *_, **__: None)
    monkeypatch.setattr(skein, "Client", _MonkeyClient)
    monkeypatch.setattr(skein_launcher, "submit_func", _monkey_submit_func)

    config = {"run": None, "launcher": {"run": "yarn"}, "yarn": yarn}
    launcher = fromconfig.launcher.DefaultLauncher.fromconfig(config["launcher"])
    launcher(config, "run")
    assert got["ran"]
