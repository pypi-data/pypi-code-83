"""Yarn Launcher."""

from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Dict
from urllib import parse
import logging
import os

from cluster_pack.skein import skein_launcher
import cluster_pack
import fromconfig
import skein


LOGGER = logging.getLogger(__name__)

_DEFAULT_ENV_VARS = ("CUDA_VISIBLE_DEVICES",)

_USER = os.environ.get("USER", "fromconfig")

_DEFAULT_PACKAGE_PATH = f"viewfs://root/user/{_USER}/envs/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.pex"


class YarnLauncher(fromconfig.launcher.Launcher):
    """Launch job on yarn."""

    def __init__(self, launcher: fromconfig.launcher.Launcher = None):
        super().__init__(launcher=launcher)  # type: ignore

    def __call__(self, config: Any, command: str = ""):
        """Run code on yarn."""
        # Extract params from the yarn entry of the config
        params = (config.get("yarn") or {}) if fromconfig.utils.is_mapping(config) else {}  # type: ignore
        env_vars = params.get("env_vars", _DEFAULT_ENV_VARS)
        hadoop_file_systems = params.get("hadoop_file_systems", ())
        ignored_packages = params.get("ignored_packages", ())
        jvm_memory_in_gb = params.get("jvm_memory_in_gb", 8)
        memory = params.get("memory", "32 GiB")
        num_cores = params.get("num_cores", 8)
        package_path = params.get("package_path", _DEFAULT_PACKAGE_PATH)
        zip_file = params.get("zip_file", None)
        name = params.get("name", f"yarn-launcher-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}")

        def _run(launcher, config, command):
            """Code executed on yarn."""
            # pylint: disable=redefined-outer-name,reimported,import-outside-toplevel,
            import sys
            import fromconfig

            sys.path.append(".")  # For local imports
            launcher = launcher or fromconfig.launcher.LocalLauncher()
            launcher(config=config, command=command)

        # Launch job on yarn
        with skein.Client() as skein_client:
            app_id = skein_launcher.submit_func(
                skein_client=skein_client,
                func=_run,
                args=[self.launcher, config, command],
                name=name,
                num_cores=num_cores,
                package_path=upload_pex(package_path, ignored_packages=ignored_packages, zip_file=zip_file),
                hadoop_file_systems=list(hadoop_file_systems),
                additional_files=[str(path) for path in Path.cwd().glob("*.py")],
                env_vars={**get_env_vars(env_vars), **get_jvm_env_vars(jvm_memory_in_gb)},
                memory=memory,
            )
            report = skein_client.application_report(app_id)
            LOGGER.info(f"TRACKING_URL: {report.tracking_url}")


def get_env_vars(env_vars: Iterable[str] = ()) -> Dict[str, str]:
    """Return Environment Variables to forward to Yarn."""
    values = {}
    for name in env_vars:
        if os.environ.get(name) is not None:
            values[name] = os.environ[name]
        else:
            LOGGER.warning(f"Environment Variable {name} is None (will not be forwarded to yarn)")
    return values


def get_jvm_env_vars(jvm_memory_in_gb: str) -> Dict[str, str]:
    """Return JVM Environment Variables to forward to Yarn."""
    return {"LIBHDFS_OPTS": f"-Xms{jvm_memory_in_gb}g -Xmx{jvm_memory_in_gb}g", "MALLOC_ARENA_MAX": "0"}


def upload_pex(package_path: str, ignored_packages: Iterable[str] = None, zip_file: str = None) -> str:
    """Upload Current Environment and return path to PEX on HDFS."""
    if zip_file is None:
        LOGGER.info(f"Uploading pex to {package_path}")
        cluster_pack.upload_env(
            package_path=package_path,
            packer=cluster_pack.packaging.PEX_PACKER,
            ignored_packages=list(ignored_packages) if ignored_packages else [],
            additional_packages={},
        )
        return package_path
    else:
        scheme = parse.urlparse(str(zip_file)).scheme
        if scheme in {"hdfs", "viewfs"}:
            LOGGER.info("Skipping pex upload")
            return zip_file
        else:
            LOGGER.info(f"Uploading pex to {package_path}")
            cluster_pack.upload_zip(zip_file=zip_file, package_path=package_path)
            return package_path
