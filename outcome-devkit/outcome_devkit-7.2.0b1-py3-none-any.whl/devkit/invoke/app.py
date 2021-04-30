"""Various functions to collect app info."""

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Protocol, TypedDict, cast

try:
    import pygit2  # noqa: WPS433

    _has_pygit = True
except ImportError:  # pragma: no cover
    _has_pygit = False

from dotenv import load_dotenv
from outcome.utils.config import Config

from outcome.devkit.invoke import env

pyproject_path = Path.cwd() / 'pyproject.toml'

pyproject_file = env.declare('pyproject.toml', str(pyproject_path))
project_config = Config(pyproject_path)


app_name = env.str_from_config('TOOL_POETRY_NAME', config=project_config)
app_version = env.str_from_config('TOOL_POETRY_VERSION', config=project_config)
app_port = env.int_from_config('APP_PORT', config=project_config)

app_package_repository_name = env.str_from_config('PACKAGE_REPOSITORY_NAME', config=project_config)
app_package_repository_url = env.str_from_config('PACKAGE_REPOSITORY_URL', config=project_config)


@dataclass
class AppInfo:
    name: str
    version: str
    port: Optional[int] = None
    package_repository_name: Optional[str] = None
    package_repository_url: Optional[str] = None


def get_app_info() -> AppInfo:  # pragma: no cover
    return AppInfo(
        env.r(app_name),
        env.r(app_version),
        env.r(app_port, require=False),
        env.r(app_package_repository_name, require=False),
        env.r(app_package_repository_url, require=False),
    )


@dataclass
class GitInfo:
    branch: str
    normalized_branch: str
    is_master: bool
    latest_commit_hash: str


class Oid(Protocol):
    def __str__(self) -> str:  # pragma: no cover
        ...


class Reference(Protocol):
    shorthand: str
    target: Oid


class Repository(Protocol):
    head: Reference


def _get_git_repository() -> Optional[Repository]:  # pragma: no cover
    # The discover_repository function seems to be part
    # of the un-typed c-extension,
    repo_path: Optional[str] = pygit2.discover_repository(os.getcwd())  # type: ignore

    if repo_path is None:
        return None

    return pygit2.Repository(repo_path)


def get_git_info() -> Optional[GitInfo]:  # pragma: no cover
    if not _has_pygit:
        return None

    repo = _get_git_repository()

    if repo is None:
        return None

    head_ref = repo.head

    branch = head_ref.shorthand
    normalized_branch = branch.replace('/', '-')
    is_master = branch in {'master', 'HEAD'}
    latest_commit_hash = str(head_ref.target)[:8]

    return GitInfo(branch, normalized_branch, is_master, latest_commit_hash)


_EnvFiles = Dict[str, Path]


class EnvFiles(TypedDict, total=False):
    env: Path
    secrets: Path
    build_secrets: Path


unresolved = {'env': '.env', 'secrets': '.secrets', 'build_secrets': '/run/secrets/build-secrets'}


def get_env_files() -> EnvFiles:  # pragma: no cover
    def resolve(path: str) -> Path:
        p = Path(path)
        return p if p.is_absolute() else Path(os.getcwd(), p)

    resolved = {k: resolve(v) for k, v in unresolved.items()}
    filtered = {k: v for k, v in resolved.items() if v.exists()}

    return EnvFiles(**filtered)


def load_env_files():  # pragma: no cover
    env_files = cast(_EnvFiles, get_env_files())

    for value in env_files.values():
        load_dotenv(value)
